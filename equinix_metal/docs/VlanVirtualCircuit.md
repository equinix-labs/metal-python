# VlanVirtualCircuit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill** | **bool** | True if the Virtual Circuit is being billed. Currently, only Virtual Circuits of Fabric VCs (Metal Billed) will be billed. Usage will start the first time the Virtual Circuit becomes active, and will not stop until it is deleted from Metal. | [optional] [default to False]
**bill_type** | [**VlanVirtualCircuitBillType**](VlanVirtualCircuitBillType.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nni_vlan** | **int** |  | [optional] 
**port** | [**InterconnectionPort**](InterconnectionPort.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**speed** | **int** | For Virtual Circuits on shared and dedicated connections, this speed should match the one set on their Interconnection Ports. For Virtual Circuits on Fabric VCs (both Metal and Fabric Billed) that have found their corresponding Fabric connection, this is the actual speed of the interconnection that was configured when setting up the interconnection on the Fabric Portal. Details on Fabric VCs are included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details. | [optional] 
**status** | [**VlanVirtualCircuitStatus**](VlanVirtualCircuitStatus.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | [**VlanVirtualCircuitType**](VlanVirtualCircuitType.md) |  | [optional] 
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


