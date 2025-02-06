import unittest
import openapi_client
from argparse import Namespace


from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import get_slurm_api_client
from slurm_api_cli_proxy.client_args_linker.args_to_payload_mapper import args_to_request_payload
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings

class PayloadBuildTest(unittest.TestCase):

    sbatch_test_param_mappings = {
        "mapping_meta": [
            {"command": "sbatch"},
            {"api_version": "0.0.39"},
            {"api_client_payload_class": "V0039JobSubmission"}
        ],
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
            }

        ]
    }

    def test_payload_build(self):

        #Namespace object created by argparse when input is
        #sbatch --export PATH=/bin/:/usr/bin/:/sbin/ --job-name jname --chdir /home/testuser --output slurm-%j.out 
        args = Namespace(
            export='PATH=/bin/:/usr/bin/:/sbin/',
            job_name = 'jname',
            chdir = '/home/testuser',
            output = 'slurm-%j.out'
        )
        
        script = "#!/bin/bash"

        #Expected generated dictionary (which would be used for generating the JSON payload)
        expected_output = {
            "script": "#!/bin/bash",  
            "job": {
                "environment": ["PATH=/bin/:/usr/bin/:/sbin/"],
                "current_working_directory": "/home/testuser",
                "name": "jname",
                "output": "slurm-%j.out"
            }
        }

        mappings = CliToJsonPayloadMappings(config_mapping_dict=self.sbatch_test_param_mappings)

        payload_dict = args_to_request_payload(script_content=script,cmd_args=args,sbatch_mappings=mappings)

        assert payload_dict == expected_output


    def xxtest_submission(self):
        
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

        req_handler = get_slurm_api_client({})

        response = req_handler.sbatch_post_request(job_request, configuration)
        
        assert (len(response.errors)==0)
        
