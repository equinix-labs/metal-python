# metal-python


[![Experimental](https://img.shields.io/badge/Stability-Experimental-red.svg)](https://github.com/equinix-labs/equinix-labs/blob/main/uniform-standards.md)

> **[Experimental](https://github.com/equinix-labs/equinix-labs/blob/main/experimental-statement.md)**
> This is experimental. Don't use it in production. Examples demonstrate that this client is usable. Please submit patches and open issues with your experience. This repo contains Python code generated from a customized [metal_openapi.fixed.yaml](metal_openapi.fixed.yaml) based on the [Equinix Metal API spec](https://api.equinix.com/metal/v1/api-docs). The client is generated using the python-nextgen generator built into the [OpenAPITools openapi-generator](https://github.com/OpenAPITools/openapi-generator).

Python SDK for Equinix Metal API , generated with openapi-generator. Pypi package name is `equinix-metal`.

## Examples

See examples in [examples](examples) directory.

## Documentation


Full Equinix Metal API documenation is available here: [https://metal.equinix.com/developers/api/](https://metal.equinix.com/developers/api/).

Generated documentation is available here: [equinix_metal/README.md](equinix_metal/README.md).


## Requirements

This project is using [OpenAPITools openapi-generator](https://github.com/OpenAPITools/openapi-generator) Docker images to generate the code. You need to have Docker installed. 

In order to limit dependencies, the Makefile uses Docker for most of the tasks. If you run the tasks for the first time, you will need to wait for Docker image download.

## Get newest API spec

Run `make fetch` to download newest API spec from upstream.


## Development

Clone this repo

```
git clone https://github.com/equinix-labs/metal-python
```

Everything in [equinix_metal](equinix_metal) directory is generated. You can change code there to debug or experiment, but be aware that it will be rewritten on next `make generate`.

Development of this package mostly means editing:
- [Makefile](Makefile)
- The spec-patching script in [scripts/patch_metal_spec.py](scripts/patch_metal_spec.py)


Once you did your edits, run `make generate` and check how the generated code has changed.

To use the regenerated code, you can install the generated package from directory:

```
pip install ./equinix_metal
```

.. and then `import equinix_metal` in a Python script.

## Release

When releasing, make sure that the desired version number is in `PACKAGE_VERSION` variable in Makefile, and that `make generate` doesn't taint git status.

Then go to [https://github.com/equinix-labs/metal-python/releases/new](https://github.com/equinix-labs/metal-python/releases/new) and create a new release from `main`. Don't choose an existing tag, but create a new one called `v{PACKAGE_VERSION}`. For example, if PACKAGE_VERSION is "0.1.2", create tag "v0.1.2". Put the tag name also to the "Release title" field.

Add release notes in format of [Terraform Provider Equinix](https://github.com/equinix/terraform-provider-equinix/releases), with at least one of the sections (NOTES, FEATURES, BUG FIXES, ENHANCEMENTS).

Click "Publish release", and the manual part should be over.

The release will create a tag, and we have a Github action in place that should create a PyPI release for version from PACKAGE_VERSION.

Verify that the [releasing Github action](https://github.com/equinix-labs/metal-python/actions) succeeded.

Verify that new version of (equinix-metal)[https://pypi.org/project/equinix-metal/#history] is avaiable on Pypi.
