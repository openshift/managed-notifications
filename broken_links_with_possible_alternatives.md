# Broken Links Report with Suggested Alternatives

**Generated:** 2026-10-23
**Total broken links:** 59
**Method:** URL fragments and path components were analyzed to infer topic, then searched against docs.redhat.com via web search engines. For missing anchors, pages were fetched and scanned for similar anchor IDs using string similarity matching.

---

## HTTP Errors (403 / 404)

### https://access.redhat.com/articles/7104155

- **Status:** 403
- **Topic:** SDN to OVN network migration knowledge article
- **Affected files:**
  - `osd/sdn_to_ovn_migration_investigation.json`

**Suggested alternatives:**

1. https://access.redhat.com/articles/7083046
2. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/ovn-kubernetes_network_plugin/migrate-from-openshift-sdn-osd
3. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/ovn-kubernetes_network_plugin/migrate-from-openshift-sdn


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/ovn-kubernetes_network_plugin/migrate-from-openshift-sdn
---

### https://access.redhat.com/solutions/5622051

- **Status:** 403
- **Topic:** PodSecurityPolicy conflicts and SCC migration
- **Affected files:**
  - `osd/PodSecurityPolicy_conflict.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/authentication_and_authorization/managing-pod-security-policies
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/authentication_and_authorization/managing-pod-security-policies

**Remarks:**

We can leave it as is
---

### https://aws.amazon.com/premiumsupport/knowledge-center/s3-resolve-503-slowdown-throttling/

- **Status:** 403 (redirects to repost.aws but returns 403)
- **Topic:** AWS S3 503 SlowDown / request rate throttling
- **Affected files:**
  - `osd/aws/InstallFailed_BucketRequestRateTooHigh.json`

**Suggested alternatives:**

1. https://repost.aws/knowledge-center/http-5xx-errors-s3
2. https://repost.aws/knowledge-center/s3-503-within-request-rate-prefix

**Remarks:**
Replace with: https://repost.aws/knowledge-center/http-5xx-errors-s3
---

### https://docs.openshift.com/container-platform/4.11/storage/understanding-persistent-storage.html#pvc-storage-class_understanding-persistent-storage

- **Status:** 404
- **Topic:** Persistent storage — PVC storage classes
- **Affected files:**
  - `osd/MultipleDefaultStorageClasses.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/understanding-persistent-storage
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.11/html/storage/understanding-persistent-storage

**Remarks:**
Replace this with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/storage/understanding-persistent-storage#storage-persistent-storage-pvc_understanding-persistent-storage

---

### https://docs.openshift.com/container-platform/4.14/cicd/builds/basic-build-operations.html#builds-basic-access-build-logs_basic-build-operations

- **Status:** 404
- **Topic:** Build operations — accessing build logs
- **Affected files:**
  - `osd/StuckNewBuilds3MinSRE.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.14/html/builds_using_buildconfig/basic-build-operations
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/builds_using_buildconfig/basic-build-operations

**Remarks:**
Replace this with : https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/builds_using_buildconfig/basic-build-operations#builds-basic-access-build-logs_basic-build-operations
---

### https://docs.openshift.com/container-platform/4.14/openshift_images/managing_images/using-image-pull-secrets.html#images-update-global-pull-secret_using-image-pull-secrets

- **Status:** 404
- **Topic:** Updating the global image pull secret
- **Affected files:**
  - `osd/pull_secret_user_mismatch.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/images/managing-images
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/images/managing-images

**Remarks:**
Replace this with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/managing-images#images-update-global-pull-secret_using-image-pull-secrets
---

### https://docs.openshift.com/container-platform/4.14/storage/expanding-persistent-volumes.html

- **Status:** 404
- **Topic:** Expanding persistent volumes
- **Affected files:**
  - `osd/KubePersistentVolumeFillingUpError-user.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/expanding-persistent-volumes
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.14/html/storage/expanding-persistent-volumes

**Remarks:**
Replace this with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/storage/expanding-persistent-volumes
---

### https://docs.openshift.com/container-platform/4.15/logging/log_storage/cluster-logging-loki.html

- **Status:** 404
- **Topic:** Cluster logging with Loki log storage
- **Affected files:**
  - `osd/rosa_clusterlogging_loki.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_logging/6.5/html/installing_logging/installing-the-loki-operator
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html/logging/log-storage

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html/logging/log-storage#installing-log-storage-loki
---

