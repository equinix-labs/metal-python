# InterconnectionMetro

The location of where the shared or Dedicated Port is located. For interconnections with Dedicated Ports,   this will be the location of the Dedicated Ports. For Fabric VCs (Metal Billed), this is where interconnection will be originating from, as we pre-authorize the use of one of our shared ports   as the origin of the interconnection using A-Side service tokens. We only allow local connections for Fabric VCs (Metal Billed), so the destination location must be the same as the origin. For Fabric VCs (Fabric Billed),    this will be the destination of the interconnection. We allow remote connections for Fabric VCs (Fabric Billed), so the origin of the interconnection can be a different metro set here.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.interconnection_metro import InterconnectionMetro

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionMetro from a JSON string
interconnection_metro_instance = InterconnectionMetro.from_json(json)
# print the JSON string representation of the object
print InterconnectionMetro.to_json()

# convert the object into a dict
interconnection_metro_dict = interconnection_metro_instance.to_dict()
# create an instance of InterconnectionMetro from a dict
interconnection_metro_form_dict = interconnection_metro.from_dict(interconnection_metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


