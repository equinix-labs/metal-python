# VlanVirtualCircuit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill** | **bool** | True if the Virtual Circuit is being billed. Currently, only Virtual Circuits of Fabric VCs (Metal Billed) will be billed. Usage will start the first time the Virtual Circuit becomes active, and will not stop until it is deleted from Metal. | [optional] [default to False]
**bill_type** | **str** | Fabric Billed if the Virtual Circuit is billed by Fabric. Metal Billed if the Virtual Circuit is billed by Metal. Legacy Virtual Circuits will have a value of nil. | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nni_vlan** | **int** |  | [optional] 
**port** | [**InterconnectionPort**](InterconnectionPort.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**provider_connection_id** | **str** | This field is relevant if using the &#x60;shared_port_vlan_to_csp&#x60; interconnection type. Once activated on the CSP, this field should contain the resource name that the virtual circuit is connected to on the provider&#39;s end. | [optional] 
**speed** | **int** | For Virtual Circuits on shared and dedicated connections, this speed should match the one set on their Interconnection Ports. For Virtual Circuits on Fabric VCs (both Metal and Fabric Billed) that have found their corresponding Fabric connection, this is the actual speed of the interconnection that was configured when setting up the interconnection on the Fabric Portal. Details on Fabric VCs are included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details. | [optional] 
**status** | **str** | The status of a Virtual Circuit is always &#39;pending&#39; on creation. The status can turn to &#39;Waiting on Customer VLAN&#39; if a Metro VLAN was not set yet on the Virtual Circuit and is the last step needed for full activation. For Dedicated interconnections, as long as the Dedicated Port has been associated to the Virtual Circuit and a NNI VNID has been set, it will turn to &#39;waiting_on_customer_vlan&#39;. For Fabric VCs, it will only change to &#39;waiting_on_customer_vlan&#39; once the corresponding Fabric connection has been found on the Fabric side. If the Fabric service token associated with the Virtual Circuit hasn&#39;t been redeemed on Fabric within the expiry time, it will change to an &#x60;expired&#x60; status. Once a Metro VLAN is set on the Virtual Circuit (which for Fabric VCs, can be set on creation of a Fabric VC) and the necessary set up is done, it will turn into &#39;Activating&#39; status as it tries to activate the Virtual Circuit. Once the Virtual Circuit fully activates and is configured on the switch, it will turn to staus &#39;active&#39;. For Fabric VCs (Metal Billed), we will start billing the moment the status of the Virtual Circuit turns to &#39;active&#39;. If there are any changes to the VLAN after the Virtual Circuit is in an &#39;active&#39; status, the status will show &#39;changing_vlan&#39; if a new VLAN has been provided, or &#39;deactivating&#39; if we are removing the VLAN. When a deletion request is issued for the Virtual Circuit, it will move to a &#39;deleting&#39; status, and we will immediately unconfigure the switch for the Virtual Circuit and issue a deletion on any associated Fabric connections. Any associated Metro VLANs on the virtual circuit will also be unassociated after the switch has been successfully unconfigured. If there are any associated Fabric connections, we will only fully delete the Virtual Circuit once we have checked that the Fabric connection was fully deprovisioned on Fabric. | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**virtual_network** | [**Href**](Href.md) |  | [optional] 
**vnid** | **int** |  | [optional] 

## Example

```python
from equinix_metal.models.vlan_virtual_circuit import VlanVirtualCircuit

# TODO update the JSON string below
json = "{}"
# create an instance of VlanVirtualCircuit from a JSON string
vlan_virtual_circuit_instance = VlanVirtualCircuit.from_json(json)
# print the JSON string representation of the object
print(VlanVirtualCircuit.to_json())

# convert the object into a dict
vlan_virtual_circuit_dict = vlan_virtual_circuit_instance.to_dict()
# create an instance of VlanVirtualCircuit from a dict
vlan_virtual_circuit_form_dict = vlan_virtual_circuit.from_dict(vlan_virtual_circuit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


