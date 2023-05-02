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
import datetime

import equinix_metal
from equinix_metal.models.device_project import DeviceProject  # noqa: E501
from equinix_metal.rest import ApiException

class TestDeviceProject(unittest.TestCase):
    """DeviceProject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeviceProject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceProject`
        """
        model = equinix_metal.models.device_project.DeviceProject()  # noqa: E501
        if include_optional :
            return DeviceProject(
                href = ''
            )
        else :
            return DeviceProject(
                href = '',
        )
        """

    def testDeviceProject(self):
        """Test DeviceProject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
