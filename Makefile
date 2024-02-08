VERSION_FILE=version
PACKAGE_VERSION := $(shell cat ${VERSION_FILE})

SPEC_PATCHED_FILE=./metal_openapi.fixed.yaml

OPENAPI_CODEGEN_TAG=v7.0.0
OPENAPI_CODEGEN_IMAGE=openapitools/openapi-generator-cli:${OPENAPI_CODEGEN_TAG}
CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)
OPENAPI_COMMAND=docker run --rm -u ${CURRENT_UID}:${CURRENT_GID} -v $(CURDIR):/local ${OPENAPI_CODEGEN_IMAGE}
GIT_REPO=metal-python
GIT_ORG=equinix-labs
OPENAPI_CONFIG:=config/openapi-generator.json
PACKAGE_NAME=equinix_metal
STITCHED_DIR=oas3.stitched
STITCHED_FILE=metal_openapi.yaml
FETCH_SPEC_COMMAND=docker run --rm -u ${CURRENT_UID}:${CURRENT_GID} -v $(CURDIR):/workdir --entrypoint sh mikefarah/yq:4.30.8 scripts/download_spec.sh
SPEC_BASE_URL:=https://api.equinix.com/metal/v1/api-docs
SPEC_ROOT_FILE:=openapi3.yaml
SPEC_FETCHED_DIR=oas3.fetched

.PHONY: all
all: stitch-spec patch-spec clean generate fetch

fetch:
		${FETCH_SPEC_COMMAND} ${SPEC_BASE_URL} ${SPEC_FETCHED_DIR} ${SPEC_ROOT_FILE}

#stitch-spec: fetch
# keep 'fetch' target independent on the API spec transformations 
stitch-spec:
	${OPENAPI_COMMAND} generate \
		-i /local/${SPEC_FETCHED_DIR}/${SPEC_ROOT_FILE} \
		-g openapi-yaml \
		-p skipOperationExample=true -p outputFile=${STITCHED_FILE} \
		-o /local/${STITCHED_DIR}

patch-spec: stitch-spec
	scripts/patch_metal_spec.py ${STITCHED_DIR}/${STITCHED_FILE} ${SPEC_PATCHED_FILE}

clean:
	rm -rf ${STITCHED_DIR}
	rm -rf ${PACKAGE_NAME}


USER_AGENT=${GIT_REPO}/${PACKAGE_VERSION}
generate: clean patch-spec
	${OPENAPI_COMMAND} generate \
		-i /local/${SPEC_PATCHED_FILE} \
		-g python \
		-o /local/${PACKAGE_NAME} \
		-c /local/${OPENAPI_CONFIG} \
		--git-repo-id ${GIT_REPO} \
		--git-user-id ${GIT_ORG}  \
		--http-user-agent ${USER_AGENT} \
	    --additional-properties=packageName=equinix_metal_t0mk,packageVersion=${PACKAGE_VERSION}
	rm -rf equinix_metal/.github
	rm -rf equinix_metal/.gitlab-ci.yml
