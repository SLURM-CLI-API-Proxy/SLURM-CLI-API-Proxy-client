from slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39 import V0039JobInfo, V0039JobRes
import time
from slurm_api_cli_proxy.client_args_linker.v39.squeue_format import default, format_squeue_output, _parse_format_string

def test_format_squeue_output():

    now = int(time.time())
    job_info = V0039JobInfo(
        job_id=12345,
        partition="partition1",
        name="test_job",
        user_name="user1",
        job_state="RUNNING",
        start_time= now - 1800, # 30 min ago
        end_time= now,
        job_resources=V0039JobRes(allocated_hosts=1, nodes="node1")
    )

    result = format_squeue_output([job_info], default, user_filter=None)
    lines = result.split("\n")
    header = lines[0]
    row = lines[1]

    assert "12345" in row
    assert "test_job" in row
    assert "user1" in row
    assert " R" in row
    assert "30:00" in row  # 30 min elapsed
    assert "node1" in row

def test_format_squeue_job_alignment():

    now = int(time.time())
    job_info = V0039JobInfo(
        job_id=123,
        partition="ptn1",
        name="testjob",
        user_name="user1",
        job_state="RUNNING",
        start_time= now - 120,  # 2 min ago
        end_time= now,
        job_resources=V0039JobRes(allocated_hosts=1, nodes="node1")
    )

    result = format_squeue_output([job_info], default, user_filter=None)
    lines = result.split("\n")
    header = lines[0]
    row = lines[1]

    expected = "               123      ptn1  testjob    user1  R       2:00      1 node1"

    assert row == expected, f"Formatted output should be \"{expected}\" but was \"{row}\""

def test_parse_default_format_string():
  
  table_layout = _parse_format_string(default)
  expected_n_columns = 8
  assert len(table_layout) == expected_n_columns, f"The default format string defines {expected_n_columns} columns"
  assert table_layout[0]['head'] == 'JOBID', f"First column name should be JOBID"
  assert table_layout[0]['align_right'] == True, "First column should align to the right"
  assert table_layout[0]['width'] == 18, "First column should define a column-width of 18"
  assert table_layout[0]['suffix'] == '', "First column should have empty suffix"
  assert table_layout[0]['spacer'] == ' ', "First column should have one space as a spacer"

  assert table_layout[7]['head'] == 'NODELIST(REASON)', f"Last column name should be JOBID"
  assert table_layout[7]['align_right'] == False, "Last column should not align to the right"
  assert table_layout[7]['width'] == 0, "Last column should define a column-width of 0"
  assert table_layout[7]['suffix'] == '', "Last column should have empty suffix"
  assert table_layout[7]['spacer'] == '', "Last column should have no spacer"
