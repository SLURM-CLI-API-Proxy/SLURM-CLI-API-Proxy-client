from datetime import timedelta

def get_D_format_value(job):
    """
    Retrieve the value for the %D format type from the given job-object.

    Args:
        job: a job object from the squeue response.
    Returns:
        str: the value to display in the table
    """
    return job.job_resources.allocated_hosts

def get_l_format_value(job):
    """
    Retrieve the value for the %l format type from the given job-object.

    Args:
        job: a job object from the squeue response.
    Returns:
        str: the value to display in the table
    """
    time_limit_info = job['time_limit']
    return get_num_value(time_limit_info)

def get_M_format_value(job):
    """
    Retrieve the value for the %M format type from the given job-object.

    Args:
        job: a job object from the squeue response.
    Returns:
        str: the value to display in the table
    """
    start_time_info = job['start_time']
    start_time = get_num_value(start_time_info)
    end_time_info = job['end_time']
    end_time = get_num_value(end_time_info)
    # These values are always set, according to the docs.
    # So we can assume these to be numbers.
    duration = timedelta(seconds=int(end_time - start_time))
    return format_duration(duration)

def get_Q_format_value(job):
    """
    Retrieve the value for the %Q format type from the given job-object.

    Args:
        job: a job object from the squeue response.
    Returns:
        str: the value to display in the table
    """
    prio_info = job['priority']
    return get_num_value(prio_info)

def get_R_format_value(job):
    """
    Retrieve the value for the %R format type from the given job-object.

    Args:
        job: a job object from the squeue response.
    Returns:
        str: the value to display in the table
    """
    return job.job_resources.nodes

def get_t_format_value(job):
    """
    Retrieve the value for the %t format type from the given job-object.

    Args:
        job: a job object from the squeue response.
    Returns:
        str: the value to display in the table
    """
    state_description = job['job_state'][0]
    # TODO: add the actual mapping 
    return state_description[:2]

def get_num_value(num_info):
    """
    Extract the value represented by the given number object.        

    Args:
        num_info: a number info object from a job object.
    Returns:
        str: the value to display in the table
    """
    if not num_info['set']:
        return "NOT_SET"
    if num_info['infinite']:
        return "INFINITE"

    return num_info['number']

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
    "json_path": "job_id",
  },
  "D": {
    "descr": "Number of nodes allocated to the job or the minimum number of nodes required by a pending job.",
    "head": "NODES",
    "method": get_D_format_value,
  },
  "i": {
    "descr": "Job id. Here, synonymous with %A.",
    "head": "JOBID",
    "json_path": "job_id",
  },
  "j": {
    "descr": "Job or job step name. (Valid for jobs and job steps)",
    "head": "NAME",
    "json_path": "name",
  },
  "l": {
    "descr": "Time limit of the job or job step in days-hours:minutes:seconds.",
    "head": "TIME_LIMIT",
    "method": get_l_format_value,
  },
  "M": {
    "descr": "Time used by the job or job step in days-hours:minutes:seconds.",
    "head": "TIME",
    "method": get_M_format_value,
  },
  "N": {
    "descr": "List of nodes allocated to the job or job step.",
    "head": "NODELIST",
    "json_path": "job_resources.nodes.list",
  },
  "P": {
    "descr": "Partition of the job or job step.",
    "head": "PARTITION",
    "json_path": "partition",
  },
  "Q": {
    "descr": "Priority of the job (large unsigned integer). Also see %p. (Valid for jobs only)",
    "head": "PRIORITY",
    "method": get_Q_format_value,
  },
  "r": {
    "descr": "The reason a job is in its current state. (Valid for jobs only)",
    "head": "REASON",
    "json_path": "state_reason",
  },
  "R": {
    "descr": "For pending jobs. The reason a job has not been started by the scheduler is printed within parenthesis.",
    "head": "NODELIST(REASON)",
    "method": get_R_format_value,
  },
  "t": {
    "descr": "Job state in compact form. (Valid for jobs only)",
    "head": "ST",
    "method": get_t_format_value,
  },
  "T": {
    "descr": "Job state in extended form. (Valid for jobs only)",
    "head": "STATE",
    "json_path": "job_state[:1]",
  },
  "u": {
    "descr": "User name for a job or job step. (Valid for jobs and job steps)",
    "head": "USER",
    "json_path": "user_name",
  },
  "y": {
    "descr": "Nice value (adjustment to a job's scheduling priority). (Valid for jobs only)",
    "head": "NICE",
    "json_path": "nice",
  }
}

types_matcher = '|'.join(type_map.keys())
type_re = f"(\\.?)(\\d*)({types_matcher})(\\w*)(\\W*)"


