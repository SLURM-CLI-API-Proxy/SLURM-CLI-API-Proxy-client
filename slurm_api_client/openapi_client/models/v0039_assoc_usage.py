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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class V0039AssocUsage(BaseModel):
    """
    V0039AssocUsage
    """ # noqa: E501
    accrue_job_count: Optional[StrictInt] = None
    group_used_wallclock: Optional[Union[StrictFloat, StrictInt]] = None
    fairshare_factor: Optional[Union[StrictFloat, StrictInt]] = None
    fairshare_shares: Optional[StrictInt] = None
    normalized_priority: Optional[Union[StrictFloat, StrictInt]] = None
    normalized_shares: Optional[Union[StrictFloat, StrictInt]] = None
    effective_normalized_usage: Optional[Union[StrictFloat, StrictInt]] = None
    normalized_usage: Optional[Union[StrictFloat, StrictInt]] = None
    raw_usage: Optional[Union[StrictFloat, StrictInt]] = None
    active_jobs: Optional[StrictInt] = None
    job_count: Optional[StrictInt] = None
    fairshare_level: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["accrue_job_count", "group_used_wallclock", "fairshare_factor", "fairshare_shares", "normalized_priority", "normalized_shares", "effective_normalized_usage", "normalized_usage", "raw_usage", "active_jobs", "job_count", "fairshare_level"]

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
        """Create an instance of V0039AssocUsage from a JSON string"""
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
        """Create an instance of V0039AssocUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accrue_job_count": obj.get("accrue_job_count"),
            "group_used_wallclock": obj.get("group_used_wallclock"),
            "fairshare_factor": obj.get("fairshare_factor"),
            "fairshare_shares": obj.get("fairshare_shares"),
            "normalized_priority": obj.get("normalized_priority"),
            "normalized_shares": obj.get("normalized_shares"),
            "effective_normalized_usage": obj.get("effective_normalized_usage"),
            "normalized_usage": obj.get("normalized_usage"),
            "raw_usage": obj.get("raw_usage"),
            "active_jobs": obj.get("active_jobs"),
            "job_count": obj.get("job_count"),
            "fairshare_level": obj.get("fairshare_level")
        })
        return _obj


