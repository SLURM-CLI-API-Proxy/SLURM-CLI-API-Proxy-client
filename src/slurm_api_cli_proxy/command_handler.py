from abc import ABC, abstractmethod
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
from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import SlurmCommandResponse, get_slurm_api_client_wrapper,ApiClientException
from slurm_api_cli_proxy.client_args_linker.args_to_payload_mapper import args_to_sbatch_request_payload,args_to_parameters_dict,args_to_scontrol_request_payload,UnsuportedArgumentException
from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import SlurmAPIClientWrapper
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


class CommandEvaluator(ABC):

    input_file_argument_name = 'proxy_cli_input_file'

    @abstractmethod
    def process_command_args(self,slurm_cli_wrapper:SlurmAPIClientWrapper,cli_args,command_mappings_config:CliToJsonPayloadMappings,configuration:openapi_client.Configuration,slurm_jwt:str)->SlurmCommandResponse:
        """
        This method, when implemented on a concrete class, must process the given arguments (cli_args)
        so that these can be used by the corresponding method, on the slurm_cli_wrapper, that
        performs the required request to the SLURM API.

        This method is not intended to be invoked directly. 

        Args:
            slurm_cli_wrapper (SlurmAPIClientWrapper): An instance of the SLURM API client wrapper 
                used to interact with the SLURM system.
            cli_args: the dictionary given by argparse
            command_mappings_config: the mapping configuration (loaded form the command's YAML file)
            configuration : The open_api client configuration, required to create the API client
            slurm_jwt : the JSON Web Token (JWT) used for authentication with the SLURM API.
        Returns:
            A command response, error code to return
        """
        
        pass


    def eval_command(self,config_file_path:str,include_input_file_arg:bool=False):
        try:
            #Command setup (general)

            #To handle a clean SIGINT (no python runtime stack trace) as the original sbatch.
            #Sbatch has an error code = 130 when aborted (ctrl-c) (codes 129-192 indicate jobs terminated by Linux signals) 
            signal.signal(signal.SIGINT, lambda signum,frame : sys.exit(130))

            squeue_mappings_file_path = pkg_resources.resource_filename(__name__, config_file_path)

            command_mappings_config = CliToJsonPayloadMappings(yaml_config_path=squeue_mappings_file_path)

            #Getting an appropriate SlurmCliWrapper based on the SLURM API Version required        
            slurm_cli_wrapper = get_slurm_api_client_wrapper(command_mappings_config)

            cli_param_parser = build_parser(command_mappings_config)

            if (include_input_file_arg):
                cli_param_parser.add_argument(self.input_file_argument_name, nargs='?', help='Input script')

            cli_args = cli_param_parser.parse_args()

            api_host, slurm_jwt = self.__get_env_vars()

            #API client basic configuratin
            configuration = openapi_client.Configuration(
                host = api_host
            )

            # use the concrete method
            response:SlurmCommandResponse = self.process_command_args(
                cli_args=cli_args,
                slurm_cli_wrapper=slurm_cli_wrapper,
                command_mappings_config=command_mappings_config,
                configuration=configuration,
                slurm_jwt=slurm_jwt
            )

            if (len(response.errors)>0):
                print(response.errors)
                #TODO check if special error codes are required
                return 1
            else:
                print(response.output)
                return 0


        #Errors catched while building the request
        except MissingEnvironmentVar as e:
            print(f"[SLURM_CLI_PROXY_ERROR]: Missing environment variable:{e.missing_var}")
            return 1
        except UnsuportedArgumentException as e:
            print(f"[SLURM_CLI_PROXY_ERROR]: Unsupported argument (or not yet implemented):{e.message}")
            return 1
        except ApiClientException as e:
            #TODO debug log
            print(f"[SLURM_CLI_PROXY_ERROR]: API client exception:{e}")
            return 1
        

    def __get_env_vars(self)->Tuple[str, str]:
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




