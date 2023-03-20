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
import datetime

import equinix_metal
from equinix_metal.models.vrf_ip_reservation_create_input import VrfIpReservationCreateInput  # noqa: E501
from equinix_metal.rest import ApiException

class TestVrfIpReservationCreateInput(unittest.TestCase):
    """VrfIpReservationCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VrfIpReservationCreateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VrfIpReservationCreateInput`
        """
        model = equinix_metal.models.vrf_ip_reservation_create_input.VrfIpReservationCreateInput()  # noqa: E501
        if include_optional :
            return VrfIpReservationCreateInput(
                cidr = 16, 
                customdata = equinix_metal.models.customdata.customdata(), 
                details = '', 
                href = '', 
                network = '10.1.2.0', 
                tags = [
                    ''
                    ], 
                type = 'vrf', 
                vrf_id = ''
            )
        else :
            return VrfIpReservationCreateInput(
                cidr = 16,
                network = '10.1.2.0',
                type = 'vrf',
                vrf_id = '',
        )
        """

    def testVrfIpReservationCreateInput(self):
        """Test VrfIpReservationCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
