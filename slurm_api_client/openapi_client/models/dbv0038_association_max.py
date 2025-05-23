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
from openapi_client.models.dbv0038_association_max_jobs import Dbv0038AssociationMaxJobs
from openapi_client.models.dbv0038_association_max_per import Dbv0038AssociationMaxPer
from openapi_client.models.dbv0038_association_max_tres import Dbv0038AssociationMaxTres
from typing import Optional, Set
from typing_extensions import Self

class Dbv0038AssociationMax(BaseModel):
    """
    Max settings
    """ # noqa: E501
    jobs: Optional[Dbv0038AssociationMaxJobs] = None
    per: Optional[Dbv0038AssociationMaxPer] = None
    tres: Optional[Dbv0038AssociationMaxTres] = None
    __properties: ClassVar[List[str]] = ["jobs", "per", "tres"]

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
        """Create an instance of Dbv0038AssociationMax from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of jobs
        if self.jobs:
            _dict['jobs'] = self.jobs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of per
        if self.per:
            _dict['per'] = self.per.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tres
        if self.tres:
            _dict['tres'] = self.tres.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Dbv0038AssociationMax from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "jobs": Dbv0038AssociationMaxJobs.from_dict(obj["jobs"]) if obj.get("jobs") is not None else None,
            "per": Dbv0038AssociationMaxPer.from_dict(obj["per"]) if obj.get("per") is not None else None,
            "tres": Dbv0038AssociationMaxTres.from_dict(obj["tres"]) if obj.get("tres") is not None else None
        })
        return _obj


