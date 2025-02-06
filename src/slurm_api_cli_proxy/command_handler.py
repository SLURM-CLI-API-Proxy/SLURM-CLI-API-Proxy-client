import argparse
import sys
import yaml
import os
import signal
from pathlib import Path
import pkg_resources
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings
from .arguments_evaluator import build_parser


def sbatch():

    #To handle a clean SIGINT (no python runtime stack trace) as the original sbatch.
    #Sbatch has an error code = 130 when aborted (ctrl-c) (codes 129-192 indicate jobs terminated by Linux signals) 
    signal.signal(signal.SIGINT, lambda signum,frame : sys.exit(130))

    sbatch_mappings_file_path = pkg_resources.resource_filename(__name__, 'mappings/sbatch_mappings_alt.yaml')

    cli_to_json_mappings = CliToJsonPayloadMappings(yaml_config_path=sbatch_mappings_file_path)

    #sbatch_args_metadata:dict = yaml.safe_load(open(sbatch_mappings_file_path))

    cli_param_parser = build_parser(cli_to_json_mappings)

    #Additional argument for the input file. 
    cli_param_parser.add_argument('input_file', nargs='?', help='Input script')

    args = cli_param_parser.parse_args()

    input_script = None

    if not args.input_file:
        #If input file is no provided, the script is read from STDIN
        input_script = sys.stdin.read().strip()
    else:
        if os.path.isfile(args.input_file):
            with open(args.input_file, 'r') as file:
                input_script = file.read().strip()
        else:
            sys.stderr.write(f"sbatch: error: Unable to open file {args.input_file}\n")
            return 1

    print(f"running sbatch with arguments:{args}. Script to be sent: {input_script}")
    print(type(args))
    return 0

def squeue():
    print(f"running squeue with arguments:{sys.argv}")

