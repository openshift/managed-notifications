# Managed-notifications

Notification templates for OpenShift Managed services

## Usage

Select the corresponding message and send it as a `POST` to
[api.openshift.com servicelog](https://api.openshift.com/?urls.primaryName=Service%20logs#/default/post_api_service_logs_v1_cluster_logs).

> :warning: Please review each template before post to make sure all the
> parameters are passed with -p
>
> :books: If you are not sure which servicelog to send, you can use the
> generic one in [osd/unknown_failure.json](./osd/unknown_failure.json)

### Examples

Using [osdctl](https://github.com/openshift/osdctl)

1. Authenticate at <https://cloud.redhat.com/openshift/token>
2. Post servicelog

```bash
osdctl servicelog post <cluster UUID> -t <notificationTemplateUrl>
```

Example:

```bash
osdctl servicelog post aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee \
  -t https://raw.githubusercontent.com/openshift/managed-notifications/\
master/osd/aws/InstallFailed_TooManyBuckets.json
```

Note: `Osdctl` supports the usage of the unique cluster name, or the
internal- and external ID as clusterID.

### Tags

Some template files have a `_tag` field for easier searching.

For example, in GitHub, searching `t_network` will show you all the network
related template files.

## MCP Search Server

This repository includes an MCP (Model Context Protocol) server that provides
semantic search capabilities over the notification templates. See
[mcp/README.md](mcp/README.md) for setup and usage instructions.

## Validating Managed Notifications

Run `make validate` to perform basic validations against the notifications
configured in this repo.
