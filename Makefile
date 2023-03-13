PACKAGE_VERSION=0.0.1

SPEC_PATCHED_FILE=./metal_openapi.fixed.yaml
OPENAPI_CODEGEN_SHA=sha256:925bc39fc00f8198cde01a2315afa815b37b2a44a9a43afed298adfc79da5770
OPENAPI_CODEGEN_IMAGE=openapitools/openapi-generator-cli@${OPENAPI_CODEGEN_SHA}
CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)
# TODO: switch back to Docker once openapi-generator-cli fixes python-nextgen bugs
#OPENAPI_COMMAND=docker run --rm -u ${CURRENT_UID}:${CURRENT_GID} -v $(CURDIR):/local ${OPENAPI_CODEGEN_IMAGE}
OPENAPI_COMMAND=java -jar oag.jar
STITCHED_DIR=oas3.stitched
STITCHED_FILE=metal_openapi.yaml
FETCH_SPEC_COMMAND=docker run --rm -v $(CURDIR):/workdir --entrypoint sh mikefarah/yq:4.30.8 scripts/download_spec.sh
SPEC_BASE_URL:=https://api.equinix.com/metal/v1/api-docs
SPEC_ROOT_FILE:=openapi3.yaml
SPEC_FETCHED_DIR=oas3.fetched
GIT_REPO=metal-python
GIT_ORG=equinix-labs
OPENAPI_CONFIG:=oas3.config.json
PACKAGE_NAME=equinix_metal
USER_AGENT=${GIT_REPO}/${PACKAGE_VERSION}

.PHONY: all
all: stitch-spec patch-spec clean generate fetch build release tag-release test-release test deps

fetch:
		${FETCH_SPEC_COMMAND} ${SPEC_BASE_URL} ${SPEC_FETCHED_DIR} ${SPEC_ROOT_FILE}

stitch-spec: fetch
#	${OPENAPI_COMMAND} generate \
		-i /local/${SPEC_FETCHED_DIR}/${SPEC_ROOT_FILE} \
		-g openapi-yaml \
		-p skipOperationExample=true -p outputFile=${STITCHED_FILE} \
		-o /local/${STITCHED_DIR}
	${OPENAPI_COMMAND} generate \
		-i ${SPEC_FETCHED_DIR}/${SPEC_ROOT_FILE} \
		-g openapi-yaml \
		-p skipOperationExample=true -p outputFile=${STITCHED_FILE} \
		-o ${STITCHED_DIR}

patch-spec: stitch-spec
	scripts/patch_metal_spec.py ${STITCHED_DIR}/${STITCHED_FILE} ${SPEC_PATCHED_FILE}

clean:
	rm -rf ${STITCHED_DIR}
	rm -rf ${PACKAGE_NAME}
	rm -rf ${PACKAGE_NAME}.egg-info
	rm -rf build dist

generate: clean patch-spec
#	${OPENAPI_COMMAND} generate \
		-i /local/${SPEC_PATCHED_FILE} \
		-g python-nextgen \
		-o /local/${PACKAGE_NAME} \
		--git-repo-id ${GIT_REPO} \
		--git-user-id ${GIT_ORG}  \
		--http-user-agent ${USER_AGENT} \
	    --additional-properties=packageName=${PACKAGE_NAME},packageVersion=${PACKAGE_VERSION}
	${OPENAPI_COMMAND} generate \
		-i ${SPEC_PATCHED_FILE} \
		-g python-nextgen \
		-o ${PACKAGE_NAME} \
		--git-repo-id ${GIT_REPO} \
		--git-user-id ${GIT_ORG}  \
		--http-user-agent ${USER_AGENT} \
	    --additional-properties=packageName=${PACKAGE_NAME},packageVersion=${PACKAGE_VERSION}

deps:
	cd ${PACKAGE_NAME} && pip install -r requirements.txt -r test-requirements.txt

test: deps
	cd ${PACKAGE_NAME} && PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python pytest

build:
	python ${PACKAGE_NAME}/setup.py sdist bdist_wheel

tag-release:
	git tag -a v${PACKAGE_VERSION} -m "v${PACKAGE_VERSION}" && \
	git push origin --tags v${PACKAGE_VERSION}

test-release: build
	twine upload -r testpypi dist/*

release: build
	twine upload dist/*
    