### https://docs.openshift.com/container-platform/4.16/networking/ovn_kubernetes_network_provider/migrate-from-openshift-sdn.html#removing-egress-router-pods-before-initiating-limited-live-migration_migrate-from-openshift-sdn

- **Status:** 404
- **Topic:** OVN-Kubernetes migration — removing egress router pods before migration
- **Affected files:**
  - `osd/NetworkMigrationBlocked.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/ovn-kubernetes_network_plugin/migrate-from-openshift-sdn-osd
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/networking/ovn-kubernetes-network-plugin
3. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/ovn-kubernetes_network_plugin/migrate-from-openshift-sdn

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/networking/ovn-kubernetes-network-plugin#nw-ovn-kubernetes-live-migration-about_migrate-from-openshift-sdn
---

### https://docs.openshift.com/container-platform/latest/cicd/builds/understanding-image-builds.html

- **Status:** 404
- **Topic:** Understanding image builds
- **Affected files:**
  - `osd/StuckNewBuilds3MinSRE.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/builds_using_buildconfig/understanding-image-builds
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.12/html-single/builds/index

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/builds_using_buildconfig/understanding-image-builds
---

### https://docs.openshift.com/container-platform/latest/cicd/pipelines/reducing-pipelines-resource-consumption.html

- **Status:** 404
- **Topic:** Reducing OpenShift Pipelines resource consumption
- **Affected files:**
  - `osd/pipelines_resource_problem.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_pipelines/latest/html/building_pipelines/reducing-pipelines-resource-consumption
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/cicd/pipelines


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_pipelines/1.24/html/managing_performance_and_resource_use/reducing-pipelines-resource-consumption
---

### https://docs.openshift.com/container-platform/latest/installing/installing_aws/installation-config-parameters-aws.html#installation-configuration-parameters-optional-aws_installation-config-parameters-aws

- **Status:** 404
- **Topic:** AWS installation configuration parameters (optional settings)
- **Affected files:**
  - `osd/aws/InstallFailed_InvalidSubnet.json`
  - `osd/aws/InstallFailed_STS_PrivateLink.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/installing_on_aws/installation-config-parameters-aws
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/prepare_your_environment/rosa-sts-required-aws-service-quotas


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/installing_on_aws/installation-config-parameters-aws#installation-configuration-parameters-optional-aws_installation-config-parameters-aws
---

### https://docs.openshift.com/container-platform/latest/installing/installing_aws/installing-aws-account.html#installation-aws-limits_installing-aws-account

- **Status:** 404
- **Topic:** AWS account installation — service limits and quotas
- **Affected files:**
  - `osd/aws/VPCLimitExceeded.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/installing_on_aws/installing-aws-account
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/prepare_your_environment/rosa-sts-required-aws-service-quotas


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-sts-required-aws-service-quotas
---

### https://docs.openshift.com/container-platform/latest/networking/configuring-a-custom-pki.html

- **Status:** 404
- **Topic:** Configuring a custom PKI (certificate bundle)
- **Affected files:**
  - `osd/user-ca-bundle_invalid.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/configuring_network_settings/configuring-a-custom-pki
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/networking/configuring-a-custom-pki


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/configuring_network_settings/configuring-a-custom-pki
---

### https://docs.openshift.com/container-platform/latest/nodes/clusters/nodes-cluster-limit-ranges.html

- **Status:** 404
- **Topic:** Cluster node limit ranges and resource quotas
- **Affected files:**
  - `osd/workernode_overloaded.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/scalability_and_performance/compute-resource-quotas
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/nodes/using-pods


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/scalability_and_performance/compute-resource-quotas
---

### https://docs.openshift.com/container-platform/latest/openshift_images/managing_images/using-image-pull-secrets.html#images-update-global-pull-secret_using-image-pull-secrets

- **Status:** 404
- **Topic:** Updating the global image pull secret
- **Affected files:**
  - `osd/update_pull_secret.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/images/managing-images
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/images/managing-images


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/managing-images#images-update-global-pull-secret_using-image-pull-secrets
---

