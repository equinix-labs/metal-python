# VrfVirtualCircuitStatus

The status changes of a VRF virtual circuit are generally the same as Virtual Circuits that aren't in a VRF. However, for VRF Virtual Circuits on Fabric VCs, the status will change to 'waiting_on_peering_details' once the Fabric service token associated with the virtual circuit has been redeemed on Fabric, and Metal has found the associated Fabric connection. At this point, users can update the subnet, MD5 password, customer IP and/or metal IP accordingly. For VRF Virtual Circuits on Dedicated Ports, we require all peering details to be set on creation of a VRF Virtual Circuit. The status will change to `changing_peering_details` whenever an active VRF Virtual Circuit has any of its peering details updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


