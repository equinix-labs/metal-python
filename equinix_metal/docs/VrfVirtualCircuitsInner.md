# VrfVirtualCircuitsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ip** | **str** | An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used. | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**md5** | **str** | The MD5 password for the BGP peering in plaintext (not a checksum). | [optional] 
**metal_ip** | **str** | An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used. | [optional] 
**name** | **str** |  | [optional] 
**peer_asn** | **int** | The peer ASN that will be used with the VRF on the Virtual Circuit. | [optional] 
**port** | [**Href**](Href.md) |  | [optional] 
**status** | **str** |  | [optional] 
**subnet** | **str** | The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. | [optional] 

## Example

```python
from equinix_metal.models.vrf_virtual_circuits_inner import VrfVirtualCircuitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VrfVirtualCircuitsInner from a JSON string
vrf_virtual_circuits_inner_instance = VrfVirtualCircuitsInner.from_json(json)
# print the JSON string representation of the object
print VrfVirtualCircuitsInner.to_json()

# convert the object into a dict
vrf_virtual_circuits_inner_dict = vrf_virtual_circuits_inner_instance.to_dict()
# create an instance of VrfVirtualCircuitsInner from a dict
vrf_virtual_circuits_inner_form_dict = vrf_virtual_circuits_inner.from_dict(vrf_virtual_circuits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