### https://docs.openshift.com/container-platform/latest/storage/expanding-persistent-volumes.html

- **Status:** 404
- **Topic:** Expanding persistent volumes
- **Affected files:**
  - `osd/KubePersistentVolumeFillingUpError-user.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/expanding-persistent-volumes


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/storage/expanding-persistent-volumes
---

### https://docs.openshift.com/container-platform/latest/storage/understanding-ephemeral-storage.html

- **Status:** 404
- **Topic:** Understanding ephemeral storage
- **Affected files:**
  - `osd/customer_emptydir_storage_preventing_drain.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/understanding-ephemeral-storage


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/storage/understanding-ephemeral-storage
---

### https://docs.openshift.com/container-platform/latest/updating/preparing_for_updates/updating-cluster-prepare.html#kube-api-removals_updating-cluster-prepare

- **Status:** 404
- **Topic:** Cluster update preparation — Kubernetes API removals
- **Affected files:**
  - `osd/upgrade_paused_acknowledgement.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/updating_clusters/preparing-to-update-a-cluster
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/updating_clusters/preparing-to-update-a-cluster


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/updating_clusters/preparing-to-update-a-cluster#kube-api-removals_updating-cluster-prepare
---

### https://docs.openshift.com/dedicated/applications/deployments/osd-config-custom-domains-applications.html

- **Status:** 404
- **Topic:** Configuring custom domains for OSD applications
- **Affected files:**
  - `osd/rosa_cert_signed_by_unknown_authority.json`
  - `osd/rosa_invalid_tls_cert.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/building_applications/deployments#rosa-config-custom-domains-applications
2. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/building_applications/deployments


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/building_applications/deployments#rosa-config-custom-domains-applications
---

### https://docs.openshift.com/dedicated/authentication/managing-security-context-constraints.html#role-based-access-to-ssc_configuring-internal-oauth

- **Status:** 404
- **Topic:** Role-based access to Security Context Constraints (SCC)
- **Affected files:**
  - `osd/bad_scc_priority.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/authentication_and_authorization/managing-security-context-constraints
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/authentication_and_authorization/managing-pod-security-policies


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/authentication_and_authorization/managing-pod-security-policies
---

### https://docs.openshift.com/dedicated/nodes/pods/nodes-pods-configuring.html

- **Status:** 404
- **Topic:** Configuring pods on OSD — pod disruption budgets
- **Affected files:**
  - `osd/customer_pdb_preventing_drain_automated.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/nodes/working-with-pods
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/nodes/working-with-pods


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/nodes/working-with-pods
---

### https://docs.openshift.com/dedicated/nodes/rosa-managing-worker-nodes.html

- **Status:** 404
- **Topic:** Managing worker nodes on OSD — machine pools
- **Affected files:**
  - `osd/cluster_overloaded.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/cluster_administration/managing-compute-nodes-using-machine-pools
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/cluster_administration/managing-compute-nodes-using-machine-pools


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/cluster_administration/managing-compute-nodes-using-machine-pools
---

### https://docs.openshift.com/dedicated/osd_architecture/osd_policy/osd-service-definition.html#gcp-compute-types_osd-service-definition

- **Status:** 404
- **Topic:** OSD service definition — GCP compute instance types
- **Affected files:**
  - `osd/gcp/unable_to_create_machine_invalid_type.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/introduction_to_openshift_dedicated/policies-and-service-definition
2. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/planning_your_environment/gcp-ccs


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/introduction_to_openshift_dedicated/policies-and-service-definition#gcp-compute-types_osd-service-definition
---

### https://docs.openshift.com/dedicated/osd_architecture/osd_policy/policy-responsibility-matrix.html

