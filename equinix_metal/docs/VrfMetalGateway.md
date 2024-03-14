# VrfMetalGateway


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
from equinix_metal.models.vrf_metal_gateway import VrfMetalGateway

# TODO update the JSON string below
json = "{}"
# create an instance of VrfMetalGateway from a JSON string
vrf_metal_gateway_instance = VrfMetalGateway.from_json(json)
# print the JSON string representation of the object
print(VrfMetalGateway.to_json())

# convert the object into a dict
vrf_metal_gateway_dict = vrf_metal_gateway_instance.to_dict()
# create an instance of VrfMetalGateway from a dict
vrf_metal_gateway_form_dict = vrf_metal_gateway.from_dict(vrf_metal_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


