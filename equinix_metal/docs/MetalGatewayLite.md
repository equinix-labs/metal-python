# MetalGatewayLite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**gateway_address** | **str** | The gateway address with subnet CIDR value for this Metal Gateway. For example, a Metal Gateway using an IP reservation with block 10.1.2.0/27 would have a gateway address of 10.1.2.1/27. | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**state** | [**MetalGatewayState**](MetalGatewayState.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**vlan** | **int** | The VLAN id of the Virtual Network record associated to this Metal Gateway. | [optional] 

## Example

```python
from equinix_metal.models.metal_gateway_lite import MetalGatewayLite

# TODO update the JSON string below
json = "{}"
# create an instance of MetalGatewayLite from a JSON string
metal_gateway_lite_instance = MetalGatewayLite.from_json(json)
# print the JSON string representation of the object
print(MetalGatewayLite.to_json())

# convert the object into a dict
metal_gateway_lite_dict = metal_gateway_lite_instance.to_dict()
# create an instance of MetalGatewayLite from a dict
metal_gateway_lite_form_dict = metal_gateway_lite.from_dict(metal_gateway_lite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


