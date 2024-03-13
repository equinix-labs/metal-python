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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from equinix_metal.models.fabric_service_token import FabricServiceToken
from equinix_metal.models.facility import Facility
from equinix_metal.models.href import Href
from equinix_metal.models.interconnection_port import InterconnectionPort
from equinix_metal.models.metro import Metro
from equinix_metal.models.organization import Organization
from equinix_metal.models.project import Project
from typing import Optional, Set
from typing_extensions import Self

class Interconnection(BaseModel):
    """
    Interconnection
    """ # noqa: E501
    authorization_code: Optional[StrictStr] = Field(default=None, description="For Fabric VCs (Metal Billed), this allows Fabric to connect the Metal network to any connection Fabric facilitates. Fabric uses this token to be able to give more detailed information about the Metal end of the network, when viewing resources from within Fabric.")
    contact_email: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    description: Optional[StrictStr] = None
    facility: Optional[Facility] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    metro: Optional[Metro] = Field(default=None, description="The location of where the shared or Dedicated Port is located. For interconnections with Dedicated Ports,   this will be the location of the Dedicated Ports. For Fabric VCs (Metal Billed), this is where interconnection will be originating from, as we pre-authorize the use of one of our shared ports   as the origin of the interconnection using A-Side service tokens. We only allow local connections for Fabric VCs (Metal Billed), so the destination location must be the same as the origin. For Fabric VCs (Fabric Billed),    this will be the destination of the interconnection. We allow remote connections for Fabric VCs (Fabric Billed), so the origin of the interconnection can be a different metro set here.")
    mode: Optional[StrictStr] = Field(default=None, description="The mode of the interconnection (only relevant to Dedicated Ports). Shared connections won't have this field. Can be either 'standard' or 'tunnel'.   The default mode of an interconnection on a Dedicated Port is 'standard'. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances.")
    name: Optional[StrictStr] = None
    organization: Optional[Organization] = None
    ports: Optional[List[InterconnectionPort]] = Field(default=None, description="For Fabric VCs, these represent Virtual Port(s) created for the interconnection. For dedicated interconnections, these represent the Dedicated Port(s).")
    project: Optional[Project] = None
    redundancy: Optional[StrictStr] = Field(default=None, description="Either 'primary', meaning a single interconnection, or 'redundant', meaning a redundant interconnection.")
    requested_by: Optional[Href] = None
    service_tokens: Optional[List[FabricServiceToken]] = Field(default=None, description="For Fabric VCs (Metal Billed), this will show details of the A-Side service tokens issued for the interconnection. For Fabric VCs (Fabric Billed), this will show the details of the Z-Side service tokens issued for the interconnection. Dedicated interconnections will not have any service tokens issued. There will be one per interconnection, so for redundant interconnections, there should be two service tokens issued.")
    speed: Optional[StrictInt] = Field(default=None, description="For interconnections on Dedicated Ports and shared connections, this represents the interconnection's speed in bps. For Fabric VCs, this field refers to the maximum speed of the interconnection in bps. This value will default to 10Gbps for Fabric VCs (Fabric Billed).")
    status: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None
    token: Optional[StrictStr] = Field(default=None, description="This token is used for shared interconnections to be used as the Fabric Token. This field is entirely deprecated.")
    type: Optional[StrictStr] = Field(default=None, description="The 'shared' type of interconnection refers to shared connections, or later also known as Fabric Virtual Connections (or Fabric VCs). The 'dedicated' type of interconnection refers to interconnections created with Dedicated Ports. The 'shared_port_vlan' type of interconnection refers to shared connections created without service tokens. The 'shared_port_vlan_to_csp' type of interconnection refers to connections created directly to a supported cloud service provider.")
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["authorization_code", "contact_email", "created_at", "description", "facility", "href", "id", "metro", "mode", "name", "organization", "ports", "project", "redundancy", "requested_by", "service_tokens", "speed", "status", "tags", "token", "type", "updated_at"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['standard', 'tunnel']):
            raise ValueError("must be one of enum values ('standard', 'tunnel')")
        return value

    @field_validator('redundancy')
    def redundancy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['primary', 'redundant']):
            raise ValueError("must be one of enum values ('primary', 'redundant')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['shared', 'dedicated', 'shared_port_vlan', 'shared_port_vlan_to_csp']):
            raise ValueError("must be one of enum values ('shared', 'dedicated', 'shared_port_vlan', 'shared_port_vlan_to_csp')")
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
        """Create an instance of Interconnection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of facility
        if self.facility:
            _dict['facility'] = self.facility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metro
        if self.metro:
            _dict['metro'] = self.metro.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item in self.ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ports'] = _items
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_by
        if self.requested_by:
            _dict['requested_by'] = self.requested_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in service_tokens (list)
        _items = []
        if self.service_tokens:
            for _item in self.service_tokens:
                if _item:
                    _items.append(_item.to_dict())
            _dict['service_tokens'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Interconnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorization_code": obj.get("authorization_code"),
            "contact_email": obj.get("contact_email"),
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "facility": Facility.from_dict(obj["facility"]) if obj.get("facility") is not None else None,
            "href": obj.get("href"),
            "id": obj.get("id"),
            "metro": Metro.from_dict(obj["metro"]) if obj.get("metro") is not None else None,
            "mode": obj.get("mode"),
            "name": obj.get("name"),
            "organization": Organization.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "ports": [InterconnectionPort.from_dict(_item) for _item in obj["ports"]] if obj.get("ports") is not None else None,
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "redundancy": obj.get("redundancy"),
            "requested_by": Href.from_dict(obj["requested_by"]) if obj.get("requested_by") is not None else None,
            "service_tokens": [FabricServiceToken.from_dict(_item) for _item in obj["service_tokens"]] if obj.get("service_tokens") is not None else None,
            "speed": obj.get("speed"),
            "status": obj.get("status"),
            "tags": obj.get("tags"),
            "token": obj.get("token"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


