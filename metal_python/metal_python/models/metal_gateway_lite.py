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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class MetalGatewayLite(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created_at: Optional[datetime] = None
    gateway_address: Optional[StrictStr] = Field(None, description="The gateway address with subnet CIDR value for this Metal Gateway. For example, a Metal Gateway using an IP reservation with block 10.1.2.0/27 would have a gateway address of 10.1.2.1/27.")
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    state: Optional[StrictStr] = Field(None, description="The current state of the Metal Gateway. 'Ready' indicates the gateway record has been configured, but is currently not active on the network. 'Active' indicates the gateway has been configured on the network. 'Deleting' is a temporary state used to indicate that the gateway is in the process of being un-configured from the network, after which the gateway record will be deleted.")
    updated_at: Optional[datetime] = None
    vlan: Optional[StrictInt] = Field(None, description="The VLAN id of the Virtual Network record associated to this Metal Gateway.")
    __properties = ["created_at", "gateway_address", "href", "id", "state", "updated_at", "vlan"]

    @validator('state')
    def state_validate_enum(cls, v):
        if v is None:
            return v

        if type(v) is list:
            for i in v:
                if i not in ('ready', 'active', 'deleting'):
                    raise ValueError("each list item must be one of ('ready', 'active', 'deleting')")
        else:
            if v not in ('ready', 'active', 'deleting'):
                raise ValueError("must be on of enum values ('ready', 'active', 'deleting')")

        return v

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
    def from_json(cls, json_str: str) -> MetalGatewayLite:
        """Create an instance of MetalGatewayLite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MetalGatewayLite:
        """Create an instance of MetalGatewayLite from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MetalGatewayLite.parse_obj(obj)

        _obj = MetalGatewayLite.parse_obj({
            "created_at": obj.get("created_at"),
            "gateway_address": obj.get("gateway_address"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "updated_at": obj.get("updated_at"),
            "vlan": obj.get("vlan")
        })
        return _obj

