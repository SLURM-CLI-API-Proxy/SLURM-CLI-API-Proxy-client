import argparse
import sys

def sbatch():
    print(f"running sbatch with arguments:{sys.argv}")

def squeue():
    print(f"running squeue with arguments:{sys.argv}")
