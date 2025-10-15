#!/usr/bin/bash

# Example how to run only tests of the version you want to test
pytest -m "not integration"  -v --ignore=/home/cschelp2/SLURM-CLI-API-Proxy-client/slurm_api_client_v39_40 --ignore=/home/cschelp2/SLURM-CLI-API-Proxy-client/src/tests/v39
