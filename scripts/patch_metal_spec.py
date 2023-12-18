#!/usr/bin/env python3

import yaml
from yaml.loader import FullLoader
import copy
import sys
from collections import OrderedDict

if len(sys.argv) != 3:
    print("Usage: {} <input file> <output file>".format(sys.argv[0]))
    sys.exit(1)

INFILE = sys.argv[1]
OUTFILE = sys.argv[2]


def setup_yaml():
    """ https://stackoverflow.com/a/8661021 """

    def represent_dict_order(self, data): return self.represent_mapping(
        'tag:yaml.org,2002:map', data.items())
    yaml.add_representer(OrderedDict, represent_dict_order)


setup_yaml()

def loadYaml(fn):
    with open(fn) as f:
        return yaml.load(f, Loader=FullLoader)


originalSpec = loadYaml(INFILE)

fixedSpec = copy.deepcopy(originalSpec)

# FIX 0. organization href to project
fixedSpec['components']['schemas']['Project']['properties']['organization'] = {
    "$ref": "#/components/schemas/Href"
}

# FIX 1. href property to all schemas if they have "properties" and don't already have "href"
for s in fixedSpec['components']['schemas']:
    if 'properties' in fixedSpec['components']['schemas'][s]:
        if 'href' not in fixedSpec['components']['schemas'][s]['properties']:
            fixedSpec['components']['schemas'][s]['properties']['href'] = {
                "type": "string",
                "format": "uri"
            }

# FIX 2. remove defaults for always_pxe and hardware_reservation_id
fixSchemas = ["DeviceCreateInput"]
removeProperties = ["always_pxe", "hardware_reservation_id"]
for s in fixSchemas:
    for p in removeProperties:
        if p in fixedSpec['components']['schemas'][s]['properties']:
            del fixedSpec['components']['schemas'][s]['properties'][p]['default']


# FIX 5. add backend_transfer_enabled to Project Schema
project_props = fixedSpec['components']['schemas']['Project']['properties']
project_props['backend_transfer_enabled'] = {'type': 'boolean'}

# FIX 8. make requested_by mandatory for parsing ip reservation
# .. in order to distinguish from ip assignment and vrf

fixedSpec['components']['schemas']['IPAssignment']['required'] = [
    'assigned_to']

# FIX 9. make  IPReservation assignments href, instead of IPAssignment,
# .. so that it's not parsed as a list of IPAssignments which has mandatory fields

fixedSpec['components']['schemas']['IPReservation']['properties']['assignments']['items'] = {
    "$ref": "#/components/schemas/Href"
}

# FIX 11. Make all Address parameters non-mandatory

del fixedSpec['components']['schemas']['Address']['required']

# FIX 12. Adding items for validation of enum PlanSpec

fixedSpec['components']['schemas']['Plan_specs_drives_inner']['properties']['type']['enum'].append('NVMe')
fixedSpec['components']['schemas']['Plan_specs_nics_inner']['properties']['type']['enum'].append('100Gbps')


with open(OUTFILE, 'w') as f:
    originalSpec = yaml.dump(
        fixedSpec, f, default_flow_style=False)


print(INFILE, "was fixed into", OUTFILE)
