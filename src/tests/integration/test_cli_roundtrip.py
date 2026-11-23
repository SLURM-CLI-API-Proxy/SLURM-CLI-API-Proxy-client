"""sbatch -> squeue -> scancel through the installed proxy commands against a test
cluster (testing/slurm-container/start.sh sets PROXY_SLURM_API_URL, SLURM_JWT, SLURM_USER)."""
import json
import os
import subprocess
import sys
import time

import pytest

pytestmark = pytest.mark.integration

if not all(os.environ.get(v) for v in ("PROXY_SLURM_API_URL", "SLURM_JWT", "SLURM_USER")):
    pytest.skip("test cluster environment not set", allow_module_level=True)


def run(cmd, *args, stdin=None):
    exe = os.path.join(os.path.dirname(sys.executable), cmd)
    return subprocess.run([exe, *args], input=stdin, capture_output=True, text=True)


def job_states(job_id):
    out = run("squeue", "--json")
    assert out.returncode == 0, out.stderr
    return [j["job_state"] for j in json.loads(out.stdout)["jobs"] if str(j["job_id"]) == job_id]


def test_sbatch_directives_squeue_scancel():
    script = "#!/bin/bash\n#SBATCH -J proxy-roundtrip\n#SBATCH -t 00:05:00\n#SBATCH --mem=50M\nsleep 120\n"
    sub = run("sbatch", "--parsable", "-D", "/tmp", stdin=script)
    assert sub.returncode == 0, sub.stderr
    job_id = sub.stdout.strip()
    assert job_id.isdigit()

    jobs = json.loads(run("squeue", "--json").stdout)["jobs"]
    job = next(j for j in jobs if str(j["job_id"]) == job_id)
    # directives were applied
    assert job["name"] == "proxy-roundtrip"
    assert job["time_limit"]["number"] == 5
    assert job["memory_per_node"]["number"] == 50

    cancel = run("scancel", job_id)
    assert cancel.returncode == 0, cancel.stderr
    for _ in range(15):
        if all("CANCELLED" in s for s in job_states(job_id)):
            break
        time.sleep(1)
    assert all("CANCELLED" in s for s in job_states(job_id))


def test_scancel_unknown_job_is_silent():
    out = run("scancel", "99999999")
    assert out.returncode == 0 and out.stderr == ""


def test_sbatch_bad_partition_fails():
    out = run("sbatch", "-p", "no-such-partition", "-D", "/tmp", stdin="#!/bin/bash\nhostname\n")
    assert out.returncode == 1
    assert "partition" in out.stderr.lower()
    assert out.stdout == ""
