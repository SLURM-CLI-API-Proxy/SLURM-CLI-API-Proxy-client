import yaml
import os
from pathlib import Path
import argparse
import shlex
from typing import List
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings

def build_parser(mappings:CliToJsonPayloadMappings):

    args_type_to_python_type_map = {"str":str,"int":int,"bool":bool}

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





def sbatch_directive_tokens(script: str) -> List[str]:
    """
    Collects the options given as '#SBATCH' directives in a job script.

    Like sbatch, directives are read from the top of the script until the first line
    that is neither blank nor a comment. Text after a '#' inside a directive is a
    comment. E.g. '#SBATCH -J job  # name' -> ['-J', 'job'].
    """
    tokens: List[str] = []
    for line in script.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if not stripped.startswith("#"):
            break
        if stripped.startswith("#SBATCH"):
            tokens.extend(shlex.split(stripped[len("#SBATCH"):], comments=True))
    return tokens


class DirectiveError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def parse_sbatch_directives(mappings: CliToJsonPayloadMappings, script: str) -> dict:
    """
    Parses a script's '#SBATCH' directives with the same option definitions as the
    sbatch command line. Returns the options that were set (argparse names).

    The SLURM REST API does not process '#SBATCH' lines in the submitted script, so the
    proxy has to apply them itself (as sbatch does on the client side).

    Raises:
        DirectiveError: for directives that the proxy does not support or that are invalid
    """
    tokens = sbatch_directive_tokens(script)
    if not tokens:
        return {}
    parser = build_parser(mappings)
    parser.exit_on_error = False
    try:
        namespace, unknown = parser.parse_known_args(tokens)
    except (argparse.ArgumentError, SystemExit) as e:
        raise DirectiveError(f"invalid #SBATCH directive: {e}") from e
    if unknown:
        raise DirectiveError(f"unsupported #SBATCH directive(s): {' '.join(unknown)}")
    return {k: v for k, v in vars(namespace).items() if v is not None and v is not False}
