import argparse
import sys
import yaml
import os
import signal
from pathlib import Path
import pkg_resources
import traceback
from typing import Tuple
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings
from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import get_slurm_api_client_wrapper,ApiClientException
from slurm_api_cli_proxy.client_args_linker.args_to_payload_mapper import args_to_sbatch_request_payload,args_to_squeue_parameters_dict,args_to_scontrol_request_payload,UnsuportedArgumentException
from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import SbatchResponse
import openapi_client
import logging
from .arguments_evaluator import build_parser


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MissingEnvironmentVar(Exception):    
    def __init__(self, missing_var, message="Required environment variables are missing"):
        self.missing_var = missing_var
        self.message = message
        super().__init__(self.message)


def sbatch():
    #To handle a clean SIGINT (no python runtime stack trace) as the original sbatch.
    #Sbatch has an error code = 130 when aborted (ctrl-c) (codes 129-192 indicate jobs terminated by Linux signals) 
    signal.signal(signal.SIGINT, lambda signum,frame : sys.exit(130))


    sbatch_mappings_file_path = pkg_resources.resource_filename(__name__, 'mappings/sbatch_mappings_r23.11_v0.0.39.yaml')

    cli_to_json_mappings = CliToJsonPayloadMappings(yaml_config_path=sbatch_mappings_file_path)

    #sbatch_args_metadata:dict = yaml.safe_load(open(sbatch_mappings_file_path))

    cli_param_parser = build_parser(cli_to_json_mappings)

    #Additional argument to capture the input file path. 
    cli_param_parser.add_argument('proxy_cli_input_file', nargs='?', help='Input script')

    args = cli_param_parser.parse_args()

    input_script = None

    if not args.proxy_cli_input_file:
        #If input file is no provided, the script is read from STDIN
        input_script = sys.stdin.read().strip()
    else:
        if os.path.isfile(args.proxy_cli_input_file):
            with open(args.proxy_cli_input_file, 'r') as file:
                input_script = file.read().strip()
        else:
            sys.stderr.write(f"sbatch: error: Unable to open file {args.proxy_cli_input_file}\n")
            return 1


    #Removing the (provisional) argument used to capture the input file    
    cli_args_dict = vars(args)
    cli_args_dict.pop('proxy_cli_input_file')

    try:
        #transforms the values given to the parameters and the script file into a dictionary
        #with the structure required by the JSON file sent by the SLURM API client
        job_request = args_to_sbatch_request_payload(script_content=input_script,cmd_args_dict=cli_args_dict,sbatch_mappings=cli_to_json_mappings)

        #Getting an appropriate SlurmCliWrapper based on the SLURM API Version required
        #TODO pass an actual config file (wrapper version is hard coded at the moment)
        slurm_cli_wrapper = get_slurm_api_client_wrapper(cli_to_json_mappings)

        api_host, slurm_jwt = __get_env_vars()

        #API client basic configuratin
        configuration = openapi_client.Configuration(
            host = api_host
        )

        response:SbatchResponse = slurm_cli_wrapper.sbatch_post_request(job_request, configuration,slurm_jwt)

        if (len(response.errors)>0):
            print(response.errors)
            #TODO check if special error codes are required
            return 1
        else:
            print(f"Submitted batch job {response.job_id}")
            return 0

    #Errors catched while building the request
    except MissingEnvironmentVar as e:
        print(f"[SLURM_CLI_PROXY_ERROR]: Missing environment variable:{e.missing_var}")
        return 1
    except UnsuportedArgumentException as e:
        print(f"[SLURM_CLI_PROXY_ERROR]: Unsupported argument (or not yet implemented):{e.argument}")
        return 1
    except Exception as e:
        #TODO debug log
        print(e)
        print(f"[SLURM_CLI_PROXY_ERROR] - Unexpected error:{e}")
        return 1