- **Status:** 404
- **Topic:** OSD shared responsibility matrix
- **Affected files:**
  - `osd/customer_stopped_control_plane_node.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/introduction_to_openshift_dedicated/policies-and-service-definition
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/introduction_to_openshift_dedicated/policies-and-service-definition#policy-responsibilities_policy-responsibility-matrix
---

### https://docs.openshift.com/dedicated/osd_gcp_clusters/creating-a-gcp-cluster-with-workload-identity-federation.html#wif-configuration-update_osd-creating-a-cluster-on-gcp-with-workload-identity-federation

- **Status:** 404
- **Topic:** GCP Workload Identity Federation (WIF) configuration update
- **Affected files:**
  - `osd/gcp/GCP_WIF_invalid_support_role.json`
  - `osd/gcp/GPC_WIF_update_configuration.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/openshift_dedicated_clusters_on_google_cloud/osd-creating-a-cluster-on-gcp-with-workload-identity-federation
2. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/planning_your_environment/gcp-ccs


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/openshift_dedicated_clusters_on_google_cloud/osd-creating-a-cluster-on-gcp-with-workload-identity-federation#wif-configuration-update_osd-creating-a-cluster-on-gcp-with-workload-identity-federation
---

### https://docs.openshift.com/dedicated/osd_planning/gcp-ccs.html#ccs-gcp-customer-requirements_gcp-ccs

- **Status:** 404
- **Topic:** GCP Customer Cloud Subscription (CCS) requirements
- **Affected files:**
  - `osd/gcp/InstallFailed_QuotaExceeded.json`
  - `osd/gcp/invalid_iaas_credentials.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/planning_your_environment/gcp-ccs
2. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/openshift_dedicated_clusters_on_google_cloud/osd-creating-a-cluster-on-gcp-with-workload-identity-federation


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/planning_your_environment/gcp-ccs#ccs-gcp-customer-requirements_gcp-ccs
---

### https://docs.openshift.com/dedicated/osd_planning/osd-limits-scalability.html#node-scaling-after-installation_osd-limits-scalability

- **Status:** 404
- **Topic:** OSD limits and scalability — node scaling after installation
- **Affected files:**
  - `osd/gcp/GCP_infranode_resized_auto.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/cluster_administration/managing-compute-nodes-using-machine-pools
2. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/planning_your_environment/limits-and-scalability


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/planning_your_environment/osd-limits-scalability#node-scaling-after-installation_osd-limits-scalability
---

### https://docs.openshift.com/dedicated/osd_policy/osd-life-cycle.html#rosa-life-cycle-dates_osd-life-cycle)

- **Status:** 404
- **Topic:** OSD life cycle dates (note: URL has a trailing `)` character — likely a typo in the template)
- **Affected files:**
  - `osd/DockerCIDROverlap45Install.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/introduction_to_openshift_dedicated/policies-and-service-definition
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#sd-life-cycle-dates_rosa-hcp-life-cycle


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#sd-life-cycle-dates_rosa-hcp-life-cycle
---

### https://docs.openshift.com/dedicated/osd_quickstart/osd-quickstart.html#deleting-cluster_osd-getting-started

- **Status:** 404
- **Topic:** OSD quickstart — deleting a cluster
- **Affected files:**
  - `osd/cluster_cannot_be_recovered.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/installing_accessing_and_deleting_openshift_dedicated_clusters/creating-your-cluster
2. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/getting_started/osd-quickstart

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/getting_started/osd-getting-started#deleting-cluster_osd-getting-started
---

### https://docs.openshift.com/pipelines/latest/resource/reducing-pipelines-resource-consumption.html

- **Status:** 404
- **Topic:** Reducing OpenShift Pipelines resource consumption
- **Affected files:**
  - `osd/pipelines_resource_problem.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_pipelines/latest/html/building_pipelines/reducing-pipelines-resource-consumption

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_pipelines/latest/html/managing_performance_and_resource_use/reducing-pipelines-resource-consumption
---

### https://docs.openshift.com/rosa/architecture/admission-plug-ins.html

- **Status:** 404
- **Topic:** Admission plug-ins (webhooks, validating/mutating)
- **Affected files:**
  - `hcp/webhook_blocking_nodepool_update.json`
  - `osd/webhooks_impacting_cluster_stability.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/architecture/admission-plug-ins
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/architecture/admission-plug-ins

