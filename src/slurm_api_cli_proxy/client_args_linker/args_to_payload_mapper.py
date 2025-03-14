import argparse
from typing import Dict, Any
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings
import os

class UnsuportedArgumentException(Exception):
    argument:str

    def __init__(self, message, argument):
        self.message = message
        self.argument = argument
        super().__init__(self.message)

def args_to_sbatch_request_payload(script_content:str,cmd_args_dict:dict,sbatch_mappings:CliToJsonPayloadMappings)->dict:
    """
    Converts sbatch command-line arguments into a payload dictionary for slurmrestd API requests.
    Args:
        script_content (str): The content of the script to be executed.
        cmd_args : a dictionary with the arguments parsed from the CLI, using the
            naming conventions of argparse (--job-name -> job_name). Eg:
            {'export': 'PATH=/bin/:/usr/bin/:/sbin/', 
             'job_name': 'jname', 
             'chdir': '/home/testuser'}
        sbatch_mappings (dict): A dictionary mapping sbatch parameters to their values.
    Returns:
        dict: A dictionary representing the payload to be sent in the API request.
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
    

    request_payload:Dict[str,Any] = {}
    request_payload["job"]={}
    request_payload["script"] = script_content

    #Default values for properties that are optional on the CLI, but are mandatory for the API Client request.
    #These value will be overriden if used when invoking the sbatch command.
    
    #TODO to be defined on the YAML file
    request_payload["job"]["environment"]=["ALL"]
    request_payload["job"]["current_working_directory"] = os.getcwd()

    for cmd_arg in cmd_args_dict:
        
        cmd_arg_value = cmd_args_dict[cmd_arg]

        # Ignore arguments that were not used on the cli: str/int arguments with a None value, 
        #   or bool arguments ('flag' arguments with no value, which are True when included)
        if cmd_arg_value != None and cmd_arg_value != False:            
            # argument name using argparse naming conventions (arg_x)
            arg_name = cmd_arg

            # original argument used by the CLI (--arg-x)
            original_arg_name = f"--{arg_name.replace('_','-')}"

            # value given to the argument            
            arg_value = cmd_args_dict[cmd_arg]

            # look in the mappings for the corresponding property that 
            # must be included on the request payload
            arg_mappings = sbatch_mappings.arguments_dict[original_arg_name]
            
            if 'api_mapping' in arg_mappings:
                ## path within the dictionary/JSON doc where the property will be included
                doc_path = arg_mappings['api_mapping']['request_property']
                
                ## if a lambda expression is included, it is used to pre-process the value
                if 'lambda_expression' in arg_mappings['api_mapping']:
                    preproc_func = eval(arg_mappings['api_mapping']['lambda_expression'])
                    arg_value = preproc_func(arg_value)

                __add_nested_path(request_payload,doc_path,arg_value)
                
            else:
                raise UnsuportedArgumentException("Command argument not supported or not yet implemented in the CLI Proxy",original_arg_name)

    return request_payload



def args_to_squeue_parameters_dict(squeue_args_dict:dict)->dict:
    """
    Get a dictionary with the arguments given in the CLI

    Args:
        cmd_args_dict : a dictionary with the squeue arguments parsed from the CLI, using the
            naming conventions of argparse (--job-name -> job_name).    
    Returns:
        dict: A dictionary with the squeue arguments using the original naming conventions of the arguments
    """

    squeue_request_params = {}

    for cmd_arg in squeue_args_dict:
        
        # Only checking arguments with an assigned value
        if squeue_args_dict[cmd_arg] != None:            
            # argument name using argparse naming conventions (e.g, arg_x)
            arg_name = cmd_arg

            # original argument used by the CLI (e.g., --arg-x)
            original_arg_name = f"--{arg_name.replace('_','-')}"

            # value given to the argument            
            arg_value = squeue_args_dict[cmd_arg]
            
            squeue_request_params[original_arg_name]=arg_value

    return squeue_request_params


def __add_nested_path(dictionary:dict, path:str, value=None):
    """Add nested properties to dictionary based on a dotted path."""
    parts = path.split('.')
    
    current = dictionary
    for part in parts[:-1]:  # Handle all but the last part
        current.setdefault(part, {})
        current = current[part]
    
    # Set the final value
    current[parts[-1]] = value
    
    return dictionary
