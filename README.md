## Badges

(Customize these badges with your own links, and check https://shields.io/ or https://badgen.net/ to see which other badges are available.)

| fair-software.eu recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/hcadavid/slurm_api_cli_proxy) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/hcadavid/slurm_api_cli_proxy)](https://github.com/hcadavid/slurm_api_cli_proxy) |
| (3/5) community registry           | [![RSD](https://img.shields.io/badge/rsd-slurm_api_cli_proxy-00a3e3.svg)](https://www.research-software.nl/software/slurm_api_cli_proxy) [![workflow pypi badge](https://img.shields.io/pypi/v/slurm_api_cli_proxy.svg?colorB=blue)](https://pypi.python.org/project/slurm_api_cli_proxy/) |
| (4/5) citation                     | [![DOI](https://zenodo.org/badge/DOI/<replace-with-created-DOI>.svg)](https://doi.org/<replace-with-created-DOI>)|
| (5/5) checklist                    | [![workflow cii badge](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>/badge)](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>) |
| howfairis                          | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu) |
| **Other best practices**           | &nbsp; |
| Static analysis                    | [![workflow scq badge](https://sonarcloud.io/api/project_badges/measure?project=hcadavid_slurm_api_cli_proxy&metric=alert_status)](https://sonarcloud.io/dashboard?id=hcadavid_slurm_api_cli_proxy) |
| Coverage                           | [![workflow scc badge](https://sonarcloud.io/api/project_badges/measure?project=hcadavid_slurm_api_cli_proxy&metric=coverage)](https://sonarcloud.io/dashboard?id=hcadavid_slurm_api_cli_proxy) || Documentation                      | [![Documentation Status](https://readthedocs.org/projects/slurm_api_cli_proxy/badge/?version=latest)](https://slurm_api_cli_proxy.readthedocs.io/en/latest/?badge=latest) || **GitHub Actions**                 | &nbsp; |
| Build                              | [![build](https://github.com/hcadavid/slurm_api_cli_proxy/actions/workflows/build.yml/badge.svg)](https://github.com/hcadavid/slurm_api_cli_proxy/actions/workflows/build.yml) |
| Citation data consistency          | [![cffconvert](https://github.com/hcadavid/slurm_api_cli_proxy/actions/workflows/cffconvert.yml/badge.svg)](https://github.com/hcadavid/slurm_api_cli_proxy/actions/workflows/cffconvert.yml) || SonarCloud                         | [![sonarcloud](https://github.com/hcadavid/slurm_api_cli_proxy/actions/workflows/sonarcloud.yml/badge.svg)](https://github.com/hcadavid/slurm_api_cli_proxy/actions/workflows/sonarcloud.yml) |## How to use slurm_api_cli_proxy

Takes locally issued SLURM commands (\"sbatch\", \"srun\", ...) and forwards them to an HPC cluster through the SLURM REST-API.

The project setup is documented in [project_setup.md](project_setup.md). Feel free to remove this document (and/or the link to this document) if you don't need it.

## Status

- [X] Baseline project
- [ ] Setting up GitHub actions/badges
- [X] Client for SLURM REST API 0.0.38, 0.0.39, and 0.0.40 generated and integrated
- [X] Proxy sbatch (workin as an stand-alone command) with the input parameters parsing, basic validation and return error codes equivalent to the original one.
- [X] Dynamic definition of command arguments through YAML files
- [X] SLURM REST API Client reference examples
- [ ] Mapping between input parameters, API resources and Payload parameters
- [ ] Dynamic generation of request Payloads and request execution
- [ ] Mapping return codes to CLI STDOUT results
- [ ] Defining strategies for the consistency of output file paths (local vs cluster file system)
- [ ] Approach for setting Proxy parameters (target API URI)
- [ ] Handling API JWT reset
- [ ] squeue proxy: formatting STDOUT messages
- [ ] Testing integration with golang programs (handling STDIN/STDERR) & Unix piping
- [ ] ...

## Installation 

```
pip install git+https://github.com/hcadavid/SLURM_CLI_PROXY.git
```


## Documentation

Based on the SLURM OpenAPI specification, and the clients created for it with https://github.com/OpenAPITools/openapi-generator

### Reference API mocks

- https://app.swaggerhub.com/apis/hcadavid6/slurm-rest_api_ro/0.0.38
- https://app.swaggerhub.com/apis/hcadavid6/slurm-rest_api_rw_jobs/0.0.37

### Reference OpenAPI specs

- https://api.swaggerhub.com/apis/hcadavid6/slurm-rest_api_ro/0.0.38

### Containerized SLURM clusters

- https://github.com/rancavil/slurm-cluster
- https://codebase.helmholtz.cloud/ufz-tsm/slurm-scheduler
- https://github.com/nathan-hess/docker-slurm
- https://github.com/giovtorres/slurm-docker-cluster
- https://github.com/JBris/slurm-rest-api-docker



## Contributing

If you want to contribute to the development of slurm_api_cli_proxy,
have a look at the [contribution guidelines](CONTRIBUTING.md).

## Credits

This package was created with [Copier](https://github.com/copier-org/copier) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