**Remarks:**
- For `hcp/webhook_blocking_nodepool_update.json`, replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/architecture/admission-plug-ins
- For `osd/webhooks_impacting_cluster_stability.json`, replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/architecture/admission-plug-ins
---

### https://docs.openshift.com/rosa/cloud_experts_tutorials/cloud-experts-update-component-routes.html

- **Status:** 404
- **Topic:** Cloud experts tutorial — updating component routes (custom domains)
- **Affected files:**
  - `osd/invalid_ingress_component_route.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/tutorials/cloud-experts-update-component-routes
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/tutorials/cloud-experts-update-component-routes

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/tutorials/cloud-experts-update-component-routes
---

### https://docs.openshift.com/rosa/networking/networking_operators/ingress-operator.html#nw-create-custom-ingress-controller_configuring-ingress

- **Status:** 404
- **Topic:** Creating custom ingress controllers on ROSA
- **Affected files:**
  - `osd/custom_ingress_controller_misconfiguration.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/networking/configuring-ingress-cluster-traffic
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/networking/configuring-ingress-cluster-traffic

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/networking_operators/configuring-ingress#nw-create-custom-ingress-controller_configuring-ingress
---

### https://docs.openshift.com/rosa/nodes/clusters/nodes-cluster-limit-ranges.html

- **Status:** 404
- **Topic:** Cluster node limit ranges and resource quotas on ROSA
- **Affected files:**
  - `osd/no_resources_to_run_userworkloadmonitoring.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/scalability_and_performance/compute-resource-quotas
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/nodes/using-pods


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/nodes/working-with-clusters#nodes-cluster-limit-ranges
---

### https://docs.openshift.com/rosa/openshift_images/image-configuration.html

- **Status:** 404
- **Topic:** Image configuration and registry policies on ROSA
- **Affected files:**
  - `osd/invalid_registry_policy.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/images/image-configuration
2. https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/images/image-configuration

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/images/image-configuration-classic
---

### https://docs.openshift.com/rosa/rosa_architecture/rosa_policy_service_definition/rosa-policy-responsibility-matrix.html

- **Status:** 404
- **Topic:** ROSA shared responsibility matrix
- **Affected files:**
  - `osd/customer_stopped_control_plane_node_rosa.json`
  - `osd/customer_stopped_infra_node.json`
  - `osd/customer_stopped_infra_node_rosa.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/introduction_to_rosa/policies-and-service-definition


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/introduction_to_rosa/policies-and-service-definition#rosa-policy-responsibilities_rosa-policy-responsibility-matrix
---

### https://docs.openshift.com/rosa/rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.html

- **Status:** 404
- **Topic:** Managing ROSA worker nodes — machine pools
- **Affected files:**
  - `osd/BadMachineConfigPool.json`
  - `osd/unable_to_create_machine_invalid_type.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/cluster_administration/managing-compute-nodes-using-machine-pools
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/cluster_administration/managing-compute-nodes-using-machine-pools

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/cluster_administration/managing-compute-nodes-using-machine-pools
---

### https://docs.openshift.com/rosa/rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.html#rosa-scaling-worker-nodes_rosa-managing-worker-nodes

- **Status:** 404
- **Topic:** Scaling ROSA worker nodes
- **Affected files:**
  - `hcp/ip_range_is_full.json`
  - `hcp/node_ip_range_is_full.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/cluster_administration/managing-compute-nodes-using-machine-pools
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/cluster_administration/managing-compute-nodes-using-machine-pools


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/cluster_administration/managing-compute-nodes-using-machine-pools#rosa-scaling-worker-nodes_rosa-managing-worker-nodes
---

### https://docs.openshift.com/rosa/rosa_planning/rosa-aws-prereqs.html#rosa-policy-iam_prerequisites

- **Status:** 404
- **Topic:** ROSA AWS prerequisites — IAM policy requirements
- **Affected files:**
  - `osd/RosaInstallationFailedOnInvalidIamRoles.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/prepare_your_environment/rosa-sts-aws-prereqs
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-sts-aws-prereqs

