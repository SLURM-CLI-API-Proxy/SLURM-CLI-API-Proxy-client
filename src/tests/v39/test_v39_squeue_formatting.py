import pytest
from slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39 import format_squeue_job, V0039JobInfo, V0039JobRes, slurm_statuses
import time

def test_format_squeue_job():
    job_info = V0039JobInfo(
        job_id=12345,
        partition="partition1",
        name="test_job",
        user_name="user1",
        job_state="RUNNING",
        start_time=int(time.time()) - 1800,  # 30 min ago
        job_resources=V0039JobRes(allocated_hosts=1, nodes="node1")
    )
    job_resources = V0039JobRes(allocated_hosts=1, nodes="node1")

    result = format_squeue_job(job_info, job_resources)

    assert "12345" in result
    assert "test_job" in result
    assert "user1" in result
    assert slurm_statuses["RUNNING"] in result
    assert "30:00" in result  # 30 min elapsed
    assert "node1" in result

