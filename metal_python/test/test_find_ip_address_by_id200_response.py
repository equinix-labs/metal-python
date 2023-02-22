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
from metal_python.models.find_ip_address_by_id200_response import FindIPAddressById200Response  # noqa: E501
from metal_python.rest import ApiException

class TestFindIPAddressById200Response(unittest.TestCase):
    """FindIPAddressById200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FindIPAddressById200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindIPAddressById200Response`
        """
        model = metal_python.models.find_ip_address_by_id200_response.FindIPAddressById200Response()  # noqa: E501
        if include_optional :
            return FindIPAddressById200Response(
                address = '', 
                address_family = 56, 
                assigned_to = metal_python.models.href.Href(
                    href = '', ), 
                cidr = 56, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                enabled = True, 
                gateway = '', 
                global_ip = True, 
                href = '', 
                id = '', 
                manageable = True, 
                management = True, 
                metro = metal_python.models.metro.Metro(
                    code = '', 
                    country = '', 
                    id = '', 
                    name = '', 
                    href = '', ), 
                netmask = '', 
                network = '', 
                parent_block = metal_python.models.parent_block.ParentBlock(
                    cidr = 56, 
                    href = '', 
                    netmask = '', 
                    network = '', ), 
                public = True, 
                addon = True, 
                assignments = [
                    metal_python.models.href.Href(
                        href = '', )
                    ], 
                available = '', 
                bill = True, 
                customdata = metal_python.models.customdata.customdata(), 
                details = '', 
                facility = None, 
                metal_gateway = metal_python.models.metal_gateway_lite.MetalGatewayLite(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    gateway_address = '10.1.2.1/27', 
                    href = '', 
                    id = '', 
                    state = 'ready', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    vlan = 1001, ), 
                project = metal_python.models.project.Project(
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
                    backend_transfer_enabled = True, ), 
                project_lite = metal_python.models.project.Project(
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
                    backend_transfer_enabled = True, ), 
                requested_by = metal_python.models.href.Href(
                    href = '', ), 
                state = '', 
                tags = [
                    ''
                    ], 
                type = 'vrf', 
                created_by = metal_python.models.href.Href(
                    href = '', ), 
                vrf = metal_python.models.vrf.Vrf(
                    id = '', 
                    name = '', 
                    description = '', 
                    local_asn = 56, 
                    ip_ranges = [
                        ''
                        ], 
                    project = metal_python.models.project.Project(
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
                        backend_transfer_enabled = True, ), 
                    metro = metal_python.models.metro.Metro(
                        code = '', 
                        country = '', 
                        id = '', 
                        name = '', 
                        href = '', ), 
                    created_by = metal_python.models.user.User(
                        avatar_thumb_url = '', 
                        avatar_url = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        customdata = metal_python.models.customdata.customdata(), 
                        email = '', 
                        emails = [
                            
                            ], 
                        first_name = '', 
                        fraud_score = '', 
                        full_name = '', 
                        href = '', 
                        id = '', 
                        last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_name = '', 
                        max_organizations = 56, 
                        max_projects = 56, 
                        phone_number = '', 
                        short_id = '', 
                        timezone = '', 
                        two_factor_auth = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    href = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else :
            return FindIPAddressById200Response(
                assigned_to = metal_python.models.href.Href(
                    href = '', ),
                type = 'vrf',
                vrf = metal_python.models.vrf.Vrf(
                    id = '', 
                    name = '', 
                    description = '', 
                    local_asn = 56, 
                    ip_ranges = [
                        ''
                        ], 
                    project = metal_python.models.project.Project(
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
                        backend_transfer_enabled = True, ), 
                    metro = metal_python.models.metro.Metro(
                        code = '', 
                        country = '', 
                        id = '', 
                        name = '', 
                        href = '', ), 
                    created_by = metal_python.models.user.User(
                        avatar_thumb_url = '', 
                        avatar_url = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        customdata = metal_python.models.customdata.customdata(), 
                        email = '', 
                        emails = [
                            
                            ], 
                        first_name = '', 
                        fraud_score = '', 
                        full_name = '', 
                        href = '', 
                        id = '', 
                        last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_name = '', 
                        max_organizations = 56, 
                        max_projects = 56, 
                        phone_number = '', 
                        short_id = '', 
                        timezone = '', 
                        two_factor_auth = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    href = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testFindIPAddressById200Response(self):
        """Test FindIPAddressById200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
