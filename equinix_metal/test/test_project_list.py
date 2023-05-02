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
from equinix_metal.models.project_list import ProjectList  # noqa: E501
from equinix_metal.rest import ApiException

class TestProjectList(unittest.TestCase):
    """ProjectList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectList`
        """
        model = equinix_metal.models.project_list.ProjectList()  # noqa: E501
        if include_optional :
            return ProjectList(
                href = '', 
                meta = equinix_metal.models.meta.Meta(
                    current_page = 56, 
                    first = equinix_metal.models.href.Href(
                        href = '', ), 
                    href = '', 
                    last = equinix_metal.models.href.Href(
                        href = '', ), 
                    last_page = 56, 
                    next = , 
                    previous = , 
                    self = , 
                    total = 56, ), 
                projects = [
                    equinix_metal.models.project.Project(
                        backend_transfer_enabled = True, 
                        bgp_config = equinix_metal.models.href.Href(
                            href = '', ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        customdata = equinix_metal.models.customdata.customdata(), 
                        devices = [
                            equinix_metal.models.href.Href(
                                href = '', )
                            ], 
                        href = '', 
                        id = '', 
                        invitations = [
                            
                            ], 
                        max_devices = equinix_metal.models.max_devices.max_devices(), 
                        members = [
                            
                            ], 
                        memberships = [
                            
                            ], 
                        name = '', 
                        network_status = equinix_metal.models.network_status.network_status(), 
                        organization = , 
                        payment_method = , 
                        ssh_keys = [
                            
                            ], 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        volumes = [
                            
                            ], )
                    ]
            )
        else :
            return ProjectList(
        )
        """

    def testProjectList(self):
        """Test ProjectList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
