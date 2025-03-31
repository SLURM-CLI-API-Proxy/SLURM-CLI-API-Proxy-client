import yaml
import os
from pathlib import Path
import argparse
from typing import List
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings

def build_parser(mappings:CliToJsonPayloadMappings):

    args_type_to_python_type_map = {"str":str,"int":int,"bool":bool,"list":list}

    #local_path = Path(__file__).resolve().parent
    #sbatch_args_metadata = yaml.safe_load(open(config_path))
    parser = argparse.ArgumentParser()

    #Is there an rgument followed by a space-separated key-value pairs (e.g. argz Propx=A Propy=B)?
    #Currently the CLI parser support only one
    kvargument_included = False        

    #Arguments that are subcommands, that is, arguments that have their own set of sub-arguments
    #e.g, sxxxxxx update ValX=2 ValB=3
    #     syyyyyy delete 12345
    subcommand_choices:List[str] = []

    for arg in mappings.arguments_list:

        # CLI options with no arguments
        if arg['data_type'] == "bool":
            if (arg['abbreviation'] is None):            
                parser.add_argument(arg['name'],                                                                           help="", required=arg['is_mandatory'], action='store_true')            
            else:        
                parser.add_argument(arg['abbreviation'],arg['name'],                                                       help="", required=arg['is_mandatory'], action='store_true')
        # CLI 'command' arguments followed by key-value sets, e.g., 
        elif arg['data_type'] == "subcommand":            
            subcommand_choices.append(arg['name'])
        else:
            if (arg['abbreviation'] == None):            
                parser.add_argument(arg['name'],                     type= args_type_to_python_type_map[arg['data_type']], help="", required=arg['is_mandatory'])            
            else:        
                parser.add_argument(arg['abbreviation'],arg['name'], type= args_type_to_python_type_map[arg['data_type']], help="", required=arg['is_mandatory'])


    if len(subcommand_choices)>0:
        parser.add_argument('subcommand', nargs='?', choices=subcommand_choices, help='command cmd-arg1 cmd-arg2', default=None)
        parser.add_argument('subcommand_args', nargs='*', help='Subcommand arguments')


    return parser




# https://stackoverflow.com/questions/23032514/argparse-disable-same-argument-occurrences
# class UniqueStore(argparse.Action):
#     def __call__(self, parser, namespace, values, option_string):
#         if getattr(namespace, self.dest, self.default) is not self.default:
#             parser.error(option_string + " appears several times.")
#         setattr(namespace, self.dest, values)