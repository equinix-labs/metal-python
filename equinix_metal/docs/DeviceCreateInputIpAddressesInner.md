# DeviceCreateInputIpAddressesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **int** | Address Family for IP Address | [optional] 
**cidr** | **int** | Cidr Size for the IP Block created. Valid values depends on the operating system being provisioned. (28..32 for IPv4 addresses, 124..127 for IPv6 addresses) | [optional] 
**ip_reservations** | **List[str]** | UUIDs of any IP reservations to use when assigning IPs | [optional] 
**public** | **bool** | Address Type for IP Address | [optional] [default to True]
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.device_create_input_ip_addresses_inner import DeviceCreateInputIpAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCreateInputIpAddressesInner from a JSON string
device_create_input_ip_addresses_inner_instance = DeviceCreateInputIpAddressesInner.from_json(json)
# print the JSON string representation of the object
print DeviceCreateInputIpAddressesInner.to_json()

# convert the object into a dict
device_create_input_ip_addresses_inner_dict = device_create_input_ip_addresses_inner_instance.to_dict()
# create an instance of DeviceCreateInputIpAddressesInner from a dict
device_create_input_ip_addresses_inner_form_dict = device_create_input_ip_addresses_inner.from_dict(device_create_input_ip_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


