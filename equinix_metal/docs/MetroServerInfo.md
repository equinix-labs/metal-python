# MetroServerInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**metro** | **str** | The metro ID or code to check the capacity in. | [optional] 
**plan** | **str** | The plan ID or slug to check the capacity of. | [optional] 
**quantity** | **str** | The number of servers to check the capacity of. | [optional] 

## Example

```python
from equinix_metal.models.metro_server_info import MetroServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MetroServerInfo from a JSON string
metro_server_info_instance = MetroServerInfo.from_json(json)
# print the JSON string representation of the object
print MetroServerInfo.to_json()

# convert the object into a dict
metro_server_info_dict = metro_server_info_instance.to_dict()
# create an instance of MetroServerInfo from a dict
metro_server_info_form_dict = metro_server_info.from_dict(metro_server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


