# Limitations & mismatches between the local CLI and the Proxy CLI


## sbatch (v0.0.39)


- The real `sbatch` command validates the input script for inconsistencies (e.g., the first line not starting with start with #!) and prevent the job to be started. When using the sbatch proxy, the content of the script is submitted as part of the corresponding API request. Therefore, when inconsistent slurm scripts are used with the proxy, a new job will be started, and eventually fail once the slurmctld process it.

- The `sbatch` command sets the current path (where the command is executed) as the default value for `--chdir` if it is not defined explicitly. If the current path doesn't exist on the worker node where the job will be executed, the job will fail. To ensure consistency, the working `--chdir` argument should always be used with a path within the worker node:

    ```
    sbatch --job-name dajob --chdir /home/hcadavid  tests/slurm_test_scripts/slurm_write_job.sh
    ```

## scontrol  (v0.0.39)

- Only job updates are supported. Node, partition and reservation resources are immutable in the SLURM API (only GET method).
- Only one job can be updated at a time: only the '/job/{job_id}' endpoint (for a single job) is available.
- `scontrol` has an interactive mode when no command is given. The proxy doesn't support such a behaviour.
- It has been observed that updating 'nice' through the API may cause the slurmrestd daemon to crash.


