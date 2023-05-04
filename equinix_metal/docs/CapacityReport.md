# CapacityReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ams1** | [**CapacityPerFacility**](CapacityPerFacility.md) |  | [optional] 
**atl1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 
**dfw1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 
**ewr1** | [**CapacityPerFacility**](CapacityPerFacility.md) |  | [optional] 
**fra1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 
**href** | **str** |  | [optional] 
**iad1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 
**lax1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 
**nrt1** | [**CapacityPerFacility**](CapacityPerFacility.md) |  | [optional] 
**ord1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 
**sea1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 
**sin1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 
**sjc1** | [**CapacityPerFacility**](CapacityPerFacility.md) |  | [optional] 
**syd1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 
**yyz1** | [**CapacityPerNewFacility**](CapacityPerNewFacility.md) |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_report import CapacityReport

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityReport from a JSON string
capacity_report_instance = CapacityReport.from_json(json)
# print the JSON string representation of the object
print CapacityReport.to_json()

# convert the object into a dict
capacity_report_dict = capacity_report_instance.to_dict()
# create an instance of CapacityReport from a dict
capacity_report_form_dict = capacity_report.from_dict(capacity_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


