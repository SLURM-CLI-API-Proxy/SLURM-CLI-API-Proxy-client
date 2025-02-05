import unittest
import openapi_client
from argparse import Namespace


from slurm_api_cli_proxy.client_args_linker.api_request_handler import get_args_linker
from slurm_api_cli_proxy.client_args_linker.args_to_payload_mapper import args_to_request_payload


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
                "api_mapping": {"request_property": "job.environment"}
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
            }
        ]
    }

    def test_payload_build(self):
        """"
        E.g.:
        {
            "script": "#!/bin/bash ...",  
            "job": {
                "environment": ["PATH=/bin/:/usr/bin/:/sbin/"],
                "current_working_directory": "/home/hcadavid",
                "name": "test slurmrestd job",
                "output": "slurm-%j.out"
            }
        }
        """

        script = """"
        #!/bin/bash
        #SBATCH --job-name=file_writer
        #SBATCH --output=%x_%j.out
        #SBATCH --error=%x_%j.err
        #SBATCH --time=1:00
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=1
        #SBATCH --cpus-per-task=1
        echo "Hello from Slurm job $SLURM_JOB_ID!" >> /tmp/output.txt
        # Write content to a file
        """

        args = Namespace(
            export='PATH=/bin/:/usr/bin/:/sbin/',
            job_name = 'jname',
            output = 'slurm-%j.out',
            non_used_arg_a = None,
            non_used_arg_b = None,
        )

        payload_dict = args_to_request_payload(script_content=script,cmd_args=args,sbatch_mappings=self.sbatch_test_param_mappings)

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
        
