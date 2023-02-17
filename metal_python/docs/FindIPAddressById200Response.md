# FindIPAddressById200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**address_family** | **int** |  | [optional] 
**assigned_to** | [**Href**](Href.md) |  | [optional] 
**cidr** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**gateway** | **str** |  | [optional] 
**global_ip** | **bool** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**manageable** | **bool** |  | [optional] 
**management** | **bool** |  | [optional] 
**metro** | [**Metro**](Metro.md) |  | [optional] 
**netmask** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**parent_block** | [**ParentBlock**](ParentBlock.md) |  | [optional] 
**public** | **bool** |  | [optional] 
**addon** | **bool** |  | [optional] 
**assignments** | [**List[IPAssignment]**](IPAssignment.md) |  | [optional] 
**available** | **str** |  | [optional] 
**bill** | **bool** |  | [optional] 
**customdata** | **object** |  | [optional] 
**details** | **str** |  | [optional] 
**facility** | [**IPReservationFacility**](IPReservationFacility.md) |  | [optional] 
**metal_gateway** | [**MetalGatewayLite**](MetalGatewayLite.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**project_lite** | [**Project**](Project.md) |  | [optional] 
**requested_by** | [**Href**](Href.md) |  | [optional] 
**state** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**created_by** | [**Href**](Href.md) |  | [optional] 
**vrf** | [**Vrf**](Vrf.md) |  | 

## Example

```python
from metal_python.models.find_ip_address_by_id200_response import FindIPAddressById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FindIPAddressById200Response from a JSON string
find_ip_address_by_id200_response_instance = FindIPAddressById200Response.from_json(json)
# print the JSON string representation of the object
print FindIPAddressById200Response.to_json()

# convert the object into a dict
find_ip_address_by_id200_response_dict = find_ip_address_by_id200_response_instance.to_dict()
# create an instance of FindIPAddressById200Response from a dict
find_ip_address_by_id200_response_form_dict = find_ip_address_by_id200_response.from_dict(find_ip_address_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


