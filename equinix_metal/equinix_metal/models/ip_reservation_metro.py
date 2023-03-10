# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr

class IPReservationMetro(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    code: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    __properties = ["code", "country", "id", "name", "href"]

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
    def from_json(cls, json_str: str) -> IPReservationMetro:
        """Create an instance of IPReservationMetro from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IPReservationMetro:
        """Create an instance of IPReservationMetro from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IPReservationMetro.parse_obj(obj)

        _obj = IPReservationMetro.parse_obj({
            "code": obj.get("code"),
            "country": obj.get("country"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "href": obj.get("href")
        })
        return _obj

