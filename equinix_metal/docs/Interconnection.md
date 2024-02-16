# Interconnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_code** | **str** | For Fabric VCs (Metal Billed), this allows Fabric to connect the Metal network to any connection Fabric facilitates. Fabric uses this token to be able to give more detailed information about the Metal end of the network, when viewing resources from within Fabric. | [optional] 
**contact_email** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**facility** | [**Href**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metro** | [**Metro**](Metro.md) |  | [optional] 
**mode** | **str** | The mode of the interconnection (only relevant to Dedicated Ports). Shared connections won&#39;t have this field. Can be either &#39;standard&#39; or &#39;tunnel&#39;.   The default mode of an interconnection on a Dedicated Port is &#39;standard&#39;. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances. | [optional] 
**name** | **str** |  | [optional] 
**organization** | [**Href**](Href.md) |  | [optional] 
**ports** | [**List[InterconnectionPort]**](InterconnectionPort.md) | For Fabric VCs, these represent Virtual Port(s) created for the interconnection. For dedicated interconnections, these represent the Dedicated Port(s). | [optional] 
**redundancy** | **str** | Either &#39;primary&#39;, meaning a single interconnection, or &#39;redundant&#39;, meaning a redundant interconnection. | [optional] 
**requested_by** | [**Href**](Href.md) |  | [optional] 
**service_tokens** | [**List[FabricServiceToken]**](FabricServiceToken.md) | For Fabric VCs (Metal Billed), this will show details of the A-Side service tokens issued for the interconnection. For Fabric VCs (Fabric Billed), this will show the details of the Z-Side service tokens issued for the interconnection. Dedicated interconnections will not have any service tokens issued. There will be one per interconnection, so for redundant interconnections, there should be two service tokens issued. | [optional] 
**speed** | **int** | For interconnections on Dedicated Ports and shared connections, this represents the interconnection&#39;s speed in bps. For Fabric VCs, this field refers to the maximum speed of the interconnection in bps. This value will default to 10Gbps for Fabric VCs (Fabric Billed). | [optional] 
**status** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**token** | **str** | This token is used for shared interconnections to be used as the Fabric Token. This field is entirely deprecated. | [optional] 
**type** | **str** | The &#39;shared&#39; type of interconnection refers to shared connections, or later also known as Fabric Virtual Connections (or Fabric VCs). The &#39;dedicated&#39; type of interconnection refers to interconnections created with Dedicated Ports. | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from equinix_metal.models.interconnection import Interconnection

# TODO update the JSON string below
json = "{}"
# create an instance of Interconnection from a JSON string
interconnection_instance = Interconnection.from_json(json)
# print the JSON string representation of the object
print Interconnection.to_json()

# convert the object into a dict
interconnection_dict = interconnection_instance.to_dict()
# create an instance of Interconnection from a dict
interconnection_form_dict = interconnection.from_dict(interconnection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