**Remarks:**
Replace with https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/prepare_your_environment/rosa-hcp-prereqs
---

### https://docs.openshift.com/rosa/rosa_planning/rosa-limits-scalability.html

- **Status:** 404
- **Topic:** ROSA limits and scalability
- **Affected files:**
  - `osd/PodNetworkCIDRExhaustion.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/prepare_your_environment/rosa-planning-environment
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-planning-environment

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/prepare_your_environment/rosa-planning-environment
---

### https://docs.openshift.com/rosa/rosa_planning/rosa-planning-environment.html

- **Status:** 404
- **Topic:** ROSA planning environment — prerequisites and configuration
- **Affected files:**
  - `osd/workernode_overloaded_pid_limit_rosa.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/prepare_your_environment/rosa-planning-environment
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-planning-environment


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/prepare_your_environment/rosa-planning-environment
---

## Missing Anchors

The page loads successfully but the anchor (fragment identifier) no longer exists on the page. The documentation may have been reorganized, renaming sections and their corresponding anchor IDs.

### https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/authentication_and_authorization/overview-of-authentication-authorization#authentication-overview

- **Missing anchor:** `#authentication-overview`
- **Redirects to:** https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/authentication_and_authorization/overview-of-authentication-authorization
- **Topic:** ROSA authentication overview
- **Affected files:**
  - `osd/Failed_Logins.json`

**Suggested alternatives (updated anchors):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/authentication_and_authorization/overview-of-authentication-authorization#authentication-overview_overview-of-authentication-authorization
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/authentication_and_authorization/overview-of-authentication-authorization#overview-of-authentication-authorization

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/authentication_and_authorization/overview-of-authentication-authorization
---

### https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/building_applications/deployments#osd-applications-renew-custom-domains_osd-config-custom-domains-applications

- **Missing anchor:** `#osd-applications-renew-custom-domains_osd-config-custom-domains-applications`
- **Redirects to:** https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/building_applications/deployments
- **Topic:** Renewing custom domain certificates
- **Affected files:**
  - `osd/custom_domain_cert_misconfiguration.json`

**Suggested alternatives (updated anchors — "osd" prefix renamed to "rosa"):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/building_applications/deployments#rosa-applications-config-custom-domains_rosa-config-custom-domains-applications
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/building_applications/deployments#rosa-config-custom-domains-applications


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/building_applications/deployments#rosa-applications-renew-custom-domains_rosa-config-custom-domains-applications
---

### https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/building_applications/deployments#osd-config-custom-domains-applications

- **Missing anchor:** `#osd-config-custom-domains-applications`
- **Redirects to:** https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/building_applications/deployments
- **Topic:** Configuring custom domains for applications
- **Affected files:**
  - `osd/auth_operator_cert_expired.json`
  - `osd/custom_domain_misconfiguration.json`
  - `osd/rosa_cert_signed_by_unknown_authority.json`
  - `osd/rosa_invalid_tls_cert.json`

**Suggested alternatives (updated anchor — "osd" prefix renamed to "rosa"):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/building_applications/deployments#rosa-config-custom-domains-applications


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/building_applications/deployments#rosa-config-custom-domains-applications
---

### https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#rosa-limited-support_rosa-life-cycle

- **Missing anchor:** `#rosa-limited-support_rosa-life-cycle`
- **Redirects to:** https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition
- **Topic:** ROSA limited support policy — life cycle
- **Affected files:**
  - `osd/limited_support/EOLClusterStillSupported.json`
  - `osd/limited_support/EOLExtension.json`
  - `osd/limited_support/LimitedSupportCloud.json`
  - `osd/limited_support/LimitedSupportCluster.json`

**Suggested alternatives (anchor suffix changed from "rosa-life-cycle" to "rosa-hcp-life-cycle"):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#rosa-limited-support_rosa-hcp-life-cycle

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#rosa-limited-support_rosa-hcp-life-cycle
---

### https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#rosa-sdpolicy-instance-types_rosa-service-definition

