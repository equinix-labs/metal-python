# BgpConfigRequestInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** |  | 
**deployment_type** | **str** |  | 
**href** | **str** |  | [optional] 
**md5** | **str** |  | [optional] 
**use_case** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.bgp_config_request_input import BgpConfigRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of BgpConfigRequestInput from a JSON string
bgp_config_request_input_instance = BgpConfigRequestInput.from_json(json)
# print the JSON string representation of the object
print BgpConfigRequestInput.to_json()

# convert the object into a dict
bgp_config_request_input_dict = bgp_config_request_input_instance.to_dict()
# create an instance of BgpConfigRequestInput from a dict
bgp_config_request_input_form_dict = bgp_config_request_input.from_dict(bgp_config_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


