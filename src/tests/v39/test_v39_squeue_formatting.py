import pytest
from slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39 import V0039JobInfo, V0039JobRes, slurm_statuses
from slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39 import _format_duration
import time
from datetime import timedelta

# def test_format_squeue_job_fields():
#     job_info = V0039JobInfo(
#         job_id=12345,
#         partition="partition1",
#         name="test_job",
#         user_name="user1",
#         job_state="RUNNING",
#         start_time=int(time.time()) - 1800, # 30 min ago
#         job_resources=V0039JobRes(allocated_hosts=1, nodes="node1")
#     )
#     job_resources = V0039JobRes(allocated_hosts=1, nodes="node1")

#     result = format_squeue_job(job_info, job_resources)

#     assert "12345" in result
#     assert "test_job" in result
#     assert "user1" in result
#     assert slurm_statuses["RUNNING"] in result
#     assert "30:00" in result  # 30 min elapsed
#     assert "node1" in result

# # TODO We might also want to test if the field content truncation behaviour
# # is consistent with the SLURM CLI

# def test_format_squeue_job_alignment():
#     job_info = V0039JobInfo(
#         job_id=123,
#         partition="ptn1",
#         name="testjob",
#         user_name="user1",
#         job_state="RUNNING",
#         start_time=int(time.time()) - 120,  # 2 min ago
#         job_resources=V0039JobRes(allocated_hosts=1, nodes="node1")
#     )
#     job_resources = V0039JobRes(allocated_hosts=1, nodes="node1")

#     result = format_squeue_job(job_info, job_resources)
#     expected = "  123      ptn1  testjob    user1  R        2:00     1 node1\n"

#     assert result == expected, f"Formatted output should be \"{expected}\" but was \"{result}\""



def test_format_duration_gt10days():
    td = timedelta(days=10, hours=0, minutes=1, seconds=1)
    expected = "10:00:01:01"
    assert _format_duration(td) == expected, f"Output should be: {expected}"

def test_format_duration_lt10days():
    td = timedelta(days=1, hours=1, minutes=1, seconds=1)
    expected = "1:01:01:01"
    assert _format_duration(td) == expected, f"Output should be: {expected}"

def test_format_duration_lt10hours():
    td = timedelta(days=0, hours=1, minutes=0, seconds=1)
    expected = "1:00:01"
    assert _format_duration(td) == expected, f"Output should be: {expected}"

def test_format_duration_gt10hours():
    td = timedelta(days=0, hours=10, minutes=1, seconds=1)
    expected = "10:01:01"
    assert _format_duration(td) == expected, f"Output should be: {expected}"

def test_format_duration_lt10minutes():
    td = timedelta(days=0, hours=0, minutes=1, seconds=0)
    expected = "1:00"
    assert _format_duration(td) == expected, f"Output should be: {expected}"

def test_format_duration_gt10minutes():
    td = timedelta(days=0, hours=0, minutes=10, seconds=1)
    expected = "10:01"
    assert _format_duration(td) == expected, f"Output should be: {expected}"

def test_format_duration_seconds_with_leading_zeros():
    td = timedelta(days=0, hours=0, minutes=0, seconds=1)
    expected = "0:01"
    assert _format_duration(td) == expected, f"Output should be: {expected}"



