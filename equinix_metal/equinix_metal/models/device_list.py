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
from equinix_metal.models.device import Device
from equinix_metal.models.meta import Meta

class DeviceList(BaseModel):
    """
    DeviceList
    """
    devices: Optional[conlist(Device)] = None
    href: Optional[StrictStr] = None
    meta: Optional[Meta] = None
    __properties = ["devices", "href", "meta"]

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
    def from_json(cls, json_str: str) -> DeviceList:
        """Create an instance of DeviceList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in devices (list)
        _items = []
        if self.devices:
            for _item in self.devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['devices'] = _items
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceList:
        """Create an instance of DeviceList from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DeviceList.parse_obj(obj)

        _obj = DeviceList.parse_obj({
            "devices": [Device.from_dict(_item) for _item in obj.get("devices")] if obj.get("devices") is not None else None,
            "href": obj.get("href"),
            "meta": Meta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None
        })
        return _obj

