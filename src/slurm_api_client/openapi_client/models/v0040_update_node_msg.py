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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v0040_uint32_no_val import V0040Uint32NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0040UpdateNodeMsg(BaseModel):
    """
    V0040UpdateNodeMsg
    """ # noqa: E501
    comment: Optional[StrictStr] = Field(default=None, description="arbitrary comment")
    cpu_bind: Optional[StrictInt] = Field(default=None, description="default CPU binding type")
    extra: Optional[StrictStr] = Field(default=None, description="arbitrary string")
    features: Optional[List[StrictStr]] = None
    features_act: Optional[List[StrictStr]] = None
    gres: Optional[StrictStr] = Field(default=None, description="new generic resources for node")
    address: Optional[List[StrictStr]] = None
    hostname: Optional[List[StrictStr]] = None
    name: Optional[List[StrictStr]] = None
    state: Optional[List[StrictStr]] = Field(default=None, description="assign new node state")
    reason: Optional[StrictStr] = Field(default=None, description="reason for node being DOWN or DRAINING")
    reason_uid: Optional[StrictStr] = Field(default=None, description="user ID of sending (needed if user root is sending message)")
    resume_after: Optional[V0040Uint32NoVal] = None
    weight: Optional[V0040Uint32NoVal] = None
    __properties: ClassVar[List[str]] = ["comment", "cpu_bind", "extra", "features", "features_act", "gres", "address", "hostname", "name", "state", "reason", "reason_uid", "resume_after", "weight"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'PERFCTRS', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM']):
                raise ValueError("each list item must be one of ('INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'PERFCTRS', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM')")
        return value

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
        """Create an instance of V0040UpdateNodeMsg from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of resume_after
        if self.resume_after:
            _dict['resume_after'] = self.resume_after.to_dict()
        # override the default output from pydantic by calling `to_dict()` of weight
        if self.weight:
            _dict['weight'] = self.weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040UpdateNodeMsg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comment": obj.get("comment"),
            "cpu_bind": obj.get("cpu_bind"),
            "extra": obj.get("extra"),
            "features": obj.get("features"),
            "features_act": obj.get("features_act"),
            "gres": obj.get("gres"),
            "address": obj.get("address"),
            "hostname": obj.get("hostname"),
            "name": obj.get("name"),
            "state": obj.get("state"),
            "reason": obj.get("reason"),
            "reason_uid": obj.get("reason_uid"),
            "resume_after": V0040Uint32NoVal.from_dict(obj["resume_after"]) if obj.get("resume_after") is not None else None,
            "weight": V0040Uint32NoVal.from_dict(obj["weight"]) if obj.get("weight") is not None else None
        })
        return _obj


