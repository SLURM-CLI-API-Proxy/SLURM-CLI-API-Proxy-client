import argparse

def args_to_request_payload(script_content:str,cmd_args:argparse.Namespace,sbatch_mappings:dict)->dict:
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
    
    
    #params = args_mappings_map['parameters']

    for cmd_arg in cmd_args_dict:
        if cmd_arg != None:
            # argument set in the command line
            pname = cmd_arg
            pval = cmd_args_dict[cmd_arg]

            # look in the mappings for the corresponding property that 
            # must be included on the request payload
                        
            sbatch_mappings['parameters'][f"--{pname.replace('_','-')}"]



    request_payload = {}

    request_payload["script"] = script_content
    request_payload["job"] = {}
    request_payload["job"]["name"] = "noname"

    return request_payload






    pass

