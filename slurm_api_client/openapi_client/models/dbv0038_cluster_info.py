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
from openapi_client.models.dbv0038_cluster_info_associations import Dbv0038ClusterInfoAssociations
from openapi_client.models.dbv0038_cluster_info_controller import Dbv0038ClusterInfoController
from openapi_client.models.dbv0038_response_tres import Dbv0038ResponseTres
from typing import Optional, Set
from typing_extensions import Self

class Dbv0038ClusterInfo(BaseModel):
    """
    Dbv0038ClusterInfo
    """ # noqa: E501
    controller: Optional[Dbv0038ClusterInfoController] = None
    flags: Optional[List[StrictStr]] = Field(default=None, description="List of properties of cluster")
    name: Optional[StrictStr] = Field(default=None, description="Cluster name")
    nodes: Optional[StrictStr] = Field(default=None, description="Assigned nodes")
    select_plugin: Optional[StrictStr] = Field(default=None, description="Configured select plugin")
    associations: Optional[Dbv0038ClusterInfoAssociations] = None
    rpc_version: Optional[StrictInt] = Field(default=None, description="Number rpc version")
    tres: Optional[List[Dbv0038ResponseTres]] = Field(default=None, description="List of TRES in cluster")
    __properties: ClassVar[List[str]] = ["controller", "flags", "name", "nodes", "select_plugin", "associations", "rpc_version", "tres"]

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
        """Create an instance of Dbv0038ClusterInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of controller
        if self.controller:
            _dict['controller'] = self.controller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of associations
        if self.associations:
            _dict['associations'] = self.associations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tres (list)
        _items = []
        if self.tres:
            for _item_tres in self.tres:
                if _item_tres:
                    _items.append(_item_tres.to_dict())
            _dict['tres'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Dbv0038ClusterInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "controller": Dbv0038ClusterInfoController.from_dict(obj["controller"]) if obj.get("controller") is not None else None,
            "flags": obj.get("flags"),
            "name": obj.get("name"),
            "nodes": obj.get("nodes"),
            "select_plugin": obj.get("select_plugin"),
            "associations": Dbv0038ClusterInfoAssociations.from_dict(obj["associations"]) if obj.get("associations") is not None else None,
            "rpc_version": obj.get("rpc_version"),
            "tres": [Dbv0038ResponseTres.from_dict(_item) for _item in obj["tres"]] if obj.get("tres") is not None else None
        })
        return _obj


