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
from equinix_metal.models.ip_reservation import IPReservation  # noqa: E501
from equinix_metal.rest import ApiException

class TestIPReservation(unittest.TestCase):
    """IPReservation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IPReservation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPReservation`
        """
        model = equinix_metal.models.ip_reservation.IPReservation()  # noqa: E501
        if include_optional :
            return IPReservation(
                addon = True, 
                address = '', 
                address_family = 56, 
                assignments = [
                    equinix_metal.models.href.Href(
                        href = '', )
                    ], 
                available = '', 
                bill = True, 
                cidr = 56, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                customdata = equinix_metal.models.customdata.customdata(), 
                details = '', 
                enabled = True, 
                facility = None, 
                gateway = '', 
                global_ip = True, 
                href = '', 
                id = '', 
                manageable = True, 
                management = True, 
                metal_gateway = equinix_metal.models.metal_gateway_lite.MetalGatewayLite(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    gateway_address = '10.1.2.1/27', 
                    href = '', 
                    id = '', 
                    state = 'ready', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    vlan = 1001, ), 
                metro = None, 
                netmask = '', 
                network = '', 
                project = equinix_metal.models.project.Project(
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
                        
                        ], ), 
                project_lite = equinix_metal.models.href.Href(
                    href = '', ), 
                public = True, 
                requested_by = equinix_metal.models.href.Href(
                    href = '', ), 
                state = '', 
                tags = [
                    ''
                    ], 
                type = 'global_ipv4'
            )
        else :
            return IPReservation(
                type = 'global_ipv4',
        )
        """

    def testIPReservation(self):
        """Test IPReservation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
