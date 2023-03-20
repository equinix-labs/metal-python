# ProjectCreateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customdata** | **object** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | 
**payment_method_id** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.project_create_input import ProjectCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateInput from a JSON string
project_create_input_instance = ProjectCreateInput.from_json(json)
# print the JSON string representation of the object
print ProjectCreateInput.to_json()

# convert the object into a dict
project_create_input_dict = project_create_input_instance.to_dict()
# create an instance of ProjectCreateInput from a dict
project_create_input_form_dict = project_create_input.from_dict(project_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


