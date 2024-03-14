# MetalGateway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**created_by** | [**Href**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ip_reservation** | [**IPReservation**](IPReservation.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**state** | [**MetalGatewayState**](MetalGatewayState.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 

## Example

```python
from equinix_metal.models.metal_gateway import MetalGateway

# TODO update the JSON string below
json = "{}"
# create an instance of MetalGateway from a JSON string
metal_gateway_instance = MetalGateway.from_json(json)
# print the JSON string representation of the object
print(MetalGateway.to_json())

# convert the object into a dict
metal_gateway_dict = metal_gateway_instance.to_dict()
# create an instance of MetalGateway from a dict
metal_gateway_form_dict = metal_gateway.from_dict(metal_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


