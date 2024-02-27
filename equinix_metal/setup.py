# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. Currently the search parameter is only available on devices, ssh_keys, api_keys and memberships endpoints.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "equinix-metal"
VERSION = "0.7.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >=2.6.3, <3",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="Metal API",
    author="Equinix Metal API Team",
    author_email="support@equinixmetal.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Metal API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Equinix Metal",
    long_description_content_type='text/markdown',
    long_description="""\
    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at &lt;https://api.equinix.com/metal/v1&gt;. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at &lt;https://metal.equinix.com/developers/api&gt;.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the &#x60;page&#x60; and &#x60;per_page&#x60; query parameters.  The &#x60;page&#x60; parameter is used to specify the page number. The first page is &#x60;1&#x60;. The &#x60;per_page&#x60; parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the &#x60;sort_by&#x60; query parameter with the root level field name as the value. The &#x60;sort_direction&#x60; parameter is used to specify the sort direction, either either &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the &#x60;type&#x60; field, as in the following request:  &#x60;&#x60;&#x60;sh curl -H &#39;X-Auth-Token: my_authentication_token&#39; \\   https://api.equinix.com/metal/v1/projects/id/ips?type&#x3D;public_ipv4 &#x60;&#x60;&#x60;  Only IP addresses with the &#x60;type&#x60; field set to &#x60;public_ipv4&#x60; will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. Currently the search parameter is only available on devices, ssh_keys, api_keys and memberships endpoints.  To search resources you can use the &#x60;search&#x60; query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns &#x60;href&#x60; values (API links) to the associated resource.  &#x60;&#x60;&#x60;json {   ...   \&quot;project\&quot;: {     \&quot;href\&quot;: \&quot;/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\&quot;   } } &#x60;&#x60;&#x60;  If you&#39;re going need the project details, you can avoid a second API request.  Specify the contained &#x60;href&#x60; resources and collections that you&#39;d like to have included in the response using the &#x60;include&#x60; query parameter.  For example:  &#x60;&#x60;&#x60;sh curl -H &#39;X-Auth-Token: my_authentication_token&#39; \\   https://api.equinix.com/metal/v1/user?include&#x3D;projects &#x60;&#x60;&#x60;  The &#x60;include&#x60; parameter is generally accepted in &#x60;GET&#x60;, &#x60;POST&#x60;, &#x60;PUT&#x60;, and &#x60;PATCH&#x60; requests where &#x60;href&#x60; resources are presented.  To have multiple resources include, use a comma-separated list (e.g. &#x60;?include&#x3D;emails,projects,memberships&#x60;).  &#x60;&#x60;&#x60;sh curl -H &#39;X-Auth-Token: my_authentication_token&#39; \\   https://api.equinix.com/metal/v1/user?include&#x3D;emails,projects,memberships &#x60;&#x60;&#x60;  You may also include nested associations up to three levels deep using dot notation (&#x60;?include&#x3D;memberships.projects&#x60;):  &#x60;&#x60;&#x60;sh curl -H &#39;X-Auth-Token: my_authentication_token&#39; \\   https://api.equinix.com/metal/v1/user?include&#x3D;memberships.projects &#x60;&#x60;&#x60;  To exclude resources, and optimize response delivery, use the &#x60;exclude&#x60; query parameter. The &#x60;exclude&#x60; parameter is generally accepted in &#x60;GET&#x60;, &#x60;POST&#x60;, &#x60;PUT&#x60;, and &#x60;PATCH&#x60; requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an &#x60;href&#x60; field. 
    """,  # noqa: E501
    package_data={"equinix_metal": ["py.typed"]},
)
