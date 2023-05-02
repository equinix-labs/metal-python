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
from equinix_metal.models.ssh_key import SSHKey  # noqa: E501
from equinix_metal.rest import ApiException

class TestSSHKey(unittest.TestCase):
    """SSHKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SSHKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SSHKey`
        """
        model = equinix_metal.models.ssh_key.SSHKey()  # noqa: E501
        if include_optional :
            return SSHKey(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                entity = equinix_metal.models.href.Href(
                    href = '', ), 
                fingerprint = '', 
                href = '', 
                id = '', 
                key = '', 
                label = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return SSHKey(
        )
        """

    def testSSHKey(self):
        """Test SSHKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
