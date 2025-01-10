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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class V0038License(BaseModel):
    """
    V0038License
    """ # noqa: E501
    license_name: Optional[StrictStr] = Field(default=None, description="name of license", alias="LicenseName")
    total: Optional[StrictInt] = Field(default=None, description="total number of licenses", alias="Total")
    used: Optional[StrictInt] = Field(default=None, description="number of licenses in use", alias="Used")
    free: Optional[StrictInt] = Field(default=None, description="number of licenses available", alias="Free")
    reserved: Optional[StrictInt] = Field(default=None, description="number of licenses reserved", alias="Reserved")
    remote: Optional[StrictBool] = Field(default=None, description="license is remote", alias="Remote")
    __properties: ClassVar[List[str]] = ["LicenseName", "Total", "Used", "Free", "Reserved", "Remote"]

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
        """Create an instance of V0038License from a JSON string"""
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
        """Create an instance of V0038License from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LicenseName": obj.get("LicenseName"),
            "Total": obj.get("Total"),
            "Used": obj.get("Used"),
            "Free": obj.get("Free"),
            "Reserved": obj.get("Reserved"),
            "Remote": obj.get("Remote")
        })
        return _obj


