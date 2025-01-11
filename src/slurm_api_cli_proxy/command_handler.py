import argparse
import sys
import yaml
import os
from pathlib import Path
from .arguments_evaluator import build_parser

def sbatch():
    
    local_path = Path(__file__).resolve().parent
    cli_param_parser = build_parser(os.path.join(local_path,"mappings","sbatch_mappings_alt.yaml"))

    args = cli_param_parser.parse_args()

    print(f"running sbatch with arguments:{args}")

def squeue():
    print(f"running squeue with arguments:{sys.argv}")

