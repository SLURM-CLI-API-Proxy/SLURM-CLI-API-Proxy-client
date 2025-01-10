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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Dbv0038DiagStatisticsRollupsInner(BaseModel):
    """
    Rollup statistics
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="Type of rollup")
    last_run: Optional[StrictInt] = Field(default=None, description="Timestamp of last rollup")
    last_cycle: Optional[StrictInt] = Field(default=None, description="Timestamp of last cycle")
    max_cycle: Optional[StrictInt] = Field(default=None, description="Max time of all cycles")
    total_time: Optional[StrictInt] = Field(default=None, description="Total time (s) spent doing rollup")
    mean_cycles: Optional[StrictInt] = Field(default=None, description="Average time (s) of cycle")
    __properties: ClassVar[List[str]] = ["type", "last_run", "last_cycle", "max_cycle", "total_time", "mean_cycles"]

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
        """Create an instance of Dbv0038DiagStatisticsRollupsInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Dbv0038DiagStatisticsRollupsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "last_run": obj.get("last_run"),
            "last_cycle": obj.get("last_cycle"),
            "max_cycle": obj.get("max_cycle"),
            "total_time": obj.get("total_time"),
            "mean_cycles": obj.get("mean_cycles")
        })
        return _obj


