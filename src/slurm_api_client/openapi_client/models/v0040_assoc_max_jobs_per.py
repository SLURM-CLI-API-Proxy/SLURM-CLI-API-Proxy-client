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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v0040_uint32_no_val import V0040Uint32NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0040AssocMaxJobsPer(BaseModel):
    """
    V0040AssocMaxJobsPer
    """ # noqa: E501
    count: Optional[V0040Uint32NoVal] = None
    accruing: Optional[V0040Uint32NoVal] = None
    submitted: Optional[V0040Uint32NoVal] = None
    wall_clock: Optional[V0040Uint32NoVal] = None
    __properties: ClassVar[List[str]] = ["count", "accruing", "submitted", "wall_clock"]

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
        """Create an instance of V0040AssocMaxJobsPer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of count
        if self.count:
            _dict['count'] = self.count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accruing
        if self.accruing:
            _dict['accruing'] = self.accruing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of submitted
        if self.submitted:
            _dict['submitted'] = self.submitted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wall_clock
        if self.wall_clock:
            _dict['wall_clock'] = self.wall_clock.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040AssocMaxJobsPer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": V0040Uint32NoVal.from_dict(obj["count"]) if obj.get("count") is not None else None,
            "accruing": V0040Uint32NoVal.from_dict(obj["accruing"]) if obj.get("accruing") is not None else None,
            "submitted": V0040Uint32NoVal.from_dict(obj["submitted"]) if obj.get("submitted") is not None else None,
            "wall_clock": V0040Uint32NoVal.from_dict(obj["wall_clock"]) if obj.get("wall_clock") is not None else None
        })
        return _obj


