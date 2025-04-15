# Setup and usage

## Requirements
- Linux, MacOS or [Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/)
- Python version ≥3.10

## Installation 

```shell
# Check python version (requiring ≥3.10)
python --version

# Create a new virtual environment
python -m venv env
source env/bin/activate

# install 
pip install .

```

A virtual environment is *required* to install the the non-pypi dependencies. You can also use `conda` to manage python environments. If running from a shell terminal, the virtual environment where the package was installed must be active on it.

## Testing

### Unit and integration tests

```shell
#Start a dockerized slurm cluster on localhost (works on Linux only)
source src/tests/slurm_test_scripts/start_dockerized_slurm.sh

#Run tests 
pytest
```

### Running unit tests only (doesn't require the dockerized slurm cluster)

```shell
# Run tests, excluding integration ones (which require the dockerized slurm cluster running on localhost)
pytest -m "not integration"
```

### Static type checking

```shell
#Static type checking with mypy. 
mypy src --check-untyped-defs
```

## Usage from a shell terminal

1. Define the URI of the target SLURM API through the `PROXY_SLURM_API_URL` environment variable:

```shell
#Example:
export PROXY_SLURM_API_URL=http://slurm-controller:6820
```

2. Set the SLURM_JWT environment variable with the API token of the target SLURM API. An script is provided to do this if you have ssh access to the SLURM workload manager:

```shell
# Setting the SLURM_JWT variable (can be obtained by running 'scontrol token' on the SLURM workload manager)
export SLURM_JWT=<token>

# Setting the SLURM_JWT variable through the provided script (password for opening an ssh session will be requested)
# source update_token.sh <slurm-wlm-user> <slurm-wlm-host>. E.g.:
source update_token.sh userx slurm-controller
```
   
3. Run slurm commands as you would do* with the real ones:

```shell

#sbatch help
sbatch --help

#request a job defined on a shell script
sbatch --job-name jobx --chdir /home/userx  src/tests/slurm_test_scripts/slurm_write_job.sh

#capture a job definition through STDIN and request its execution
sbatch --job-name jobx --chdir /home/userx

#show running jobs
squeue 

#show running jobs in json format
squeue --json

#update a job
scontrol update JobId=206 MinCPUsNode=1

#hold/release a given job
scontrol hold 209
scontrol release 209

```


