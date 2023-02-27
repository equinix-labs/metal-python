SPEC_PATCHED_FILE=./metal_openapi.fixed.yaml
OPENAPI_CODEGEN_SHA=sha256:925bc39fc00f8198cde01a2315afa815b37b2a44a9a43afed298adfc79da5770
OPENAPI_CODEGEN_IMAGE=openapitools/openapi-generator-cli@${OPENAPI_CODEGEN_SHA}
CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)

# TODO: switch back to Docker once openapi-generator-cli fixes python-nextgen bugs
#OPENAPI_COMMAND=docker run --rm -u ${CURRENT_UID}:${CURRENT_GID} -v $(CURDIR):/local ${OPENAPI_CODEGEN_IMAGE}
OPENAPI_COMMAND=java -jar oag.jar

.PHONY: all
all: stitch-spec patch-spec clean generate fetch

STITCHED_DIR=oas3.stitched
STITCHED_FILE=metal_openapi.yaml
FETCH_SPEC_COMMAND=docker run --rm -v $(CURDIR):/workdir --entrypoint sh mikefarah/yq:4.30.8 scripts/download_spec.sh
SPEC_BASE_URL:=https://api.packet.net/api-docs-test
SPEC_ROOT_FILE:=openapi3.yaml
SPEC_FETCHED_DIR=oas3.fetched

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

GIT_REPO=metal-python
GIT_ORG=t0mk
OPENAPI_CONFIG:=oas3.config.json
PACKAGE_NAME=equinix_metal
PACKAGE_VERSION=0.0.1

generate: clean patch-spec
#	${OPENAPI_COMMAND} generate \
		-i /local/${SPEC_PATCHED_FILE} \
		-g python-nextgen \
		-o /local/${PACKAGE_NAME} \
		--git-repo-id ${GIT_REPO} \
		--git-user-id ${GIT_ORG}  \
	    --additional-properties=packageName=${PACKAGE_NAME},packageVersion=${PACKAGE_VERSION}
	${OPENAPI_COMMAND} generate \
		-i ${SPEC_PATCHED_FILE} \
		-g python-nextgen \
		-o ${PACKAGE_NAME} \
		--git-repo-id ${GIT_REPO} \
		--git-user-id ${GIT_ORG}  \
	    --additional-properties=packageName=${PACKAGE_NAME},packageVersion=${PACKAGE_VERSION}
