# MetroCapacityList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**MetroCapacityReport**](MetroCapacityReport.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.metro_capacity_list import MetroCapacityList

# TODO update the JSON string below
json = "{}"
# create an instance of MetroCapacityList from a JSON string
metro_capacity_list_instance = MetroCapacityList.from_json(json)
# print the JSON string representation of the object
print MetroCapacityList.to_json()

# convert the object into a dict
metro_capacity_list_dict = metro_capacity_list_instance.to_dict()
# create an instance of MetroCapacityList from a dict
metro_capacity_list_form_dict = metro_capacity_list.from_dict(metro_capacity_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


