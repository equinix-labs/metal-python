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
from equinix_metal.models.user_lite import UserLite  # noqa: E501
from equinix_metal.rest import ApiException

class TestUserLite(unittest.TestCase):
    """UserLite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserLite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserLite`
        """
        model = equinix_metal.models.user_lite.UserLite()  # noqa: E501
        if include_optional :
            return UserLite(
                avatar_thumb_url = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                email = '', 
                first_name = '', 
                full_name = '', 
                href = '', 
                id = '', 
                last_name = '', 
                short_id = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return UserLite(
                id = '',
                short_id = '',
        )
        """

    def testUserLite(self):
        """Test UserLite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
