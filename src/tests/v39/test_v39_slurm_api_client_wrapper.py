import pytest
import json
from slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39 import V39SlurmAPIClientWrapper
from openapi_client.models.v0039_job_res import V0039JobRes
from openapi_client.models.v0039_jobs_response import V0039JobsResponse
from openapi_client.models.v0039_job_info import V0039JobInfo
import slurm_api_cli_proxy.client_args_linker.v39.squeue_format as squeue_format

class MockJobsResponse(V0039JobsResponse):
    mock_to_json_output:str|None = None
    jobs:list[V0039JobInfo] = []

    def to_json(self):
        return self.mock_to_json_output
    
def test_process_squeue_output_json():
    cli_params = {
       "--json": True
    }
    response = MockJobsResponse()
    response.mock_to_json_output = '{"meta":{}, "wellformed":"json"}'

    result = V39SlurmAPIClientWrapper.process_squeue_output(cli_params, response)

    assert "meta" not in result, "The meta object should have been removed from the response."
    try:
        json.dumps(result)
    except:
        pytest.fail("Remaining response should still be valid json.")

def test_process_squeue_output_user_filter():
   cli_params = {
      "--user": "one-user",
      "--json": False,
      "--format": "%u"
   }
   response = MockJobsResponse()
   my_job = V0039JobInfo()
   my_job.user_name = "one-user"
   my_job.job_resources = V0039JobRes()

   other_job = V0039JobInfo()
   other_job.user_name = "other-user"
   other_job.job_resources = V0039JobRes()

   response.jobs = [my_job, other_job]

   result = V39SlurmAPIClientWrapper.process_squeue_output(cli_params, response)
   lines = result.split("\n")

   assert len([line for line in lines if len(line)>0]) == 2, "Should contain 2 lines: the table header and one job info line."
   info_line = lines[1]
   assert "one-user" in info_line, "The job in the output should be of the give user, not the other one."


def test_process_squeue_output_format_default():
    # "--format=%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R"
    cli_params = { "--json": False }
    response = MockJobsResponse()
    result = V39SlurmAPIClientWrapper.process_squeue_output(cli_params, response)
    assert "JOBID" in result, "Default format should contain job id."
    assert "PARTITION" in result, "Default format should contain partition."
    assert "NAME" in result, "Default format should contain job name."
    assert "USER" in result, "Default format should contain user name."
    assert "TIME" in result, "Default format should contain elapsed run time."
    assert "NODES" in result, "Default format should contain nodes."
    assert "NODELIST(REASON)" in result, "Default format should contain nodelist with reason."

def test_process_squeue_output_format_long():
   # "--format=%.18i %.9P %.8j %.8u %.8T %.10M %.9l %.6D %R"
    cli_params = {
        "--long": True,
        "--json": False,
    }
    response = MockJobsResponse()
    result = V39SlurmAPIClientWrapper.process_squeue_output(cli_params, response)
    assert "JOBID" in result, "Long format should contain job id."
    assert "PARTITION" in result, "Long format should contain partition."
    assert "NAME" in result, "Long format should contain job name."
    assert "USER" in result, "Long format should contain user name."
    assert "STATE" in result, "Long format should contain full state."
    assert "TIME" in result, "Long format should contain elapsed run time."
    assert "TIME_LIMI" in result, "Long format should contain time limit. (truncated)"
    assert "NODES" in result, "Long format should contain nodes."
    assert "NODELIST(REASON)" in result, "Long format should contain nodelist with reason."

def test_process_squeue_output_format_steps():
   # "--format=%.15i %.8j %.9P %.8u %.9M %N"
    cli_params = {
        "--steps": True,
        "--json": False,
    }
    response = MockJobsResponse()
    result = V39SlurmAPIClientWrapper.process_squeue_output(cli_params, response)
    assert "JOBID" in result, "Steps format should contain job id."
    assert "NAME" in result, "Steps format should contain job name."
    assert "PARTITION" in result, "Steps format should contain partition."
    assert "USER" in result, "Steps format should contain user name."
    assert "TIME" in result, "Steps format should contain elapsed run time."
    assert "NODELIST" in result, "Steps format should contain nodelist without reason."

def test_process_squeue_output_format_galaxy():
   # "--format=%A %t"
    cli_params = {
        "--format": "%A %t",
        "--json": False,
    }
    response = MockJobsResponse()
    result = V39SlurmAPIClientWrapper.process_squeue_output(cli_params, response)
    assert "JOBID" in result, "Galaxy Pulsar format should contain job id."
    assert "ST" in result, "Galaxy Pulsar format should contain short state."

def test_process_squeue_output_format_arvados():
   # "--format=%j %y %Q %T %r"
    cli_params = {
        "--format": "%j %y %Q %T %r",
        "--json": False,
    }
    response = MockJobsResponse()
    result = V39SlurmAPIClientWrapper.process_squeue_output(cli_params, response)
    assert "NAME" in result, "Galaxy Pulsar format should contain job name."
    assert "NICE" in result, "Galaxy Pulsar format should contain nice priority."
    assert "PRIORITY" in result, "Galaxy Pulsar format should contain raw priority."
    assert "STATE" in result, "Long format should contain full state."
    assert "REASON" in result, "Long format should contain the reason for the current state."

