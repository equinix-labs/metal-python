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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, conlist, validator
from equinix_metal.models.href import Href
from equinix_metal.models.ip_reservation_facility import IPReservationFacility
from equinix_metal.models.ip_reservation_metro import IPReservationMetro
from equinix_metal.models.metal_gateway_lite import MetalGatewayLite
from equinix_metal.models.project import Project

class IPReservation(BaseModel):
    """
    IPReservation
    """
    addon: Optional[StrictBool] = None
    address: Optional[StrictStr] = None
    address_family: Optional[StrictInt] = None
    assignments: Optional[conlist(Href)] = None
    available: Optional[StrictStr] = None
    bill: Optional[StrictBool] = None
    cidr: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    customdata: Optional[Dict[str, Any]] = None
    details: Optional[StrictStr] = None
    enabled: Optional[StrictBool] = None
    facility: Optional[IPReservationFacility] = None
    gateway: Optional[StrictStr] = None
    global_ip: Optional[StrictBool] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    manageable: Optional[StrictBool] = None
    management: Optional[StrictBool] = None
    metal_gateway: Optional[MetalGatewayLite] = None
    metro: Optional[IPReservationMetro] = None
    netmask: Optional[StrictStr] = None
    network: Optional[StrictStr] = None
    project: Optional[Project] = None
    project_lite: Optional[Href] = None
    public: Optional[StrictBool] = None
    requested_by: Optional[Href] = None
    state: Optional[StrictStr] = None
    tags: Optional[conlist(StrictStr)] = None
    type: StrictStr = ...
    __properties = ["addon", "address", "address_family", "assignments", "available", "bill", "cidr", "created_at", "customdata", "details", "enabled", "facility", "gateway", "global_ip", "href", "id", "manageable", "management", "metal_gateway", "metro", "netmask", "network", "project", "project_lite", "public", "requested_by", "state", "tags", "type"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v not in ('global_ipv4', 'public_ipv4', 'private_ipv4', 'public_ipv6'):
            raise ValueError("must be one of enum values ('global_ipv4', 'public_ipv4', 'private_ipv4', 'public_ipv6')")
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
    def from_json(cls, json_str: str) -> IPReservation:
        """Create an instance of IPReservation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in assignments (list)
        _items = []
        if self.assignments:
            for _item in self.assignments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assignments'] = _items
        # override the default output from pydantic by calling `to_dict()` of facility
        if self.facility:
            _dict['facility'] = self.facility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metal_gateway
        if self.metal_gateway:
            _dict['metal_gateway'] = self.metal_gateway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metro
        if self.metro:
            _dict['metro'] = self.metro.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_lite
        if self.project_lite:
            _dict['project_lite'] = self.project_lite.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_by
        if self.requested_by:
            _dict['requested_by'] = self.requested_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IPReservation:
        """Create an instance of IPReservation from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IPReservation.parse_obj(obj)

        _obj = IPReservation.parse_obj({
            "addon": obj.get("addon"),
            "address": obj.get("address"),
            "address_family": obj.get("address_family"),
            "assignments": [Href.from_dict(_item) for _item in obj.get("assignments")] if obj.get("assignments") is not None else None,
            "available": obj.get("available"),
            "bill": obj.get("bill"),
            "cidr": obj.get("cidr"),
            "created_at": obj.get("created_at"),
            "customdata": obj.get("customdata"),
            "details": obj.get("details"),
            "enabled": obj.get("enabled"),
            "facility": IPReservationFacility.from_dict(obj.get("facility")) if obj.get("facility") is not None else None,
            "gateway": obj.get("gateway"),
            "global_ip": obj.get("global_ip"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "manageable": obj.get("manageable"),
            "management": obj.get("management"),
            "metal_gateway": MetalGatewayLite.from_dict(obj.get("metal_gateway")) if obj.get("metal_gateway") is not None else None,
            "metro": IPReservationMetro.from_dict(obj.get("metro")) if obj.get("metro") is not None else None,
            "netmask": obj.get("netmask"),
            "network": obj.get("network"),
            "project": Project.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "project_lite": Href.from_dict(obj.get("project_lite")) if obj.get("project_lite") is not None else None,
            "public": obj.get("public"),
            "requested_by": Href.from_dict(obj.get("requested_by")) if obj.get("requested_by") is not None else None,
            "state": obj.get("state"),
            "tags": obj.get("tags"),
            "type": obj.get("type")
        })
        return _obj

