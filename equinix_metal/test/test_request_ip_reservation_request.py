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
from equinix_metal.models.request_ip_reservation_request import RequestIPReservationRequest  # noqa: E501
from equinix_metal.rest import ApiException

class TestRequestIPReservationRequest(unittest.TestCase):
    """RequestIPReservationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RequestIPReservationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestIPReservationRequest`
        """
        model = equinix_metal.models.request_ip_reservation_request.RequestIPReservationRequest()  # noqa: E501
        if include_optional :
            return RequestIPReservationRequest(
                comments = '', 
                customdata = equinix_metal.models.customdata.customdata(), 
                details = '', 
                facility = '', 
                fail_on_approval_required = True, 
                href = '', 
                metro = 'SV', 
                quantity = 56, 
                tags = [
                    ''
                    ], 
                type = 'vrf', 
                cidr = 16, 
                network = '10.1.2.0', 
                vrf_id = ''
            )
        else :
            return RequestIPReservationRequest(
                quantity = 56,
                type = 'vrf',
                cidr = 16,
                network = '10.1.2.0',
                vrf_id = '',
        )
        """

    def testRequestIPReservationRequest(self):
        """Test RequestIPReservationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
