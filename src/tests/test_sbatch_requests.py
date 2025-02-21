import unittest
import openapi_client
import os
import pytest
from argparse import Namespace


from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import get_slurm_api_client_wrapper
from slurm_api_cli_proxy.client_args_linker.args_to_payload_mapper import args_to_sbatch_request_payload
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings

class ApiRequestsTest(unittest.TestCase):

    sbatch_test_param_mappings = {
        "mapping_meta": {
            "command": "sbatch",
            "api_version": "0.0.39",
            "api_client_payload_class": "V0039JobSubmission",
            "wlm_release": "23.11",
            "wrapper_package": "slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39",
            "wrapper_class": "V39SlurmAPIClientWrapper"
        },
        "parameters": [
            {
                "name": "--export",
                "abbreviation": "--export",
                "is_mandatory": False,
                "data_type": "str",
                "api_mapping": {
                                "request_property": "job.environment",
                                "lambda_expression": "lambda p: p.split(',')"
                                }
            },
            {
                "name": "--job-name",
                "abbreviation": "-J",
                "is_mandatory": False,
                "data_type": "str",
                "api_mapping": {"request_property": "job.name"}
            },
            {
                "name": "--output",
                "abbreviation": "-o",
                "is_mandatory": False,
                "data_type": "str",
                "api_mapping": {"request_property": "job.output"}
            },
            {
                "name": "--chdir",
                "abbreviation": "-D",
                "is_mandatory": False,
                "data_type": "str",
                "api_mapping": {"request_property": "job.current_working_directory"}
            },
            {
                "name": "--ignored-arg",
                "abbreviation": "-NA",
                "is_mandatory": False,
                "data_type": "str",
                "api_mapping": {"request_property": "should.not.be.included"}
            }


        ]
    }


    @pytest.mark.integration
    def test_sbatch_post_request(self):
        
        
        configuration = openapi_client.Configuration(
            host = "http://localhost:6821"
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

        mappings = CliToJsonPayloadMappings(config_mapping_dict=self.sbatch_test_param_mappings)

        req_handler = get_slurm_api_client_wrapper(mappings)

        slurm_jwt = os.environ["SLURM_JWT"]

        response = req_handler.sbatch_post_request(job_request, configuration, slurmrestd_token=slurm_jwt)
        

        assert (len(response.errors)==0)
        
