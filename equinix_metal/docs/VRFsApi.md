# equinix_metal.VRFsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_vrf_ip_reservation**](VRFsApi.md#find_vrf_ip_reservation) | **GET** /vrfs/{vrf_id}/ips/{id} | Retrieve all VRF IP Reservations in the VRF


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

