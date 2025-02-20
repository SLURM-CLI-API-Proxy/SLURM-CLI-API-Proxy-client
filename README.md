## Badges





| fair-software.eu recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/LICENSE) |
| (3/5) community registry           | [![RSD](https://img.shields.io/badge/rsd-slurm_api_cli_proxy-00a3e3.svg)](https://www.research-software.nl/software/slurm-cli-api-proxy) [![workflow pypi badge](https://img.shields.io/pypi/v/slurm_cli_api_proxy.svg?colorB=blue)](https://pypi.python.org/project/slurm_api_cli_proxy/) |
| (4/5) citation                     | [![DOI](https://zenodo.org/badge/DOI/<replace-with-created-DOI>.svg)](https://doi.org/<replace-with-created-DOI>)|
| (5/5) checklist                    | [![workflow cii badge](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>/badge)](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>) |
| howfairis                          | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu) |
| **Other best practices**           | &nbsp; |
| Static analysis                    | [![workflow scq badge](https://sonarcloud.io/api/project_badges/measure?project=SLURM-CLI-API-Proxy_SLURM-CLI-API-Proxy-client&metric=alert_status)](https://sonarcloud.io/dashboard?id=SLURM-CLI-API-Proxy_SLURM-CLI-API-Proxy-client) |
| Coverage                           | [![workflow scc badge](https://sonarcloud.io/api/project_badges/measure?project=SLURM-CLI-API-Proxy_SLURM-CLI-API-Proxy-client&metric=coverage)](https://sonarcloud.io/dashboard?id=SLURM-CLI-API-Proxy_SLURM-CLI-API-Proxy-client) |
| Documentation                      | [![pages-build-deployment](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/pages/pages-build-deployment)
| **GitHub Actions**                 | &nbsp; |
| Build                              | [![build](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/build.yml/badge.svg)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/build.yml) |
| Citation data consistency          | [![cffconvert](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/cffconvert.yml/badge.svg)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/cffconvert.yml) |
| SonarCloud                         | [![sonarcloud](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/sonarcloud.yml/badge.svg)](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/actions/workflows/sonarcloud.yml) |




![alt text](docs/img/slurm_proxy_title.svg)

SLURM CLI-API Proxy client is a tool designed to bridge existing applications and scripts that rely on the SLURM CLI. The tool mimics a selection of SLURM CLI commands, translating them into REST API calls, enabling seamless integration of existing tools with external SLURM workload managers. 

Due to the extensive range of optional SLURM command arguments, only a limited subset is supported. However, the tool is designed for flexibility—the support to new arguments can be easily enabled by mapping them to the corresponding API request parameters or payload properties. Additionally, the design prioritizes extensibility, allowing support for alternative SLURM API versions (currently working with v0.0.39). The developers documentation detailing these design elements is still a work in progress.




## Setup and usage

### Requirement
- Linux, MacOS or [Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/)
- Python version ≥3.10

### Installation 

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

### Usage from a shell terminal

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

```

🚧 Alpha release notice* 🚧

- Only `sbatch` and `squeue` commands have been implemented, with a limited number of arguments
- Design refinements are still in progress
- Documentation and testing coverage are ongoing

If you encounter issues or have feedback, please report them through the project's issue tracker.


## Contributing

If you want to contribute to the development of slurm_api_cli_proxy,
have a look at the [contribution guidelines](CONTRIBUTING.md).

## Credits

This package was created with [Copier](https://github.com/copier-org/copier) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
