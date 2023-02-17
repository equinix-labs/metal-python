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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from metal_python.models.href import Href

class Event(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    body: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    interpolated: Optional[StrictStr] = None
    relationships: Optional[List[Href]] = None
    state: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    modified_by: Optional[Dict[str, Any]] = None
    ip: Optional[StrictStr] = None
    __properties = ["body", "created_at", "href", "id", "interpolated", "relationships", "state", "type", "modified_by", "ip"]

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
    def from_json(cls, json_str: str) -> Event:
        """Create an instance of Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in relationships (list)
        _items = []
        if self.relationships:
            for _item in self.relationships:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relationships'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Event:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Event.parse_obj(obj)

        _obj = Event.parse_obj({
            "body": obj.get("body"),
            "created_at": obj.get("created_at"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "interpolated": obj.get("interpolated"),
            "relationships": [Href.from_dict(_item) for _item in obj.get("relationships")] if obj.get("relationships") is not None else None,
            "state": obj.get("state"),
            "type": obj.get("type"),
            "modified_by": obj.get("modified_by"),
            "ip": obj.get("ip")
        })
        return _obj

