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
from equinix_metal.api.devices_api import DevicesApi  # noqa: E501
from equinix_metal.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = equinix_metal.api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_device(self):
        """Test case for create_device

        Create a device  # noqa: E501
        """
        pass

    def test_create_ip_assignment(self):
        """Test case for create_ip_assignment

        Create an ip assignment  # noqa: E501
        """
        pass

    def test_delete_device(self):
        """Test case for delete_device

        Delete the device  # noqa: E501
        """
        pass

    def test_find_device_by_id(self):
        """Test case for find_device_by_id

        Retrieve a device  # noqa: E501
        """
        pass

    def test_find_ip_assignments(self):
        """Test case for find_ip_assignments

        Retrieve all ip assignments  # noqa: E501
        """
        pass

    def test_find_organization_devices(self):
        """Test case for find_organization_devices

        Retrieve all devices of an organization  # noqa: E501
        """
        pass

    def test_find_project_devices(self):
        """Test case for find_project_devices

        Retrieve all devices of a project  # noqa: E501
        """
        pass

    def test_update_device(self):
        """Test case for update_device

        Update the device  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
