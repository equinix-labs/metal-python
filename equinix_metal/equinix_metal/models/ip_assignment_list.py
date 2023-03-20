# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist
from equinix_metal.models.ip_assignment import IPAssignment

class IPAssignmentList(BaseModel):
    """
    IPAssignmentList
    """
    href: Optional[StrictStr] = None
    ip_addresses: Optional[conlist(IPAssignment)] = None
    __properties = ["href", "ip_addresses"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> IPAssignmentList:
        """Create an instance of IPAssignmentList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ip_addresses (list)
        _items = []
        if self.ip_addresses:
            for _item in self.ip_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ip_addresses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IPAssignmentList:
        """Create an instance of IPAssignmentList from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IPAssignmentList.parse_obj(obj)

        _obj = IPAssignmentList.parse_obj({
            "href": obj.get("href"),
            "ip_addresses": [IPAssignment.from_dict(_item) for _item in obj.get("ip_addresses")] if obj.get("ip_addresses") is not None else None
        })
        return _obj

