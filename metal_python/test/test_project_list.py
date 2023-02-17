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
from metal_python.models.project_list import ProjectList  # noqa: E501
from metal_python.rest import ApiException

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
        model = metal_python.models.project_list.ProjectList()  # noqa: E501
        if include_optional :
            return ProjectList(
                meta = metal_python.models.meta.Meta(
                    first = metal_python.models.href.Href(
                        href = '', ), 
                    last = metal_python.models.href.Href(
                        href = '', ), 
                    next = , 
                    previous = , 
                    self = , 
                    total = 56, 
                    current_page = 56, 
                    last_page = 56, 
                    href = '', ), 
                projects = [
                    metal_python.models.project.Project(
                        bgp_config = metal_python.models.href.Href(
                            href = '', ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        customdata = metal_python.models.customdata.customdata(), 
                        devices = [
                            metal_python.models.href.Href(
                                href = '', )
                            ], 
                        id = '', 
                        invitations = [
                            
                            ], 
                        max_devices = metal_python.models.max_devices.max_devices(), 
                        members = [
                            
                            ], 
                        memberships = [
                            
                            ], 
                        name = '', 
                        network_status = metal_python.models.network_status.network_status(), 
                        payment_method = , 
                        ssh_keys = [
                            
                            ], 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        volumes = [
                            
                            ], 
                        organization = , 
                        href = '', 
                        backend_transfer_enabled = True, )
                    ], 
                href = ''
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
