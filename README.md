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
- Python version ≥3.12

### Installation 

```shell
# Check python version (requiring ≥3.12)
python --version
```

```shell
# If the python version is <3.12
Make sure python3.12 is available on the host.
And create a virtual environment with python 3.12
```


```shell
# install python3.12 (or higher)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12
sudo apt install python3.12-venv
```

```shell
# Create a new virtual environment
python3.12 -m venv env
# activate virtual environment
source env/bin/activate

# install 
pip install .
```

A virtual environment is *required* to install the the non-pypi dependencies. You can also use `conda` to manage python environments. If running from a shell terminal, the virtual environment where the package was installed must be active on it.

### Testing

#### Unit and integration tests

```shell
# Start a dockerized slurm cluster on localhost (works on Linux only)
source src/tests/slurm_test_scripts/start_dockerized_slurm.sh

# Run tests 
pytest
```

#### Running unit tests only (doesn't require the dockerized slurm cluster)

```shell
# Run tests, excluding integration ones (which require the dockerized slurm cluster running on localhost)
pytest -m "not integration"
```

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

```

🚧 Release notice* 🚧

Only `sbatch` and `squeue` and `scontrol` commands have been implemented, with a limited number of arguments. However, the tool is designed in a way that new arguments can be integrated as these are needed. This requires only to specify a mapping between the value given to the new argument and the property sent on the payload of the corresponding API request. More details on this are available on the [developer's documentation](https://slurm-cli-api-proxy.github.io/SLURM-CLI-API-Proxy-client/).

If you encounter issues or have feedback, please report them through the project's issue tracker.


## Contributing

If you want to contribute to the development of slurm_api_cli_proxy,
have a look at the [contribution guidelines](CONTRIBUTING.md).

## Credits

This package was created with [Copier](https://github.com/copier-org/copier) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