- **Missing anchor:** `#rosa-sdpolicy-instance-types_rosa-service-definition`
- **Redirects to:** https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition
- **Topic:** ROSA service definition — supported instance types
- **Affected files:**
  - `osd/unsupported_workload.json`

**Suggested alternatives (anchor suffix changed from "rosa-service-definition" to "rosa-hcp-service-definition"):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#rosa-sdpolicy-instance-types_rosa-hcp-service-definition


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/introduction_to_rosa/policies-and-service-definition#rosa-instance-types
---

### https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#sd-life-cycle-dates_rosa-life-cycle

- **Missing anchor:** `#sd-life-cycle-dates_rosa-life-cycle`
- **Redirects to:** https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition
- **Topic:** ROSA life cycle dates
- **Affected files:**
  - `osd/DockerCIDROverlap45Install.json`
  - `osd/eol_date_extended.json`

**Suggested alternatives (anchor suffix changed from "rosa-life-cycle" to "rosa-hcp-life-cycle"):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#sd-life-cycle-dates_rosa-hcp-life-cycle

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#sd-life-cycle-dates_rosa-hcp-life-cycle
---

### https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/monitoring/managing-alerts#expiring-silences_managing-alerts

- **Missing anchor:** `#expiring-silences_managing-alerts`
- **Redirects to:** https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/monitoring/managing-alerts
- **Topic:** Managing alert silences — expiring silences
- **Affected files:**
  - `osd/aws/AlertmanagerSilencesActiveSRE.json`

**Suggested alternatives (anchor split into role-specific variants):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/monitoring/managing-alerts#expiring-silences_managing-alerts-as-an-administrator
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/monitoring/managing-alerts#expiring-silences_managing-alerts-as-a-developer

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/monitoring/managing-alerts#expiring-silences_managing-alerts-as-a-developer
---

### https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/nodes/working-with-pods#nodes-pods-pod-distruption-about_nodes-pods-configuring

- **Missing anchor:** `#nodes-pods-pod-distruption-about_nodes-pods-configuring`
- **Redirects to:** https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/nodes/working-with-pods
- **Topic:** Pod disruption budgets (note: original anchor has typo "distruption" → "disruption")
- **Affected files:**
  - `osd/customer_pdb_preventing_drain.json`
  - `osd/customer_pdb_preventing_drain_automated.json`
  - `osd/customer_pod_preventing_drain.json`
  - `osd/customer_pods_preventing_drain_automated.json`
  - `osd/incorrect_PodDisruptionBudget.json`
  - `osd/rosa_customer_pdb_preventing_drain.json`

**Suggested alternatives (typo corrected in anchor):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/nodes/working-with-pods#nodes-pods-pod-disruption-about_nodes-pods-configuring

**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/nodes/working-with-pods#nodes-pods-pod-disruption-about_nodes-pods-configuring
---

### https://access.redhat.com/support/cases/#/case/$

- **Missing anchor:** `#/case/$`
- **Topic:** Support case portal (dynamic SPA URL — `$` is a placeholder for case ID)
- **Affected files:**
  - `osd/generic_customer_support_case_notification.json`

**Suggested alternatives:**

1. https://access.redhat.com/support/cases/


**Remarks:**
We can leave it as is
---

### https://console.redhat.com/openshift/downloads#tool-pull-secret

- **Missing anchor:** `#tool-pull-secret`
- **Topic:** OpenShift downloads page — pull secret tool (Single Page App; anchor handled by JavaScript)
- **Affected files:**
  - `osd/pull_secret_rotated.json`

**Suggested alternatives:**

1. https://console.redhat.com/openshift/downloads

**Remarks:**
Replace with: https://console.redhat.com/openshift/install/pull-secret
---

### https://docs.redhat.com/en/documentation/openshift_dedicated/4/html-single/planning_your_environment/index#aws-ccs-networking-prereqs_aws-ccs

- **Missing anchor:** `#aws-ccs-networking-prereqs_aws-ccs`
- **Topic:** AWS CCS networking prerequisites
- **Affected files:**
  - `osd/NetworkMisconfiguration_WithDoc.json`

