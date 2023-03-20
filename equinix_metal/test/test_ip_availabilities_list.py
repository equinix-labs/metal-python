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
from equinix_metal.models.ip_availabilities_list import IPAvailabilitiesList  # noqa: E501
from equinix_metal.rest import ApiException

class TestIPAvailabilitiesList(unittest.TestCase):
    """IPAvailabilitiesList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IPAvailabilitiesList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPAvailabilitiesList`
        """
        model = equinix_metal.models.ip_availabilities_list.IPAvailabilitiesList()  # noqa: E501
        if include_optional :
            return IPAvailabilitiesList(
                available = [
                    ''
                    ], 
                href = ''
            )
        else :
            return IPAvailabilitiesList(
        )
        """

    def testIPAvailabilitiesList(self):
        """Test IPAvailabilitiesList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
