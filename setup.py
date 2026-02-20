from setuptools import setup, find_packages
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
slurm_api_client_path = os.path.join(current_dir, 'slurm_api_client')


# Generate requirements from requirements.txt
requirements = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read().splitlines()

setup(
    name="slurm_api_cli_proxy",
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
)
