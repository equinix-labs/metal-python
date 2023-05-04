# equinix_metal.VRFsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vrf**](VRFsApi.md#create_vrf) | **POST** /projects/{id}/vrfs | Create a new VRF in the specified project
[**create_vrf_route**](VRFsApi.md#create_vrf_route) | **POST** /vrfs/{id}/routes | Create a VRF route
[**delete_vrf**](VRFsApi.md#delete_vrf) | **DELETE** /vrfs/{id} | Delete the VRF
[**delete_vrf_route_by_id**](VRFsApi.md#delete_vrf_route_by_id) | **DELETE** /routes/{id} | Delete a VRF Route
[**find_vrf_by_id**](VRFsApi.md#find_vrf_by_id) | **GET** /vrfs/{id} | Retrieve a VRF
[**find_vrf_ip_reservation**](VRFsApi.md#find_vrf_ip_reservation) | **GET** /vrfs/{vrf_id}/ips/{id} | Retrieve all VRF IP Reservations in the VRF
[**find_vrf_ip_reservations**](VRFsApi.md#find_vrf_ip_reservations) | **GET** /vrfs/{id}/ips | Retrieve all VRF IP Reservations in the VRF
[**find_vrf_route_by_id**](VRFsApi.md#find_vrf_route_by_id) | **GET** /routes/{id} | Retrieve a VRF Route
[**find_vrfs**](VRFsApi.md#find_vrfs) | **GET** /projects/{id}/vrfs | Retrieve all VRFs in the project
[**get_vrf_routes**](VRFsApi.md#get_vrf_routes) | **GET** /vrfs/{id}/routes | Retrieve all routes in the VRF
[**update_vrf**](VRFsApi.md#update_vrf) | **PUT** /vrfs/{id} | Update the VRF
[**update_vrf_route_by_id**](VRFsApi.md#update_vrf_route_by_id) | **PUT** /routes/{id} | Update a VRF Route


# **create_vrf**
> Vrf create_vrf(id, vrf_create_input)

Create a new VRF in the specified project

Creates a new VRF in the specified project

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | Project UUID
    vrf_create_input = equinix_metal.VrfCreateInput() # VrfCreateInput | VRF to create

    try:
        # Create a new VRF in the specified project
        api_response = api_instance.create_vrf(id, vrf_create_input)
        print("The response of VRFsApi->create_vrf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->create_vrf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **vrf_create_input** | [**VrfCreateInput**](VrfCreateInput.md)| VRF to create | 

### Return type

[**Vrf**](Vrf.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vrf_route**
> VrfRoute create_vrf_route(id, vrf_route_create_input)

Create a VRF route

Create a route in a VRF. Currently only static default routes are supported.  Notice: VRFs are a test feature currently under active development, and only available to certain users. Please contact Customer Success for more information. 

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | VRF UUID
    vrf_route_create_input = equinix_metal.VrfRouteCreateInput() # VrfRouteCreateInput | 

    try:
        # Create a VRF route
        api_response = api_instance.create_vrf_route(id, vrf_route_create_input)
        print("The response of VRFsApi->create_vrf_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->create_vrf_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VRF UUID | 
 **vrf_route_create_input** | [**VrfRouteCreateInput**](VrfRouteCreateInput.md)|  | 

### Return type

[**VrfRoute**](VrfRoute.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vrf**
> delete_vrf(id)

Delete the VRF

Deletes the VRF

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | VRF UUID

    try:
        # Delete the VRF
        api_instance.delete_vrf(id)
    except Exception as e:
        print("Exception when calling VRFsApi->delete_vrf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VRF UUID | 

### Return type

void (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | no content |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vrf_route_by_id**
> VrfRoute delete_vrf_route_by_id(id, include=include, exclude=exclude)

Delete a VRF Route

Trigger the deletion of a VRF Route resource. The status of the route will update to 'deleting', and the route resource will remain accessible while background operations remove the route from the network. Once the route has been removed from the network, the resource will be fully deleted.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | VRF Route UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Delete a VRF Route
        api_response = api_instance.delete_vrf_route_by_id(id, include=include, exclude=exclude)
        print("The response of VRFsApi->delete_vrf_route_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->delete_vrf_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VRF Route UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VrfRoute**](VrfRoute.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_vrf_by_id**
> Vrf find_vrf_by_id(id, include=include, exclude=exclude)

Retrieve a VRF

Returns a single VRF resource

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | VRF UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve a VRF
        api_response = api_instance.find_vrf_by_id(id, include=include, exclude=exclude)
        print("The response of VRFsApi->find_vrf_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->find_vrf_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VRF UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Vrf**](Vrf.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_vrf_ip_reservation**
> VrfIpReservation find_vrf_ip_reservation(vrf_id, id, include=include, exclude=exclude)

Retrieve all VRF IP Reservations in the VRF

Returns the IP Reservation for the VRF.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    vrf_id = 'vrf_id_example' # str | VRF UUID
    id = 'id_example' # str | IP UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve all VRF IP Reservations in the VRF
        api_response = api_instance.find_vrf_ip_reservation(vrf_id, id, include=include, exclude=exclude)
        print("The response of VRFsApi->find_vrf_ip_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->find_vrf_ip_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vrf_id** | **str**| VRF UUID | 
 **id** | **str**| IP UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VrfIpReservation**](VrfIpReservation.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_vrf_ip_reservations**
> VrfIpReservationList find_vrf_ip_reservations(id, include=include, exclude=exclude)

Retrieve all VRF IP Reservations in the VRF

Returns the list of VRF IP Reservations for the VRF.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | VRF UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve all VRF IP Reservations in the VRF
        api_response = api_instance.find_vrf_ip_reservations(id, include=include, exclude=exclude)
        print("The response of VRFsApi->find_vrf_ip_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->find_vrf_ip_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VRF UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VrfIpReservationList**](VrfIpReservationList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_vrf_route_by_id**
> VrfRoute find_vrf_route_by_id(id, include=include, exclude=exclude)

Retrieve a VRF Route

Returns a single VRF Route resource

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | VRF Route UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve a VRF Route
        api_response = api_instance.find_vrf_route_by_id(id, include=include, exclude=exclude)
        print("The response of VRFsApi->find_vrf_route_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->find_vrf_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VRF Route UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VrfRoute**](VrfRoute.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_vrfs**
> VrfList find_vrfs(id, include=include, exclude=exclude, metro=metro)

Retrieve all VRFs in the project

Returns the list of VRFs for a single project.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | Project UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    metro = 'metro_example' # str | Filter by Metro ID (uuid) or Metro Code (optional)

    try:
        # Retrieve all VRFs in the project
        api_response = api_instance.find_vrfs(id, include=include, exclude=exclude, metro=metro)
        print("The response of VRFsApi->find_vrfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->find_vrfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **metro** | **str**| Filter by Metro ID (uuid) or Metro Code | [optional] 

### Return type

[**VrfList**](VrfList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vrf_routes**
> VrfRouteList get_vrf_routes(id, include=include, exclude=exclude)

Retrieve all routes in the VRF

Returns the list of routes for the VRF

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | VRF UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve all routes in the VRF
        api_response = api_instance.get_vrf_routes(id, include=include, exclude=exclude)
        print("The response of VRFsApi->get_vrf_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->get_vrf_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VRF UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VrfRouteList**](VrfRouteList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vrf**
> Vrf update_vrf(id, vrf_update_input)

Update the VRF

Updates the VRF.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | VRF UUID
    vrf_update_input = equinix_metal.VrfUpdateInput() # VrfUpdateInput | VRF to update

    try:
        # Update the VRF
        api_response = api_instance.update_vrf(id, vrf_update_input)
        print("The response of VRFsApi->update_vrf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->update_vrf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VRF UUID | 
 **vrf_update_input** | [**VrfUpdateInput**](VrfUpdateInput.md)| VRF to update | 

### Return type

[**Vrf**](Vrf.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vrf_route_by_id**
> VrfRoute update_vrf_route_by_id(id, include=include, exclude=exclude)

Update a VRF Route

Requests a VRF Route be redeployed across the network. Updating the prefix or next-hop address on a route is not currently supported.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import os
import equinix_metal
from equinix_metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = equinix_metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with equinix_metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = equinix_metal.VRFsApi(api_client)
    id = 'id_example' # str | VRF Route UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Update a VRF Route
        api_response = api_instance.update_vrf_route_by_id(id, include=include, exclude=exclude)
        print("The response of VRFsApi->update_vrf_route_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VRFsApi->update_vrf_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VRF Route UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VrfRoute**](VrfRoute.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

