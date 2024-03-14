# VrfRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**href** | **str** |  | [optional] [readonly] 
**id** | **str** | The unique identifier for the newly-created resource | [optional] [readonly] 
**metal_gateway** | [**VrfMetalGateway**](VrfMetalGateway.md) |  | [optional] 
**next_hop** | **str** | The next-hop IPv4 address for the route | [optional] 
**prefix** | **str** | The IPv4 prefix for the route, in CIDR-style notation | [optional] 
**status** | [**VrfRouteStatus**](VrfRouteStatus.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | [**VrfRouteType**](VrfRouteType.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 
**vrf** | [**Vrf**](Vrf.md) |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_route import VrfRoute

# TODO update the JSON string below
json = "{}"
# create an instance of VrfRoute from a JSON string
vrf_route_instance = VrfRoute.from_json(json)
# print the JSON string representation of the object
print(VrfRoute.to_json())

# convert the object into a dict
vrf_route_dict = vrf_route_instance.to_dict()
# create an instance of VrfRoute from a dict
vrf_route_form_dict = vrf_route.from_dict(vrf_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