def squeue():

    #To handle a clean SIGINT (no python runtime stack trace) as the original sbatch.
    #Sbatch has an error code = 130 when aborted (ctrl-c) (codes 129-192 indicate jobs terminated by Linux signals) 
    signal.signal(signal.SIGINT, lambda signum,frame : sys.exit(130))

    squeue_mappings_file_path = pkg_resources.resource_filename(__name__, 'mappings/squeue_mappings_r23.11_v0.0.39.yaml')

    cli_to_json_mappings = CliToJsonPayloadMappings(yaml_config_path=squeue_mappings_file_path)

    cli_param_parser = build_parser(cli_to_json_mappings)

    cli_args = cli_param_parser.parse_args()

    #dictionary with the arguments/values given to the squeue command
    request_args = args_to_squeue_parameters_dict(squeue_args_dict=vars(cli_args))

    try:

        #Getting an appropriate SlurmCliWrapper based on the SLURM API Version required        
        slurm_cli_wrapper = get_slurm_api_client_wrapper(cli_to_json_mappings)

        api_host, slurm_jwt = __get_env_vars()

        #API client basic configuratin
        configuration = openapi_client.Configuration(
            host = api_host
        )

        response = slurm_cli_wrapper.squeue_get_request(request_args, configuration,slurm_jwt)

        if (len(response.slurm_errors)>0):
            print(response.slurm_errors)
            #TODO check if special error codes are required
            return 1
        else:
            print(response.pre_processed_output)
            return 0

    #Errors catched while building the request
    except MissingEnvironmentVar as e:
        print(f"[SLURM_CLI_PROXY_ERROR]: Missing environment variable:{e.missing_var}")
        return 1
    except UnsuportedArgumentException as e:
        print(f"[SLURM_CLI_PROXY_ERROR]: Unsupported argument (or not yet implemented):{e.argument}")
        return 1
    except ApiClientException as e:
        #TODO debug log
        print(f"[SLURM_CLI_PROXY_ERROR]: API client exception:{e}")
        return 1


def scontrol():

    #To handle a clean SIGINT (no python runtime stack trace) as the original sbatch.
    #Sbatch has an error code = 130 when aborted (ctrl-c) (codes 129-192 indicate jobs terminated by Linux signals) 
    signal.signal(signal.SIGINT, lambda signum,frame : sys.exit(130))

    scontrol_mappings_file_path:str = pkg_resources.resource_filename(__name__, 'mappings/scontrol_mappings_r23.11_v0.0.39.yaml')

    cli_to_json_mappings = CliToJsonPayloadMappings(yaml_config_path=scontrol_mappings_file_path)

    cli_param_parser = build_parser(cli_to_json_mappings)

    cli_args = cli_param_parser.parse_args()

    request_args: dict
    target_job_id: str

    request_args, target_job_id = args_to_scontrol_request_payload(cmd_args_dict=vars(cli_args),scontrol_mappings=cli_to_json_mappings)
    
    try:
        #Getting an appropriate SlurmCliWrapper based on the SLURM API Version required        
        slurm_cli_wrapper = get_slurm_api_client_wrapper(cli_to_json_mappings)

        api_host, slurm_jwt = __get_env_vars()

        #API client basic configuratin
        configuration = openapi_client.Configuration(
            host = api_host
        )

        response = slurm_cli_wrapper.scontrol_update_request(target_job_id=target_job_id,request=request_args,conf=configuration,slurmrestd_token=slurm_jwt)

    #Errors catched while building the request
    except MissingEnvironmentVar as e:
        print(f"[SLURM_CLI_PROXY_ERROR]: Missing environment variable:{e.missing_var}")
        return 1
    except UnsuportedArgumentException as e:
        print(f"[SLURM_CLI_PROXY_ERROR]: Unsupported argument (or not yet implemented):{e.argument}")
        return 1
    except ApiClientException as e:
        #TODO debug log
        print(f"[SLURM_CLI_PROXY_ERROR]: API client exception:{e}")
        return 1




def __get_env_vars()->Tuple[str, str]:
    """
    Retrieves the required environment variables for SLURM API proxy.
    This function checks for the presence of the "SLURM_JWT" and "PROXY_SLURM_API_URL"
    environment variables. 
    Returns:
        Tuple[str, str]: A tuple containing the values of "PROXY_SLURM_API_URL" and "SLURM_JWT"
                            environment variables, respectively.
    Raises:
        MissingEnvironmentVar: If either "SLURM_JWT" or "PROXY_SLURM_API_URL" environment 
                                variable is not set.
    """

    if "SLURM_JWT" not in os.environ:
        raise MissingEnvironmentVar(missing_var="SLURM_JWT")
    
    if "PROXY_SLURM_API_URL" not in os.environ:
        raise MissingEnvironmentVar(missing_var="PROXY_SLURM_API_URL")

    return os.environ["PROXY_SLURM_API_URL"],os.environ["SLURM_JWT"]
