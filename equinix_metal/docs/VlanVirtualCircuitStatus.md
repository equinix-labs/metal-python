# VlanVirtualCircuitStatus

The status of a Virtual Circuit is always 'pending' on creation. The status can turn to 'Waiting on Customer VLAN' if a Metro VLAN was not set yet on the Virtual Circuit and is the last step needed for full activation. For Dedicated interconnections, as long as the Dedicated Port has been associated to the Virtual Circuit and a NNI VNID has been set, it will turn to 'waiting_on_customer_vlan'. For Fabric VCs, it will only change to 'waiting_on_customer_vlan' once the corresponding Fabric connection has been found on the Fabric side. If the Fabric service token associated with the Virtual Circuit hasn't been redeemed on Fabric within the expiry time, it will change to an `expired` status. Once a Metro VLAN is set on the Virtual Circuit (which for Fabric VCs, can be set on creation of a Fabric VC) and the necessary set up is done, it will turn into 'Activating' status as it tries to activate the Virtual Circuit. Once the Virtual Circuit fully activates and is configured on the switch, it will turn to staus 'active'. For Fabric VCs (Metal Billed), we will start billing the moment the status of the Virtual Circuit turns to 'active'. If there are any changes to the VLAN after the Virtual Circuit is in an 'active' status, the status will show 'changing_vlan' if a new VLAN has been provided, or 'deactivating' if we are removing the VLAN. When a deletion request is issued for the Virtual Circuit, it will move to a 'deleting' status, and we will immediately unconfigure the switch for the Virtual Circuit and issue a deletion on any associated Fabric connections. Any associated Metro VLANs on the virtual circuit will also be unassociated after the switch has been successfully unconfigured. If there are any associated Fabric connections, we will only fully delete the Virtual Circuit once we have checked that the Fabric connection was fully deprovisioned on Fabric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


