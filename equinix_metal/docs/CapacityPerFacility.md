# CapacityPerFacility


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baremetal_0** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 
**baremetal_1** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 
**baremetal_2** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 
**baremetal_2a** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 
**baremetal_2a2** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 
**baremetal_3** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 
**baremetal_s** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 
**c2_medium_x86** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 
**href** | **str** |  | [optional] 
**m2_xlarge_x86** | [**CapacityLevelPerBaremetal**](CapacityLevelPerBaremetal.md) |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_per_facility import CapacityPerFacility

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityPerFacility from a JSON string
capacity_per_facility_instance = CapacityPerFacility.from_json(json)
# print the JSON string representation of the object
print CapacityPerFacility.to_json()

# convert the object into a dict
capacity_per_facility_dict = capacity_per_facility_instance.to_dict()
# create an instance of CapacityPerFacility from a dict
capacity_per_facility_form_dict = capacity_per_facility.from_dict(capacity_per_facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


