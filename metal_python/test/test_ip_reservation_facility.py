# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import metal_python
from metal_python.models.ip_reservation_facility import IPReservationFacility  # noqa: E501
from metal_python.rest import ApiException

class TestIPReservationFacility(unittest.TestCase):
    """IPReservationFacility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IPReservationFacility
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPReservationFacility`
        """
        model = metal_python.models.ip_reservation_facility.IPReservationFacility()  # noqa: E501
        if include_optional :
            return IPReservationFacility(
                address = metal_python.models.address.Address(
                    address = '', 
                    address2 = '', 
                    city = '', 
                    coordinates = metal_python.models.coordinates.Coordinates(
                        latitude = '', 
                        longitude = '', 
                        href = '', ), 
                    country = '', 
                    state = '', 
                    zip_code = '', 
                    href = '', ), 
                code = '', 
                features = ["baremetal","backend_transfer","global_ipv4"], 
                id = '', 
                ip_ranges = ["2604:1380::/36","147.75.192.0/21"], 
                metro = None, 
                name = '', 
                href = ''
            )
        else :
            return IPReservationFacility(
        )
        """

    def testIPReservationFacility(self):
        """Test IPReservationFacility"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
