# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. The fields available for search differ by resource, as does the search strategy.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from equinix_metal.models.href import Href
from equinix_metal.models.metal_gateway_lite import MetalGatewayLite
from equinix_metal.models.metro import Metro
from equinix_metal.models.project import Project
from equinix_metal.models.vrf import Vrf

class VrfIpReservation(BaseModel):
    """
    VrfIpReservation
    """
    address: Optional[StrictStr] = None
    address_family: Optional[StrictInt] = None
    bill: Optional[StrictBool] = None
    cidr: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    created_by: Optional[Href] = None
    customdata: Optional[Dict[str, Any]] = None
    details: Optional[StrictStr] = None
    gateway: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    manageable: Optional[StrictBool] = None
    management: Optional[StrictBool] = None
    metal_gateway: Optional[MetalGatewayLite] = None
    metro: Optional[Metro] = None
    netmask: Optional[StrictStr] = None
    network: Optional[StrictStr] = None
    project: Optional[Project] = None
    project_lite: Optional[Project] = None
    public: Optional[StrictBool] = None
    state: Optional[StrictStr] = None
    tags: Optional[conlist(StrictStr)] = None
    type: StrictStr = Field(...)
    vrf: Vrf = Field(...)
    __properties = ["address", "address_family", "bill", "cidr", "created_at", "created_by", "customdata", "details", "gateway", "href", "id", "manageable", "management", "metal_gateway", "metro", "netmask", "network", "project", "project_lite", "public", "state", "tags", "type", "vrf"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('vrf'):
            raise ValueError("must be one of enum values ('vrf')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> VrfIpReservation:
        """Create an instance of VrfIpReservation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of vrf
        if self.vrf:
            _dict['vrf'] = self.vrf.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VrfIpReservation:
        """Create an instance of VrfIpReservation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VrfIpReservation.parse_obj(obj)

        _obj = VrfIpReservation.parse_obj({
            "address": obj.get("address"),
            "address_family": obj.get("address_family"),
            "bill": obj.get("bill"),
            "cidr": obj.get("cidr"),
            "created_at": obj.get("created_at"),
            "created_by": Href.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "customdata": obj.get("customdata"),
            "details": obj.get("details"),
            "gateway": obj.get("gateway"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "manageable": obj.get("manageable"),
            "management": obj.get("management"),
            "metal_gateway": MetalGatewayLite.from_dict(obj.get("metal_gateway")) if obj.get("metal_gateway") is not None else None,
            "metro": Metro.from_dict(obj.get("metro")) if obj.get("metro") is not None else None,
            "netmask": obj.get("netmask"),
            "network": obj.get("network"),
            "project": Project.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "project_lite": Project.from_dict(obj.get("project_lite")) if obj.get("project_lite") is not None else None,
            "public": obj.get("public"),
            "state": obj.get("state"),
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "vrf": Vrf.from_dict(obj.get("vrf")) if obj.get("vrf") is not None else None
        })
        return _obj


