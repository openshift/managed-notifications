# Managed-notifications

Notification templates for OpenShift Managed services

## Usage

Select the corresopnding message and send as a `POST` to 
[api.openshift.com servicelog](https://api.openshift.com/?urls.primaryName=Service%20logs#/default/post_api_service_logs_v1_cluster_logs). 
`CLUSTER_UUID` is a required parameter.

### Examples

Using [osdctl](https://github.com/openshift/osdctl)

1. Authenticate at https://cloud.redhat.com/openshift/token
1. Post servicelog

    osdctl servicelog post -t <notificationTemplateUrl> -p CLUSTER_UUID=<UUID>
