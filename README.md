# Managed-notifications

Notification templates for OpenShift Managed services

## Usage

Select the corresponding message and send it as a `POST` to
[api.openshift.com servicelog](https://api.openshift.com/?urls.primaryName=Service%20logs#/default/post_api_service_logs_v1_cluster_logs).

> :warning: Please review each template before post to make sure all the parameters are passed with -p 

> :books: If you are not sure which servicelog to send, you can use the generic one [here](./osd/unknown_failure.json)

### Examples

Using [osdctl](https://github.com/openshift/osdctl)

1. Upgrade your osdctl installation to 0.8.0 or higher. 
2. Authenticate at https://cloud.redhat.com/openshift/token
3. Post servicelog

    ```
    osdctl servicelog post <clusterID> -t <notificationTemplateUrl> 
    ```

    Example:

    ```
    osdctl servicelog post aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee -t https://raw.githubusercontent.com/openshift/managed-notifications/master/osd/aws/InstallFailed_TooManyBuckets.json
    ```

Note: `Osdctl` supports the usage of the unique cluster name, or the internal- and external ID as clusterID.
