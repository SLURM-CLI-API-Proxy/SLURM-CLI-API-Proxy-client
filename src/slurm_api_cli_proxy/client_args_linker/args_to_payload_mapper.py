import argparse
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings



def args_to_request_payload(script_content:str,cmd_args:argparse.Namespace,sbatch_mappings:CliToJsonPayloadMappings)->dict:
    """
    Converts command-line arguments into a payload dictionary for API requests.
    Args:
        script_content (str): The content of the script to be executed.
        cmd_args (argparse.Namespace): The parsed command-line arguments.
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
    
    # Parameters 
    cmd_args_dict = vars(cmd_args)

    request_payload = {}   
    request_payload["script"] = script_content

    for cmd_arg in cmd_args_dict:
        
        # Only checking arguments with a set value
        #TODO include also the 'boolean' (with no value) ones

        if cmd_arg != None:
            
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
                doc_path = arg_mappings['api_mapping']['request_property']

                __add_nested_path(request_payload,doc_path,arg_value)
                
            else:
                raise Exception(f"Command argument not supported or not yet implemented in the CLI Proxy:{original_arg_name}")

    return request_payload


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
