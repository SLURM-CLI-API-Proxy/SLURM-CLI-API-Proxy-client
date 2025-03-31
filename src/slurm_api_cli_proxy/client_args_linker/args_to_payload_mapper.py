import argparse
from typing import Dict, Any, Tuple
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings
import os

class InternalConfigurationException(Exception):
    def __init__(self, message):
        self.message = message        
        super().__init__(self.message)


class UnsuportedArgumentException(Exception):
    argument:str

    def __init__(self, message, argument=None):
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



def args_to_scontrol_request_payload(cmd_args_dict:dict,scontrol_mappings:CliToJsonPayloadMappings)->Tuple[dict,str]:
    """
    Maps command-line arguments to a payload structure for an `scontrol` request.
    This function processes the command-line arguments provided in `cmd_args_dict` and maps them to a 
    structured payload dictionary based on the mappings defined in `scontrol_mappings`. It supports 
    subcommands and their respective arguments, validating them against the accepted configurations.
    Args:
        cmd_args_dict (dict) <- what was received as arguments from the CLI 
            A dictionary containing the command-line arguments. It must include:
            - 'subcommand': The subcommand to be executed.
            - 'subcommand_args': A list of arguments for the subcommand in the form of key=value pairs.
        scontrol_mappings (CliToJsonPayloadMappings): <- the mapping configuration (how the arguments should
                be transformed into an API request JSON payload)
            An object containing the mappings from CLI arguments to JSON payload properties. 
    Returns:
        Tuple[dict, int]: 
            - A dictionary representing the request payload to be sent to the API.
            - The target job ID captured through the CLI 
    Raises:
        UnsuportedArgumentException: 
            - If no subcommand is provided in `cmd_args_dict`.
            - If an unsupported or invalid argument is provided for the subcommand.
    """

    target_job_id:str

    # Payload to be returned (the one to be used on the API request)
    request_payload:Dict[str,Any] = {}

    # Payload properties required by default
    request_payload["environment"]=["ALL"]
    
    # Subcommand received from the CLI
    subcommand = cmd_args_dict['subcommand']

    # scontrol works in interactive mode if no command is given. This is not supported by the proxy
    if (subcommand == None):
        raise UnsuportedArgumentException(f"scontrol: interactive mode is not supported - a command is required.")

    # Some subcommands of 'scontrol' have implicit payload properties that need to be included
    # regardless of the arguments given. e.g., scontrol relase requires including 'hold=false'. 
    # These are defined on the optional request_property_value of the 'subcommand' entries.
    if 'request_property_value' in scontrol_mappings.arguments_dict[subcommand]:
        default_payload_entries:dict = scontrol_mappings.arguments_dict[subcommand]['request_property_value']
        for default_payload_entry in default_payload_entries.keys():
            request_payload[default_payload_entry] = default_payload_entries[default_payload_entry]

    # Some subcommands of scontrol have 'specifications' in the form of a series of key-value entries. These
    # are defined in the 'subcommand_specs' in the corresponding YAML file
    if 'subcommand_specs' in scontrol_mappings.arguments_dict[subcommand]:

        # Arguments settings that are accepted according to the YML config
        accepted_subcommand_args:dict = scontrol_mappings.arguments_dict[subcommand]['subcommand_specs']

        # Arguments/settings given to the sub-command
        subcommand_args_dict:dict[str,str] = __parse_sub_command_specs(cmd_args_dict['subcommand_args'],subcommand)

        for subcommand_arg in subcommand_args_dict.keys():
            if (subcommand_arg in accepted_subcommand_args.keys()):
                
                #Get the property name used on the payload (defined on the YAML)
                pname = accepted_subcommand_args[subcommand_arg]['api_mapping']
                ptype = accepted_subcommand_args[subcommand_arg]['data_type']

                #Get the value set on the CLI
                svalue=subcommand_args_dict[subcommand_arg]

                try:                    
                    if (ptype == "int"):
                        request_payload[pname] = int(svalue)
                    elif (ptype == "str"):
                        request_payload[pname] = str(svalue)
                    else:
                        raise InternalConfigurationException(f"[SLURM_CLI_PROXY_ERROR] Scontrol - Internal misconfiguration error: type {ptype} is not supported for command's key-value properties")
                except ValueError as e:
                    raise UnsuportedArgumentException(f"Scontrol - an {ptype} value is expected for {subcommand_arg} key-value argument")                    

            else:
                raise UnsuportedArgumentException(f"Invalid or unsupported specification of the {subcommand} command:{subcommand_arg}",subcommand_arg)

        # if the job_id was set by one of the commands specifications, remove it from the payload
        # and use it as the target job id.
        if ("job_id" in request_payload):
            target_job_id = request_payload.pop("job_id")
        else:
            raise UnsuportedArgumentException(f"No jobid was provided to the scrontrol command:  {subcommand}")
    
    # The given subcommand requires a single argument. 
    # Note: this implementation only supports scontrol 'commands' with the jobid as their only argument
    elif 'subcommand_arg' in scontrol_mappings.arguments_dict[subcommand]:
        num_args = len(cmd_args_dict['subcommand_args'])
        if num_args == 0:
            raise UnsuportedArgumentException(f"Too few arguments for {subcommand}")
        elif num_args > 1:
            raise UnsuportedArgumentException(f"Only one argument is supported for {subcommand}")
        else:
            target_job_id = cmd_args_dict['subcommand_args'][0]            

    return request_payload, str(target_job_id)


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


def __parse_sub_command_specs(pairs: list[str],command:str) -> dict[str, str]:
    """
    Converts a list of strings in the form 'a=x' into a dictionary.

    Args:
        pairs (list[str]): A list of strings in the form 'a=x'.

    Returns:
        dict[str, str]: A dictionary where the key is 'a' and the value is 'x'.
    """
    result = {}
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)  # Split into key and value at the first '='
            result[key] = value
        else:
            raise ValueError(f"Invalid format for the {command} command specification: {pair}. Expected 'key=value' or an int value.")
    return result