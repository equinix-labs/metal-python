# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://deploy.equinix.com/developers/api/metal/>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. Currently the search parameter is only available on devices, ssh_keys, api_keys and memberships endpoints.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix_metal.models.bgp_session import BgpSession
from equinix_metal.models.global_bgp_range import GlobalBgpRange
from equinix_metal.models.href import Href
from typing import Optional, Set
from typing_extensions import Self

class BgpConfig(BaseModel):
    """
    BgpConfig
    """ # noqa: E501
    asn: Optional[Annotated[int, Field(le=4294967295, strict=True, ge=0)]] = Field(default=None, description="Autonomous System Number. ASN is required with Global BGP. With Local BGP the private ASN, 65000, is assigned.")
    created_at: Optional[datetime] = None
    deployment_type: Optional[StrictStr] = Field(default=None, description="In a Local BGP deployment, a customer uses an internal ASN to control routes within a single Equinix Metal datacenter. This means that the routes are never advertised to the global Internet. Global BGP, on the other hand, requires a customer to have a registered ASN and IP space. ")
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    max_prefix: Optional[StrictInt] = Field(default=10, description="The maximum number of route filters allowed per server")
    md5: Optional[StrictStr] = Field(default=None, description="(Optional) Password for BGP session in plaintext (not a checksum)")
    project: Optional[Href] = None
    ranges: Optional[List[GlobalBgpRange]] = Field(default=None, description="The IP block ranges associated to the ASN (Populated in Global BGP only)")
    requested_at: Optional[datetime] = None
    route_object: Optional[StrictStr] = Field(default=None, description="Specifies AS-MACRO (aka AS-SET) to use when building client route filters")
    sessions: Optional[List[BgpSession]] = Field(default=None, description="The direct connections between neighboring routers that want to exchange routing information.")
    status: Optional[StrictStr] = Field(default=None, description="Status of the BGP Config. Status \"requested\" is valid only with the \"global\" deployment_type.")
    __properties: ClassVar[List[str]] = ["asn", "created_at", "deployment_type", "href", "id", "max_prefix", "md5", "project", "ranges", "requested_at", "route_object", "sessions", "status"]

    @field_validator('deployment_type')
    def deployment_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['global', 'local']):
            raise ValueError("must be one of enum values ('global', 'local')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['requested', 'enabled', 'disabled']):
            raise ValueError("must be one of enum values ('requested', 'enabled', 'disabled')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BgpConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ranges (list)
        _items = []
        if self.ranges:
            for _item in self.ranges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ranges'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sessions (list)
        _items = []
        if self.sessions:
            for _item in self.sessions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sessions'] = _items
        # set to None if md5 (nullable) is None
        # and model_fields_set contains the field
        if self.md5 is None and "md5" in self.model_fields_set:
            _dict['md5'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BgpConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asn": obj.get("asn"),
            "created_at": obj.get("created_at"),
            "deployment_type": obj.get("deployment_type"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "max_prefix": obj.get("max_prefix") if obj.get("max_prefix") is not None else 10,
            "md5": obj.get("md5"),
            "project": Href.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "ranges": [GlobalBgpRange.from_dict(_item) for _item in obj["ranges"]] if obj.get("ranges") is not None else None,
            "requested_at": obj.get("requested_at"),
            "route_object": obj.get("route_object"),
            "sessions": [BgpSession.from_dict(_item) for _item in obj["sessions"]] if obj.get("sessions") is not None else None,
            "status": obj.get("status")
        })
        return _obj


