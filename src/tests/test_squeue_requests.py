import unittest
import openapi_client
import os
import pytest
from argparse import Namespace


from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import get_slurm_api_client_wrapper
from slurm_api_cli_proxy.client_args_linker.args_to_payload_mapper import args_to_parameters_dict
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings

class ApiRequestsTest(unittest.TestCase):

    squeue_test_param_mappings = {
        "mapping_meta": {
            "command": "squeue",
            "api_version": "0.0.39",
            "wlm_release": "23.11",
            "wrapper_package": "slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39",
            "wrapper_class": "V39SlurmAPIClientWrapper"
        },
        "parameters": [
            {
                "name": "--user",
                "abbreviation": "-u",
                "is_mandatory": False,
                "data_type": "str"
            },
            {
                "name": "--name",
                "abbreviation": "--name",
                "is_mandatory": False,
                "data_type": "str"
            },
            {
                "name": "--json",
                "abbreviation": "--json",
                "is_mandatory": False,
                "data_type": "bool"
            }
        ]        
    }

    def test_squeue_get_request(self):
                
        configuration = openapi_client.Configuration(
            host = "http://localhost:6821"
        )

        cli_to_json_mappings = CliToJsonPayloadMappings(config_mapping_dict=self.squeue_test_param_mappings)

        #Simulating the result of argparse.parse_args() with no arguments given on the CLI
        cli_args = Namespace(
            user=None, name=None, json=False
        )

        request_args = args_to_parameters_dict(command_args_dict=vars(cli_args))

        slurm_cli_wrapper = get_slurm_api_client_wrapper(cli_to_json_mappings)

        slurm_jwt = os.environ["SLURM_JWT"]
        
        response = slurm_cli_wrapper.squeue_get_request(request_args, configuration,slurm_jwt)

        assert response.output.lstrip().startswith("JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)")


        
