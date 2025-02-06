# Limitations & mismatches between the local CLI and the Proxy CLI


## sbatch

### Behaviour mismatches

- The local CLI can validate the input script for inconsistencies (e.g., the first line not starting with start with #!) and prevent the job to be started. When using the sbatch proxy, the content of the script is submitted as part of the corresponding API request. Therefore, when inconsistent slurm scripts are used with the proxy, a new job will be started, and eventually faile once the slurmctld process it.


