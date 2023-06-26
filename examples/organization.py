#!/usr/bin/env python3

# Example of hardware_reservation resource fetch

import os
import time

import equinix_metal


def get_equinix_metal_client(api_token):
    conf = equinix_metal.Configuration(
        host="https://api.equinix.com/metal/v1"
    )
    conf.api_key['x_auth_token'] = api_token
    conf.debug=  True
    return equinix_metal.ApiClient(conf)


client = get_equinix_metal_client(os.environ["METAL_AUTH_TOKEN"])


org_api = equinix_metal.OrganizationsApi(client)
resp = org_api.find_organizations()

print(resp)

