# coding: utf-8

"""
    Slurm Rest API

    API to access and control Slurm DB.

    The version of the OpenAPI document: Slurm-23.11.4&openapi/dbv0.0.38&openapi/dbv0.0.39&openapi/v0.0.39&openapi/slurmctld&openapi/v0.0.38&openapi/slurmdbd
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v0039_job_exit_code import V0039JobExitCode
from openapi_client.models.v0039_step_cpu import V0039StepCPU
from openapi_client.models.v0039_step_nodes import V0039StepNodes
from openapi_client.models.v0039_step_statistics import V0039StepStatistics
from openapi_client.models.v0039_step_step import V0039StepStep
from openapi_client.models.v0039_step_task import V0039StepTask
from openapi_client.models.v0039_step_tasks import V0039StepTasks
from openapi_client.models.v0039_step_time import V0039StepTime
from openapi_client.models.v0039_step_tres import V0039StepTres
from typing import Optional, Set
from typing_extensions import Self

class V0039Step(BaseModel):
    """
    V0039Step
    """ # noqa: E501
    time: Optional[V0039StepTime] = None
    exit_code: Optional[V0039JobExitCode] = None
    nodes: Optional[V0039StepNodes] = None
    tasks: Optional[V0039StepTasks] = None
    pid: Optional[StrictStr] = None
    cpu: Optional[V0039StepCPU] = Field(default=None, alias="CPU")
    kill_request_user: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    statistics: Optional[V0039StepStatistics] = None
    step: Optional[V0039StepStep] = None
    task: Optional[V0039StepTask] = None
    tres: Optional[V0039StepTres] = None
    __properties: ClassVar[List[str]] = ["time", "exit_code", "nodes", "tasks", "pid", "CPU", "kill_request_user", "state", "statistics", "step", "task", "tres"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V0039Step from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of time
        if self.time:
            _dict['time'] = self.time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exit_code
        if self.exit_code:
            _dict['exit_code'] = self.exit_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nodes
        if self.nodes:
            _dict['nodes'] = self.nodes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tasks
        if self.tasks:
            _dict['tasks'] = self.tasks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu
        if self.cpu:
            _dict['CPU'] = self.cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of step
        if self.step:
            _dict['step'] = self.step.to_dict()
        # override the default output from pydantic by calling `to_dict()` of task
        if self.task:
            _dict['task'] = self.task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tres
        if self.tres:
            _dict['tres'] = self.tres.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0039Step from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "time": V0039StepTime.from_dict(obj["time"]) if obj.get("time") is not None else None,
            "exit_code": V0039JobExitCode.from_dict(obj["exit_code"]) if obj.get("exit_code") is not None else None,
            "nodes": V0039StepNodes.from_dict(obj["nodes"]) if obj.get("nodes") is not None else None,
            "tasks": V0039StepTasks.from_dict(obj["tasks"]) if obj.get("tasks") is not None else None,
            "pid": obj.get("pid"),
            "CPU": V0039StepCPU.from_dict(obj["CPU"]) if obj.get("CPU") is not None else None,
            "kill_request_user": obj.get("kill_request_user"),
            "state": obj.get("state"),
            "statistics": V0039StepStatistics.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
            "step": V0039StepStep.from_dict(obj["step"]) if obj.get("step") is not None else None,
            "task": V0039StepTask.from_dict(obj["task"]) if obj.get("task") is not None else None,
            "tres": V0039StepTres.from_dict(obj["tres"]) if obj.get("tres") is not None else None
        })
        return _obj


