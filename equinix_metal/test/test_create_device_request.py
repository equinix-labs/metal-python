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
from equinix_metal.models.create_device_request import CreateDeviceRequest  # noqa: E501
from equinix_metal.rest import ApiException

class TestCreateDeviceRequest(unittest.TestCase):
    """CreateDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateDeviceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateDeviceRequest`
        """
        model = equinix_metal.models.create_device_request.CreateDeviceRequest()  # noqa: E501
        if include_optional :
            return CreateDeviceRequest(
                href = '', 
                metro = 'sv', 
                always_pxe = True, 
                billing_cycle = 'hourly', 
                customdata = { }, 
                description = '', 
                features = [
                    ''
                    ], 
                hardware_reservation_id = 'next-available', 
                hostname = '', 
                ip_addresses = [
                    equinix_metal.models.device_create_input_ip_addresses_inner.DeviceCreateInput_ip_addresses_inner(
                        address_family = 4, 
                        cidr = 28, 
                        href = '', 
                        ip_reservations = [
                            ''
                            ], 
                        public = False, )
                    ], 
                ipxe_script_url = '', 
                locked = True, 
                no_ssh_keys = True, 
                operating_system = '', 
                plan = 'c3.large.x86', 
                private_ipv4_subnet_size = 56, 
                project_ssh_keys = [
                    ''
                    ], 
                public_ipv4_subnet_size = 56, 
                spot_instance = True, 
                spot_price_max = 1.23, 
                ssh_keys = [
                    equinix_metal.models.ssh_key_input.SSHKeyInput(
                        href = '', 
                        key = '', 
                        label = '', )
                    ], 
                tags = [
                    ''
                    ], 
                termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user_ssh_keys = [
                    ''
                    ], 
                userdata = '', 
                facility = None
            )
        else :
            return CreateDeviceRequest(
                metro = 'sv',
                operating_system = '',
                plan = 'c3.large.x86',
                facility = None,
        )
        """

    def testCreateDeviceRequest(self):
        """Test CreateDeviceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
