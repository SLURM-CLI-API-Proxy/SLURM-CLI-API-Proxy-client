import yaml
import os
from pathlib import Path
import argparse

def build_parser(config_path:str):

    local_path = Path(__file__).resolve().parent
    sbatch_args_metadata = yaml.safe_load(open(config_path))
    parser = argparse.ArgumentParser()

    for arg in sbatch_args_metadata['parameters']:

        arg_data_type = __get_python_type(arg['data_type'])

        # CLI options with no arguments
        if arg_data_type is bool:
            if (arg['abbreviation'] is None):            
                parser.add_argument(arg['name'],                     help="", required=arg['is_mandatory'], action='store_true')            
            else:        
                parser.add_argument(arg['abbreviation'],arg['name'], help="", required=arg['is_mandatory'], action='store_true')
        # CLI options with specific type of argument
        else:
            if (arg['abbreviation'] is None):            
                parser.add_argument(arg['name'],                     type= arg_data_type, help="", required=arg['is_mandatory'])            
            else:        
                parser.add_argument(arg['abbreviation'],arg['name'], type= arg_data_type, help="", required=arg['is_mandatory'])


    return parser


def __get_python_type(type_str):
    if (type_str == "str"):
        return str
    elif (type_str == "int"):
        return int



# https://stackoverflow.com/questions/23032514/argparse-disable-same-argument-occurrences
class UniqueStore(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        if getattr(namespace, self.dest, self.default) is not self.default:
            parser.error(option_string + " appears several times.")
        setattr(namespace, self.dest, values)