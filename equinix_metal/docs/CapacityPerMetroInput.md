# CapacityPerMetroInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**servers** | [**List[MetroServerInfo]**](MetroServerInfo.md) |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_per_metro_input import CapacityPerMetroInput

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityPerMetroInput from a JSON string
capacity_per_metro_input_instance = CapacityPerMetroInput.from_json(json)
# print the JSON string representation of the object
print CapacityPerMetroInput.to_json()

# convert the object into a dict
capacity_per_metro_input_dict = capacity_per_metro_input_instance.to_dict()
# create an instance of CapacityPerMetroInput from a dict
capacity_per_metro_input_form_dict = capacity_per_metro_input.from_dict(capacity_per_metro_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


