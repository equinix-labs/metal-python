# metal-python

Python SDK for Equinix Metal API , generated with openapi-generator. Pypi package name is `equinix_metal`.

## Generating

Simply `$ make generate`. Make will download spec, stich them together and fix them with the patching script.

## Patching Equinix Metal OpenAPI spec

We need to do some fixes to the default openapi yaml specification
from Equinix Metal. The [scripts/patch_metal_spec.py](scripts/patch_metal_spec.py) script modifies the
fetched (and stitched) spec into [metal_openapi.fixed.yaml](metal_openapi.fixed.yaml) which is then passed to
openapi-generator-cli.

## Examples

See example scripts in [examples](examples) directory.



