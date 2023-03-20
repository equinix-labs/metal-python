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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class BondPortData(BaseModel):
    """
    BondPortData
    """
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(None, description="ID of the bonding port")
    name: Optional[StrictStr] = Field(None, description="Name of the port interface for the bond (\"bond0\")")
    __properties = ["href", "id", "name"]

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
    def from_json(cls, json_str: str) -> BondPortData:
        """Create an instance of BondPortData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BondPortData:
        """Create an instance of BondPortData from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return BondPortData.parse_obj(obj)

        _obj = BondPortData.parse_obj({
            "href": obj.get("href"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj

