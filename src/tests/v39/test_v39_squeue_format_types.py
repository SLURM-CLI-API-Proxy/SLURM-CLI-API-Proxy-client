from datetime import timedelta

from slurm_api_cli_proxy.client_args_linker.v39.squeue_format_types import format_duration

def testformat_duration_gt10days():
    td = timedelta(days=10, hours=0, minutes=1, seconds=1)
    expected = "10:00:01:01"
    assert format_duration(td) == expected, f"Output should be: {expected}"

def testformat_duration_lt10days():
    td = timedelta(days=1, hours=1, minutes=1, seconds=1)
    expected = "1:01:01:01"
    assert format_duration(td) == expected, f"Output should be: {expected}"

def testformat_duration_lt10hours():
    td = timedelta(days=0, hours=1, minutes=0, seconds=1)
    expected = "1:00:01"
    assert format_duration(td) == expected, f"Output should be: {expected}"

def testformat_duration_gt10hours():
    td = timedelta(days=0, hours=10, minutes=1, seconds=1)
    expected = "10:01:01"
    assert format_duration(td) == expected, f"Output should be: {expected}"

def testformat_duration_lt10minutes():
    td = timedelta(days=0, hours=0, minutes=1, seconds=0)
    expected = "1:00"
    assert format_duration(td) == expected, f"Output should be: {expected}"

def testformat_duration_gt10minutes():
    td = timedelta(days=0, hours=0, minutes=10, seconds=1)
    expected = "10:01"
    assert format_duration(td) == expected, f"Output should be: {expected}"

def testformat_duration_seconds_with_leading_zeros():
    td = timedelta(days=0, hours=0, minutes=0, seconds=1)
    expected = "0:01"
    assert format_duration(td) == expected, f"Output should be: {expected}"