**Suggested alternatives (anchor renamed):**

1. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html-single/planning_your_environment/index#network-prereqs_aws-ccs
2. https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/planning_your_environment/aws-ccs


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/openshift_dedicated/4/html-single/planning_your_environment/index#network-prereqs_aws-ccs
---

### https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/support/troubleshooting#sd-managed-resources-overview_sd-managed-resources

- **Missing anchor:** `#sd-managed-resources-overview_sd-managed-resources`
- **Topic:** Managed resources overview for ROSA support/troubleshooting
- **Affected files:**
  - `osd/Non_Red_Hat_Access_Core_Secrets.json`
  - `osd/Non_System_Change_SRE_API_Endpoint.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/support/troubleshooting
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/support/troubleshooting#sd-managed-resources
---

### https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html-single/cluster_administration/index#machine-pools

- **Missing anchor:** `#machine-pools`
- **Topic:** ROSA Classic cluster administration — machine pools
- **Affected files:**
  - `osd/cluster_overloaded.json`
  - `osd/pipelines_resource_problem.json`

**Suggested alternatives (anchor renamed):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html-single/cluster_administration/index#managing-compute-nodes-using-machine-pools
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/cluster_administration/managing-compute-nodes-using-machine-pools


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html-single/cluster_administration/index#managing-compute-nodes-using-machine-pools
---

### https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html-single/prepare_your_environment/index#firewalls

- **Missing anchor:** `#firewalls`
- **Topic:** ROSA Classic environment preparation — firewall requirements
- **Affected files:**
  - `osd/aws/InstallFailed_PrivateLink_Firewall.json`
  - `osd/limited_support/egressFailureLimitedSupport.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-sts-aws-prereqs
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-cloud-expert-prereq-checklist


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-sts-aws-prereqs#rosa-classic-firewall-prerequisites_rosa-sts-aws-prereqs
---

### https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/introduction_to_rosa/rosa-sts-about-iam-resources#rosa-sts-oidc-provider-requirements-for-operators_rosa-sts-about-iam-resources

- **Missing anchor:** `#rosa-sts-oidc-provider-requirements-for-operators_rosa-sts-about-iam-resources`
- **Topic:** ROSA STS OIDC provider requirements for operators
- **Affected files:**
  - `osd/aws/sts_thumbprint.json`

**Suggested alternatives (anchor keyword changed from "provider-requirements" to "requirements"):**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/introduction_to_rosa/rosa-sts-about-iam-resources#rosa-sts-oidc-requirements-for-operators_rosa-sts-about-iam-resources


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/introduction_to_rosa/rosa-sts-about-iam-resources#rosa-sts-oidc-requirements-for-operators_rosa-sts-about-iam-resources
---

### https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/monitoring/getting-started#sd-accessing-monitoring-for-user-defined-projects

- **Missing anchor:** `#sd-accessing-monitoring-for-user-defined-projects`
- **Topic:** Accessing monitoring for user-defined projects
- **Affected files:**
  - `osd/silence_namespace_alerts_notice.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/monitoring/getting-started
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html-single/monitoring/index


**Remarks:**
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/monitoring/configuring-user-workload-monitoring
---

### https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-cloud-expert-prereq-checklist#firewall

- **Missing anchor:** `#firewall`
- **Topic:** ROSA Classic prerequisite checklist — firewall configuration
- **Affected files:**
  - `osd/required_network_egresses_are_blocked.json`

**Suggested alternatives:**

1. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-cloud-expert-prereq-checklist
2. https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-sts-aws-prereqs


**Remarks:**
The following looks to be the likeliest match of the pre-requisites after the documentaions were restructured. We may need to confirm with the documentation team about this section.
Replace with: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-sts-aws-prereqs#rosa-classic-firewall-prerequisites_rosa-sts-aws-prereqs
---

## Summary

| Metric | Count |
|--------|-------|
| Total broken links | 59 |
| HTTP 403 errors | 4 |
| HTTP 404 errors (docs.openshift.com) | 39 |
| Missing anchors | 16 |
| Links with suggested alternatives | 59 |
