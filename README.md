## Badges


| fair-software.eu recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/LICENSE) |
| (3/5) community registry           | [![RSD](https://img.shields.io/badge/rsd-slurm_api_cli_proxy-00a3e3.svg)](https://www.research-software.nl/software/slurm-cli-api-proxy) [![workflow pypi badge](https://img.shields.io/pypi/v/slurm_cli_api_proxy.svg?colorB=blue)](https://pypi.python.org/project/slurm_api_cli_proxy/) |
| (4/5) citation                     | [![DOI](https://zenodo.org/badge/DOI/<replace-with-created-DOI>.svg)](https://doi.org/<replace-with-created-DOI>)|
| (5/5) checklist                    |  |
| howfairis                          | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu) |
| **Other best practices**           | &nbsp; |
| Static analysis                    | [![workflow scq badge](https://sonarcloud.io/api/project_badges/measure?project=SLURM-CLI-API-Proxy_SLURM-CLI-API-Proxy-client&metric=alert_status)](https://sonarcloud.io/dashboard?id=SLURM-CLI-API-Proxy_SLURM-CLI-API-Proxy-client) |
| Coverage                           | [![workflow scc badge](https://sonarcloud.io/api/project_badges/measure?project=SLURM-CLI-API-Proxy_SLURM-CLI-API-Proxy-client&metric=coverage)](https://sonarcloud.io/dashboard?id=SLURM-CLI-API-Proxy_SLURM-CLI-API-Proxy-client) |
| Documentation                      | [![pages-build-deployment](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/pages/pages-build-deployment)
| **GitHub Actions**                 | &nbsp; |
| Citation data consistency          | [![cffconvert](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/cffconvert.yml/badge.svg)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/cffconvert.yml) |
| Tests & SonarQube analysis   | [![sonarcloud](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/unit_tests.yml) |




![alt text](docs/img/slurm_proxy_title.svg)

SLURM CLI-API Proxy client is a tool designed to bridge existing applications and scripts that rely on the SLURM CLI. The tool mimics a selection of SLURM CLI commands, translating them into REST API calls, enabling seamless integration of existing tools with external SLURM workload managers. 

Due to the extensive range of optional SLURM command arguments, only a limited subset is supported. However, the tool is designed for flexibility—the support to new arguments can be easily enabled by mapping them to the corresponding API request parameters or payload properties. Additionally, the design prioritizes extensibility, allowing support for alternative SLURM API versions (currently working with v0.0.39 or v0.0.43). The [developers documentation](https://slurm-cli-api-proxy.github.io/SLURM-CLI-API-Proxy-client/) provides further details on these design elements.



## Setup and usage

### Requirement
- Linux, MacOS or [Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/)
- Python version ≥3.10

### Installation 

```shell
# Create and activate a virtual environment (Python >= 3.10)
python3 -m venv env
source env/bin/activate

# install the proxy commands (sbatch, squeue, sinfo, scontrol, scancel)
pip install .

# optional extras
pip install '.[test]'   # pytest, mypy, ...
pip install '.[dask]'   # dask-jobqueue, for running Dask workers on SLURM through the proxy
pip install '.[dev]'    # test + docs + openapi-generator
```

A virtual environment is recommended: the proxy installs commands named `sbatch`, `squeue`, etc., which would otherwise shadow a real SLURM installation. If running from a shell terminal, the virtual environment where the package was installed must be active on it.

### Testing

#### Unit tests (no SLURM cluster needed)

```shell
pytest -m "not integration"
```

#### Integration tests

A single-node SLURM 25.05 cluster with `slurmrestd` (JWT authentication) is provided as a container in [`testing/slurm-container`](testing/slurm-container). It is built from source, so it also runs on arm64 (e.g. Apple Silicon), and it doesn't need `--privileged`.

```shell
# Build (first time: compiles SLURM, a few minutes) and start the test cluster on localhost:6821,
# and export PROXY_SLURM_API_URL, SLURM_JWT and SLURM_USER (user 'testuser')
source testing/slurm-container/start.sh

# Integration tests that run against the cluster from the host
pytest -m "integration and not dask"

# Dask on SLURM through the proxy (dask-jobqueue). Runs inside the container, so the
# Dask workers can reach the scheduler on any Docker setup.
testing/slurm-container/run_dask_test.sh

# Stop the cluster
docker rm -f testslurm
```

The older script `src/tests/slurm_test_scripts/start_dockerized_slurm.sh` (xenon-middleware image, Linux only, `--privileged`) still works for the original integration tests.

#### Static type checking

```shell
# Static type checking with mypy. 
mypy src --check-untyped-defs
```

### Usage from a shell terminal

1. Define the URI of the target SLURM API through the `PROXY_SLURM_API_URL` environment variable:

```shell
# Example:
export PROXY_SLURM_API_URL=http://slurm-controller:6820
```
```shell
# Or in the case of Snellius, the Dutch national supercomputer:
export PROXY_SLURM_API_URL=https://slurm.snellius.surf.nl
```

2. Set the SLURM_JWT environment variable with the API token of the target SLURM API. An script is provided to do this if you have ssh access to the SLURM workload manager:

```shell
# ON THE SLURM HOST generate a token, with an optional lifespan specification in seconds
scontrol token [lifespan=<int in seconds>]
```

```shell
# Setting the SLURM_JWT
# the token already is prepended with the environment variable name "SLURM_JWT="
# so you just have to type "export " and paste the output of the scrontrol token command
export SLURM_JWT=<token>
```
```shell
# Or setting the SLURM_JWT and SLURM_USER variables through the provided script (password for opening an ssh session will be requested)
# source update_token.sh <slurm-wlm-user> <slurm-wlm-host>. E.g.:
source update_token.sh userx slurm-controller
```

2. Set the SLURM_USER environment variable to the username of the user on who's account the JWT token was created. The value of SLURM_USER is used to set a sbatch command's default directory to this user's home:

```shell
export SLURM_USER=<username>
```

4. Run slurm commands as you would do* with the real ones:

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

#cancel jobs, or send them a signal
scancel 209 210
scancel --name jobx
scancel --signal SIGUSR1 209

#print only the job id of a new job
sbatch --parsable my_job.sh

```

`#SBATCH` directives at the top of a job script are applied as `sbatch` does (command-line options take precedence). The SLURM REST API itself ignores them, so the proxy parses them; directives the proxy doesn't support are reported as an error rather than silently ignored.

Supported `sbatch` options: `-J/--job-name`, `-o/--output`, `-e/--error`, `-D/--chdir`, `--export`, `-A/--account`, `-p/--partition`, `-q/--qos`, `--reservation`, `--comment`, `-d/--dependency`, `-n/--ntasks`, `--ntasks-per-node`, `-c/--cpus-per-task`, `-N/--nodes`, `--mem`, `--mem-per-cpu`, `-t/--time`, `-C/--constraint`, `--gres`, `--parsable`.

`scancel` supports job ids and `-s/--signal`, `-n/--name`, `-u/--user`, `-p/--partition`, `-A/--account`, `-q/--qos`, `-R/--reservation`, `-t/--state`, `-w/--nodelist`, `-Q/--quiet`. As with `scancel` (SLURM 25.05), jobs that no longer exist are not reported; other failures exit with SLURM's error number (e.g. 210 for permission denied).

### Using Dask on SLURM through the proxy

[dask-jobqueue](https://jobqueue.dask.org)'s `SLURMCluster` submits workers with `sbatch` and stops them with `scancel`, so it works with the proxy commands. The workers must be able to reach the Dask scheduler (the machine where you create the cluster), and `python` must point to a Python with `distributed` installed **on the SLURM cluster**:

```python
import os, sys
from dask_jobqueue.slurm import SLURMCluster, SLURMJob

class ProxySLURMJob(SLURMJob):
    # use the proxy commands from this environment, even if a real SLURM CLI is on PATH
    submit_command = os.path.join(os.path.dirname(sys.executable), "sbatch")
    cancel_command = os.path.join(os.path.dirname(sys.executable), "scancel")

cluster = SLURMCluster(
    job_cls=ProxySLURMJob,
    cores=4, memory="8GiB", walltime="01:00:00", queue="my-partition", account="my-project",
    python="/path/on/cluster/to/venv/bin/python",
    log_directory="/home/<user>/dask-logs",
)
cluster.scale(jobs=2)
```

If the proxy's virtual environment is active and no real SLURM CLI is installed, the default `SLURMCluster` (without `job_cls`) works as well.


🚧 Release notice* 🚧

Only `sbatch`, `squeue`, `sinfo`, `scontrol` and `scancel` have been implemented, with a limited number of arguments. However, the tool is designed in a way that new arguments can be integrated as these are needed. This requires only to specify a mapping between the value given to the new argument and the property sent on the payload of the corresponding API request. More details on this are available on the [developer's documentation](https://slurm-cli-api-proxy.github.io/SLURM-CLI-API-Proxy-client/).

If you encounter issues or have feedback, please report them through the project's issue tracker.


## Contributing

If you want to contribute to the development of slurm_api_cli_proxy,
have a look at the [contribution guidelines](CONTRIBUTING.md).

## Credits

This package was created with [Copier](https://github.com/copier-org/copier) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
