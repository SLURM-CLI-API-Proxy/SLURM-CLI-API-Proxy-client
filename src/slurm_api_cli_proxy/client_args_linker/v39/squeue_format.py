import re
from jsonpath import JSONPath as JP
import slurm_api_cli_proxy.client_args_linker.v39.squeue_format_types as ft

default = "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R" 
# -l, --long
long = "%.18i %.9P %.8j %.8u %.8T %.10M %.9l %.6D %R" 
# -s, --steps
steps = "%.15i %.8j %.9P %.8u %.9M %N"

def format_squeue_output(jobs, squeue_format_string, user_filter):
    table_layout = _parse_format_string(squeue_format_string)
    squeue_output = _apply_table_layout(jobs, table_layout, user_filter)
    return squeue_output

def _parse_format_string(format):
    """
    Takes an squeue format string according to https://slurm.schedmd.com/squeue.html and
    parses it to a list of column-info dictionaries for table-formatting.

    Args:
        format: format string.
        The string can be explicitly defined by the user or one of the presets ("default", "long", "steps") 
    Returns:
        list: A list of dictionaries with column-info ("table-layout")  
    """
    tokens = [token for token in format.split('%') if len(token)>0]
    table_layout = []
    for token in tokens:
        matches = re.findall(ft.type_re, token)
        if len(matches) != 1:
            raise ValueError(f"Invalid format token '{token}'")
        single_match = matches[0]  
        if len(single_match) != 5:
            raise ValueError(f"Invalid format token '{token}'")
        align_right, width, coltype, suffix, spacer  = single_match
        if not width and align_right:
            raise ValueError(f"No alignment ('.') without width allowed: '{token}'.")
        
        # resolve type-info from mapping
        type_info = ft.types_map[coltype]
        column = type_info.copy()

        column.pop('descr')
        column['align_right'] = (align_right == '.')
        column['width'] = int(width) if width else 0
        column['suffix'] = suffix
        column['spacer'] = spacer

        table_layout.append(column)
    
    return table_layout
    
def _apply_table_layout(jobs, table_layout, user_filter):
    """
    Takes a list of job objects as returned by the jobs (or squeue) call and extracts the table header and job content and format according to the given table-layout.
    Filters on the user_filter, if provided.

    Args:
        jobs: list of job objects from the response object
        table-layout: list of column-info dictionaries to extract content from job objects and format it.
        user_filter: if set, string with the user name the jobs to display must match.
    Returns:
        string: The content of the formatted output table.
    """
    output = _write_header(table_layout)
    for job in jobs:
        if job.job_resources is None:
            raise ValueError(f"Unexpected 'None' value for job {job} resources")
        if user_filter and job.user_name != user_filter:
            continue

        job_row = ''
        for column in table_layout:
            if 'json_path' in column:
                value = str(JP("$."+column['json_path']).parse(job)[0])
            else:
                method_key = column['method']
                method = ft.types_map[method_key]
                value = str(method(job))

            if not column['width']:
                job_row += value
            elif column['align_right']:
                # align (=pad) right and/or truncate
                job_row += value.rjust(column['width'])[:column['width']]
            else:
                # align (=pad) left and/or truncate
                job_row += value.ljust(column['width'])[:column['width']]

            job_row += column['suffix'] + column['spacer']

        output += job_row + "\n"

    return output

def _write_header(table_layout):
    """
    Creates the output table header with the necessary column heads, alignment and width.

    Args:
        table_layout: a list of column-info dictionaries
    Returns:
        str: the header of the output table
    """
    header = ''
    for column in table_layout:
        if not column['width']:
            header += column['head']
        elif column['align_right']:
        # align (=pad) right and/or truncate
            header += column['head'].rjust(column['width'])[:column['width']]
        else:
            # align (=pad) left and/or truncate
            header += column['head'].ljust(column['width'])[:column['width']]

        header += column['suffix'] + column['spacer']

    return header + "\n"    
