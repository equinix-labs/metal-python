# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://deploy.equinix.com/developers/api/metal/>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. Currently the search parameter is only available on devices, ssh_keys, api_keys and memberships endpoints.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix_metal.models.metal_gateway import MetalGateway

class TestMetalGateway(unittest.TestCase):
    """MetalGateway unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetalGateway:
        """Test MetalGateway
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetalGateway`
        """
        model = MetalGateway()
        if include_optional:
            return MetalGateway(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = equinix_metal.models.href.Href(
                    href = '', ),
                href = '',
                id = '',
                ip_reservation = equinix_metal.models.ip_reservation.IPReservation(
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
                    facility = null, 
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
                    metro = null, 
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
                        name = '0', 
                        network_status = equinix_metal.models.network_status.network_status(), 
                        organization = , 
                        payment_method = , 
                        ssh_keys = [
                            
                            ], 
                        tags = [
                            ''
                            ], 
                        type = 'default', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        volumes = [
                            
                            ], ), 
                    project_lite = , 
                    public = True, 
                    requested_by = , 
                    state = '', 
                    tags = [
                        ''
                        ], 
                    type = 'global_ipv4', ),
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
                    name = '0', 
                    network_status = equinix_metal.models.network_status.network_status(), 
                    organization = , 
                    payment_method = , 
                    ssh_keys = [
                        
                        ], 
                    tags = [
                        ''
                        ], 
                    type = 'default', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', 
                    volumes = [
                        
                        ], ),
                state = 'ready',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                virtual_network = equinix_metal.models.virtual_network.VirtualNetwork(
                    assigned_to = equinix_metal.models.project.Project(
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
                        name = '0', 
                        network_status = equinix_metal.models.network_status.network_status(), 
                        organization = , 
                        payment_method = , 
                        ssh_keys = [
                            
                            ], 
                        tags = [
                            ''
                            ], 
                        type = 'default', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        volumes = [
                            
                            ], ), 
                    assigned_to_virtual_circuit = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    facility = , 
                    href = '', 
                    id = '', 
                    instances = [
                        equinix_metal.models.device.Device(
                            actions = [
                                equinix_metal.models.device_actions_inner.Device_actions_inner(
                                    href = '', 
                                    name = '', 
                                    type = '', )
                                ], 
                            always_pxe = True, 
                            billing_cycle = '', 
                            bonding_mode = 56, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_by = null, 
                            customdata = { }, 
                            description = '', 
                            firmware_set_id = '', 
                            hardware_reservation = equinix_metal.models.hardware_reservation.HardwareReservation(
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                custom_rate = 1050.5, 
                                device = equinix_metal.models.device.Device(
                                    always_pxe = True, 
                                    billing_cycle = '', 
                                    bonding_mode = 56, 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    description = '', 
                                    firmware_set_id = '', 
                                    hostname = '', 
                                    href = '', 
                                    id = '', 
                                    image_url = '', 
                                    ip_addresses = [
                                        equinix_metal.models.ip_assignment.IPAssignment(
                                            address = '', 
                                            address_family = 56, 
                                            assigned_to = , 
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
                                            next_hop = '', 
                                            parent_block = equinix_metal.models.parent_block.ParentBlock(
                                                cidr = 56, 
                                                href = '', 
                                                netmask = '', 
                                                network = '', ), 
                                            public = True, 
                                            state = 'pending', )
                                        ], 
                                    ipxe_script_url = '', 
                                    iqn = '', 
                                    locked = True, 
                                    metro = null, 
                                    network_frozen = True, 
                                    network_ports = [
                                        equinix_metal.models.port.Port(
                                            bond = equinix_metal.models.bond_port_data.BondPortData(
                                                href = '', 
                                                id = '', 
                                                name = '', ), 
                                            data = equinix_metal.models.port_data.PortData(
                                                bonded = True, 
                                                href = '', 
                                                mac = '', ), 
                                            disbond_operation_supported = True, 
                                            href = '', 
                                            id = '', 
                                            name = 'bond0', 
                                            native_virtual_network = equinix_metal.models.virtual_network.VirtualNetwork(
                                                assigned_to_virtual_circuit = True, 
                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                description = '', 
                                                href = '', 
                                                id = '', 
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
                                            network_type = 'layer2-bonded', 
                                            type = 'NetworkPort', 
                                            virtual_networks = [
                                                
                                                ], )
                                        ], 
                                    operating_system = equinix_metal.models.operating_system.OperatingSystem(
                                        build_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        default_operating_system = True, 
                                        deprecation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        distro = '', 
                                        distro_label = '', 
                                        end_of_life_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        end_of_service_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        href = '', 
                                        id = '', 
                                        licensed = True, 
                                        lifecycle_state = '', 
                                        name = '', 
                                        preinstallable = True, 
                                        pricing = equinix_metal.models.pricing.pricing(), 
                                        provisionable_on = [
                                            ''
                                            ], 
                                        release_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        release_notes = '', 
                                        slug = '', 
                                        version = '', ), 
                                    plan = equinix_metal.models.plan.Plan(
                                        available_in = [
                                            equinix_metal.models.plan_available_in_inner.Plan_available_in_inner(
                                                href = '', 
                                                price = equinix_metal.models.plan_available_in_inner_price.Plan_available_in_inner_price(
                                                    hour = 1.23, 
                                                    href = '', ), )
                                            ], 
                                        available_in_metros = [
                                            equinix_metal.models.plan_available_in_metros_inner.Plan_available_in_metros_inner(
                                                href = '', )
                                            ], 
                                        categories = [
                                            ''
                                            ], 
                                        class = 'm3.large.x86', 
                                        deployment_types = [
                                            'on_demand'
                                            ], 
                                        description = '', 
                                        href = '', 
                                        id = '', 
                                        legacy = True, 
                                        line = '', 
                                        name = '', 
                                        pricing = equinix_metal.models.pricing.pricing(), 
                                        slug = 'm3.large.x86', 
                                        specs = equinix_metal.models.plan_specs.Plan_specs(
                                            cpus = [
                                                equinix_metal.models.plan_specs_cpus_inner.Plan_specs_cpus_inner(
                                                    count = 56, 
                                                    href = '', 
                                                    type = '', )
                                                ], 
                                            drives = [
                                                equinix_metal.models.plan_specs_drives_inner.Plan_specs_drives_inner(
                                                    category = '', 
                                                    count = 56, 
                                                    href = '', 
                                                    size = '3.84TB', 
                                                    type = '', )
                                                ], 
                                            features = equinix_metal.models.plan_specs_features.Plan_specs_features(
                                                href = '', 
                                                raid = True, 
                                                txt = True, 
                                                uefi = True, ), 
                                            href = '', 
                                            memory = equinix_metal.models.plan_specs_memory.Plan_specs_memory(
                                                href = '', 
                                                total = '', ), 
                                            nics = [
                                                equinix_metal.models.plan_specs_nics_inner.Plan_specs_nics_inner(
                                                    count = 2, 
                                                    href = '', 
                                                    type = '', )
                                                ], ), 
                                        type = 'standard', ), 
                                    project = equinix_metal.models.project.Project(
                                        backend_transfer_enabled = True, 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        href = '', 
                                        id = '', 
                                        max_devices = equinix_metal.models.max_devices.max_devices(), 
                                        name = '0', 
                                        network_status = equinix_metal.models.network_status.network_status(), 
                                        type = 'default', 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        url = '', ), 
                                    project_lite = null, 
                                    provisioning_events = [
                                        equinix_metal.models.event.Event(
                                            body = '', 
                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            href = '', 
                                            id = '', 
                                            interpolated = '', 
                                            ip = '', 
                                            modified_by = equinix_metal.models.modified_by.modified_by(), 
                                            relationships = [
                                                
                                                ], 
                                            state = '', 
                                            type = '', )
                                        ], 
                                    provisioning_percentage = 1.337, 
                                    root_password = '', 
                                    short_id = '', 
                                    sos = '', 
                                    spot_instance = True, 
                                    spot_price_max = 1.337, 
                                    state = 'queued', 
                                    storage = equinix_metal.models.storage.Storage(
                                        disks = [
                                            equinix_metal.models.disk.Disk(
                                                href = '', 
                                                partitions = [
                                                    equinix_metal.models.partition.Partition(
                                                        href = '', 
                                                        label = '', 
                                                        number = 56, 
                                                        size = '', )
                                                    ], 
                                                wipe_table = True, )
                                            ], 
                                        filesystems = [
                                            equinix_metal.models.filesystem.Filesystem(
                                                href = '', 
                                                mount = equinix_metal.models.mount.Mount(
                                                    format = '', 
                                                    href = '', 
                                                    options = [
                                                        ''
                                                        ], 
                                                    point = '', ), )
                                            ], 
                                        href = '', 
                                        raid = [
                                            equinix_metal.models.raid.Raid(
                                                href = '', 
                                                level = '', 
                                                name = '', )
                                            ], ), 
                                    switch_uuid = '', 
                                    termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    user = '', 
                                    userdata = '', ), 
                                href = '', 
                                id = '', 
                                need_of_service = True, 
                                plan = equinix_metal.models.plan.Plan(
                                    class = 'm3.large.x86', 
                                    description = '', 
                                    href = '', 
                                    id = '', 
                                    legacy = True, 
                                    line = '', 
                                    name = '', 
                                    pricing = equinix_metal.models.pricing.pricing(), 
                                    slug = 'm3.large.x86', 
                                    type = 'standard', ), 
                                project = , 
                                provisionable = True, 
                                short_id = '', 
                                spare = True, 
                                switch_uuid = '', 
                                termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            hostname = '', 
                            href = '', 
                            id = '', 
                            image_url = '', 
                            ip_addresses = [
                                equinix_metal.models.ip_assignment.IPAssignment(
                                    address = '', 
                                    address_family = 56, 
                                    assigned_to = , 
                                    cidr = 56, 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    enabled = True, 
                                    gateway = '', 
                                    global_ip = True, 
                                    href = '', 
                                    id = '', 
                                    manageable = True, 
                                    management = True, 
                                    netmask = '', 
                                    network = '', 
                                    next_hop = '', 
                                    public = True, 
                                    state = 'pending', )
                                ], 
                            ipxe_script_url = '', 
                            iqn = '', 
                            locked = True, 
                            metro = null, 
                            network_frozen = True, 
                            network_ports = [
                                equinix_metal.models.port.Port(
                                    disbond_operation_supported = True, 
                                    href = '', 
                                    id = '', 
                                    name = 'bond0', 
                                    network_type = 'layer2-bonded', 
                                    type = 'NetworkPort', )
                                ], 
                            operating_system = equinix_metal.models.operating_system.OperatingSystem(
                                build_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                default_operating_system = True, 
                                deprecation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                distro = '', 
                                distro_label = '', 
                                end_of_life_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                end_of_service_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                href = '', 
                                id = '', 
                                licensed = True, 
                                lifecycle_state = '', 
                                name = '', 
                                preinstallable = True, 
                                pricing = equinix_metal.models.pricing.pricing(), 
                                release_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                release_notes = '', 
                                slug = '', 
                                version = '', ), 
                            plan = , 
                            project = , 
                            project_lite = null, 
                            provisioning_events = [
                                equinix_metal.models.event.Event(
                                    body = '', 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    href = '', 
                                    id = '', 
                                    interpolated = '', 
                                    ip = '', 
                                    modified_by = equinix_metal.models.modified_by.modified_by(), 
                                    state = '', 
                                    type = '', )
                                ], 
                            provisioning_percentage = 1.337, 
                            root_password = '', 
                            short_id = '', 
                            sos = '', 
                            spot_instance = True, 
                            spot_price_max = 1.337, 
                            state = 'queued', 
                            storage = equinix_metal.models.storage.Storage(
                                href = '', ), 
                            switch_uuid = '', 
                            termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            user = '', 
                            userdata = '', )
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
                    metro = equinix_metal.models.metro.Metro(
                        code = '', 
                        country = '', 
                        href = '', 
                        id = '', 
                        name = '', ), 
                    metro_code = '', 
                    tags = [
                        ''
                        ], 
                    vxlan = 56, )
            )
        else:
            return MetalGateway(
        )
        """

    def testMetalGateway(self):
        """Test MetalGateway"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
