"""API and connection errors give short CLI messages (no raw HTTP dump) for all commands."""
import json
import sys
from unittest import mock

import pytest
from urllib3.exceptions import MaxRetryError, NewConnectionError

from openapi_client.exceptions import ApiException, UnauthorizedException
from openapi_client.models.v0043_openapi_job_info_resp import V0043OpenapiJobInfoResp
from slurm_api_cli_proxy import command_handler

ENV = {"PROXY_SLURM_API_URL": "http://slurm.test:6820", "SLURM_JWT": "tok", "SLURM_USER": "alice"}

# What slurmrestd 25.05 returns for an invalid/expired token (HTTP 511)
BAD_TOKEN_BODY = json.dumps({
    "jobs": [],
    "meta": {"plugin": {"type": "openapi/slurmctld"}},
    "errors": [{
        "description": "Unable to query jobs",
        "error_number": 1007,
        "error": "Protocol authentication error",
        "source": "slurm_load_jobs()",
    }],
    "warnings": [],
})


@pytest.fixture
def env(monkeypatch):
    for k, v in ENV.items():
        monkeypatch.setenv(k, v)


def api_error(status, reason, body=None, cls=ApiException):
    e = cls(status=status, reason=reason)
    e.body = body
    return e


def connection_error():
    return MaxRetryError(None, "/slurm/v0.0.43/jobs/", reason=NewConnectionError(None, "Connection refused"))  # type: ignore[arg-type]


COMMANDS = [
    # (command function, argv, patched API method)
    (command_handler.squeue, ["squeue"], "slurm_v0043_get_jobs"),
    (command_handler.sinfo, ["sinfo"], "slurm_v0043_get_partitions"),
    (command_handler.scontrol, ["scontrol", "hold", "5"], "slurm_v0043_post_job"),
]


@pytest.mark.parametrize("func,argv,method", COMMANDS)
def test_bad_token_is_short_with_hint(env, monkeypatch, capsys, func, argv, method):
    monkeypatch.setattr(sys, "argv", argv)
    err = api_error(511, "Network Authentication Required", BAD_TOKEN_BODY)
    with mock.patch(f"openapi_client.SlurmApi.{method}", side_effect=err):
        assert func() == 1
    out = capsys.readouterr()
    cmd = argv[0]
    assert out.out == ""
    lines = out.err.strip().splitlines()
    assert lines == [
        f"{cmd}: error: Unable to query jobs: Protocol authentication error",
        f"{cmd}: error: the SLURM API did not accept the token in SLURM_JWT (missing, invalid or expired?)",
    ]


@pytest.mark.parametrize("func,argv,method", COMMANDS)
def test_unauthorized_without_body(env, monkeypatch, capsys, func, argv, method):
    monkeypatch.setattr(sys, "argv", argv)
    with mock.patch(f"openapi_client.SlurmApi.{method}", side_effect=api_error(401, "Unauthorized", cls=UnauthorizedException)):
        assert func() == 1
    err = capsys.readouterr().err
    assert "HTTP 401" in err and "SLURM_JWT" in err
    assert "HTTPHeaderDict" not in err


@pytest.mark.parametrize("func,argv,method", COMMANDS + [
    (command_handler.scancel, ["scancel", "5"], "slurm_v0043_delete_jobs"),
])
def test_connection_error(env, monkeypatch, capsys, func, argv, method):
    monkeypatch.setattr(sys, "argv", argv)
    with mock.patch(f"openapi_client.SlurmApi.{method}", side_effect=connection_error()):
        assert func() == 1
    err = capsys.readouterr().err.strip()
    assert err.startswith(f"{argv[0]}: error: cannot reach the SLURM API at http://slurm.test:6820")
    assert len(err.splitlines()) == 1


def test_sbatch_connection_error(env, monkeypatch, capsys, tmp_path):
    script = tmp_path / "job.sh"
    script.write_text("#!/bin/bash\nhostname\n")
    monkeypatch.setattr(sys, "argv", ["sbatch", str(script)])
    with mock.patch("openapi_client.SlurmApi.slurm_v0043_post_job_submit", side_effect=connection_error()):
        assert command_handler.sbatch() == 1
    assert "cannot reach the SLURM API" in capsys.readouterr().err


def test_tls_error_status_0(env, monkeypatch, capsys):
    # the generated client raises ApiException(status=0) for TLS errors
    monkeypatch.setattr(sys, "argv", ["squeue"])
    err = api_error(0, "SSLError: certificate verify failed")
    with mock.patch("openapi_client.SlurmApi.slurm_v0043_get_jobs", side_effect=err):
        assert command_handler.squeue() == 1
    assert capsys.readouterr().err.strip() == "squeue: error: cannot reach the SLURM API: SSLError: certificate verify failed"


def test_errors_in_successful_response_are_formatted(env, monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["squeue"])
    resp = V0043OpenapiJobInfoResp.from_dict({
        "jobs": [],
        "last_backfill": {"set": True, "infinite": False, "number": 0},
        "last_update": {"set": True, "infinite": False, "number": 0},
        "errors": [{"description": "Unable to query jobs", "error": "Something failed", "error_number": 9}],
        "warnings": [{"description": "Partial data"}],
    })
    with mock.patch("openapi_client.SlurmApi.slurm_v0043_get_jobs", return_value=resp):
        assert command_handler.squeue() == 1
    err = capsys.readouterr().err
    assert "squeue: error: Unable to query jobs: Something failed" in err
    assert "error_number=" not in err
    # slurmrestd's informational warnings are not printed (the real squeue doesn't have them)
    assert "Partial data" not in err


def test_api_warnings_not_printed_on_success(env, monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["squeue"])
    resp = V0043OpenapiJobInfoResp.from_dict({
        "jobs": [],
        "last_backfill": {"set": True, "infinite": False, "number": 0},
        "last_update": {"set": True, "infinite": False, "number": 0},
        "errors": [],
        "warnings": [{"description": "Zero jobs to dump"}],
    })
    with mock.patch("openapi_client.SlurmApi.slurm_v0043_get_jobs", return_value=resp):
        assert command_handler.squeue() == 0
    out = capsys.readouterr()
    assert "JOBID" in out.out and out.err == ""
