# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. The fields available for search differ by resource, as does the search strategy.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import equinix_metal
from equinix_metal.models.vrf_route_list import VrfRouteList  # noqa: E501
from equinix_metal.rest import ApiException

class TestVrfRouteList(unittest.TestCase):
    """VrfRouteList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VrfRouteList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VrfRouteList`
        """
        model = equinix_metal.models.vrf_route_list.VrfRouteList()  # noqa: E501
        if include_optional :
            return VrfRouteList(
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
                routes = [
                    equinix_metal.models.vrf_route.VrfRoute(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        href = '/routes/e1ff9c2b-051a-4688-965f-153e274f77e0', 
                        id = 'e1ff9c2b-051a-4688-965f-153e274f77e0', 
                        metal_gateway = equinix_metal.models.vrf_metal_gateway.VrfMetalGateway(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_by = equinix_metal.models.href.Href(
                                href = '', ), 
                            href = '', 
                            id = '', 
                            ip_reservation = equinix_metal.models.vrf_ip_reservation.VrfIpReservation(
                                address = '', 
                                address_family = 56, 
                                bill = True, 
                                cidr = 56, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                customdata = equinix_metal.models.customdata.customdata(), 
                                details = '', 
                                gateway = '', 
                                href = '', 
                                id = '', 
                                manageable = True, 
                                management = True, 
                                metro = equinix_metal.models.metro.Metro(
                                    code = '', 
                                    country = '', 
                                    href = '', 
                                    id = '', 
                                    name = '', ), 
                                netmask = '', 
                                network = '', 
                                project = equinix_metal.models.project.Project(
                                    backend_transfer_enabled = True, 
                                    bgp_config = equinix_metal.models.href.Href(
                                        href = '', ), 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    customdata = equinix_metal.models.customdata.customdata(), 
                                    devices = [
                                        
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
                                project_lite = equinix_metal.models.project.Project(
                                    backend_transfer_enabled = True, 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    customdata = equinix_metal.models.customdata.customdata(), 
                                    href = '', 
                                    id = '', 
                                    max_devices = equinix_metal.models.max_devices.max_devices(), 
                                    name = '', 
                                    network_status = equinix_metal.models.network_status.network_status(), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                public = True, 
                                state = '', 
                                tags = [
                                    ''
                                    ], 
                                type = 'vrf', 
                                vrf = equinix_metal.models.vrf.Vrf(
                                    bgp_dynamic_neighbors_bfd_enabled = True, 
                                    bgp_dynamic_neighbors_enabled = True, 
                                    bgp_dynamic_neighbors_export_route_map = True, 
                                    bill = True, 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    description = '', 
                                    href = '', 
                                    id = '', 
                                    ip_ranges = [
                                        ''
                                        ], 
                                    local_asn = 56, 
                                    name = '', 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    virtual_circuits = [
                                        equinix_metal.models.vrf_virtual_circuit.VrfVirtualCircuit(
                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            customer_ip = '12.0.0.2', 
                                            description = '', 
                                            href = '', 
                                            id = '', 
                                            md5 = '', 
                                            metal_ip = '12.0.0.1', 
                                            name = '', 
                                            nni_vlan = 56, 
                                            peer_asn = 56, 
                                            port = , 
                                            speed = 56, 
                                            status = '', 
                                            subnet = '12.0.0.0/30', 
                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                        ], ), ), 
                            project = , 
                            state = 'ready', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            virtual_network = equinix_metal.models.virtual_network.VirtualNetwork(
                                assigned_to = , 
                                assigned_to_virtual_circuit = True, 
                                description = '', 
                                facility = , 
                                href = '', 
                                id = '', 
                                instances = [
                                    
                                    ], 
                                metal_gateways = [
                                    equinix_metal.models.metal_gateway_lite.MetalGatewayLite(
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        gateway_address = '10.1.2.1/27', 
                                        href = '', 
                                        id = '', 
                                        state = 'ready', 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        vlan = 1001, )
                                    ], 
                                metro_code = '', 
                                vxlan = 56, ), 
                            vrf = equinix_metal.models.vrf.Vrf(
                                bgp_dynamic_neighbors_bfd_enabled = True, 
                                bgp_dynamic_neighbors_enabled = True, 
                                bgp_dynamic_neighbors_export_route_map = True, 
                                bill = True, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                description = '', 
                                href = '', 
                                id = '', 
                                local_asn = 56, 
                                name = '', 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ), 
                        next_hop = '192.168.1.254', 
                        prefix = '0.0.0.0/0', 
                        status = 'active', 
                        type = 'static', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        virtual_network = equinix_metal.models.virtual_network.VirtualNetwork(
                            assigned_to_virtual_circuit = True, 
                            description = '', 
                            href = '', 
                            id = '', 
                            metro_code = '', 
                            vxlan = 56, ), 
                        vrf = , )
                    ]
            )
        else :
            return VrfRouteList(
        )
        """

    def testVrfRouteList(self):
        """Test VrfRouteList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
