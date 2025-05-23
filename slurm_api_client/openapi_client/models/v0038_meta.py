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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.dbv0038_meta_plugin import Dbv0038MetaPlugin
from openapi_client.models.dbv0038_meta_slurm import Dbv0038MetaSlurm
from typing import Optional, Set
from typing_extensions import Self

class V0038Meta(BaseModel):
    """
    V0038Meta
    """ # noqa: E501
    plugin: Optional[Dbv0038MetaPlugin] = None
    slurm: Optional[Dbv0038MetaSlurm] = Field(default=None, alias="Slurm")
    __properties: ClassVar[List[str]] = ["plugin", "Slurm"]

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
        """Create an instance of V0038Meta from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of plugin
        if self.plugin:
            _dict['plugin'] = self.plugin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of slurm
        if self.slurm:
            _dict['Slurm'] = self.slurm.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0038Meta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plugin": Dbv0038MetaPlugin.from_dict(obj["plugin"]) if obj.get("plugin") is not None else None,
            "Slurm": Dbv0038MetaSlurm.from_dict(obj["Slurm"]) if obj.get("Slurm") is not None else None
        })
        return _obj


