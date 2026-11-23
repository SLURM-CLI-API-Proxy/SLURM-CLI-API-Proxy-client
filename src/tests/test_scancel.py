"""scancel: argument mapping and response handling (no SLURM cluster needed)."""
import json
import sys
from unittest import mock

import pytest

from openapi_client.models.v0043_openapi_kill_jobs_resp import V0043OpenapiKillJobsResp
from openapi_client.rest import ApiException
from slurm_api_cli_proxy import command_handler
from slurm_api_cli_proxy.client_args_linker.args_to_payload_mapper import (
    UnsuportedArgumentException,
    args_to_scancel_request_payload,
)
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings
from importlib import resources

ENV = {"PROXY_SLURM_API_URL": "http://slurm.test:6820", "SLURM_JWT": "tok", "SLURM_USER": "alice"}


@pytest.fixture
def mappings():
    ref = resources.files("slurm_api_cli_proxy") / "mappings/scancel_mappings_r25.05_v0.0.43.yaml"
    with resources.as_file(ref) as path:
        return CliToJsonPayloadMappings(yaml_config_path=str(path))


@pytest.fixture
def env(monkeypatch):
    for k, v in ENV.items():
        monkeypatch.setenv(k, v)


def test_payload_job_ids_and_signal(mappings):
    payload = args_to_scancel_request_payload(["123", "124_5"], {"signal": "SIGUSR1", "quiet": False}, mappings)
    assert payload == {"jobs": ["123", "124_5"], "signal": "SIGUSR1"}


def test_payload_filters(mappings):
    payload = args_to_scancel_request_payload([], {"name": "dask-worker", "user": "alice", "state": "pd,r", "nodelist": "n1,n2"}, mappings)
    assert payload == {
        "job_name": "dask-worker",
        "user_name": "alice",
        "job_state": ["PENDING", "RUNNING"],
        "nodes": ["n1", "n2"],
    }


def test_payload_requires_job_or_filter(mappings):
    with pytest.raises(UnsuportedArgumentException):
        args_to_scancel_request_payload([], {"signal": "SIGTERM"}, mappings)


def _resp(status):
    return V0043OpenapiKillJobsResp.from_dict({"status": status, "errors": [], "warnings": []})


# Only failures are listed in 'status'; an empty list means all jobs were signalled.
GONE = {
    "step_id": "999",
    "job_id": {"set": True, "infinite": False, "number": 999},
    "error": {"string": "Invalid job id specified", "code": 2017, "message": "Invalid job id specified"},
}
DENIED = {
    "step_id": "5",
    "job_id": {"set": True, "infinite": False, "number": 5},
    "error": {"string": "Access/permission denied", "code": 2002, "message": "Access/permission denied"},
}


def run_scancel(monkeypatch, argv, response=None, side_effect=None):
    monkeypatch.setattr(sys, "argv", ["scancel", *argv])
    with mock.patch("openapi_client.SlurmApi.slurm_v0043_delete_jobs", return_value=response, side_effect=side_effect) as call:
        rc = command_handler.scancel()
    return rc, call


def test_scancel_ok(env, monkeypatch, capsys):
    rc, call = run_scancel(monkeypatch, ["123"], _resp([]))
    assert rc == 0
    assert call.call_args.args[0].to_dict() == {"jobs": ["123"]}
    assert capsys.readouterr().err == ""


def test_scancel_gone_jobs_are_silent(env, monkeypatch, capsys):
    # As scancel in Slurm 25.05: unknown/finished jobs are not reported, exit 0
    rc, _ = run_scancel(monkeypatch, ["123", "999"], _resp([GONE]))
    assert rc == 0
    assert capsys.readouterr().err == ""


def test_scancel_permission_denied(env, monkeypatch, capsys):
    # As scancel: message on stderr, exit code = Slurm errno % 256 (2002 -> 210)
    rc, _ = run_scancel(monkeypatch, ["5"], _resp([DENIED]))
    assert rc == 210
    assert "Kill job error on job id 5: Access/permission denied" in capsys.readouterr().err


def test_scancel_no_identification(env, monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["scancel"])
    assert command_handler.scancel() == 1
    assert "No job identification provided" in capsys.readouterr().err


def test_scancel_http_error_with_job_status(env, monkeypatch, capsys):
    err = ApiException(status=500, reason="Internal Server Error")
    err.body = json.dumps({"status": [DENIED], "errors": [], "warnings": []})
    rc, _ = run_scancel(monkeypatch, ["5"], side_effect=err)
    assert rc == 210
    assert "job id 5" in capsys.readouterr().err


def test_scancel_auth_error(env, monkeypatch, capsys):
    rc, _ = run_scancel(monkeypatch, ["123"], side_effect=ApiException(status=401, reason="Unauthorized"))
    assert rc == 1
    assert "HTTP 401" in capsys.readouterr().err