class SbatchEvaluator(CommandEvaluator):
    def process_command_args(self,slurm_cli_wrapper:SlurmAPIClientWrapper,cli_args,command_mappings_config:CliToJsonPayloadMappings,configuration:openapi_client.Configuration,slurm_jwt:str)->SlurmCommandResponse:

        input_script = None

        if not cli_args.proxy_cli_input_file:
            #If input file is no provided, the script is read from STDIN
            input_script = sys.stdin.read().strip()
        else:
            if os.path.isfile(cli_args.proxy_cli_input_file):
                with open(cli_args.proxy_cli_input_file, 'r') as file:
                    input_script = file.read().strip()
            else:
                return SlurmCommandResponse(errors=[f"sbatch: error: Unable to open file {cli_args.proxy_cli_input_file}\n"])

        #Removing the (provisional) argument used to capture the input file    
        cli_args_dict = vars(cli_args)
        cli_args_dict.pop(self.input_file_argument_name)

        #transforms the values given to the parameters and the script file into a dictionary
        #with the structure required by the JSON file sent by the SLURM API client
        job_request = args_to_sbatch_request_payload(script_content=input_script,cmd_args_dict=cli_args_dict,sbatch_mappings=command_mappings_config)

        response:SlurmCommandResponse = slurm_cli_wrapper.sbatch_post_request(job_request, configuration,slurm_jwt)

        return response


class SqueueEvaluator(CommandEvaluator):
    def process_command_args(self,slurm_cli_wrapper:SlurmAPIClientWrapper,cli_args,command_mappings_config:CliToJsonPayloadMappings,configuration:openapi_client.Configuration,slurm_jwt:str)->SlurmCommandResponse:  

        #dictionary with the arguments/values given to the squeue command
        request_args = args_to_parameters_dict(command_args_dict=vars(cli_args))

        response:SlurmCommandResponse = slurm_cli_wrapper.squeue_get_request(request_args, configuration,slurm_jwt)

        return response


class ScontrolEvaluator(CommandEvaluator):
    def process_command_args(self,slurm_cli_wrapper:SlurmAPIClientWrapper,cli_args,command_mappings_config:CliToJsonPayloadMappings,configuration:openapi_client.Configuration,slurm_jwt:str)->SlurmCommandResponse:    

        request_args, target_job_id = args_to_scontrol_request_payload(cmd_args_dict=vars(cli_args),scontrol_mappings=command_mappings_config)

        response:SlurmCommandResponse = slurm_cli_wrapper.scontrol_update_request(target_job_id=target_job_id,request=request_args,conf=configuration,slurmrestd_token=slurm_jwt)

        return response

class SinfoEvaluator(CommandEvaluator):
    def process_command_args(self,slurm_cli_wrapper:SlurmAPIClientWrapper,cli_args,command_mappings_config:CliToJsonPayloadMappings,configuration:openapi_client.Configuration,slurm_jwt:str)->SlurmCommandResponse:    

        #dictionary with the arguments/values given to the squeue command
        request_args = args_to_parameters_dict(command_args_dict=vars(cli_args))

        response:SlurmCommandResponse = slurm_cli_wrapper.sinfo_get_request(request_args, configuration,slurm_jwt)

        return response


def sbatch():

    eval = SbatchEvaluator()
    eval.eval_command(config_file_path='mappings/sbatch_mappings_r23.11_v0.0.39.yaml',include_input_file_arg=True)


def squeue():

    eval = SqueueEvaluator()
    eval.eval_command(config_file_path='mappings/squeue_mappings_r23.11_v0.0.39.yaml')    


def scontrol():

    eval = ScontrolEvaluator()
    eval.eval_command(config_file_path='mappings/scontrol_mappings_r23.11_v0.0.39.yaml')    


def sinfo():

    eval = SinfoEvaluator()
    eval.eval_command(config_file_path='mappings/sinfo_mappings_r23.11_v0.0.39.yaml')    
    





