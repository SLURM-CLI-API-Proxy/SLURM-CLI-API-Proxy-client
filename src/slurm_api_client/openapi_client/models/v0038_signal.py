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
import json
from enum import Enum
from typing_extensions import Self


class V0038Signal(str, Enum):
    """
    POSIX signal name
    """

    """
    allowed enum values
    """
    HUP = 'HUP'
    INT = 'INT'
    QUIT = 'QUIT'
    ABRT = 'ABRT'
    KILL = 'KILL'
    ALRM = 'ALRM'
    TERM = 'TERM'
    USR1 = 'USR1'
    USR2 = 'USR2'
    URG = 'URG'
    CONT = 'CONT'
    STOP = 'STOP'
    TSTP = 'TSTP'
    TTIN = 'TTIN'
    TTOU = 'TTOU'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V0038Signal from a JSON string"""
        return cls(json.loads(json_str))


