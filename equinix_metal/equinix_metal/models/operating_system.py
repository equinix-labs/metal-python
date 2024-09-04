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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OperatingSystem(BaseModel):
    """
    OperatingSystem
    """ # noqa: E501
    build_date: Optional[date] = Field(default=None, description="The date on which the current OS image was build and released")
    default_operating_system: Optional[StrictBool] = Field(default=None, description="Default operating system for the distro.")
    deprecation_date: Optional[date] = Field(default=None, description="The date when the OS is deprecated")
    distro: Optional[StrictStr] = None
    distro_label: Optional[StrictStr] = None
    end_of_life_date: Optional[date] = Field(default=None, description="The OS no longer receives any updates and may be disabled at any time")
    end_of_service_date: Optional[date] = Field(default=None, description="When the OS is nearing end of life, typically 30 days before end of life")
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    licensed: Optional[StrictBool] = Field(default=None, description="Licenced OS is priced according to pricing property")
    lifecycle_state: Optional[StrictStr] = Field(default=None, description="Where in the support lifecycle the OS is")
    name: Optional[StrictStr] = None
    preinstallable: Optional[StrictBool] = Field(default=None, description="Servers can be already preinstalled with OS in order to shorten provision time.")
    pricing: Optional[Dict[str, Any]] = Field(default=None, description="This object contains price per time unit and optional multiplier value if licence price depends on hardware plan or components (e.g. number of cores)")
    provisionable_on: Optional[List[StrictStr]] = None
    release_date: Optional[date] = Field(default=None, description="The date when the OS was released")
    release_notes: Optional[StrictStr] = Field(default=None, description="The current release notes for this OS image, typically in Markdown format")
    slug: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["build_date", "default_operating_system", "deprecation_date", "distro", "distro_label", "end_of_life_date", "end_of_service_date", "href", "id", "licensed", "lifecycle_state", "name", "preinstallable", "pricing", "provisionable_on", "release_date", "release_notes", "slug", "version"]

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
        """Create an instance of OperatingSystem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "default_operating_system",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OperatingSystem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "build_date": obj.get("build_date"),
            "default_operating_system": obj.get("default_operating_system"),
            "deprecation_date": obj.get("deprecation_date"),
            "distro": obj.get("distro"),
            "distro_label": obj.get("distro_label"),
            "end_of_life_date": obj.get("end_of_life_date"),
            "end_of_service_date": obj.get("end_of_service_date"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "licensed": obj.get("licensed"),
            "lifecycle_state": obj.get("lifecycle_state"),
            "name": obj.get("name"),
            "preinstallable": obj.get("preinstallable"),
            "pricing": obj.get("pricing"),
            "provisionable_on": obj.get("provisionable_on"),
            "release_date": obj.get("release_date"),
            "release_notes": obj.get("release_notes"),
            "slug": obj.get("slug"),
            "version": obj.get("version")
        })
        return _obj


