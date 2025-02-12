# Limitations & mismatches between the local CLI and the Proxy CLI


## sbatch


### Behaviour mismatches

- The local CLI can validate the input script for inconsistencies (e.g., the first line not starting with start with #!) and prevent the job to be started. When using the sbatch proxy, the content of the script is submitted as part of the corresponding API request. Therefore, when inconsistent slurm scripts are used with the proxy, a new job will be started, and eventually faile once the slurmctld process it.

- The sbatch command sets the current path (where the command is executed) as the default value for `--chdir` if it is not defined explicitly. If the current path doesn't exist on the worker node where the job will be executed, it will fail. To ensure consistency, the `--chdir` argument should always be used.

    ```
    sbatch --job-name dajob --chdir /home/hcadavid  tests/slurm_test_scripts/slurm_write_job.sh
    ```
