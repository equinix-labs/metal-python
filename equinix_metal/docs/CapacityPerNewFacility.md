# CapacityPerNewFacility


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baremetal_1e** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_per_new_facility import CapacityPerNewFacility

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityPerNewFacility from a JSON string
capacity_per_new_facility_instance = CapacityPerNewFacility.from_json(json)
# print the JSON string representation of the object
print CapacityPerNewFacility.to_json()

# convert the object into a dict
capacity_per_new_facility_dict = capacity_per_new_facility_instance.to_dict()
# create an instance of CapacityPerNewFacility from a dict
capacity_per_new_facility_form_dict = capacity_per_new_facility.from_dict(capacity_per_new_facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


