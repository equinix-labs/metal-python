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
from equinix_metal.models.ssh_key import SSHKey

class SSHKeyList(BaseModel):
    """
    SSHKeyList
    """
    href: Optional[StrictStr] = None
    ssh_keys: Optional[conlist(SSHKey)] = None
    __properties = ["href", "ssh_keys"]

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
    def from_json(cls, json_str: str) -> SSHKeyList:
        """Create an instance of SSHKeyList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ssh_keys (list)
        _items = []
        if self.ssh_keys:
            for _item in self.ssh_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ssh_keys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SSHKeyList:
        """Create an instance of SSHKeyList from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SSHKeyList.parse_obj(obj)

        _obj = SSHKeyList.parse_obj({
            "href": obj.get("href"),
            "ssh_keys": [SSHKey.from_dict(_item) for _item in obj.get("ssh_keys")] if obj.get("ssh_keys") is not None else None
        })
        return _obj

