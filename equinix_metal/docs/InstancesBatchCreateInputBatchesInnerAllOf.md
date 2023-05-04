# InstancesBatchCreateInputBatchesInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostnames** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 
**quantity** | **int** | The number of devices to create in this batch. The hostname may contain an &#x60;{{index}}&#x60; placeholder, which will be replaced with the index of the device in the batch. For example, if the hostname is &#x60;device-{{index}}&#x60;, the first device in the batch will have the hostname &#x60;device-01&#x60;, the second device will have the hostname &#x60;device-02&#x60;, and so on. | [optional] 

## Example

```python
from equinix_metal.models.instances_batch_create_input_batches_inner_all_of import InstancesBatchCreateInputBatchesInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesBatchCreateInputBatchesInnerAllOf from a JSON string
instances_batch_create_input_batches_inner_all_of_instance = InstancesBatchCreateInputBatchesInnerAllOf.from_json(json)
# print the JSON string representation of the object
print InstancesBatchCreateInputBatchesInnerAllOf.to_json()

# convert the object into a dict
instances_batch_create_input_batches_inner_all_of_dict = instances_batch_create_input_batches_inner_all_of_instance.to_dict()
# create an instance of InstancesBatchCreateInputBatchesInnerAllOf from a dict
instances_batch_create_input_batches_inner_all_of_form_dict = instances_batch_create_input_batches_inner_all_of.from_dict(instances_batch_create_input_batches_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


