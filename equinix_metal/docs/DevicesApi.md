# equinix_metal.DevicesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bgp_session**](DevicesApi.md#create_bgp_session) | **POST** /devices/{id}/bgp/sessions | Create a BGP session
[**create_device**](DevicesApi.md#create_device) | **POST** /projects/{id}/devices | Create a device
[**create_ip_assignment**](DevicesApi.md#create_ip_assignment) | **POST** /devices/{id}/ips | Create an ip assignment
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /devices/{id} | Delete the device
[**find_bgp_sessions**](DevicesApi.md#find_bgp_sessions) | **GET** /devices/{id}/bgp/sessions | Retrieve all BGP sessions
[**find_device_by_id**](DevicesApi.md#find_device_by_id) | **GET** /devices/{id} | Retrieve a device
[**find_device_customdata**](DevicesApi.md#find_device_customdata) | **GET** /devices/{id}/customdata | Retrieve the custom metadata of an instance
[**find_device_metadata_by_id**](DevicesApi.md#find_device_metadata_by_id) | **GET** /devices/{id}/metadata | Retrieve metadata
[**find_device_userdata_by_id**](DevicesApi.md#find_device_userdata_by_id) | **GET** /devices/{id}/userdata | Retrieve userdata
[**find_instance_bandwidth**](DevicesApi.md#find_instance_bandwidth) | **GET** /devices/{id}/bandwidth | Retrieve an instance bandwidth
[**find_ip_assignment_customdata**](DevicesApi.md#find_ip_assignment_customdata) | **GET** /devices/{instance_id}/ips/{id}/customdata | Retrieve the custom metadata of an IP Assignment
[**find_ip_assignments**](DevicesApi.md#find_ip_assignments) | **GET** /devices/{id}/ips | Retrieve all ip assignments
[**find_organization_devices**](DevicesApi.md#find_organization_devices) | **GET** /organizations/{id}/devices | Retrieve all devices of an organization
[**find_project_devices**](DevicesApi.md#find_project_devices) | **GET** /projects/{id}/devices | Retrieve all devices of a project
[**find_traffic**](DevicesApi.md#find_traffic) | **GET** /devices/{id}/traffic | Retrieve device traffic
[**get_bgp_neighbor_data**](DevicesApi.md#get_bgp_neighbor_data) | **GET** /devices/{id}/bgp/neighbors | Retrieve BGP neighbor data for this device
[**perform_action**](DevicesApi.md#perform_action) | **POST** /devices/{id}/actions | Perform an action
[**update_device**](DevicesApi.md#update_device) | **PUT** /devices/{id} | Update the device


# **create_bgp_session**
> BgpSession create_bgp_session(id, bgp_session_input)

Create a BGP session

Creates a BGP session.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    bgp_session_input = equinix_metal.BGPSessionInput() # BGPSessionInput | BGP session to create

    try:
        # Create a BGP session
        api_response = api_instance.create_bgp_session(id, bgp_session_input)
        print("The response of DevicesApi->create_bgp_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_bgp_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **bgp_session_input** | [**BGPSessionInput**](BGPSessionInput.md)| BGP session to create | 

### Return type

[**BgpSession**](BgpSession.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device**
> Device create_device(id, create_device_request)

Create a device

Creates a new device and provisions it in the specified location.  Device type-specific options are accepted.  For example, `baremetal` devices accept `operating_system`, `hostname`, and `plan`. These parameters may not be accepted for other device types. The default device type is `baremetal`.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Project UUID
    create_device_request = equinix_metal.CreateDeviceRequest() # CreateDeviceRequest | Device to create

    try:
        # Create a device
        api_response = api_instance.create_device(id, create_device_request)
        print("The response of DevicesApi->create_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **create_device_request** | [**CreateDeviceRequest**](CreateDeviceRequest.md)| Device to create | 

### Return type

[**Device**](Device.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ip_assignment**
> IPAssignment create_ip_assignment(id, ip_assignment_input)

Create an ip assignment

Creates an ip assignment for a device.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    ip_assignment_input = equinix_metal.IPAssignmentInput() # IPAssignmentInput | IPAssignment to create

    try:
        # Create an ip assignment
        api_response = api_instance.create_ip_assignment(id, ip_assignment_input)
        print("The response of DevicesApi->create_ip_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_ip_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **ip_assignment_input** | [**IPAssignmentInput**](IPAssignmentInput.md)| IPAssignment to create | 

### Return type

[**IPAssignment**](IPAssignment.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> delete_device(id, force_delete=force_delete)

Delete the device

Deletes a device and deprovisions it in our datacenter.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    force_delete = True # bool | Force the deletion of the device, by detaching any storage volume still active. (optional)

    try:
        # Delete the device
        api_instance.delete_device(id, force_delete=force_delete)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **force_delete** | **bool**| Force the deletion of the device, by detaching any storage volume still active. | [optional] 

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_bgp_sessions**
> BgpSessionList find_bgp_sessions(id)

Retrieve all BGP sessions

Provides a listing of available BGP sessions for the device.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID

    try:
        # Retrieve all BGP sessions
        api_response = api_instance.find_bgp_sessions(id)
        print("The response of DevicesApi->find_bgp_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_bgp_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 

### Return type

[**BgpSessionList**](BgpSessionList.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_device_by_id**
> Device find_device_by_id(id, include=include, exclude=exclude)

Retrieve a device

Type-specific options (such as facility for baremetal devices) will be included as part of the main data structure.                          State value can be one of: active inactive queued or provisioning

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve a device
        api_response = api_instance.find_device_by_id(id, include=include, exclude=exclude)
        print("The response of DevicesApi->find_device_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**Device**](Device.md)

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

# **find_device_customdata**
> find_device_customdata(id)

Retrieve the custom metadata of an instance

Provides the custom metadata stored for this instance in json format

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Instance UUID

    try:
        # Retrieve the custom metadata of an instance
        api_instance.find_device_customdata(id)
    except Exception as e:
        print("Exception when calling DevicesApi->find_device_customdata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Instance UUID | 

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
**200** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_device_metadata_by_id**
> Metadata find_device_metadata_by_id(id)

Retrieve metadata

Retrieve device metadata

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID

    try:
        # Retrieve metadata
        api_response = api_instance.find_device_metadata_by_id(id)
        print("The response of DevicesApi->find_device_metadata_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_device_metadata_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 

### Return type

[**Metadata**](Metadata.md)

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
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_device_userdata_by_id**
> Userdata find_device_userdata_by_id(id)

Retrieve userdata

Retrieve device userdata

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID

    try:
        # Retrieve userdata
        api_response = api_instance.find_device_userdata_by_id(id)
        print("The response of DevicesApi->find_device_userdata_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_device_userdata_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 

### Return type

[**Userdata**](Userdata.md)

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
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_instance_bandwidth**
> find_instance_bandwidth(id, var_from, until)

Retrieve an instance bandwidth

Retrieve an instance bandwidth for a given period of time.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    var_from = 'var_from_example' # str | Timestamp from range
    until = 'until_example' # str | Timestamp to range

    try:
        # Retrieve an instance bandwidth
        api_instance.find_instance_bandwidth(id, var_from, until)
    except Exception as e:
        print("Exception when calling DevicesApi->find_instance_bandwidth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **var_from** | **str**| Timestamp from range | 
 **until** | **str**| Timestamp to range | 

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
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ip_assignment_customdata**
> find_ip_assignment_customdata(instance_id, id)

Retrieve the custom metadata of an IP Assignment

Provides the custom metadata stored for this IP Assignment in json format

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
    api_instance = equinix_metal.DevicesApi(api_client)
    instance_id = 'instance_id_example' # str | Instance UUID
    id = 'id_example' # str | Ip Assignment UUID

    try:
        # Retrieve the custom metadata of an IP Assignment
        api_instance.find_ip_assignment_customdata(instance_id, id)
    except Exception as e:
        print("Exception when calling DevicesApi->find_ip_assignment_customdata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance UUID | 
 **id** | **str**| Ip Assignment UUID | 

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
**200** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ip_assignments**
> IPAssignmentList find_ip_assignments(id, include=include, exclude=exclude)

Retrieve all ip assignments

Returns all ip assignments for a device.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve all ip assignments
        api_response = api_instance.find_ip_assignments(id, include=include, exclude=exclude)
        print("The response of DevicesApi->find_ip_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_ip_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**IPAssignmentList**](IPAssignmentList.md)

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
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_organization_devices**
> DeviceList find_organization_devices(id, facility=facility, hostname=hostname, reserved=reserved, tag=tag, type=type, include=include, exclude=exclude, page=page, per_page=per_page)

Retrieve all devices of an organization

Provides a collection of devices for a given organization.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Organization UUID
    facility = 'facility_example' # str | Filter by device facility (optional)
    hostname = 'hostname_example' # str | Filter by partial hostname (optional)
    reserved = True # bool | Filter only reserved instances (optional)
    tag = 'tag_example' # str | Filter by device tag (optional)
    type = 'type_example' # str | Filter by instance type (ondemand,spot,reserved) (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Retrieve all devices of an organization
        api_response = api_instance.find_organization_devices(id, facility=facility, hostname=hostname, reserved=reserved, tag=tag, type=type, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of DevicesApi->find_organization_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_organization_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization UUID | 
 **facility** | **str**| Filter by device facility | [optional] 
 **hostname** | **str**| Filter by partial hostname | [optional] 
 **reserved** | **bool**| Filter only reserved instances | [optional] 
 **tag** | **str**| Filter by device tag | [optional] 
 **type** | **str**| Filter by instance type (ondemand,spot,reserved) | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**DeviceList**](DeviceList.md)

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

# **find_project_devices**
> DeviceList find_project_devices(id, facility=facility, hostname=hostname, reserved=reserved, tag=tag, type=type, include=include, exclude=exclude, page=page, per_page=per_page)

Retrieve all devices of a project

Provides a collection of devices for a given project.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Project UUID
    facility = 'facility_example' # str | Filter by device facility (optional)
    hostname = 'hostname_example' # str | Filter by partial hostname (optional)
    reserved = True # bool | Filter only reserved instances (optional)
    tag = 'tag_example' # str | Filter by device tag (optional)
    type = 'type_example' # str | Filter by instance type (ondemand,spot,reserved) (optional)
    include = ['include_example'] # List[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
    exclude = ['exclude_example'] # List[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
    page = 1 # int | Page to return (optional) (default to 1)
    per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Retrieve all devices of a project
        api_response = api_instance.find_project_devices(id, facility=facility, hostname=hostname, reserved=reserved, tag=tag, type=type, include=include, exclude=exclude, page=page, per_page=per_page)
        print("The response of DevicesApi->find_project_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->find_project_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project UUID | 
 **facility** | **str**| Filter by device facility | [optional] 
 **hostname** | **str**| Filter by partial hostname | [optional] 
 **reserved** | **bool**| Filter only reserved instances | [optional] 
 **tag** | **str**| Filter by device tag | [optional] 
 **type** | **str**| Filter by instance type (ondemand,spot,reserved) | [optional] 
 **include** | [**List[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**List[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**DeviceList**](DeviceList.md)

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

# **find_traffic**
> find_traffic(id, direction, interval=interval, bucket=bucket, timeframe=timeframe)

Retrieve device traffic

Returns traffic for a specific device.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    direction = 'direction_example' # str | Traffic direction
    interval = 'interval_example' # str | Traffic interval (optional)
    bucket = 'bucket_example' # str | Traffic bucket (optional)
    timeframe = {'key': equinix_metal.FindTrafficTimeframeParameter()} # FindTrafficTimeframeParameter |  (optional)

    try:
        # Retrieve device traffic
        api_instance.find_traffic(id, direction, interval=interval, bucket=bucket, timeframe=timeframe)
    except Exception as e:
        print("Exception when calling DevicesApi->find_traffic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **direction** | **str**| Traffic direction | 
 **interval** | **str**| Traffic interval | [optional] 
 **bucket** | **str**| Traffic bucket | [optional] 
 **timeframe** | [**FindTrafficTimeframeParameter**](.md)|  | [optional] 

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
**200** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgp_neighbor_data**
> BgpSessionNeighbors get_bgp_neighbor_data(id)

Retrieve BGP neighbor data for this device

Provides a summary of the BGP neighbor data associated to the BGP sessions for this device.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID

    try:
        # Retrieve BGP neighbor data for this device
        api_response = api_instance.get_bgp_neighbor_data(id)
        print("The response of DevicesApi->get_bgp_neighbor_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_bgp_neighbor_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 

### Return type

[**BgpSessionNeighbors**](BgpSessionNeighbors.md)

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

# **perform_action**
> perform_action(id, device_action_input)

Perform an action

Performs an action for the given device.  Possible actions include: power_on, power_off, reboot, reinstall, and rescue (reboot the device into rescue OS.)

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    device_action_input = equinix_metal.DeviceActionInput() # DeviceActionInput | Action to perform

    try:
        # Perform an action
        api_instance.perform_action(id, device_action_input)
    except Exception as e:
        print("Exception when calling DevicesApi->perform_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **device_action_input** | [**DeviceActionInput**](DeviceActionInput.md)| Action to perform | 

### Return type

void (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | accepted |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> Device update_device(id, device_update_input)

Update the device

Updates the device.

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
    api_instance = equinix_metal.DevicesApi(api_client)
    id = 'id_example' # str | Device UUID
    device_update_input = equinix_metal.DeviceUpdateInput() # DeviceUpdateInput | Facility to update

    try:
        # Update the device
        api_response = api_instance.update_device(id, device_update_input)
        print("The response of DevicesApi->update_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device UUID | 
 **device_update_input** | [**DeviceUpdateInput**](DeviceUpdateInput.md)| Facility to update | 

### Return type

[**Device**](Device.md)

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

