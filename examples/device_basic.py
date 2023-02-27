#!/usr/bin/env python3

import os
import time

import equinix_metal


def get_equinix_metal_client(api_token):
    conf = equinix_metal.Configuration(
        host="https://api.equinix.com/metal/v1"
    )
    print(api_token)
    conf.api_key['x_auth_token'] = api_token
    return equinix_metal.ApiClient(conf)


def wait_for_device_active(client, did):
    wait_timeout = time.time() + time.time() + 60 * 5
    while wait_timeout > time.time():
        device = equinix_metal.DevicesApi(client).find_device_by_id(did)
        if device.state == 'active':
            return device
        print(
            f"Waiting for device {did} to become active, device state is {device.state}")
        time.sleep(5)
    raise Exception("Timed out waiting for device to become active")


client = get_equinix_metal_client(os.environ["METAL_AUTH_TOKEN"])
project_id = os.environ["METAL_PROJECT_ID"]

# Since there are 2 models for CreateDeviceRequest, we need to create the
# appropriate one and then pass it to the CreateDeviceRequest constructor.
# The second model is DeviceCreateInFacilityInput.

cdm = equinix_metal.DeviceCreateInMetroInput(
    operating_system="ubuntu_18_04",
    plan="c3.small.x86",
    hostname="test",
    metro="sv",
    billing_cycle="hourly",
    tags=["test"]
)

cdr = equinix_metal.CreateDeviceRequest(actual_instance=cdm)
print("About to create device in project: " + project_id)
devices_api = equinix_metal.DevicesApi(client)
new_device_resp = devices_api.create_device(project_id, cdr)

print("New Device:")
print(new_device_resp)

active_device_resp = wait_for_device_active(client, new_device_resp.id)

print("Device is active:")
print(active_device_resp)

print("About to delete device")
device_del_resp = equinix_metal.DevicesApi(
    client).delete_device(new_device_resp.id)
print("Deleted device")
