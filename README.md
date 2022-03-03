# Managed-notifications

Notification templates for OpenShift Managed services

## Usage

Select the corresponding message and send it as a `POST` to
[api.openshift.com servicelog](https://api.openshift.com/?urls.primaryName=Service%20logs#/default/post_api_service_logs_v1_cluster_logs).

> :warning: Please review each template before post to make sure all the parameters are passed with -p 

> :books: If you are not sure which servicelog to send, you can use the generic one [here](./osd/unknown_failure.json)

> :information_source: Upgrade your osdctl installation to 0.9.0 or higher. 
### Examples

Using [osdctl](https://github.com/openshift/osdctl)

1. Authenticate at https://cloud.redhat.com/openshift/token
2. Post servicelog

    ```
    osdctl servicelog post <cluster UUID> -t <notificationTemplateUrl> 
    ```

    Example:

    ```
    osdctl servicelog post aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee -t https://raw.githubusercontent.com/openshift/managed-notifications/master/osd/aws/InstallFailed_TooManyBuckets.json
    ```

Note: `Osdctl` supports the usage of the unique cluster name, or the internal- and external ID as clusterID.
