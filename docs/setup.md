# Setup

## Installation (to be changed when once the repo is public)

1. Setup a Python virtual environment
2. Run the following:
```
git clone git@github.com:hcadavid/SLURM_CLI_PROXY.git
cd SLURM_CLI_PROXY
pip install .
```

## Use

If running from a shell terminal, the virtual environment where the package was installed must be active on it. Once this is done, the SLURM proxy commands can be used as the original ones:

````
sbatch --help
````

To call these commands from other programs, the 'bin' folder of the virtual environment where the package was installed (e.g., `/venvpath/venv/bin`) must be on the PATH environment variable of these programs.