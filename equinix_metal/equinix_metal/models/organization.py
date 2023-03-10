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
from pydantic import BaseModel, Field, StrictBytes, StrictFloat, StrictInt, StrictStr
from equinix_metal.models.address import Address
from equinix_metal.models.href import Href

class Organization(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    address: Optional[Address] = None
    billing_address: Optional[Address] = None
    created_at: Optional[datetime] = None
    credit_amount: Optional[StrictFloat] = None
    customdata: Optional[Dict[str, Any]] = None
    description: Optional[StrictStr] = None
    enforce_2fa_at: Optional[datetime] = Field(None, description="Force to all members to have enabled the two factor authentication after that date, unless the value is null")
    id: Optional[StrictStr] = None
    logo: Optional[StrictBytes] = None
    members: Optional[List[Href]] = None
    memberships: Optional[List[Href]] = None
    name: Optional[StrictStr] = None
    projects: Optional[List[Href]] = None
    terms: Optional[StrictInt] = None
    twitter: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    website: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    __properties = ["address", "billing_address", "created_at", "credit_amount", "customdata", "description", "enforce_2fa_at", "id", "logo", "members", "memberships", "name", "projects", "terms", "twitter", "updated_at", "website", "href"]

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
    def from_json(cls, json_str: str) -> Organization:
        """Create an instance of Organization from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billing_address'] = self.billing_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item in self.members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['members'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in memberships (list)
        _items = []
        if self.memberships:
            for _item in self.memberships:
                if _item:
                    _items.append(_item.to_dict())
            _dict['memberships'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in projects (list)
        _items = []
        if self.projects:
            for _item in self.projects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['projects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Organization:
        """Create an instance of Organization from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Organization.parse_obj(obj)

        _obj = Organization.parse_obj({
            "address": Address.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "billing_address": Address.from_dict(obj.get("billing_address")) if obj.get("billing_address") is not None else None,
            "created_at": obj.get("created_at"),
            "credit_amount": obj.get("credit_amount"),
            "customdata": obj.get("customdata"),
            "description": obj.get("description"),
            "enforce_2fa_at": obj.get("enforce_2fa_at"),
            "id": obj.get("id"),
            "logo": obj.get("logo"),
            "members": [Href.from_dict(_item) for _item in obj.get("members")] if obj.get("members") is not None else None,
            "memberships": [Href.from_dict(_item) for _item in obj.get("memberships")] if obj.get("memberships") is not None else None,
            "name": obj.get("name"),
            "projects": [Href.from_dict(_item) for _item in obj.get("projects")] if obj.get("projects") is not None else None,
            "terms": obj.get("terms"),
            "twitter": obj.get("twitter"),
            "updated_at": obj.get("updated_at"),
            "website": obj.get("website"),
            "href": obj.get("href")
        })
        return _obj

