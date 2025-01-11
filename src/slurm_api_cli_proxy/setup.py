from setuptools import setup, find_packages

setup(
    name="slurm_api_cli_proxy",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sbatch=slurm_api_cli_proxy.command_handler:sbatch",
            "squeue=slurm_api_cli_proxy.command_handler:squeue",
        ],
    },
)
