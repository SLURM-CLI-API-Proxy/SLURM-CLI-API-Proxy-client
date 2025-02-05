import unittest
import openapi_client

from slurm_api_cli_proxy.client_args_linker.api_request_handler import get_args_linker

        
configuration = openapi_client.Configuration(
    host = "http://slurm-controller:6820"
)

job_request = {
    "script": """#!/bin/bash
        echo I worked > /tmp/atemp_file.txt
        sleep 10
        """,  
    "job": {
        "environment": ["PATH=/bin/:/usr/bin/:/sbin/"],
        "current_working_directory": "/home/hcadavid",
        "name": "test slurmrestd job",
        "output": "slurm-%j.out"
    }
}

req_handler = get_args_linker({})

print(type(req_handler))

response = req_handler.sbatch_post_request(job_request, configuration)

if (len(response.errors)>0):
    print("error")

