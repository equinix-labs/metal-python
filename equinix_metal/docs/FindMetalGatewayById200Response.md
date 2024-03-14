# FindMetalGatewayById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**created_by** | [**Href**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ip_reservation** | [**VrfIpReservation**](VrfIpReservation.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**state** | [**MetalGatewayState**](MetalGatewayState.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 
**vrf** | [**Vrf**](Vrf.md) |  | [optional] 

## Example

```python
from equinix_metal.models.find_metal_gateway_by_id200_response import FindMetalGatewayById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FindMetalGatewayById200Response from a JSON string
find_metal_gateway_by_id200_response_instance = FindMetalGatewayById200Response.from_json(json)
# print the JSON string representation of the object
print(FindMetalGatewayById200Response.to_json())

# convert the object into a dict
find_metal_gateway_by_id200_response_dict = find_metal_gateway_by_id200_response_instance.to_dict()
# create an instance of FindMetalGatewayById200Response from a dict
find_metal_gateway_by_id200_response_form_dict = find_metal_gateway_by_id200_response.from_dict(find_metal_gateway_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


