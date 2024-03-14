# Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** |  | [optional] 
**customdata** | **Dict[str, object]** |  | [optional] 
**facility** | **str** | The facility code of the instance | [optional] 
**hostname** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**iqn** | **str** |  | [optional] 
**metro** | **str** | The metro code of the instance | [optional] 
**network** | [**MetadataNetwork**](MetadataNetwork.md) |  | [optional] 
**operating_system** | **object** |  | [optional] 
**plan** | **str** | The plan slug of the instance | [optional] 
**private_subnets** | **List[str]** | An array of the private subnets | [optional] 
**reserved** | **bool** |  | [optional] 
**specs** | **object** | The specs of the plan version of the instance | [optional] 
**ssh_keys** | **List[str]** |  | [optional] 
**state** | [**DeviceState**](DeviceState.md) |  | [optional] 
**switch_short_id** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**volumes** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_form_dict = metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


