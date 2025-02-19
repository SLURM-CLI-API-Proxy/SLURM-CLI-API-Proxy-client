import unittest
import openapi_client
import os
from argparse import Namespace


from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import get_slurm_api_client_wrapper
from slurm_api_cli_proxy.client_args_linker.args_to_payload_mapper import args_to_sbatch_request_payload
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings

class PayloadBuildTest(unittest.TestCase):

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

    

    def test_payload_build(self):
        """
        Test the payload building process for SLURM job submission.
        This test verifies that the function `args_to_sbatch_request_payload` correctly
        converts command-line arguments into a dictionary suitable for generating a JSON
        payload for SLURM job submission.
        The test uses a Namespace object created by argparse with the following arguments:
        """
        

        #Namespace object created by argparse when input is
        #sbatch --export PATH=/bin/:/usr/bin/:/sbin/ --job-name jname --chdir /home/testuser --output slurm-%j.out 
        args = Namespace(
            export='PATH=/bin/:/usr/bin/:/sbin/',
            job_name = 'jname',
            chdir = '/home/testuser',
            output = 'slurm-%j.out',
            #simulating a non-used argument, which should be ignored
            ignored_arg = None
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

        payload_dict = args_to_sbatch_request_payload(script_content=script,cmd_args_dict=vars(args),sbatch_mappings=mappings)

        assert payload_dict == expected_output


    def test_payload_build_default_values(self):
        """
        Test the payload building when no values are given to arguments that are not mandatory on the CLI but on the API request.
        This test verifies that the payload is generated with default values when mandatory values are not given.
        """


        #Namespace object created by argparse when input is
        #sbatch --job-name jname
        args = Namespace(
            job_name = 'jname',
            chdir = '/home/testuser'
        )

        script = "#!/bin/bash"

        #Expected generated dictionary (which would be used for generating the JSON payload)
        #The mandatory environment property must be included even when no specified with --export
        expected_output = {
            "script": "#!/bin/bash",  
            "job": {
                "environment": ["ALL"],
                "current_working_directory": "/home/testuser",
                "name": "jname",
            }
        }

        mappings = CliToJsonPayloadMappings(config_mapping_dict=self.sbatch_test_param_mappings)

        payload_dict = args_to_sbatch_request_payload(script_content=script,cmd_args_dict=vars(args),sbatch_mappings=mappings)

        assert payload_dict == expected_output

