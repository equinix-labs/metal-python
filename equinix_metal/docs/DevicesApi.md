# equinix_metal.DevicesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DevicesApi.md#create_device) | **POST** /projects/{id}/devices | Create a device
[**create_ip_assignment**](DevicesApi.md#create_ip_assignment) | **POST** /devices/{id}/ips | Create an ip assignment
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /devices/{id} | Delete the device
[**find_device_by_id**](DevicesApi.md#find_device_by_id) | **GET** /devices/{id} | Retrieve a device
[**find_ip_assignments**](DevicesApi.md#find_ip_assignments) | **GET** /devices/{id}/ips | Retrieve all ip assignments
[**find_organization_devices**](DevicesApi.md#find_organization_devices) | **GET** /organizations/{id}/devices | Retrieve all devices of an organization
[**find_project_devices**](DevicesApi.md#find_project_devices) | **GET** /projects/{id}/devices | Retrieve all devices of a project
[**update_device**](DevicesApi.md#update_device) | **PUT** /devices/{id} | Update the device


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

