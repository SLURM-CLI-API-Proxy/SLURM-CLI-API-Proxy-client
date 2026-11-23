"""CLI behaviour that scripts and tools (e.g. dask-jobqueue) rely on:
exit codes, sbatch's job-id output, errors on stderr."""
import json
import sys
from unittest import mock

import pytest

from openapi_client.rest import ApiException
from slurm_api_cli_proxy import command_handler
from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import SlurmCommandResponse
from slurm_api_cli_proxy.client_args_linker.v43.slurm_api_client_wrapper_v43 import V43SlurmAPIClientWrapper
from openapi_client.models.v0043_openapi_job_submit_response import V0043OpenapiJobSubmitResponse


ENV = {"PROXY_SLURM_API_URL": "http://slurm.test:6820", "SLURM_JWT": "tok", "SLURM_USER": "alice"}


def test_response_defaults_are_not_shared():
    a = SlurmCommandResponse()
    a.errors.append("boom")
    assert SlurmCommandResponse().errors == []


def test_missing_env_exits_nonzero(monkeypatch, capsys):
    for k in ENV:
        monkeypatch.delenv(k, raising=False)
    monkeypatch.setattr(sys, "argv", ["squeue"])
    assert command_handler.squeue() == 1
    captured = capsys.readouterr()
    assert "SLURM_JWT" in captured.err and captured.out == ""


def _submit_response(job_id=123, user_msg=None):
    return V0043OpenapiJobSubmitResponse(job_id=job_id, job_submit_user_msg=user_msg, errors=[], warnings=[])


@pytest.fixture
def env(monkeypatch):
    for k, v in ENV.items():
        monkeypatch.setenv(k, v)


@pytest.mark.parametrize("extra_args,expected", [([], "Submitted batch job 123"), (["--parsable"], "123")])
def test_sbatch_prints_job_id(env, monkeypatch, capsys, tmp_path, extra_args, expected):
    script = tmp_path / "job.sh"
    script.write_text("#!/bin/bash\necho hi\n")
    monkeypatch.setattr(sys, "argv", ["sbatch", *extra_args, str(script)])
    with mock.patch("openapi_client.SlurmApi.slurm_v0043_post_job_submit", return_value=_submit_response()) as post:
        assert command_handler.sbatch() == 0
    assert capsys.readouterr().out.strip() == expected
    # --parsable is handled by the proxy, not sent to the API
    sent = post.call_args.args[0].to_dict()
    assert "parsable" not in json.dumps(sent)


def test_sbatch_api_error_goes_to_stderr_with_exit_1(env, monkeypatch, capsys, tmp_path):
    script = tmp_path / "job.sh"
    script.write_text("#!/bin/bash\necho hi\n")
    monkeypatch.setattr(sys, "argv", ["sbatch", str(script)])
    err = ApiException(status=500, reason="Internal Server Error")
    err.body = json.dumps({"errors": [{"description": "Invalid partition name specified", "error": "Invalid partition name specified", "error_number": 2000}]})
    with mock.patch("openapi_client.SlurmApi.slurm_v0043_post_job_submit", side_effect=err):
        assert command_handler.sbatch() == 1
    captured = capsys.readouterr()
    assert "Invalid partition name specified" in captured.err
    assert captured.out == ""


def test_errors_from_api_exception_without_body():
    err = ApiException(status=401, reason="Unauthorized")
    assert V43SlurmAPIClientWrapper.errors_from_api_exception(err, "scancel") == [
        "scancel: error: SLURM API request failed (HTTP 401): Unauthorized",
        "scancel: error: the SLURM API did not accept the token in SLURM_JWT (missing, invalid or expired?)",
    ]
