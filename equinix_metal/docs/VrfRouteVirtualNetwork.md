# VrfRouteVirtualNetwork

A link to the Virtual Network to which this VRF Route is associated, through the Metal Gateway

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**assigned_to** | [**Href**](Href.md) |  | [optional] 
**assigned_to_virtual_circuit** | **bool** | True if the virtual network is attached to a virtual circuit. False if not. | [optional] 
**description** | **str** |  | [optional] 
**facility** | [**Href**](Href.md) |  | [optional] 
**id** | **str** |  | [optional] 
**instances** | [**List[Href]**](Href.md) | A list of instances with ports currently associated to this Virtual Network. | [optional] 
**metal_gateways** | [**List[MetalGatewayLite]**](MetalGatewayLite.md) | A list of metal gateways currently associated to this Virtual Network. | [optional] 
**metro** | [**Href**](Href.md) |  | [optional] 
**metro_code** | **str** | The Metro code of the metro in which this Virtual Network is defined. | [optional] 
**vxlan** | **int** |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_route_virtual_network import VrfRouteVirtualNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of VrfRouteVirtualNetwork from a JSON string
vrf_route_virtual_network_instance = VrfRouteVirtualNetwork.from_json(json)
# print the JSON string representation of the object
print VrfRouteVirtualNetwork.to_json()

# convert the object into a dict
vrf_route_virtual_network_dict = vrf_route_virtual_network_instance.to_dict()
# create an instance of VrfRouteVirtualNetwork from a dict
vrf_route_virtual_network_form_dict = vrf_route_virtual_network.from_dict(vrf_route_virtual_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


