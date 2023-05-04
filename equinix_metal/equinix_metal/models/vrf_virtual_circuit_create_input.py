# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. The fields available for search differ by resource, as does the search strategy.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field.   # noqa: E501

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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, conlist

class VrfVirtualCircuitCreateInput(BaseModel):
    """
    VrfVirtualCircuitCreateInput
    """
    customer_ip: Optional[StrictStr] = Field(None, description="An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used.")
    description: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    md5: Optional[StrictStr] = Field(None, description="The MD5 password for the BGP peering in plaintext (not a checksum).")
    metal_ip: Optional[StrictStr] = Field(None, description="An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used.")
    name: Optional[StrictStr] = None
    nni_vlan: conint(strict=True, le=4094, ge=2) = ...
    peer_asn: StrictInt = Field(..., description="The peer ASN that will be used with the VRF on the Virtual Circuit.")
    project_id: StrictStr = ...
    speed: Optional[StrictInt] = Field(None, description="speed can be passed as integer number representing bps speed or string (e.g. '52m' or '100g' or '4 gbps')")
    subnet: StrictStr = Field(..., description="The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. The subnet specified must be contained within an already-defined IP Range for the VRF.")
    tags: Optional[conlist(StrictStr)] = None
    vrf: StrictStr = Field(..., description="The UUID of the VRF that will be associated with the Virtual Circuit.")
    __properties = ["customer_ip", "description", "href", "md5", "metal_ip", "name", "nni_vlan", "peer_asn", "project_id", "speed", "subnet", "tags", "vrf"]

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
    def from_json(cls, json_str: str) -> VrfVirtualCircuitCreateInput:
        """Create an instance of VrfVirtualCircuitCreateInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if md5 (nullable) is None
        if self.md5 is None:
            _dict['md5'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VrfVirtualCircuitCreateInput:
        """Create an instance of VrfVirtualCircuitCreateInput from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return VrfVirtualCircuitCreateInput.parse_obj(obj)

        _obj = VrfVirtualCircuitCreateInput.parse_obj({
            "customer_ip": obj.get("customer_ip"),
            "description": obj.get("description"),
            "href": obj.get("href"),
            "md5": obj.get("md5"),
            "metal_ip": obj.get("metal_ip"),
            "name": obj.get("name"),
            "nni_vlan": obj.get("nni_vlan"),
            "peer_asn": obj.get("peer_asn"),
            "project_id": obj.get("project_id"),
            "speed": obj.get("speed"),
            "subnet": obj.get("subnet"),
            "tags": obj.get("tags"),
            "vrf": obj.get("vrf")
        })
        return _obj

