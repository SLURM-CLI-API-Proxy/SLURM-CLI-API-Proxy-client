# Limitations & mismatches between the local CLI and the Proxy CLI


## sbatch


### Behaviour mismatches

- The local CLI can validate the input script for inconsistencies (e.g., the first line not starting with start with #!) and prevent the job to be started. When using the sbatch proxy, the content of the script is submitted as part of the corresponding API request. Therefore, when inconsistent slurm scripts are used with the proxy, a new job will be started, and eventually faile once the slurmctld process it.

- The sbatch command sets the current path (where the command is executed) as the default value for `--chdir` if it is not defined explicitly. If the current path doesn't exist on the worker node where the job will be executed, it will fail. To ensure consistency, the `--chdir` argument should always be used.

    ```
    sbatch --job-name dajob --chdir /home/hcadavid  tests/slurm_test_scripts/slurm_write_job.sh
    ```

- `scontrol`: only job updates can be implemented. Node, partition and reservation resources are immutable in the api (only GET method):

    Only one job can be updated at a time (only '/job/{job_id}' endpoint available)

    No interactive mode

    ```shell

    #Supported: 

    # Time-related parameters
    scontrol update JobId=<jobid> TimeLimit=<time-specification>
    # Examples: 30:00, 1:30:00, 1-00:00:00

    # Priority and scheduling
    scontrol update JobId=<jobid> Priority=<value>
    scontrol update JobId=<jobid> Nice=<adjustment>
    scontrol update JobId=<jobid> Dependency=<dependency-spec>

    # Resource allocation
    scontrol update JobId=<jobid> MinMemoryNode=<MB>
    scontrol update JobId=<jobid> MinCPUsNode=<count>
    scontrol update JobId=<jobid> TRES=<tres-spec>
    # Example: TRES=cpu=5,mem=8192M,gres/gpu:1



    # Not supported:

    # State management
    scontrol update NodeName=<name> State={IDLE|ALLOCATED|DOWN|DRAIN|DRAINED|FAIL|FAILING|MAINTENANCE|POWER_DOWN|POWERED_DOWN|POWERING_DOWN|POWERING_UP|RESUME|UNDRAIN}

    # Resource configuration
    scontrol update NodeName=<name> ActiveFeatures=<features>
    scontrol update NodeName=<name> AvailableFeatures=<features>
    scontrol update NodeName=<name> Weight=<weight>
    scontrol update NodeName=<name> CpuBind={none|board|socket|ldom|core|thread|off}

    # Generic resources
    scontrol update NodeName=<name> Gres=<gres-spec>
    # Example: Gres=gpu:2,license/iop1:1
    Partition Parameters

    # Time limits
    scontrol update PartitionName=<name> MaxTime=<time-specification>
    scontrol update PartitionName=<name> DefaultTime=<time-specification>

    # Resource constraints
    scontrol update PartitionName=<name> MaxNodes=<count>
    scontrol update PartitionName=<name> MaxCPUsPerNode=<count>
    scontrol update PartitionName=<name> MinNodes=<count>

    # Access control
    scontrol update PartitionName=<name> AllowGroups=<group-list>
    scontrol update PartitionName=<name> AllowAccounts=<account-list>
    scontrol update PartitionName=<name> AllowQos=<qos-list>

    # State management
    scontrol update PartitionName=<name> State={UP|DOWN}
    ```


    ## Note: updating 'nice' through the API may cuase the slurmrestd daemon to crash

        
    ```
    2025-03-21T10:47:16.990319+00:00 slurm-controller slurmrestd[985]: slurmrestd: fatal: parsing of DATA_PARSER_NICE is not implemented
    2025-03-21T10:47:16.990345+00:00 slurm-controller slurmrestd[985]: fatal: parsing of DATA_PARSER_NICE is not implemented
    2025-03-21T10:47:17.100309+00:00 slurm-controller systemd[1]: slurmrestd.service: Main process exited, code=dumped, status=6/ABRT
    2025-03-21T10:47:17.100400+00:00 slurm-controller systemd[1]: slurmrestd.service: Failed with result 'core-dump'.
    2025-03-21T10:49:04.152128+00:00 slurm-controller tailscaled[682]: Received error: PollNetMap: unexpected EOF
    ```


