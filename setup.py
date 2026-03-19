from setuptools import setup, find_packages
import os
from pathlib import Path

current_dir = os.path.abspath(os.path.dirname(__file__))
slurm_api_client_path = os.path.join(current_dir, 'slurm_api_client')
long_description = Path.joinpath(current_dir, "README.md").read_text()


# Generate requirements from requirements.txt
requirements = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read().splitlines()

setup(
    name="slurm_api_cli_proxy",
    description="Translate SLURM CLI commands to SLURM REST API calls",
    author="Héctor Cadavid, Carsten Schelp",
    version="0.2.1",
    packages= ["src", "slurm_api_client"],
    include_package_data=True,
    package_data={'slurm_api_cli_proxy': ['mappings/*.yaml']},
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "sbatch=slurm_api_cli_proxy.command_handler:sbatch",
            "squeue=slurm_api_cli_proxy.command_handler:squeue",
            "sinfo=slurm_api_cli_proxy.command_handler:sinfo",
            "scontrol=slurm_api_cli_proxy.command_handler:scontrol",
        ],
    },
    licence="Apache-2.0",
    keywords='slurm cli rest api proxy',
    url="https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/tree/main",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
      "License :: OSI Approved :: Apache Software License 2.0",
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "Programming Language :: Python :: 3.12",
    ],
)
