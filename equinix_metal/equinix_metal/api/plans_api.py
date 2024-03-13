# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. Currently the search parameter is only available on devices, ssh_keys, api_keys and memberships endpoints.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from equinix_metal.models.plan_list import PlanList

from equinix_metal.api_client import ApiClient, RequestSerialized
from equinix_metal.api_response import ApiResponse
from equinix_metal.rest import RESTResponseType


class PlansApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
    @validate_call
    def find_plans(
        self,
        categories: Annotated[Optional[List[StrictStr]], Field(description="Filter plans by its category")] = None,
        type: Annotated[Optional[StrictStr], Field(description="Filter plans by its plan type")] = None,
        slug: Annotated[Optional[StrictStr], Field(description="Filter plans by slug")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.")] = None,
        exclude: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PlanList:
        """Retrieve all plans

        Provides a listing of available plans to provision your device on.

        :param categories: Filter plans by its category
        :type categories: List[str]
        :param type: Filter plans by its plan type
        :type type: str
        :param slug: Filter plans by slug
        :type slug: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: List[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._find_plans_serialize(
            categories=categories,
            type=type,
            slug=slug,
            include=include,
            exclude=exclude,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanList",
            '401': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def find_plans_with_http_info(
        self,
        categories: Annotated[Optional[List[StrictStr]], Field(description="Filter plans by its category")] = None,
        type: Annotated[Optional[StrictStr], Field(description="Filter plans by its plan type")] = None,
        slug: Annotated[Optional[StrictStr], Field(description="Filter plans by slug")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.")] = None,
        exclude: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PlanList]:
        """Retrieve all plans

        Provides a listing of available plans to provision your device on.

        :param categories: Filter plans by its category
        :type categories: List[str]
        :param type: Filter plans by its plan type
        :type type: str
        :param slug: Filter plans by slug
        :type slug: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: List[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._find_plans_serialize(
            categories=categories,
            type=type,
            slug=slug,
            include=include,
            exclude=exclude,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanList",
            '401': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def find_plans_without_preload_content(
        self,
        categories: Annotated[Optional[List[StrictStr]], Field(description="Filter plans by its category")] = None,
        type: Annotated[Optional[StrictStr], Field(description="Filter plans by its plan type")] = None,
        slug: Annotated[Optional[StrictStr], Field(description="Filter plans by slug")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.")] = None,
        exclude: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve all plans

        Provides a listing of available plans to provision your device on.

        :param categories: Filter plans by its category
        :type categories: List[str]
        :param type: Filter plans by its plan type
        :type type: str
        :param slug: Filter plans by slug
        :type slug: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: List[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._find_plans_serialize(
            categories=categories,
            type=type,
            slug=slug,
            include=include,
            exclude=exclude,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanList",
            '401': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _find_plans_serialize(
        self,
        categories,
        type,
        slug,
        include,
        exclude,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'categories[]': 'multi',
            'include': 'csv',
            'exclude': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if categories is not None:
            
            _query_params.append(('categories[]', categories))
            
        if type is not None:
            
            _query_params.append(('type', type))
            
        if slug is not None:
            
            _query_params.append(('slug', slug))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if exclude is not None:
            
            _query_params.append(('exclude', exclude))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'x_auth_token'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/plans',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


    @validate_call
    def find_plans_by_project(
        self,
        id: Annotated[StrictStr, Field(description="Project UUID")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.")] = None,
        exclude: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PlanList:
        """Retrieve all plans visible by the project

        Returns a listing of available plans for the given project

        :param id: Project UUID (required)
        :type id: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: List[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._find_plans_by_project_serialize(
            id=id,
            include=include,
            exclude=exclude,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanList",
            '401': "Error",
            '403': "Error",
            '404': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def find_plans_by_project_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Project UUID")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.")] = None,
        exclude: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PlanList]:
        """Retrieve all plans visible by the project

        Returns a listing of available plans for the given project

        :param id: Project UUID (required)
        :type id: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: List[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._find_plans_by_project_serialize(
            id=id,
            include=include,
            exclude=exclude,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanList",
            '401': "Error",
            '403': "Error",
            '404': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def find_plans_by_project_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Project UUID")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.")] = None,
        exclude: Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve all plans visible by the project

        Returns a listing of available plans for the given project

        :param id: Project UUID (required)
        :type id: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: List[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._find_plans_by_project_serialize(
            id=id,
            include=include,
            exclude=exclude,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanList",
            '401': "Error",
            '403': "Error",
            '404': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _find_plans_by_project_serialize(
        self,
        id,
        include,
        exclude,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'csv',
            'exclude': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if exclude is not None:
            
            _query_params.append(('exclude', exclude))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'x_auth_token'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/projects/{id}/plans',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


