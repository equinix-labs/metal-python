# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. Currently the search parameter is only available on devices, ssh_keys, api_keys and memberships endpoints.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from equinix_metal.models.href import Href
from equinix_metal.models.project_type import ProjectType
from typing import Optional, Set
from typing_extensions import Self

class Project(BaseModel):
    """
    Project
    """ # noqa: E501
    backend_transfer_enabled: Optional[StrictBool] = None
    bgp_config: Optional[Href] = None
    created_at: Optional[datetime] = None
    customdata: Optional[Dict[str, Any]] = None
    devices: Optional[List[Href]] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    invitations: Optional[List[Href]] = None
    max_devices: Optional[Dict[str, Any]] = None
    members: Optional[List[Href]] = None
    memberships: Optional[List[Href]] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=80)]] = Field(default=None, description="The name of the project. Cannot contain characters encoded in greater than 3 bytes such as emojis.")
    network_status: Optional[Dict[str, Any]] = None
    organization: Optional[Href] = None
    payment_method: Optional[Href] = None
    ssh_keys: Optional[List[Href]] = None
    tags: Optional[List[StrictStr]] = None
    type: Optional[ProjectType] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    volumes: Optional[List[Href]] = None
    __properties: ClassVar[List[str]] = ["backend_transfer_enabled", "bgp_config", "created_at", "customdata", "devices", "href", "id", "invitations", "max_devices", "members", "memberships", "name", "network_status", "organization", "payment_method", "ssh_keys", "tags", "type", "updated_at", "url", "volumes"]

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
        """Create an instance of Project from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bgp_config
        if self.bgp_config:
            _dict['bgp_config'] = self.bgp_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in devices (list)
        _items = []
        if self.devices:
            for _item in self.devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['devices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in invitations (list)
        _items = []
        if self.invitations:
            for _item in self.invitations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['invitations'] = _items
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
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['payment_method'] = self.payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ssh_keys (list)
        _items = []
        if self.ssh_keys:
            for _item in self.ssh_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ssh_keys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item in self.volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Project from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backend_transfer_enabled": obj.get("backend_transfer_enabled"),
            "bgp_config": Href.from_dict(obj["bgp_config"]) if obj.get("bgp_config") is not None else None,
            "created_at": obj.get("created_at"),
            "customdata": obj.get("customdata"),
            "devices": [Href.from_dict(_item) for _item in obj["devices"]] if obj.get("devices") is not None else None,
            "href": obj.get("href"),
            "id": obj.get("id"),
            "invitations": [Href.from_dict(_item) for _item in obj["invitations"]] if obj.get("invitations") is not None else None,
            "max_devices": obj.get("max_devices"),
            "members": [Href.from_dict(_item) for _item in obj["members"]] if obj.get("members") is not None else None,
            "memberships": [Href.from_dict(_item) for _item in obj["memberships"]] if obj.get("memberships") is not None else None,
            "name": obj.get("name"),
            "network_status": obj.get("network_status"),
            "organization": Href.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "payment_method": Href.from_dict(obj["payment_method"]) if obj.get("payment_method") is not None else None,
            "ssh_keys": [Href.from_dict(_item) for _item in obj["ssh_keys"]] if obj.get("ssh_keys") is not None else None,
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "volumes": [Href.from_dict(_item) for _item in obj["volumes"]] if obj.get("volumes") is not None else None
        })
        return _obj


