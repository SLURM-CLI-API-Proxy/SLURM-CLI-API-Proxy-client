import click
import os
import subprocess

@click.group()
def cli():
    pass

@cli.command()
@click.argument('script', type=click.Path(exists=True))
@click.option('--job-name', default=None)
@click.option('--output', default=None)
@click.option('--error', default=None)
@click.option('--time', type=float, help='Time limit for the job')
@click.option('--nodes', type=int, help='Number of nodes')
@click.option('--ntasks', type=int, help='Number of tasks')
@click.option('--cpus', type=int, help='Number of CPUs per node')
@click.option('--mem', type=str, help='Memory per CPU (e.g., 1G)')
def submit(script, job_name, output, error, time, nodes, ntasks, cpus, mem):
    """Submit a job to Slurm"""
    
    # Validate and prepare options
    if not script:
        raise click.ClickException("Script file is required")
    
    if not output:
        output = f"slurm-{os.getpid()}.out"
    if not error:
        error = f"slurm-{os.getpid()}.err"
    
    # Prepare sbatch command
    sbatch_cmd = ["sbatch"]
    
    # Add job name if provided
    if job_name:
        sbatch_cmd.extend(["-J", job_name])
    
    # Add output and error files
    sbatch_cmd.extend(["-o", output, "-e", error])
    
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
    
    # Execute the sbatch command
    try:
        print(f"Requesting {sbatch_cmd}") 
    except subprocess.CalledProcessError as e:
        click.echo(f"Error submitting job: {e.stderr}", err=True)

if __name__ == "__main__":
    cli()
