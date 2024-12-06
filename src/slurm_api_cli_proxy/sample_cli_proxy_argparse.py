import argparse
import os
import subprocess
import sys

def submit_job(script, output=None, error=None, time=None, nodes=None, ntasks=None, cpus=None, mem=None):
    """Submit a job to Slurm"""
    
    # Prepare sbatch command
    sbatch_cmd = ["sbatch"]
    
    # Add output and error files
    if output:
        sbatch_cmd.extend(["-o", output])
    else:
        output = f"slurm-{os.getpid()}.out"
        sbatch_cmd.extend(["-o", output])
    
    if error:
        sbatch_cmd.extend(["-e", error])
    else:
        error = f"slurm-{os.getpid()}.err"
        sbatch_cmd.extend(["-e", error])
    
    # Add time limit if provided
    if time:
        sbatch_cmd.extend(["--time", str(time)])
    
    # Add resource constraints
    if nodes:
        sbatch_cmd.extend(["--nodes", str(nodes)])
    if ntasks:
        sbatch_cmd.extend(["--ntasks", str(ntasks)])
    if cpus:
        sbatch_cmd.extend(["--cpus-per-task", str(cpus)])
    if mem:
        sbatch_cmd.extend(["--mem-per-cpu", mem])
    
    # Add script to the command
    sbatch_cmd.append(script)
    
    try:
        print(f"Sbatch command: {sbatch_cmd}")
    except subprocess.CalledProcessError as e:
        print(f"Error submitting job: {e.stderr}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Submit a job to Slurm")
    
    parser.add_argument('script', type=str, help='Path to the script to run')
    parser.add_argument('--output', type=str, default=None, help='Output file name')
    parser.add_argument('--error', type=str, default=None, help='Error file name')
    parser.add_argument('--time', type=str, default=None, help='Time limit for the job')
    parser.add_argument('--nodes', type=int, default=None, help='Number of nodes')
    parser.add_argument('--ntasks', type=int, default=None, help='Number of tasks')
    parser.add_argument('--cpus', type=int, default=None, help='Number of CPUs per node')
    parser.add_argument('--mem', type=str, default=None, help='Memory per CPU (e.g., 1G)')
    
    args = parser.parse_args()
    
    submit_job(args.script, args.output, args.error, args.time, args.nodes, args.ntasks, args.cpus, args.mem)

if __name__ == "__main__":
    main()