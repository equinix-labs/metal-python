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
from metal_python.models.device import Device  # noqa: E501
from metal_python.rest import ApiException

class TestDevice(unittest.TestCase):
    """Device unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Device
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Device`
        """
        model = metal_python.models.device.Device()  # noqa: E501
        if include_optional :
            return Device(
                always_pxe = True, 
                billing_cycle = '', 
                bonding_mode = 56, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = None, 
                customdata = { }, 
                description = '', 
                facility = metal_python.models.facility.Facility(
                    address = metal_python.models.address.Address(
                        address = '', 
                        address2 = '', 
                        city = '', 
                        coordinates = metal_python.models.coordinates.Coordinates(
                            latitude = '', 
                            longitude = '', 
                            href = '', ), 
                        country = '', 
                        state = '', 
                        zip_code = '', 
                        href = '', ), 
                    code = '', 
                    features = ["baremetal","backend_transfer","global_ipv4"], 
                    id = '', 
                    ip_ranges = ["2604:1380::/36","147.75.192.0/21"], 
                    metro = null, 
                    name = '', 
                    href = '', ), 
                hardware_reservation = metal_python.models.href.Href(
                    href = '', ), 
                hostname = '', 
                href = '', 
                id = '', 
                image_url = '', 
                ip_addresses = [
                    metal_python.models.ip_assignment.IPAssignment(
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
                        metro = null, 
                        netmask = '', 
                        network = '', 
                        parent_block = metal_python.models.parent_block.ParentBlock(
                            cidr = 56, 
                            href = '', 
                            netmask = '', 
                            network = '', ), 
                        public = True, )
                    ], 
                ipxe_script_url = '', 
                iqn = '', 
                locked = True, 
                metro = None, 
                network_ports = [
                    metal_python.models.port.Port(
                        bond = metal_python.models.bond_port_data.BondPortData(
                            id = '', 
                            name = '', 
                            href = '', ), 
                        data = metal_python.models.port_data.PortData(
                            mac = '', 
                            bonded = True, 
                            href = '', ), 
                        disbond_operation_supported = True, 
                        href = '', 
                        id = '', 
                        name = 'bond0', 
                        type = 'NetworkPort', 
                        network_type = 'layer2-bonded', 
                        native_virtual_network = metal_python.models.virtual_network.VirtualNetwork(
                            assigned_to = metal_python.models.href.Href(
                                href = '', ), 
                            assigned_to_virtual_circuit = True, 
                            description = '', 
                            facility = metal_python.models.href.Href(
                                href = '', ), 
                            href = '', 
                            id = '', 
                            instances = [
                                
                                ], 
                            metal_gateways = [
                                metal_python.models.metal_gateway_lite.MetalGatewayLite(
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    gateway_address = '10.1.2.1/27', 
                                    href = '', 
                                    id = '', 
                                    state = 'ready', 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    vlan = 1001, )
                                ], 
                            metro = , 
                            metro_code = '', 
                            vxlan = 56, ), 
                        virtual_networks = [
                            
                            ], )
                    ], 
                operating_system = metal_python.models.operating_system.OperatingSystem(
                    distro = '', 
                    distro_label = '', 
                    id = '', 
                    licensed = True, 
                    name = '', 
                    preinstallable = True, 
                    pricing = metal_python.models.pricing.pricing(), 
                    provisionable_on = [
                        ''
                        ], 
                    slug = '', 
                    version = '', 
                    href = '', ), 
                actions = [
                    metal_python.models.device_actions_inner.Device_actions_inner(
                        type = '', 
                        name = '', 
                        href = '', )
                    ], 
                plan = metal_python.models.plan.Plan(
                    available_in = [
                        metal_python.models.plan_available_in_inner.Plan_available_in_inner(
                            href = '', 
                            price = metal_python.models.plan_available_in_inner_price.Plan_available_in_inner_price(
                                hour = 1.23, 
                                href = '', ), )
                        ], 
                    available_in_metros = [
                        metal_python.models.plan_available_in_metros_inner.Plan_available_in_metros_inner(
                            href = '', )
                        ], 
                    class = 'm3.large.x86', 
                    description = '', 
                    deployment_types = [
                        'on_demand'
                        ], 
                    id = '', 
                    legacy = True, 
                    line = 'baremetal', 
                    name = '', 
                    pricing = metal_python.models.pricing.pricing(), 
                    slug = 'm3.large.x86', 
                    specs = metal_python.models.plan_specs.Plan_specs(
                        cpus = [
                            metal_python.models.plan_specs_cpus_inner.Plan_specs_cpus_inner(
                                count = 56, 
                                type = '', 
                                href = '', )
                            ], 
                        drives = [
                            metal_python.models.plan_specs_drives_inner.Plan_specs_drives_inner(
                                count = 56, 
                                type = 'HDD', 
                                size = '3.84TB', 
                                category = 'boot', 
                                href = '', )
                            ], 
                        nics = [
                            metal_python.models.plan_specs_nics_inner.Plan_specs_nics_inner(
                                count = 2, 
                                type = '1Gbps', 
                                href = '', )
                            ], 
                        features = metal_python.models.plan_specs_features.Plan_specs_features(
                            raid = True, 
                            txt = True, 
                            uefi = True, 
                            href = '', ), 
                        href = '', ), 
                    type = 'standard', 
                    href = '', ), 
                project = None, 
                project_lite = None, 
                provisioning_events = [
                    metal_python.models.event.Event(
                        body = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        href = '', 
                        id = '', 
                        interpolated = '', 
                        relationships = [
                            metal_python.models.href.Href(
                                href = '', )
                            ], 
                        state = '', 
                        type = '', 
                        modified_by = metal_python.models.modified_by.modified_by(), 
                        ip = '', )
                    ], 
                provisioning_percentage = 1.337, 
                root_password = '', 
                short_id = '', 
                spot_instance = True, 
                spot_price_max = 1.337, 
                ssh_keys = [
                    metal_python.models.href.Href(
                        href = '', )
                    ], 
                state = 'active', 
                switch_uuid = '', 
                tags = [
                    ''
                    ], 
                termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = '', 
                userdata = '', 
                volumes = [
                    metal_python.models.href.Href(
                        href = '', )
                    ]
            )
        else :
            return Device(
        )
        """

    def testDevice(self):
        """Test Device"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
