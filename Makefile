SHELL := /bin/bash

.DEFAULT_GOAL:=help

# Validates that managed-notification descriptions end with a period.
# 1) Find files with .json extension that contain "description":
# 	 grep -rnw '.' --include "*.json" -e "description"
# 2) Pipe those files into another grep to find files that
#    have a description ending with no period:
# 	 grep -v '"description".*\."'
# We echo the error and return if a description not ending with a period is found.
.PHONY: validate
validate:
	@!(grep -rnw '.' --include "*.json" -e "description" | grep -v '"description".*\."') || (echo "Please add a period at the end of the description in the above files."; exit 1)
	@echo "Validation succeeded."

.PHONY: help
help:
	@echo 'Usage:'
	@echo '  make <target>'
	@echo ''
	@echo 'Targets:'
	@echo ' validate - validates that managed-notification descriptions end with a period.'
	@echo ' build-container - builds the MCP server container with podman.'

.PHONY: checklinks
checklinks:
	scripts/checklinks.sh

.PHONY: checkseverity
checkseverity:
	scripts/checkseverity.sh

.PHONY: build-container
build-container:
	@echo "Setting up managed-notifications directory for container build..."
	@rm -rf mcp/managed-notifications
	@mkdir -p mcp/managed-notifications
	@cp -r cluster hcp ocm osd rosa scripts mcp/managed-notifications/
	@echo "Building container with podman..."
	cd mcp && podman build --no-cache -t managed-notifications-search .
