# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import absolute_import

import unittest

import equinix_metal
from equinix_metal.api.vrfs_api import VRFsApi  # noqa: E501
from equinix_metal.rest import ApiException


class TestVRFsApi(unittest.TestCase):
    """VRFsApi unit test stubs"""

    def setUp(self):
        self.api = equinix_metal.api.vrfs_api.VRFsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_vrf_ip_reservation(self):
        """Test case for find_vrf_ip_reservation

        Retrieve all VRF IP Reservations in the VRF  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
