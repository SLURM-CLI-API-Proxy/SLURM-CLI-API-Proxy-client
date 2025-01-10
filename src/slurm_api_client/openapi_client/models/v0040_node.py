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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.v0040_acct_gather_energy import V0040AcctGatherEnergy
from openapi_client.models.v0040_ext_sensors_data import V0040ExtSensorsData
from openapi_client.models.v0040_power_mgmt_data import V0040PowerMgmtData
from openapi_client.models.v0040_uint64_no_val import V0040Uint64NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0040Node(BaseModel):
    """
    V0040Node
    """ # noqa: E501
    architecture: Optional[StrictStr] = None
    burstbuffer_network_address: Optional[StrictStr] = None
    boards: Optional[StrictInt] = None
    boot_time: Optional[V0040Uint64NoVal] = None
    cluster_name: Optional[StrictStr] = None
    cores: Optional[StrictInt] = None
    specialized_cores: Optional[StrictInt] = None
    cpu_binding: Optional[StrictInt] = None
    cpu_load: Optional[StrictInt] = None
    free_mem: Optional[V0040Uint64NoVal] = None
    cpus: Optional[StrictInt] = None
    effective_cpus: Optional[StrictInt] = None
    specialized_cpus: Optional[StrictStr] = None
    energy: Optional[V0040AcctGatherEnergy] = None
    external_sensors: Optional[V0040ExtSensorsData] = None
    extra: Optional[StrictStr] = None
    power: Optional[V0040PowerMgmtData] = None
    features: Optional[List[StrictStr]] = None
    active_features: Optional[List[StrictStr]] = None
    gres: Optional[StrictStr] = None
    gres_drained: Optional[StrictStr] = None
    gres_used: Optional[StrictStr] = None
    instance_id: Optional[StrictStr] = None
    instance_type: Optional[StrictStr] = None
    last_busy: Optional[V0040Uint64NoVal] = None
    mcs_label: Optional[StrictStr] = None
    specialized_memory: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    next_state_after_reboot: Optional[List[StrictStr]] = None
    address: Optional[StrictStr] = None
    hostname: Optional[StrictStr] = None
    state: Optional[List[StrictStr]] = None
    operating_system: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    partitions: Optional[List[StrictStr]] = None
    port: Optional[StrictInt] = None
    real_memory: Optional[StrictInt] = None
    comment: Optional[StrictStr] = None
    reason: Optional[StrictStr] = None
    reason_changed_at: Optional[V0040Uint64NoVal] = None
    reason_set_by_user: Optional[StrictStr] = None
    resume_after: Optional[V0040Uint64NoVal] = None
    reservation: Optional[StrictStr] = None
    alloc_memory: Optional[StrictInt] = None
    alloc_cpus: Optional[StrictInt] = None
    alloc_idle_cpus: Optional[StrictInt] = None
    tres_used: Optional[StrictStr] = None
    tres_weighted: Optional[Union[StrictFloat, StrictInt]] = None
    slurmd_start_time: Optional[V0040Uint64NoVal] = None
    sockets: Optional[StrictInt] = None
    threads: Optional[StrictInt] = None
    temporary_disk: Optional[StrictInt] = None
    weight: Optional[StrictInt] = None
    tres: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["architecture", "burstbuffer_network_address", "boards", "boot_time", "cluster_name", "cores", "specialized_cores", "cpu_binding", "cpu_load", "free_mem", "cpus", "effective_cpus", "specialized_cpus", "energy", "external_sensors", "extra", "power", "features", "active_features", "gres", "gres_drained", "gres_used", "instance_id", "instance_type", "last_busy", "mcs_label", "specialized_memory", "name", "next_state_after_reboot", "address", "hostname", "state", "operating_system", "owner", "partitions", "port", "real_memory", "comment", "reason", "reason_changed_at", "reason_set_by_user", "resume_after", "reservation", "alloc_memory", "alloc_cpus", "alloc_idle_cpus", "tres_used", "tres_weighted", "slurmd_start_time", "sockets", "threads", "temporary_disk", "weight", "tres", "version"]

    @field_validator('next_state_after_reboot')
    def next_state_after_reboot_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'PERFCTRS', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM']):
                raise ValueError("each list item must be one of ('INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'PERFCTRS', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM')")
        return value

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
        """Create an instance of V0040Node from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of boot_time
        if self.boot_time:
            _dict['boot_time'] = self.boot_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of free_mem
        if self.free_mem:
            _dict['free_mem'] = self.free_mem.to_dict()
        # override the default output from pydantic by calling `to_dict()` of energy
        if self.energy:
            _dict['energy'] = self.energy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_sensors
        if self.external_sensors:
            _dict['external_sensors'] = self.external_sensors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of power
        if self.power:
            _dict['power'] = self.power.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_busy
        if self.last_busy:
            _dict['last_busy'] = self.last_busy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reason_changed_at
        if self.reason_changed_at:
            _dict['reason_changed_at'] = self.reason_changed_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resume_after
        if self.resume_after:
            _dict['resume_after'] = self.resume_after.to_dict()
        # override the default output from pydantic by calling `to_dict()` of slurmd_start_time
        if self.slurmd_start_time:
            _dict['slurmd_start_time'] = self.slurmd_start_time.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040Node from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "architecture": obj.get("architecture"),
            "burstbuffer_network_address": obj.get("burstbuffer_network_address"),
            "boards": obj.get("boards"),
            "boot_time": V0040Uint64NoVal.from_dict(obj["boot_time"]) if obj.get("boot_time") is not None else None,
            "cluster_name": obj.get("cluster_name"),
            "cores": obj.get("cores"),
            "specialized_cores": obj.get("specialized_cores"),
            "cpu_binding": obj.get("cpu_binding"),
            "cpu_load": obj.get("cpu_load"),
            "free_mem": V0040Uint64NoVal.from_dict(obj["free_mem"]) if obj.get("free_mem") is not None else None,
            "cpus": obj.get("cpus"),
            "effective_cpus": obj.get("effective_cpus"),
            "specialized_cpus": obj.get("specialized_cpus"),
            "energy": V0040AcctGatherEnergy.from_dict(obj["energy"]) if obj.get("energy") is not None else None,
            "external_sensors": V0040ExtSensorsData.from_dict(obj["external_sensors"]) if obj.get("external_sensors") is not None else None,
            "extra": obj.get("extra"),
            "power": V0040PowerMgmtData.from_dict(obj["power"]) if obj.get("power") is not None else None,
            "features": obj.get("features"),
            "active_features": obj.get("active_features"),
            "gres": obj.get("gres"),
            "gres_drained": obj.get("gres_drained"),
            "gres_used": obj.get("gres_used"),
            "instance_id": obj.get("instance_id"),
            "instance_type": obj.get("instance_type"),
            "last_busy": V0040Uint64NoVal.from_dict(obj["last_busy"]) if obj.get("last_busy") is not None else None,
            "mcs_label": obj.get("mcs_label"),
            "specialized_memory": obj.get("specialized_memory"),
            "name": obj.get("name"),
            "next_state_after_reboot": obj.get("next_state_after_reboot"),
            "address": obj.get("address"),
            "hostname": obj.get("hostname"),
            "state": obj.get("state"),
            "operating_system": obj.get("operating_system"),
            "owner": obj.get("owner"),
            "partitions": obj.get("partitions"),
            "port": obj.get("port"),
            "real_memory": obj.get("real_memory"),
            "comment": obj.get("comment"),
            "reason": obj.get("reason"),
            "reason_changed_at": V0040Uint64NoVal.from_dict(obj["reason_changed_at"]) if obj.get("reason_changed_at") is not None else None,
            "reason_set_by_user": obj.get("reason_set_by_user"),
            "resume_after": V0040Uint64NoVal.from_dict(obj["resume_after"]) if obj.get("resume_after") is not None else None,
            "reservation": obj.get("reservation"),
            "alloc_memory": obj.get("alloc_memory"),
            "alloc_cpus": obj.get("alloc_cpus"),
            "alloc_idle_cpus": obj.get("alloc_idle_cpus"),
            "tres_used": obj.get("tres_used"),
            "tres_weighted": obj.get("tres_weighted"),
            "slurmd_start_time": V0040Uint64NoVal.from_dict(obj["slurmd_start_time"]) if obj.get("slurmd_start_time") is not None else None,
            "sockets": obj.get("sockets"),
            "threads": obj.get("threads"),
            "temporary_disk": obj.get("temporary_disk"),
            "weight": obj.get("weight"),
            "tres": obj.get("tres"),
            "version": obj.get("version")
        })
        return _obj


