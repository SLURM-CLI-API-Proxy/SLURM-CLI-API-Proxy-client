"""Dask workers on Slurm through the proxy (dask-jobqueue's SLURMCluster).

Needs a Slurm cluster reachable through PROXY_SLURM_API_URL/SLURM_JWT/SLURM_USER
where the workers can connect back to this process (e.g. inside the test
container: testing/slurm-container/run_dask_test.sh). Workers are started with
DASK_WORKER_PYTHON (default: this Python).
"""
import json
import os
import shutil
import subprocess
import sys
import time

import pytest

dask_jobqueue = pytest.importorskip("dask_jobqueue")
distributed = pytest.importorskip("distributed")

pytestmark = [pytest.mark.integration, pytest.mark.dask]

REQUIRED_ENV = ("PROXY_SLURM_API_URL", "SLURM_JWT", "SLURM_USER")


def proxy_command(name: str) -> str:
    """The proxy's console script, not a real Slurm CLI that may also be on PATH."""
    path = os.path.join(os.path.dirname(sys.executable), name)
    if not os.path.exists(path):
        pytest.skip(f"proxy command {name} not installed next to {sys.executable}")
    return path


def proxy_job_states(job_ids):
    out = subprocess.run([proxy_command("squeue"), "--json"], capture_output=True, text=True, check=True).stdout
    jobs = json.loads(out)["jobs"]
    return {str(j["job_id"]): j["job_state"] for j in jobs if str(j["job_id"]) in job_ids}


@pytest.fixture(scope="module")
def cluster():
    missing = [v for v in REQUIRED_ENV if not os.environ.get(v)]
    if missing:
        pytest.skip(f"missing environment: {missing}")

    from dask_jobqueue.slurm import SLURMCluster, SLURMJob

    class ProxySLURMJob(SLURMJob):
        submit_command = proxy_command("sbatch")
        cancel_command = proxy_command("scancel")

    log_dir = os.environ.get("DASK_LOG_DIR", os.path.join(os.path.expanduser("~"), "dask-logs"))
    os.makedirs(log_dir, exist_ok=True)
    c = SLURMCluster(
        job_cls=ProxySLURMJob,
        cores=1,
        processes=1,
        memory="500MiB",
        walltime="00:10:00",
        queue=os.environ.get("DASK_SLURM_PARTITION", "debug"),
        python=os.environ.get("DASK_WORKER_PYTHON", sys.executable),
        log_directory=log_dir,
        job_extra_directives=[f"-D {log_dir}"],
    )
    yield c
    c.close()


def test_dask_workers_via_proxy(cluster):
    from distributed import Client

    script = cluster.job_script()
    assert "#SBATCH -t 00:10:00" in script

    cluster.scale(2)
    with Client(cluster) as client:
        client.wait_for_workers(2, timeout=180)
        job_ids = {str(j.job_id) for j in cluster.workers.values()}
        assert len(job_ids) == 2

        # The jobs were submitted through the proxy and run in Slurm with the
        # resources from the #SBATCH directives
        states = proxy_job_states(job_ids)
        assert set(states) == job_ids
        assert all("RUNNING" in s for s in states.values())

        futures = client.map(lambda x: x * x, range(100))
        assert client.submit(sum, futures).result(timeout=60) == sum(x * x for x in range(100))
        workers = {w["host"] for w in client.scheduler_info()["workers"].values()}
        assert workers

    # Scaling down / closing cancels the jobs through the proxy's scancel
    cluster.scale(0)
    deadline = time.time() + 60
    while time.time() < deadline:
        states = proxy_job_states(job_ids)
        if all(not ({"RUNNING", "PENDING"} & set(s)) for s in states.values()):
            break
        time.sleep(2)
    else:
        pytest.fail(f"jobs still active after scale(0): {states}")
