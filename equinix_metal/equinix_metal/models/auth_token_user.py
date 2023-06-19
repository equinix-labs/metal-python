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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, conlist
from equinix_metal.models.href import Href

class AuthTokenUser(BaseModel):
    """
    AuthTokenUser
    """
    avatar_thumb_url: Optional[StrictStr] = None
    avatar_url: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    customdata: Optional[Dict[str, Any]] = None
    default_organization_id: Optional[StrictStr] = None
    default_project_id: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    emails: Optional[conlist(Href)] = None
    first_name: Optional[StrictStr] = None
    fraud_score: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    last_login_at: Optional[datetime] = None
    last_name: Optional[StrictStr] = None
    max_organizations: Optional[StrictInt] = None
    max_projects: Optional[StrictInt] = None
    phone_number: Optional[StrictStr] = None
    short_id: Optional[StrictStr] = None
    timezone: Optional[StrictStr] = None
    two_factor_auth: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    __properties = ["avatar_thumb_url", "avatar_url", "created_at", "customdata", "default_organization_id", "default_project_id", "email", "emails", "first_name", "fraud_score", "full_name", "href", "id", "last_login_at", "last_name", "max_organizations", "max_projects", "phone_number", "short_id", "timezone", "two_factor_auth", "updated_at"]

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
    def from_json(cls, json_str: str) -> AuthTokenUser:
        """Create an instance of AuthTokenUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in emails (list)
        _items = []
        if self.emails:
            for _item in self.emails:
                if _item:
                    _items.append(_item.to_dict())
            _dict['emails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthTokenUser:
        """Create an instance of AuthTokenUser from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AuthTokenUser.parse_obj(obj)

        _obj = AuthTokenUser.parse_obj({
            "avatar_thumb_url": obj.get("avatar_thumb_url"),
            "avatar_url": obj.get("avatar_url"),
            "created_at": obj.get("created_at"),
            "customdata": obj.get("customdata"),
            "default_organization_id": obj.get("default_organization_id"),
            "default_project_id": obj.get("default_project_id"),
            "email": obj.get("email"),
            "emails": [Href.from_dict(_item) for _item in obj.get("emails")] if obj.get("emails") is not None else None,
            "first_name": obj.get("first_name"),
            "fraud_score": obj.get("fraud_score"),
            "full_name": obj.get("full_name"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "last_login_at": obj.get("last_login_at"),
            "last_name": obj.get("last_name"),
            "max_organizations": obj.get("max_organizations"),
            "max_projects": obj.get("max_projects"),
            "phone_number": obj.get("phone_number"),
            "short_id": obj.get("short_id"),
            "timezone": obj.get("timezone"),
            "two_factor_auth": obj.get("two_factor_auth"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

