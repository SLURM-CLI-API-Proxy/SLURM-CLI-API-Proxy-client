"""sbatch option mapping: converters and the options used by dask-jobqueue."""
from importlib import resources

import pytest

from openapi_client.models.v0043_job_submit_req import V0043JobSubmitReq
from slurm_api_cli_proxy.arguments_evaluator import build_parser
from slurm_api_cli_proxy.client_args_linker.args_to_payload_mapper import (
    UnsuportedArgumentException,
    args_to_sbatch_request_payload,
)
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings
from slurm_api_cli_proxy.mappings.converters import gres_to_tres, memory_to_mb, time_to_minutes, time_to_minutes_no_val


@pytest.mark.parametrize("value,mb", [("500", 500), ("500M", 500), ("4G", 4096), ("4GB", 4096), ("1T", 1048576), ("512K", 1), ("1.5G", 1536), ("2g", 2048)])
def test_memory_to_mb(value, mb):
    assert memory_to_mb(value) == mb


def test_memory_invalid():
    with pytest.raises(ValueError):
        memory_to_mb("lots")


@pytest.mark.parametrize(
    "value,minutes",
    [("30", 30), ("30:30", 31), ("01:00:00", 60), ("00:10:00", 10), ("2-0", 2880), ("1-02", 1560), ("1-02:30", 1590), ("1-02:30:01", 1591)],
)
def test_time_to_minutes(value, minutes):
    assert time_to_minutes(value) == minutes


def test_time_unlimited():
    assert time_to_minutes_no_val("UNLIMITED") == {"set": True, "infinite": True, "number": 0}


def test_gres_to_tres():
    assert gres_to_tres("gpu:2") == "gres/gpu:2"
    assert gres_to_tres("gpu:a100:1,shard:2") == "gres/gpu:a100:1,gres/shard:2"


@pytest.fixture
def mappings():
    ref = resources.files("slurm_api_cli_proxy") / "mappings/sbatch_mappings_r25.05_v0.0.43.yaml"
    with resources.as_file(ref) as path:
        return CliToJsonPayloadMappings(yaml_config_path=str(path))


def payload_for(mappings, argv):
    args = vars(build_parser(mappings).parse_args(argv))
    return args_to_sbatch_request_payload("#!/bin/bash\n", args, mappings)


def test_dask_jobqueue_options(mappings):
    # The directives dask-jobqueue's SLURMCluster writes into its job scripts
    argv = ["-J", "dask-worker", "-e", "/logs/w-%J.err", "-o", "/logs/w-%J.out", "-p", "debug",
            "-A", "proj-x", "-n", "1", "--cpus-per-task=2", "--mem=1G", "-t", "00:10:00"]
    job = payload_for(mappings, argv)["job"]
    assert job["name"] == "dask-worker"
    assert job["standard_error"] == "/logs/w-%J.err"
    assert job["standard_output"] == "/logs/w-%J.out"
    assert job["partition"] == "debug" and job["account"] == "proj-x"
    assert job["tasks"] == 1 and job["cpus_per_task"] == 2
    assert job["memory_per_node"] == {"set": True, "infinite": False, "number": 1024}
    assert job["time_limit"] == {"set": True, "infinite": False, "number": 10}


def test_payload_validates_against_v0043_model(mappings):
    argv = ["-o", "out-%j.log", "--mem", "2G", "-t", "1:00:00", "--gres", "gpu:1", "-C", "a100", "-N", "1"]
    req = V0043JobSubmitReq.from_dict(payload_for(mappings, argv))
    job = req.job.to_dict()
    # -o used to be mapped to 'output', which is not a v0.0.43 job field and was dropped
    assert job["standard_output"] == "out-%j.log"
    assert job["memory_per_node"]["number"] == 2048
    assert job["time_limit"]["number"] == 60
    assert job["tres_per_node"] == "gres/gpu:1"
    assert job["constraints"] == "a100"


def test_invalid_value_is_reported(mappings):
    with pytest.raises(UnsuportedArgumentException, match="--mem"):
        payload_for(mappings, ["--mem", "lots"])


# ---- '#SBATCH' directives -------------------------------------------------------

from slurm_api_cli_proxy.arguments_evaluator import DirectiveError, parse_sbatch_directives, sbatch_directive_tokens

DASK_SCRIPT = """#!/usr/bin/env bash

#SBATCH -J dask-worker
#SBATCH -e /tmp/logs/dask-worker-%J.err
#SBATCH -o /tmp/logs/dask-worker-%J.out
#SBATCH -p debug
#SBATCH -A proj-x
#SBATCH -n 1
#SBATCH --cpus-per-task=2
#SBATCH --mem=1G
#SBATCH -t 00:10:00

/usr/bin/python3 -m distributed.cli.dask_worker tcp://10.0.0.1:8786 --nthreads 2
#SBATCH -p ignored-after-first-command
"""


def test_directive_tokens_stop_at_first_command():
    tokens = sbatch_directive_tokens(DASK_SCRIPT)
    assert tokens[:2] == ["-J", "dask-worker"]
    assert "ignored-after-first-command" not in tokens


def test_directive_inline_comment():
    assert sbatch_directive_tokens("#!/bin/bash\n#SBATCH -J job  # the name\n") == ["-J", "job"]


def test_parse_dask_directives(mappings):
    args = parse_sbatch_directives(mappings, DASK_SCRIPT)
    assert args == {
        "job_name": "dask-worker",
        "error": "/tmp/logs/dask-worker-%J.err",
        "output": "/tmp/logs/dask-worker-%J.out",
        "partition": "debug",
        "account": "proj-x",
        "ntasks": 1,
        "cpus_per_task": 2,
        "mem": "1G",
        "time": "00:10:00",
    }


def test_unsupported_directive_is_an_error(mappings):
    with pytest.raises(DirectiveError, match="--gpus-per-node"):
        parse_sbatch_directives(mappings, "#!/bin/bash\n#SBATCH --gpus-per-node=4\nhostname\n")


def test_no_directives(mappings):
    assert parse_sbatch_directives(mappings, "#!/bin/bash\nhostname\n") == {}


def test_cli_overrides_directive(monkeypatch, tmp_path, capsys):
    import sys
    from unittest import mock
    from slurm_api_cli_proxy import command_handler
    from openapi_client.models.v0043_openapi_job_submit_response import V0043OpenapiJobSubmitResponse

    for k, v in {"PROXY_SLURM_API_URL": "http://x:6820", "SLURM_JWT": "t", "SLURM_USER": "alice"}.items():
        monkeypatch.setenv(k, v)
    script = tmp_path / "job.sh"
    script.write_text("#!/bin/bash\n#SBATCH -J from-script\n#SBATCH -p debug\nhostname\n")
    monkeypatch.setattr(sys, "argv", ["sbatch", "-J", "from-cli", str(script)])
    resp = V0043OpenapiJobSubmitResponse(job_id=7, errors=[], warnings=[])
    with mock.patch("openapi_client.SlurmApi.slurm_v0043_post_job_submit", return_value=resp) as post:
        assert command_handler.sbatch() == 0
    job = post.call_args.args[0].job
    assert job.name == "from-cli" and job.partition == "debug"
