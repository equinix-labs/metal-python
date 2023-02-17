SPEC_PATCHED_FILE=./metal_openapi.fixed.yaml
OPENAPI_CODEGEN_IMAGE=openapitools/openapi-generator-cli@${OPENAPI_CODEGEN_SHA}
CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)
DOCKER_OPENAPI=docker run --rm -u ${CURRENT_UID}:${CURRENT_GID} -v $(CURDIR):/local ${OPENAPI_CODEGEN_IMAGE}





SPEC_DIR_ENTRY_POINT=oas3.fetched/openapi/public/openapi3.yaml
STITCHED_DIR=oas3.stitched
STITCHED_FILE=metal_openapi.yaml
#OPENAPI_CODEGEN_SHA=sha256:be8c2ef6be22f695410c2cc13d0ec7fdf2533fc88a7f17288ad758b7679de8df
OPENAPI_CODEGEN_SHA=sha256:2e108389ba0cc6210449fba419e755d737bd235b1d061359490c057a571b89fa

.PHONY: docker-stitch-spec
docker-stitch-spec:
	${DOCKER_OPENAPI} generate \
		-i /local/${SPEC_DIR_ENTRY_POINT} \
		-g openapi-yaml \
		-p skipOperationExample=true -p outputFile=${STITCHED_FILE} \
		-o /local/${STITCHED_DIR}

.PHONY: patch-spec
patch-spec: docker-stitch-spec
	scripts/patch_metal_spec.py ${STITCHED_DIR}/${STITCHED_FILE} ${SPEC_PATCHED_FILE}

.PHONY: clean
clean:
	rm -rf ${STITCHED_DIR}
	rm -rf ${PACKAGE_NAME}

GIT_REPO=metal-python-nextgen
GIT_ORG=t0mk
OPENAPI_CONFIG:=oas3.config.json
PACKAGE_NAME=metal_python
PACKAGE_VERSION=0.0.1

.PHONY: docker-generate
docker-generate: clean patch-spec
	${DOCKER_OPENAPI} generate \
		-i /local/${SPEC_PATCHED_FILE} \
		-g python-nextgen \
		-o /local/${PACKAGE_NAME} \
		--git-repo-id ${GIT_REPO} \
		--git-user-id ${GIT_ORG}  \
	    --additional-properties=packageName=${PACKAGE_NAME},packageVersion=${PACKAGE_VERSION}
