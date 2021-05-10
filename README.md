# Managed-notifications

Notification templates for OpenShift Managed services

## Usage

Select the corresopnding message and send as a `POST` to
[api.openshift.com servicelog](https://api.openshift.com/?urls.primaryName=Service%20logs#/default/post_api_service_logs_v1_cluster_logs).
`CLUSTER_UUID` is a required parameter.

> :warning: Please review each template before post to make sure all the parameters are passed with -p 

> :books: If you are not sure which servicelog to sen, you can use the generic on [here](./osd/unknown_failure.json)

### Examples

Using [osdctl](https://github.com/openshift/osdctl)

1. Authenticate at https://cloud.redhat.com/openshift/token
1. Post servicelog

    ```
    osdctl servicelog post -t <notificationTemplateUrl> -p CLUSTER_UUID=<UUID>
    ```

    Example:

    ```
    osdctl servicelog post -t https://raw.githubusercontent.com/openshift/managed-notifications/master/osd/aws/InstallFailed_TooManyBuckets.json -p CLUSTER_UUID=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
    ```
