import unittest
import openapi_client

from slurm_api_cli_proxy.client_args_linker.api_request_handler import get_args_linker


class PayloadBuildTest(unittest.TestCase):

    def test_payload_build(self):
        assert False


    def test_submission(self):
        #TODO to be replaced with embedded/containerized SLURM API launched by the CI/CD env
        
        configuration = openapi_client.Configuration(
            host = "http://slurm-controller:6820"
        )

        job_request = {
            "script": """#!/bin/bash
                ls > /tmp/temp_file.txt
                sleep 10
                """,  
            "job": {
                "environment": ["PATH=/bin/:/usr/bin/:/sbin/"],
                "current_working_directory": "/home/tmp",
                "name": "test slurmrestd job",
                "output": "slurm-%j.out"
            }
        }

        req_handler = get_args_linker({})

        response = req_handler.sbatch_post_request(job_request, configuration)
        
        assert (len(response.errors)==0)
        
