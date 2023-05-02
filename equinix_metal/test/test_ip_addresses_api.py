# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import equinix_metal
from equinix_metal.api.ip_addresses_api import IPAddressesApi  # noqa: E501
from equinix_metal.rest import ApiException


class TestIPAddressesApi(unittest.TestCase):
    """IPAddressesApi unit test stubs"""

    def setUp(self):
        self.api = equinix_metal.api.ip_addresses_api.IPAddressesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_ip_address(self):
        """Test case for delete_ip_address

        Unassign an ip address  # noqa: E501
        """
        pass

    def test_find_ip_address_by_id(self):
        """Test case for find_ip_address_by_id

        Retrieve an ip address  # noqa: E501
        """
        pass

    def test_find_ip_address_customdata(self):
        """Test case for find_ip_address_customdata

        Retrieve the custom metadata of an IP Reservation or IP Assignment  # noqa: E501
        """
        pass

    def test_find_ip_availabilities(self):
        """Test case for find_ip_availabilities

        Retrieve all available subnets of a particular reservation  # noqa: E501
        """
        pass

    def test_find_ip_reservations(self):
        """Test case for find_ip_reservations

        Retrieve all ip reservations  # noqa: E501
        """
        pass

    def test_request_ip_reservation(self):
        """Test case for request_ip_reservation

        Requesting IP reservations  # noqa: E501
        """
        pass

    def test_update_ip_address(self):
        """Test case for update_ip_address

        Update an ip address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
