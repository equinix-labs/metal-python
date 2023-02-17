# MetroInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metro** | **str** | Metro code or ID of where the instance should be provisioned in. Either metro or facility must be provided. | 
**href** | **str** |  | [optional] 

## Example

```python
from metal_python.models.metro_input import MetroInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetroInput from a JSON string
metro_input_instance = MetroInput.from_json(json)
# print the JSON string representation of the object
print MetroInput.to_json()

# convert the object into a dict
metro_input_dict = metro_input_instance.to_dict()
# create an instance of MetroInput from a dict
metro_input_form_dict = metro_input.from_dict(metro_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


