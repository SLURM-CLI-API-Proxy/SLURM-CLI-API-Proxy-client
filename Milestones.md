
## General

- [X] Baseline SLURM-REST API OpenAPI specification 
- [X] Baseline API STUB and Client
- [ ] An actual SLURM REST API, with job-dispatch enabled

## Architecture

- [ ] Decoupling the CLI-side from the strategy used to resolve the command (potential use of https://xenon-middleware.github.io/xenon/ as an alternative to the API?)

## CLI-Side

- [ ] CLI options and arguments mapping to a dictionary
- [ ] File-based arguments must get the input from STDIN when no file provided
- [ ] Identify cases of synchronous/asynchronous behaviour

## SLURM-side

- [ ] Scenarios: scripts on the client, not in the server.