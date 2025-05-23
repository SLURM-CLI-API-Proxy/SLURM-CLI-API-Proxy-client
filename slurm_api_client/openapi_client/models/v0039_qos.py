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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v0039_float64_no_val import V0039Float64NoVal
from openapi_client.models.v0039_qos_limits import V0039QosLimits
from openapi_client.models.v0039_qos_preempt import V0039QosPreempt
from openapi_client.models.v0039_uint32_no_val import V0039Uint32NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0039Qos(BaseModel):
    """
    V0039Qos
    """ # noqa: E501
    description: Optional[StrictStr] = None
    flags: Optional[List[StrictStr]] = None
    id: Optional[StrictInt] = None
    limits: Optional[V0039QosLimits] = None
    name: Optional[StrictStr] = None
    preempt: Optional[V0039QosPreempt] = None
    priority: Optional[V0039Uint32NoVal] = None
    usage_factor: Optional[V0039Float64NoVal] = None
    usage_threshold: Optional[V0039Float64NoVal] = None
    __properties: ClassVar[List[str]] = ["description", "flags", "id", "limits", "name", "preempt", "priority", "usage_factor", "usage_threshold"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['NOT_SET', 'ADD', 'REMOVE', 'PARTITION_MINIMUM_NODE', 'PARTITION_MAXIMUM_NODE', 'PARTITION_TIME_LIMIT', 'ENFORCE_USAGE_THRESHOLD', 'NO_RESERVE', 'REQUIRED_RESERVATION', 'DENY_LIMIT', 'OVERRIDE_PARTITION_QOS', 'NO_DECAY', 'USAGE_FACTOR_SAFE']):
                raise ValueError("each list item must be one of ('NOT_SET', 'ADD', 'REMOVE', 'PARTITION_MINIMUM_NODE', 'PARTITION_MAXIMUM_NODE', 'PARTITION_TIME_LIMIT', 'ENFORCE_USAGE_THRESHOLD', 'NO_RESERVE', 'REQUIRED_RESERVATION', 'DENY_LIMIT', 'OVERRIDE_PARTITION_QOS', 'NO_DECAY', 'USAGE_FACTOR_SAFE')")
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
        """Create an instance of V0039Qos from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict['limits'] = self.limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of preempt
        if self.preempt:
            _dict['preempt'] = self.preempt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usage_factor
        if self.usage_factor:
            _dict['usage_factor'] = self.usage_factor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usage_threshold
        if self.usage_threshold:
            _dict['usage_threshold'] = self.usage_threshold.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0039Qos from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "flags": obj.get("flags"),
            "id": obj.get("id"),
            "limits": V0039QosLimits.from_dict(obj["limits"]) if obj.get("limits") is not None else None,
            "name": obj.get("name"),
            "preempt": V0039QosPreempt.from_dict(obj["preempt"]) if obj.get("preempt") is not None else None,
            "priority": V0039Uint32NoVal.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "usage_factor": V0039Float64NoVal.from_dict(obj["usage_factor"]) if obj.get("usage_factor") is not None else None,
            "usage_threshold": V0039Float64NoVal.from_dict(obj["usage_threshold"]) if obj.get("usage_threshold") is not None else None
        })
        return _obj


