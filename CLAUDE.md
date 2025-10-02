# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Essential Commands

**Validation:**
```bash
# Validate all notification descriptions end with a period
make validate

# Check for broken links in notification templates
make checklinks

# Validate severity levels in all templates
make checkseverity
```

**MCP Server (semantic search over notifications):**
```bash
# Build MCP server container
make build-container

# See mcp/CLAUDE.md for detailed MCP server development commands
```

## Repository Architecture

This repository contains OpenShift Managed Services notification templates organized by service type:

- **osd/** - OpenShift Dedicated notifications (150+ templates)
  - **osd/aws/** - AWS-specific OSD notifications
- **rosa/** - Red Hat OpenShift Service on AWS notifications
- **hcp/** - Hosted Control Plane notifications
- **cluster/** - General cluster notifications
- **ocm/** - OpenShift Cluster Manager notifications
- **mcp/** - MCP server for semantic search over notification templates (separate subproject with own CLAUDE.md)
- **scripts/** - Validation scripts

### Notification Template Structure

Each notification is a JSON file with required fields:

```json
{
  "severity": "Debug|Info|Warning|Major|Critical",
  "service_name": "SREManualAction|...",
  "log_type": "cluster-lifecycle|...",
  "summary": "Brief summary.",
  "description": "Detailed description that must end with a period.",
  "doc_references": ["https://..."],
  "internal_only": false
}
```

**Key constraints:**
- `description` field MUST end with a period (enforced by `make validate`)
- `severity` must be one of: Debug, Info, Warning, Major, Critical (enforced by `scripts/checkseverity.sh`)
- Templates may contain variable placeholders like `${TIME}`, `${CLUSTER_ID}`, `${NAMESPACE}`

### Posting Notifications

Notifications are posted via the [OpenShift Service Logs API](https://api.openshift.com/?urls.primaryName=Service%20logs#/default/post_api_service_logs_v1_cluster_logs) using `osdctl`:

```bash
osdctl servicelog post <cluster-uuid> -t <template-url>
```

Example:
```bash
osdctl servicelog post aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee \
  -t https://raw.githubusercontent.com/openshift/managed-notifications/master/osd/aws/InstallFailed_TooManyBuckets.json
```

### Tag System

Some templates include a `_tag` field for categorization (e.g., `t_network` for network-related issues). Search GitHub with these tags to find related templates.

## MCP Server Subproject

The `mcp/` directory contains a standalone MCP (Model Context Protocol) server that provides semantic search over these notification templates using vector embeddings. This subproject:

- Has its own `mcp/CLAUDE.md` with detailed architecture and development instructions
- Uses Python + uv for dependency management
- Builds ChromaDB vector database from notification templates
- Exposes MCP tools for AI-powered notification search

When working on the MCP server, refer to `mcp/CLAUDE.md` for specific guidance.

## Validation Scripts

**scripts/checklinks.sh** - Validates all HTTP/HTTPS URLs in templates return 200 (not 404)

**scripts/checkseverity.sh** - Ensures all templates have valid severity values

These run in CI and should pass before merging changes.
