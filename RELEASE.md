# Release Instructions

(based on former pacet-python release process: https://github.com/packethost/packet-python/blob/master/RELEASE.md)

These build and release instructions are intended for the maintainers and future maintainers of this project.

## Preparing a new version

* change PACKAGE_VERSION in Makefile
* Add new version section to CHANGELOG.md
* Fix and improve things
* Run `make generate` to generate the SDK
* Run `make test` to verify that generated unittests passs
* Mention fixes and improvements in CHANGELOG
* Create a PR with these changes
* Merge

## Building

Pull down the merged changes:

```bash
git fetch origin
git checkout origin/main
```

Run generated unittests: `make test`

Build the package: `make build`


## Publishing

Make sure you have `~/.pypirc` correctly populated. It should look something like:

```
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username: username-here
password: password-here

[testpypi]
repository: https://test.pypi.org/legacy/
username: username-here (not necessarily same as real pypi)
password: password-here (not necessarily same as real pypi)
```

If you are using a token, the username is `__token__`.  Make sure you have been added to the
[project](https://pypi.org/manage/project/equinix-metal/collaboration/) and the
[test project](https://test.pypi.org/manage/project/equinix-metal/collaboration/).

Do a test-release to test.pypi.org first: `make test-release`. 

If everything went ok, tag and push the tag: make tag-release` ..

.. and publish the package to pypi: `make release`.

See the makefile targets for details.

Congratulations, you published `equinix_metal`, :raised_hands:!

