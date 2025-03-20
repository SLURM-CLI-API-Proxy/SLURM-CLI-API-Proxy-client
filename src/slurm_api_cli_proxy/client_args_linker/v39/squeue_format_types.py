from datetime import timedelta
from slurm_api_cli_proxy.client_args_linker.constants import slurm_statuses

def get_M_format_value(job):
    """
    Retrieve the value for the %M format type from the given job-object.

    Args:
        job: a job object from the squeue response.
    Returns:
        str: the value to display in the table
    """
    start_time = job.start_time
    end_time = job.end_time

    if end_time and start_time:
        duration = timedelta(seconds=int(end_time - start_time))
        return format_duration(duration)
    else:
        return ''

def format_duration(timed):
    """
    Format the duration in slurm-style:
      days (if any at all) without leading zeros.
      hours (if any at all) without a leading zero.
      minutes without a leading zero.
      seconds with a leading zero.
    """
    days, remainder = divmod(int(timed.total_seconds()), 24 * 3600)
    hours, remainder = divmod(remainder, 3600,)
    minutes, seconds = divmod(remainder, 60)
    
    result = ''
    hours_width = 1
    minutes_width = 1
    if days:
        result += f"{days}:"
        hours_width = 2
    if hours or days:
        result += f"{hours}".rjust(hours_width, '0') + ':'
        minutes_width = 2
    
    result += f"{minutes}".rjust(minutes_width, '0') + ':'
    result += f"{seconds:02}"

    return result

# Format "types" for squeue -o...
# Please refer to https://slurm.schedmd.com/squeue.html
type_map = {
  "A": {
    "descr": "Job id. Here, synonymous with %i.", 
    "head": "JOBID",
    "method": lambda job: job.job_id,
  },
  "D": {
    "descr": "Number of nodes allocated to the job or the minimum number of nodes required by a pending job.",
    "head": "NODES",
    "method": lambda job: job.job_resources.allocated_hosts,
  },
  "i": {
    "descr": "Job id. Here, synonymous with %A.",
    "head": "JOBID",
    "method": lambda job: job.job_id,
  },
  "j": {
    "descr": "Job or job step name. (Valid for jobs and job steps)",
    "head": "NAME",
    "method": lambda job: job.name,
  },
  "l": {
    "descr": "Time limit of the job or job step in days-hours:minutes:seconds.",
    "head": "TIME_LIMIT",
    "method": lambda job: job.time_limit,
  },
  "M": {
    "descr": "Time used by the job or job step in days-hours:minutes:seconds.",
    "head": "TIME",
    "method": get_M_format_value,
  },
  "N": {
    "descr": "List of nodes allocated to the job or job step.",
    "head": "NODELIST",
    "method": lambda job: job.job_resources.nodes.list,
  },
  "P": {
    "descr": "Partition of the job or job step.",
    "head": "PARTITION",
    "method": lambda job: job.partition,
  },
  "Q": {
    "descr": "Priority of the job (large unsigned integer). Also see %p. (Valid for jobs only)",
    "head": "PRIORITY",
    "method": lambda job: job.priority,
  },
  "r": {
    "descr": "The reason a job is in its current state. (Valid for jobs only)",
    "head": "REASON",
    "method": lambda job: job.state_reason,
  },
  "R": {
    "descr": "For pending jobs. The reason a job has not been started by the scheduler is printed within parenthesis.",
    "head": "NODELIST(REASON)",
    "method": lambda job: job.job_resources.nodes,
  },
  "t": {
    "descr": "Job state in compact form. (Valid for jobs only)",
    "head": "ST",
    "method": lambda job: slurm_statuses[job.job_state].rjust(2),
  },
  "T": {
    "descr": "Job state in extended form. (Valid for jobs only)",
    "head": "STATE",
    "method": lambda job: job.job_state,
  },
  "u": {
    "descr": "User name for a job or job step. (Valid for jobs and job steps)",
    "head": "USER",
    "method": lambda job: job.user_name,
  },
  "y": {
    "descr": "Nice value (adjustment to a job's scheduling priority). (Valid for jobs only)",
    "head": "NICE",
    "method": lambda job: job.nice,
  }
}

types_matcher = '|'.join(type_map.keys())
type_re = f"(\\.?)(\\d*)({types_matcher})(\\w*)(\\W*)"


