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
from metal_python.models.coordinates import Coordinates  # noqa: E501
from metal_python.rest import ApiException

class TestCoordinates(unittest.TestCase):
    """Coordinates unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Coordinates
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Coordinates`
        """
        model = metal_python.models.coordinates.Coordinates()  # noqa: E501
        if include_optional :
            return Coordinates(
                latitude = '', 
                longitude = '', 
                href = ''
            )
        else :
            return Coordinates(
        )
        """

    def testCoordinates(self):
        """Test Coordinates"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
