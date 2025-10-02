# openapi_client.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurm_v0038_cancel_job**](SlurmApi.md#slurm_v0038_cancel_job) | **DELETE** /slurm/v0.0.38/job/{job_id} | cancel or signal job
[**slurm_v0038_diag**](SlurmApi.md#slurm_v0038_diag) | **GET** /slurm/v0.0.38/diag | get diagnostics
[**slurm_v0038_get_job**](SlurmApi.md#slurm_v0038_get_job) | **GET** /slurm/v0.0.38/job/{job_id} | get job info
[**slurm_v0038_get_jobs**](SlurmApi.md#slurm_v0038_get_jobs) | **GET** /slurm/v0.0.38/jobs | get list of jobs
[**slurm_v0038_get_node**](SlurmApi.md#slurm_v0038_get_node) | **GET** /slurm/v0.0.38/node/{node_name} | get node info
[**slurm_v0038_get_nodes**](SlurmApi.md#slurm_v0038_get_nodes) | **GET** /slurm/v0.0.38/nodes | get all node info
[**slurm_v0038_get_partition**](SlurmApi.md#slurm_v0038_get_partition) | **GET** /slurm/v0.0.38/partition/{partition_name} | get partition info
[**slurm_v0038_get_partitions**](SlurmApi.md#slurm_v0038_get_partitions) | **GET** /slurm/v0.0.38/partitions | get all partition info
[**slurm_v0038_get_reservation**](SlurmApi.md#slurm_v0038_get_reservation) | **GET** /slurm/v0.0.38/reservation/{reservation_name} | get reservation info
[**slurm_v0038_get_reservations**](SlurmApi.md#slurm_v0038_get_reservations) | **GET** /slurm/v0.0.38/reservations | get all reservation info
[**slurm_v0038_ping**](SlurmApi.md#slurm_v0038_ping) | **GET** /slurm/v0.0.38/ping | ping test
[**slurm_v0038_slurmctld_get_licenses**](SlurmApi.md#slurm_v0038_slurmctld_get_licenses) | **GET** /slurm/v0.0.38/licenses | get all Slurm tracked license info
[**slurm_v0038_submit_job**](SlurmApi.md#slurm_v0038_submit_job) | **POST** /slurm/v0.0.38/job/submit | submit new job
[**slurm_v0038_update_job**](SlurmApi.md#slurm_v0038_update_job) | **POST** /slurm/v0.0.38/job/{job_id} | update job
[**slurm_v0039_cancel_job**](SlurmApi.md#slurm_v0039_cancel_job) | **DELETE** /slurm/v0.0.39/job/{job_id} | cancel or signal job
[**slurm_v0039_delete_node**](SlurmApi.md#slurm_v0039_delete_node) | **DELETE** /slurm/v0.0.39/node/{node_name} | delete node
[**slurm_v0039_diag**](SlurmApi.md#slurm_v0039_diag) | **GET** /slurm/v0.0.39/diag | get diagnostics
[**slurm_v0039_get_job**](SlurmApi.md#slurm_v0039_get_job) | **GET** /slurm/v0.0.39/job/{job_id} | get job info
[**slurm_v0039_get_jobs**](SlurmApi.md#slurm_v0039_get_jobs) | **GET** /slurm/v0.0.39/jobs | get list of jobs
[**slurm_v0039_get_node**](SlurmApi.md#slurm_v0039_get_node) | **GET** /slurm/v0.0.39/node/{node_name} | get node info
[**slurm_v0039_get_nodes**](SlurmApi.md#slurm_v0039_get_nodes) | **GET** /slurm/v0.0.39/nodes | get all node info
[**slurm_v0039_get_partition**](SlurmApi.md#slurm_v0039_get_partition) | **GET** /slurm/v0.0.39/partition/{partition_name} | get partition info
[**slurm_v0039_get_partitions**](SlurmApi.md#slurm_v0039_get_partitions) | **GET** /slurm/v0.0.39/partitions | get all partition info
[**slurm_v0039_get_reservation**](SlurmApi.md#slurm_v0039_get_reservation) | **GET** /slurm/v0.0.39/reservation/{reservation_name} | get reservation info
[**slurm_v0039_get_reservations**](SlurmApi.md#slurm_v0039_get_reservations) | **GET** /slurm/v0.0.39/reservations | get all reservation info
[**slurm_v0039_ping**](SlurmApi.md#slurm_v0039_ping) | **GET** /slurm/v0.0.39/ping | ping test
[**slurm_v0039_slurmctld_get_licenses**](SlurmApi.md#slurm_v0039_slurmctld_get_licenses) | **GET** /slurm/v0.0.39/licenses | get all Slurm tracked license info
[**slurm_v0039_submit_job**](SlurmApi.md#slurm_v0039_submit_job) | **POST** /slurm/v0.0.39/job/submit | submit new job
[**slurm_v0039_update_job**](SlurmApi.md#slurm_v0039_update_job) | **POST** /slurm/v0.0.39/job/{job_id} | update job
[**slurm_v0039_update_node**](SlurmApi.md#slurm_v0039_update_node) | **POST** /slurm/v0.0.39/node/{node_name} | update node properties
[**slurm_v0040_delete_job**](SlurmApi.md#slurm_v0040_delete_job) | **DELETE** /slurm/v0.0.40/job/{job_id} | cancel or signal job
[**slurm_v0040_delete_node**](SlurmApi.md#slurm_v0040_delete_node) | **DELETE** /slurm/v0.0.40/node/{node_name} | delete node
[**slurm_v0040_get_diag**](SlurmApi.md#slurm_v0040_get_diag) | **GET** /slurm/v0.0.40/diag | get diagnostics
[**slurm_v0040_get_job**](SlurmApi.md#slurm_v0040_get_job) | **GET** /slurm/v0.0.40/job/{job_id} | get job info
[**slurm_v0040_get_jobs**](SlurmApi.md#slurm_v0040_get_jobs) | **GET** /slurm/v0.0.40/jobs | get list of jobs
[**slurm_v0040_get_licenses**](SlurmApi.md#slurm_v0040_get_licenses) | **GET** /slurm/v0.0.40/licenses | get all Slurm tracked license info
[**slurm_v0040_get_node**](SlurmApi.md#slurm_v0040_get_node) | **GET** /slurm/v0.0.40/node/{node_name} | get node info
[**slurm_v0040_get_nodes**](SlurmApi.md#slurm_v0040_get_nodes) | **GET** /slurm/v0.0.40/nodes | get all node info
[**slurm_v0040_get_partition**](SlurmApi.md#slurm_v0040_get_partition) | **GET** /slurm/v0.0.40/partition/{partition_name} | get partition info
[**slurm_v0040_get_partitions**](SlurmApi.md#slurm_v0040_get_partitions) | **GET** /slurm/v0.0.40/partitions | get all partition info
[**slurm_v0040_get_ping**](SlurmApi.md#slurm_v0040_get_ping) | **GET** /slurm/v0.0.40/ping | ping test
[**slurm_v0040_get_reconfigure**](SlurmApi.md#slurm_v0040_get_reconfigure) | **GET** /slurm/v0.0.40/reconfigure | request slurmctld reconfigure
[**slurm_v0040_get_reservation**](SlurmApi.md#slurm_v0040_get_reservation) | **GET** /slurm/v0.0.40/reservation/{reservation_name} | get reservation info
[**slurm_v0040_get_reservations**](SlurmApi.md#slurm_v0040_get_reservations) | **GET** /slurm/v0.0.40/reservations | get all reservation info
[**slurm_v0040_get_shares**](SlurmApi.md#slurm_v0040_get_shares) | **GET** /slurm/v0.0.40/shares | get fairshare info
[**slurm_v0040_post_job**](SlurmApi.md#slurm_v0040_post_job) | **POST** /slurm/v0.0.40/job/{job_id} | update job
[**slurm_v0040_post_job_submit**](SlurmApi.md#slurm_v0040_post_job_submit) | **POST** /slurm/v0.0.40/job/submit | submit new job
[**slurm_v0040_post_node**](SlurmApi.md#slurm_v0040_post_node) | **POST** /slurm/v0.0.40/node/{node_name} | update node properties
[**slurmdb_v0038_add_clusters**](SlurmApi.md#slurmdb_v0038_add_clusters) | **POST** /slurmdb/v0.0.38/clusters | Add clusters
[**slurmdb_v0038_add_wckeys**](SlurmApi.md#slurmdb_v0038_add_wckeys) | **POST** /slurmdb/v0.0.38/wckeys | Add wckeys
[**slurmdb_v0038_delete_account**](SlurmApi.md#slurmdb_v0038_delete_account) | **DELETE** /slurmdb/v0.0.38/account/{account_name} | Delete account
[**slurmdb_v0038_delete_association**](SlurmApi.md#slurmdb_v0038_delete_association) | **DELETE** /slurmdb/v0.0.38/association | Delete association
[**slurmdb_v0038_delete_associations**](SlurmApi.md#slurmdb_v0038_delete_associations) | **DELETE** /slurmdb/v0.0.38/associations | Delete associations
[**slurmdb_v0038_delete_cluster**](SlurmApi.md#slurmdb_v0038_delete_cluster) | **DELETE** /slurmdb/v0.0.38/cluster/{cluster_name} | Delete cluster
[**slurmdb_v0038_delete_qos**](SlurmApi.md#slurmdb_v0038_delete_qos) | **DELETE** /slurmdb/v0.0.38/qos/{qos_name} | Delete QOS
[**slurmdb_v0038_delete_user**](SlurmApi.md#slurmdb_v0038_delete_user) | **DELETE** /slurmdb/v0.0.38/user/{user_name} | Delete user
[**slurmdb_v0038_delete_wckey**](SlurmApi.md#slurmdb_v0038_delete_wckey) | **DELETE** /slurmdb/v0.0.38/wckey/{wckey} | Delete wckey
[**slurmdb_v0038_diag**](SlurmApi.md#slurmdb_v0038_diag) | **GET** /slurmdb/v0.0.38/diag | Get slurmdb diagnostics
[**slurmdb_v0038_get_account**](SlurmApi.md#slurmdb_v0038_get_account) | **GET** /slurmdb/v0.0.38/account/{account_name} | Get account info
[**slurmdb_v0038_get_accounts**](SlurmApi.md#slurmdb_v0038_get_accounts) | **GET** /slurmdb/v0.0.38/accounts | Get account list
[**slurmdb_v0038_get_association**](SlurmApi.md#slurmdb_v0038_get_association) | **GET** /slurmdb/v0.0.38/association | Get association info
[**slurmdb_v0038_get_associations**](SlurmApi.md#slurmdb_v0038_get_associations) | **GET** /slurmdb/v0.0.38/associations | Get association list
[**slurmdb_v0038_get_cluster**](SlurmApi.md#slurmdb_v0038_get_cluster) | **GET** /slurmdb/v0.0.38/cluster/{cluster_name} | Get cluster info
[**slurmdb_v0038_get_clusters**](SlurmApi.md#slurmdb_v0038_get_clusters) | **GET** /slurmdb/v0.0.38/clusters | Get cluster list
[**slurmdb_v0038_get_config**](SlurmApi.md#slurmdb_v0038_get_config) | **GET** /slurmdb/v0.0.38/config | Dump all configuration information
[**slurmdb_v0038_get_job**](SlurmApi.md#slurmdb_v0038_get_job) | **GET** /slurmdb/v0.0.38/job/{job_id} | Get job info
[**slurmdb_v0038_get_jobs**](SlurmApi.md#slurmdb_v0038_get_jobs) | **GET** /slurmdb/v0.0.38/jobs | Get job list
[**slurmdb_v0038_get_qos**](SlurmApi.md#slurmdb_v0038_get_qos) | **GET** /slurmdb/v0.0.38/qos | Get QOS list
[**slurmdb_v0038_get_single_qos**](SlurmApi.md#slurmdb_v0038_get_single_qos) | **GET** /slurmdb/v0.0.38/qos/{qos_name} | Get QOS info
[**slurmdb_v0038_get_tres**](SlurmApi.md#slurmdb_v0038_get_tres) | **GET** /slurmdb/v0.0.38/tres | Get TRES info
[**slurmdb_v0038_get_user**](SlurmApi.md#slurmdb_v0038_get_user) | **GET** /slurmdb/v0.0.38/user/{user_name} | Get user info
[**slurmdb_v0038_get_users**](SlurmApi.md#slurmdb_v0038_get_users) | **GET** /slurmdb/v0.0.38/users | Get user list
[**slurmdb_v0038_get_wckey**](SlurmApi.md#slurmdb_v0038_get_wckey) | **GET** /slurmdb/v0.0.38/wckey/{wckey} | Get wckey info
[**slurmdb_v0038_get_wckeys**](SlurmApi.md#slurmdb_v0038_get_wckeys) | **GET** /slurmdb/v0.0.38/wckeys | Get wckey list
[**slurmdb_v0038_set_config**](SlurmApi.md#slurmdb_v0038_set_config) | **POST** /slurmdb/v0.0.38/config | Load all configuration information
[**slurmdb_v0038_update_account**](SlurmApi.md#slurmdb_v0038_update_account) | **POST** /slurmdb/v0.0.38/accounts | Update accounts
[**slurmdb_v0038_update_associations**](SlurmApi.md#slurmdb_v0038_update_associations) | **POST** /slurmdb/v0.0.38/associations | Set associations info
[**slurmdb_v0038_update_qos**](SlurmApi.md#slurmdb_v0038_update_qos) | **POST** /slurmdb/v0.0.38/qos | Set QOS info
[**slurmdb_v0038_update_tres**](SlurmApi.md#slurmdb_v0038_update_tres) | **POST** /slurmdb/v0.0.38/tres | Set TRES info
[**slurmdb_v0038_update_users**](SlurmApi.md#slurmdb_v0038_update_users) | **POST** /slurmdb/v0.0.38/users | Update user
[**slurmdb_v0039_add_clusters**](SlurmApi.md#slurmdb_v0039_add_clusters) | **POST** /slurmdb/v0.0.39/clusters | Add clusters
[**slurmdb_v0039_add_wckeys**](SlurmApi.md#slurmdb_v0039_add_wckeys) | **POST** /slurmdb/v0.0.39/wckeys | Add wckeys
[**slurmdb_v0039_delete_account**](SlurmApi.md#slurmdb_v0039_delete_account) | **DELETE** /slurmdb/v0.0.39/account/{account_name} | Delete account
[**slurmdb_v0039_delete_association**](SlurmApi.md#slurmdb_v0039_delete_association) | **DELETE** /slurmdb/v0.0.39/association | Delete association
[**slurmdb_v0039_delete_associations**](SlurmApi.md#slurmdb_v0039_delete_associations) | **DELETE** /slurmdb/v0.0.39/associations | Delete associations
[**slurmdb_v0039_delete_cluster**](SlurmApi.md#slurmdb_v0039_delete_cluster) | **DELETE** /slurmdb/v0.0.39/cluster/{cluster_name} | Delete cluster
[**slurmdb_v0039_delete_qos**](SlurmApi.md#slurmdb_v0039_delete_qos) | **DELETE** /slurmdb/v0.0.39/qos/{qos_name} | Delete QOS
[**slurmdb_v0039_delete_user**](SlurmApi.md#slurmdb_v0039_delete_user) | **DELETE** /slurmdb/v0.0.39/user/{user_name} | Delete user
[**slurmdb_v0039_delete_wckey**](SlurmApi.md#slurmdb_v0039_delete_wckey) | **DELETE** /slurmdb/v0.0.39/wckey/{wckey} | Delete wckey
[**slurmdb_v0039_diag**](SlurmApi.md#slurmdb_v0039_diag) | **GET** /slurmdb/v0.0.39/diag | Get slurmdb diagnostics
[**slurmdb_v0039_get_account**](SlurmApi.md#slurmdb_v0039_get_account) | **GET** /slurmdb/v0.0.39/account/{account_name} | Get account info
[**slurmdb_v0039_get_accounts**](SlurmApi.md#slurmdb_v0039_get_accounts) | **GET** /slurmdb/v0.0.39/accounts | Get account list
[**slurmdb_v0039_get_association**](SlurmApi.md#slurmdb_v0039_get_association) | **GET** /slurmdb/v0.0.39/association | Get association info
[**slurmdb_v0039_get_associations**](SlurmApi.md#slurmdb_v0039_get_associations) | **GET** /slurmdb/v0.0.39/associations | Get association list
[**slurmdb_v0039_get_cluster**](SlurmApi.md#slurmdb_v0039_get_cluster) | **GET** /slurmdb/v0.0.39/cluster/{cluster_name} | Get cluster info
[**slurmdb_v0039_get_clusters**](SlurmApi.md#slurmdb_v0039_get_clusters) | **GET** /slurmdb/v0.0.39/clusters | Get cluster list
[**slurmdb_v0039_get_config**](SlurmApi.md#slurmdb_v0039_get_config) | **GET** /slurmdb/v0.0.39/config | Dump all configuration information
[**slurmdb_v0039_get_job**](SlurmApi.md#slurmdb_v0039_get_job) | **GET** /slurmdb/v0.0.39/job/{job_id} | Get job info
[**slurmdb_v0039_get_jobs**](SlurmApi.md#slurmdb_v0039_get_jobs) | **GET** /slurmdb/v0.0.39/jobs | Get job list
[**slurmdb_v0039_get_qos**](SlurmApi.md#slurmdb_v0039_get_qos) | **GET** /slurmdb/v0.0.39/qos | Get QOS list
[**slurmdb_v0039_get_single_qos**](SlurmApi.md#slurmdb_v0039_get_single_qos) | **GET** /slurmdb/v0.0.39/qos/{qos_name} | Get QOS info
[**slurmdb_v0039_get_tres**](SlurmApi.md#slurmdb_v0039_get_tres) | **GET** /slurmdb/v0.0.39/tres | Get TRES info
[**slurmdb_v0039_get_user**](SlurmApi.md#slurmdb_v0039_get_user) | **GET** /slurmdb/v0.0.39/user/{user_name} | Get user info
[**slurmdb_v0039_get_users**](SlurmApi.md#slurmdb_v0039_get_users) | **GET** /slurmdb/v0.0.39/users | Get user list
[**slurmdb_v0039_get_wckey**](SlurmApi.md#slurmdb_v0039_get_wckey) | **GET** /slurmdb/v0.0.39/wckey/{wckey} | Get wckey info
[**slurmdb_v0039_get_wckeys**](SlurmApi.md#slurmdb_v0039_get_wckeys) | **GET** /slurmdb/v0.0.39/wckeys | Get wckey list
[**slurmdb_v0039_set_config**](SlurmApi.md#slurmdb_v0039_set_config) | **POST** /slurmdb/v0.0.39/config | Load all configuration information
[**slurmdb_v0039_update_accounts**](SlurmApi.md#slurmdb_v0039_update_accounts) | **POST** /slurmdb/v0.0.39/accounts | Update accounts
[**slurmdb_v0039_update_associations**](SlurmApi.md#slurmdb_v0039_update_associations) | **POST** /slurmdb/v0.0.39/associations | Set associations info
[**slurmdb_v0039_update_qos**](SlurmApi.md#slurmdb_v0039_update_qos) | **POST** /slurmdb/v0.0.39/qos | Set QOS info
[**slurmdb_v0039_update_tres**](SlurmApi.md#slurmdb_v0039_update_tres) | **POST** /slurmdb/v0.0.39/tres | Set TRES info
[**slurmdb_v0039_update_users**](SlurmApi.md#slurmdb_v0039_update_users) | **POST** /slurmdb/v0.0.39/users | Update user


# **slurm_v0038_cancel_job**
> slurm_v0038_cancel_job(job_id, signal=signal)

cancel or signal job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_signal import V0038Signal
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm Job ID
    signal = openapi_client.V0038Signal() # V0038Signal | signal to send to job (optional)

    try:
        # cancel or signal job
        api_instance.slurm_v0038_cancel_job(job_id, signal=signal)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_cancel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Slurm Job ID | 
 **signal** | [**V0038Signal**](.md)| signal to send to job | [optional] 

### Return type

void (empty response body)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job cancelled or sent signal |  -  |
**500** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_diag**
> V0038Diag slurm_v0038_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_diag import V0038Diag
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get diagnostics
        api_response = api_instance.slurm_v0038_diag()
        print("The response of SlurmApi->slurm_v0038_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0038Diag**](V0038Diag.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_job**
> V0038JobsResponse slurm_v0038_get_job(job_id)

get job info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_jobs_response import V0038JobsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm JobID

    try:
        # get job info
        api_response = api_instance.slurm_v0038_get_job(job_id)
        print("The response of SlurmApi->slurm_v0038_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Slurm JobID | 

### Return type

[**V0038JobsResponse**](V0038JobsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job matching JobId not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_jobs**
> V0038JobsResponse slurm_v0038_get_jobs(update_time=update_time)

get list of jobs

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_jobs_response import V0038JobsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0038_get_jobs(update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0038JobsResponse**](V0038JobsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_node**
> V0038NodesResponse slurm_v0038_get_node(node_name)

get node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_nodes_response import V0038NodesResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Slurm Node Name

    try:
        # get node info
        api_response = api_instance.slurm_v0038_get_node(node_name)
        print("The response of SlurmApi->slurm_v0038_get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Slurm Node Name | 

### Return type

[**V0038NodesResponse**](V0038NodesResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_nodes**
> V0038NodesResponse slurm_v0038_get_nodes(update_time=update_time)

get all node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_nodes_response import V0038NodesResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all node info
        api_response = api_instance.slurm_v0038_get_nodes(update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0038NodesResponse**](V0038NodesResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | no nodes in cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_partition**
> V0038PartitionsResponse slurm_v0038_get_partition(partition_name, update_time=update_time)

get partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_partitions_response import V0038PartitionsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Slurm Partition Name
    update_time = 56 # int | Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. (optional)

    try:
        # get partition info
        api_response = api_instance.slurm_v0038_get_partition(partition_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_partition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Slurm Partition Name | 
 **update_time** | **int**| Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. | [optional] 

### Return type

[**V0038PartitionsResponse**](V0038PartitionsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_partitions**
> V0038PartitionsResponse slurm_v0038_get_partitions(update_time=update_time)

get all partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_partitions_response import V0038PartitionsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all partition info
        api_response = api_instance.slurm_v0038_get_partitions(update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_partitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_partitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0038PartitionsResponse**](V0038PartitionsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_reservation**
> V0038ReservationsResponse slurm_v0038_get_reservation(reservation_name, update_time=update_time)

get reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_reservations_response import V0038ReservationsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Slurm Reservation Name
    update_time = 56 # int | Filter if no reservation (not limited to reservation in URL) changed since update_time. (optional)

    try:
        # get reservation info
        api_response = api_instance.slurm_v0038_get_reservation(reservation_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Slurm Reservation Name | 
 **update_time** | **int**| Filter if no reservation (not limited to reservation in URL) changed since update_time. | [optional] 

### Return type

[**V0038ReservationsResponse**](V0038ReservationsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_reservations**
> V0038ReservationsResponse slurm_v0038_get_reservations(update_time=update_time)

get all reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_reservations_response import V0038ReservationsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all reservation info
        api_response = api_instance.slurm_v0038_get_reservations(update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0038ReservationsResponse**](V0038ReservationsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_ping**
> V0038Pings slurm_v0038_ping()

ping test

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_pings import V0038Pings
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # ping test
        api_response = api_instance.slurm_v0038_ping()
        print("The response of SlurmApi->slurm_v0038_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0038Pings**](V0038Pings.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_slurmctld_get_licenses**
> V0038Licenses slurm_v0038_slurmctld_get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_licenses import V0038Licenses
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0038_slurmctld_get_licenses()
        print("The response of SlurmApi->slurm_v0038_slurmctld_get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_slurmctld_get_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0038Licenses**](V0038Licenses.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of get all licenses |  -  |
**0** | unable to request licenses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_submit_job**
> V0038JobSubmissionResponse slurm_v0038_submit_job(v0038_job_submission)

submit new job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_job_submission import V0038JobSubmission
from openapi_client.models.v0038_job_submission_response import V0038JobSubmissionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    v0038_job_submission = openapi_client.V0038JobSubmission() # V0038JobSubmission | submit new job

    try:
        # submit new job
        api_response = api_instance.slurm_v0038_submit_job(v0038_job_submission)
        print("The response of SlurmApi->slurm_v0038_submit_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_submit_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0038_job_submission** | [**V0038JobSubmission**](V0038JobSubmission.md)| submit new job | 

### Return type

[**V0038JobSubmissionResponse**](V0038JobSubmissionResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submitted |  -  |
**0** | job rejected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_update_job**
> slurm_v0038_update_job(job_id, v0038_job_properties)

update job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_job_properties import V0038JobProperties
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm Job ID
    v0038_job_properties = openapi_client.V0038JobProperties() # V0038JobProperties | update job

    try:
        # update job
        api_instance.slurm_v0038_update_job(job_id, v0038_job_properties)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_update_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Slurm Job ID | 
 **v0038_job_properties** | [**V0038JobProperties**](V0038JobProperties.md)| update job | 

### Return type

void (empty response body)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job information |  -  |
**500** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_cancel_job**
> Status slurm_v0039_cancel_job(job_id, signal=signal)

cancel or signal job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm Job ID
    signal = 'signal_example' # str | signal to send to job (optional)

    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0039_cancel_job(job_id, signal=signal)
        print("The response of SlurmApi->slurm_v0039_cancel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_cancel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Slurm Job ID | 
 **signal** | **str**| signal to send to job | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job cancelled or sent signal |  -  |
**0** | Job cancel request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_delete_node**
> Status slurm_v0039_delete_node(node_name)

delete node

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Slurm Node Name

    try:
        # delete node
        api_response = api_instance.slurm_v0039_delete_node(node_name)
        print("The response of SlurmApi->slurm_v0039_delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Slurm Node Name | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node deleted |  -  |
**0** | node delete request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_diag**
> V0039Diag slurm_v0039_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_diag import V0039Diag
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get diagnostics
        api_response = api_instance.slurm_v0039_diag()
        print("The response of SlurmApi->slurm_v0039_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0039Diag**](V0039Diag.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_get_job**
> V0039JobsResponse slurm_v0039_get_job(job_id)

get job info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_jobs_response import V0039JobsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm JobID

    try:
        # get job info
        api_response = api_instance.slurm_v0039_get_job(job_id)
        print("The response of SlurmApi->slurm_v0039_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Slurm JobID | 

### Return type

[**V0039JobsResponse**](V0039JobsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job matching JobId not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_get_jobs**
> V0039JobsResponse slurm_v0039_get_jobs(update_time=update_time)

get list of jobs

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_jobs_response import V0039JobsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0039_get_jobs(update_time=update_time)
        print("The response of SlurmApi->slurm_v0039_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0039JobsResponse**](V0039JobsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_get_node**
> V0039NodesResponse slurm_v0039_get_node(node_name)

get node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_nodes_response import V0039NodesResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Slurm Node Name

    try:
        # get node info
        api_response = api_instance.slurm_v0039_get_node(node_name)
        print("The response of SlurmApi->slurm_v0039_get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Slurm Node Name | 

### Return type

[**V0039NodesResponse**](V0039NodesResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_get_nodes**
> V0039NodesResponse slurm_v0039_get_nodes(update_time=update_time)

get all node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_nodes_response import V0039NodesResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all node info
        api_response = api_instance.slurm_v0039_get_nodes(update_time=update_time)
        print("The response of SlurmApi->slurm_v0039_get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0039NodesResponse**](V0039NodesResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | no nodes in cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_get_partition**
> V0039PartitionsResponse slurm_v0039_get_partition(partition_name, update_time=update_time)

get partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_partitions_response import V0039PartitionsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Slurm Partition Name
    update_time = 56 # int | Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. (optional)

    try:
        # get partition info
        api_response = api_instance.slurm_v0039_get_partition(partition_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0039_get_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_partition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Slurm Partition Name | 
 **update_time** | **int**| Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. | [optional] 

### Return type

[**V0039PartitionsResponse**](V0039PartitionsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_get_partitions**
> V0039PartitionsResponse slurm_v0039_get_partitions(update_time=update_time)

get all partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_partitions_response import V0039PartitionsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all partition info
        api_response = api_instance.slurm_v0039_get_partitions(update_time=update_time)
        print("The response of SlurmApi->slurm_v0039_get_partitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_partitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0039PartitionsResponse**](V0039PartitionsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_get_reservation**
> V0039ReservationsResponse slurm_v0039_get_reservation(reservation_name, update_time=update_time)

get reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_reservations_response import V0039ReservationsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Slurm Reservation Name
    update_time = 56 # int | Filter if no reservation (not limited to reservation in URL) changed since update_time. (optional)

    try:
        # get reservation info
        api_response = api_instance.slurm_v0039_get_reservation(reservation_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0039_get_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Slurm Reservation Name | 
 **update_time** | **int**| Filter if no reservation (not limited to reservation in URL) changed since update_time. | [optional] 

### Return type

[**V0039ReservationsResponse**](V0039ReservationsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_get_reservations**
> V0039ReservationsResponse slurm_v0039_get_reservations(update_time=update_time)

get all reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_reservations_response import V0039ReservationsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all reservation info
        api_response = api_instance.slurm_v0039_get_reservations(update_time=update_time)
        print("The response of SlurmApi->slurm_v0039_get_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0039ReservationsResponse**](V0039ReservationsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_ping**
> V0039Pings slurm_v0039_ping()

ping test

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_pings import V0039Pings
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # ping test
        api_response = api_instance.slurm_v0039_ping()
        print("The response of SlurmApi->slurm_v0039_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0039Pings**](V0039Pings.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_slurmctld_get_licenses**
> V0039LicensesInfo slurm_v0039_slurmctld_get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_licenses_info import V0039LicensesInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0039_slurmctld_get_licenses()
        print("The response of SlurmApi->slurm_v0039_slurmctld_get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_slurmctld_get_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0039LicensesInfo**](V0039LicensesInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of get all licenses |  -  |
**0** | unable to request licenses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_submit_job**
> V0039JobSubmissionResponse slurm_v0039_submit_job(v0039_job_submission)

submit new job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_job_submission import V0039JobSubmission
from openapi_client.models.v0039_job_submission_response import V0039JobSubmissionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    v0039_job_submission = openapi_client.V0039JobSubmission() # V0039JobSubmission | submit new job

    try:
        # submit new job
        api_response = api_instance.slurm_v0039_submit_job(v0039_job_submission)
        print("The response of SlurmApi->slurm_v0039_submit_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_submit_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0039_job_submission** | [**V0039JobSubmission**](V0039JobSubmission.md)| submit new job | 

### Return type

[**V0039JobSubmissionResponse**](V0039JobSubmissionResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submitted |  -  |
**0** | job rejected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_update_job**
> V0039JobUpdateResponse slurm_v0039_update_job(job_id, v0039_job_desc_msg)

update job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0039_job_desc_msg import V0039JobDescMsg
from openapi_client.models.v0039_job_update_response import V0039JobUpdateResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm Job ID
    v0039_job_desc_msg = openapi_client.V0039JobDescMsg() # V0039JobDescMsg | update job

    try:
        # update job
        api_response = api_instance.slurm_v0039_update_job(job_id, v0039_job_desc_msg)
        print("The response of SlurmApi->slurm_v0039_update_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_update_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Slurm Job ID | 
 **v0039_job_desc_msg** | [**V0039JobDescMsg**](V0039JobDescMsg.md)| update job | 

### Return type

[**V0039JobUpdateResponse**](V0039JobUpdateResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job updated |  -  |
**0** | job update failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0039_update_node**
> Status slurm_v0039_update_node(node_name, v0039_update_node_msg)

update node properties

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.status import Status
from openapi_client.models.v0039_update_node_msg import V0039UpdateNodeMsg
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Slurm Node Name
    v0039_update_node_msg = openapi_client.V0039UpdateNodeMsg() # V0039UpdateNodeMsg | update node

    try:
        # update node properties
        api_response = api_instance.slurm_v0039_update_node(node_name, v0039_update_node_msg)
        print("The response of SlurmApi->slurm_v0039_update_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_update_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Slurm Node Name | 
 **v0039_update_node_msg** | [**V0039UpdateNodeMsg**](V0039UpdateNodeMsg.md)| update node | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node update failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_delete_job**
> V0040OpenapiResp slurm_v0040_delete_job(job_id, signal=signal, flags=flags)

cancel or signal job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | JobId
    signal = 'signal_example' # str | Signal to send to Job (optional)
    flags = 'flags_example' # str | Signalling flags (optional)

    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0040_delete_job(job_id, signal=signal, flags=flags)
        print("The response of SlurmApi->slurm_v0040_delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| JobId | 
 **signal** | **str**| Signal to send to Job | [optional] 
 **flags** | **str**| Signalling flags | [optional] 

### Return type

[**V0040OpenapiResp**](V0040OpenapiResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job cancelled or sent signal |  -  |
**0** | Job cancel request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_delete_node**
> V0040OpenapiResp slurm_v0040_delete_node(node_name)

delete node

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name

    try:
        # delete node
        api_response = api_instance.slurm_v0040_delete_node(node_name)
        print("The response of SlurmApi->slurm_v0040_delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 

### Return type

[**V0040OpenapiResp**](V0040OpenapiResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node deleted |  -  |
**0** | node delete request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_diag**
> V0040OpenapiDiagResp slurm_v0040_get_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_diag_resp import V0040OpenapiDiagResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get diagnostics
        api_response = api_instance.slurm_v0040_get_diag()
        print("The response of SlurmApi->slurm_v0040_get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0040OpenapiDiagResp**](V0040OpenapiDiagResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | unable to request diagnostics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_job**
> V0040OpenapiJobInfoResp slurm_v0040_get_job(job_id, update_time=update_time, flags=flags)

get job info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_job_info_resp import V0040OpenapiJobInfoResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | JobId
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get job info
        api_response = api_instance.slurm_v0040_get_job(job_id, update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0040_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| JobId | 
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiJobInfoResp**](V0040OpenapiJobInfoResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job matching JobId not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_jobs**
> V0040OpenapiJobInfoResp slurm_v0040_get_jobs(update_time=update_time, flags=flags)

get list of jobs

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_job_info_resp import V0040OpenapiJobInfoResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0040_get_jobs(update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0040_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiJobInfoResp**](V0040OpenapiJobInfoResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_licenses**
> V0040OpenapiLicensesResp slurm_v0040_get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_licenses_resp import V0040OpenapiLicensesResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0040_get_licenses()
        print("The response of SlurmApi->slurm_v0040_get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0040OpenapiLicensesResp**](V0040OpenapiLicensesResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of get all licenses |  -  |
**0** | unable to request licenses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_node**
> V0040OpenapiNodesResp slurm_v0040_get_node(node_name, update_time=update_time, flags=flags)

get node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_nodes_resp import V0040OpenapiNodesResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node info
        api_response = api_instance.slurm_v0040_get_node(node_name, update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0040_get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiNodesResp**](V0040OpenapiNodesResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_nodes**
> V0040OpenapiNodesResp slurm_v0040_get_nodes(update_time=update_time, flags=flags)

get all node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_nodes_resp import V0040OpenapiNodesResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get all node info
        api_response = api_instance.slurm_v0040_get_nodes(update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0040_get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiNodesResp**](V0040OpenapiNodesResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | no nodes in cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_partition**
> V0040OpenapiPartitionResp slurm_v0040_get_partition(partition_name, update_time=update_time)

get partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_partition_resp import V0040OpenapiPartitionResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Slurm Partition Name
    update_time = 56 # int | Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. (optional)

    try:
        # get partition info
        api_response = api_instance.slurm_v0040_get_partition(partition_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0040_get_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_partition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Slurm Partition Name | 
 **update_time** | **int**| Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. | [optional] 

### Return type

[**V0040OpenapiPartitionResp**](V0040OpenapiPartitionResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_partitions**
> V0040OpenapiPartitionResp slurm_v0040_get_partitions(update_time=update_time)

get all partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_partition_resp import V0040OpenapiPartitionResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all partition info
        api_response = api_instance.slurm_v0040_get_partitions(update_time=update_time)
        print("The response of SlurmApi->slurm_v0040_get_partitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_partitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0040OpenapiPartitionResp**](V0040OpenapiPartitionResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_ping**
> V0040OpenapiPingArrayResp slurm_v0040_get_ping()

ping test

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_ping_array_resp import V0040OpenapiPingArrayResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # ping test
        api_response = api_instance.slurm_v0040_get_ping()
        print("The response of SlurmApi->slurm_v0040_get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0040OpenapiPingArrayResp**](V0040OpenapiPingArrayResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_reconfigure**
> V0040OpenapiResp slurm_v0040_get_reconfigure()

request slurmctld reconfigure

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # request slurmctld reconfigure
        api_response = api_instance.slurm_v0040_get_reconfigure()
        print("The response of SlurmApi->slurm_v0040_get_reconfigure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reconfigure: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0040OpenapiResp**](V0040OpenapiResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reconfigure requested successfully |  -  |
**0** | reconfigure requested failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_reservation**
> V0040OpenapiReservationResp slurm_v0040_get_reservation(reservation_name, update_time=update_time)

get reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_reservation_resp import V0040OpenapiReservationResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Slurm Reservation Name
    update_time = 56 # int | Filter if no reservation (not limited to reservation in URL) changed since update_time. (optional)

    try:
        # get reservation info
        api_response = api_instance.slurm_v0040_get_reservation(reservation_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0040_get_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Slurm Reservation Name | 
 **update_time** | **int**| Filter if no reservation (not limited to reservation in URL) changed since update_time. | [optional] 

### Return type

[**V0040OpenapiReservationResp**](V0040OpenapiReservationResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_reservations**
> V0040OpenapiReservationResp slurm_v0040_get_reservations(update_time=update_time)

get all reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_reservation_resp import V0040OpenapiReservationResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all reservation info
        api_response = api_instance.slurm_v0040_get_reservations(update_time=update_time)
        print("The response of SlurmApi->slurm_v0040_get_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0040OpenapiReservationResp**](V0040OpenapiReservationResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_shares**
> V0040OpenapiSharesResp slurm_v0040_get_shares(accounts=accounts, users=users)

get fairshare info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_shares_resp import V0040OpenapiSharesResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    accounts = 'accounts_example' # str | Accounts to query (optional)
    users = 'users_example' # str | Users to query (optional)

    try:
        # get fairshare info
        api_response = api_instance.slurm_v0040_get_shares(accounts=accounts, users=users)
        print("The response of SlurmApi->slurm_v0040_get_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounts** | **str**| Accounts to query | [optional] 
 **users** | **str**| Users to query | [optional] 

### Return type

[**V0040OpenapiSharesResp**](V0040OpenapiSharesResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shares information |  -  |
**0** | unable to query shares |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_post_job**
> V0040OpenapiJobPostResponse slurm_v0040_post_job(job_id, v0040_job_desc_msg)

update job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_job_desc_msg import V0040JobDescMsg
from openapi_client.models.v0040_openapi_job_post_response import V0040OpenapiJobPostResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | JobId
    v0040_job_desc_msg = openapi_client.V0040JobDescMsg() # V0040JobDescMsg | update job

    try:
        # update job
        api_response = api_instance.slurm_v0040_post_job(job_id, v0040_job_desc_msg)
        print("The response of SlurmApi->slurm_v0040_post_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| JobId | 
 **v0040_job_desc_msg** | [**V0040JobDescMsg**](V0040JobDescMsg.md)| update job | 

### Return type

[**V0040OpenapiJobPostResponse**](V0040OpenapiJobPostResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job updated |  -  |
**0** | job update failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_post_job_submit**
> V0040OpenapiJobSubmitResponse slurm_v0040_post_job_submit(v0040_job_submit_req)

submit new job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_job_submit_req import V0040JobSubmitReq
from openapi_client.models.v0040_openapi_job_submit_response import V0040OpenapiJobSubmitResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    v0040_job_submit_req = openapi_client.V0040JobSubmitReq() # V0040JobSubmitReq | submit new job

    try:
        # submit new job
        api_response = api_instance.slurm_v0040_post_job_submit(v0040_job_submit_req)
        print("The response of SlurmApi->slurm_v0040_post_job_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_job_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_job_submit_req** | [**V0040JobSubmitReq**](V0040JobSubmitReq.md)| submit new job | 

### Return type

[**V0040OpenapiJobSubmitResponse**](V0040OpenapiJobSubmitResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submitted |  -  |
**0** | job rejected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_post_node**
> V0040OpenapiResp slurm_v0040_post_node(node_name, v0040_update_node_msg)

update node properties

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.models.v0040_update_node_msg import V0040UpdateNodeMsg
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    v0040_update_node_msg = openapi_client.V0040UpdateNodeMsg() # V0040UpdateNodeMsg | update node

    try:
        # update node properties
        api_response = api_instance.slurm_v0040_post_node(node_name, v0040_update_node_msg)
        print("The response of SlurmApi->slurm_v0040_post_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **v0040_update_node_msg** | [**V0040UpdateNodeMsg**](V0040UpdateNodeMsg.md)| update node | 

### Return type

[**V0040OpenapiResp**](V0040OpenapiResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node update failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_add_clusters**
> Dbv0038ResponseClusterAdd slurmdb_v0038_add_clusters(dbv0038_clusters_properties)

Add clusters

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_clusters_properties import Dbv0038ClustersProperties
from openapi_client.models.dbv0038_response_cluster_add import Dbv0038ResponseClusterAdd
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0038_clusters_properties = openapi_client.Dbv0038ClustersProperties() # Dbv0038ClustersProperties | Add or update clusters

    try:
        # Add clusters
        api_response = api_instance.slurmdb_v0038_add_clusters(dbv0038_clusters_properties)
        print("The response of SlurmApi->slurmdb_v0038_add_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_add_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0038_clusters_properties** | [**Dbv0038ClustersProperties**](Dbv0038ClustersProperties.md)| Add or update clusters | 

### Return type

[**Dbv0038ResponseClusterAdd**](Dbv0038ResponseClusterAdd.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Unable to add cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_add_wckeys**
> Dbv0038ResponseWckeyAdd slurmdb_v0038_add_wckeys(dbv0038_wckey_info=dbv0038_wckey_info)

Add wckeys

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_wckey_add import Dbv0038ResponseWckeyAdd
from openapi_client.models.dbv0038_wckey_info import Dbv0038WckeyInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0038_wckey_info = openapi_client.Dbv0038WckeyInfo() # Dbv0038WckeyInfo | add wckeys (optional)

    try:
        # Add wckeys
        api_response = api_instance.slurmdb_v0038_add_wckeys(dbv0038_wckey_info=dbv0038_wckey_info)
        print("The response of SlurmApi->slurmdb_v0038_add_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_add_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0038_wckey_info** | [**Dbv0038WckeyInfo**](Dbv0038WckeyInfo.md)| add wckeys | [optional] 

### Return type

[**Dbv0038ResponseWckeyAdd**](Dbv0038ResponseWckeyAdd.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | Unable to add wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_delete_account**
> Dbv0038ResponseAccountDelete slurmdb_v0038_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_account_delete import Dbv0038ResponseAccountDelete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    account_name = 'account_name_example' # str | Slurm Account Name

    try:
        # Delete account
        api_response = api_instance.slurmdb_v0038_delete_account(account_name)
        print("The response of SlurmApi->slurmdb_v0038_delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name | 

### Return type

[**Dbv0038ResponseAccountDelete**](Dbv0038ResponseAccountDelete.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete account |  -  |
**0** | Unable to delete account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_delete_association**
> Dbv0038ResponseAssociationsDelete slurmdb_v0038_delete_association(cluster=cluster, account=account, user=user, partition=partition)

Delete association

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_associations_delete import Dbv0038ResponseAssociationsDelete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    account = 'account_example' # str | Account name (optional)
    user = 'user_example' # str | User name (optional)
    partition = 'partition_example' # str | Partition Name (optional)

    try:
        # Delete association
        api_response = api_instance.slurmdb_v0038_delete_association(cluster=cluster, account=account, user=user, partition=partition)
        print("The response of SlurmApi->slurmdb_v0038_delete_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **account** | **str**| Account name | [optional] 
 **user** | **str**| User name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0038ResponseAssociationsDelete**](Dbv0038ResponseAssociationsDelete.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete associations |  -  |
**0** | Association not found or unable to delete association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_delete_associations**
> Dbv0038ResponseAssociationsDelete slurmdb_v0038_delete_associations(cluster=cluster, account=account, user=user, partition=partition)

Delete associations

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_associations_delete import Dbv0038ResponseAssociationsDelete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    account = 'account_example' # str | Account name (optional)
    user = 'user_example' # str | User name (optional)
    partition = 'partition_example' # str | Partition Name (optional)

    try:
        # Delete associations
        api_response = api_instance.slurmdb_v0038_delete_associations(cluster=cluster, account=account, user=user, partition=partition)
        print("The response of SlurmApi->slurmdb_v0038_delete_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **account** | **str**| Account name | [optional] 
 **user** | **str**| User name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0038ResponseAssociationsDelete**](Dbv0038ResponseAssociationsDelete.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete associations |  -  |
**0** | Associations not found or unable to delete association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_delete_cluster**
> Dbv0038ResponseClusterDelete slurmdb_v0038_delete_cluster(cluster_name)

Delete cluster

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_cluster_delete import Dbv0038ResponseClusterDelete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster_name = 'cluster_name_example' # str | Slurm cluster name

    try:
        # Delete cluster
        api_response = api_instance.slurmdb_v0038_delete_cluster(cluster_name)
        print("The response of SlurmApi->slurmdb_v0038_delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name | 

### Return type

[**Dbv0038ResponseClusterDelete**](Dbv0038ResponseClusterDelete.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete cluster |  -  |
**0** | Cluster not found or unable to delete cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_delete_qos**
> Dbv0038ResponseQosDelete slurmdb_v0038_delete_qos(qos_name)

Delete QOS

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_qos_delete import Dbv0038ResponseQosDelete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    qos_name = 'qos_name_example' # str | Slurm QOS Name

    try:
        # Delete QOS
        api_response = api_instance.slurmdb_v0038_delete_qos(qos_name)
        print("The response of SlurmApi->slurmdb_v0038_delete_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name | 

### Return type

[**Dbv0038ResponseQosDelete**](Dbv0038ResponseQosDelete.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete qos |  -  |
**0** | Unable to delete QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_delete_user**
> Dbv0038ResponseUserDelete slurmdb_v0038_delete_user(user_name)

Delete user

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_user_delete import Dbv0038ResponseUserDelete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    user_name = 'user_name_example' # str | Slurm User Name

    try:
        # Delete user
        api_response = api_instance.slurmdb_v0038_delete_user(user_name)
        print("The response of SlurmApi->slurmdb_v0038_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name | 

### Return type

[**Dbv0038ResponseUserDelete**](Dbv0038ResponseUserDelete.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete user |  -  |
**0** | User not found or unable to delete user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_delete_wckey**
> Dbv0038ResponseWckeyDelete slurmdb_v0038_delete_wckey(wckey)

Delete wckey

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_wckey_delete import Dbv0038ResponseWckeyDelete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    wckey = 'wckey_example' # str | Slurm wckey name

    try:
        # Delete wckey
        api_response = api_instance.slurmdb_v0038_delete_wckey(wckey)
        print("The response of SlurmApi->slurmdb_v0038_delete_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name | 

### Return type

[**Dbv0038ResponseWckeyDelete**](Dbv0038ResponseWckeyDelete.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete wckey |  -  |
**0** | wckey not found or unable to delete wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_diag**
> Dbv0038Diag slurmdb_v0038_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_diag import Dbv0038Diag
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdb_v0038_diag()
        print("The response of SlurmApi->slurmdb_v0038_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0038Diag**](Dbv0038Diag.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Unable to query diagnostics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_account**
> Dbv0038AccountInfo slurmdb_v0038_get_account(account_name, with_deleted=with_deleted)

Get account info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_account_info import Dbv0038AccountInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    account_name = 'account_name_example' # str | Slurm Account Name
    with_deleted = True # bool | Include deleted accounts. False by default. (optional)

    try:
        # Get account info
        api_response = api_instance.slurmdb_v0038_get_account(account_name, with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0038_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name | 
 **with_deleted** | **bool**| Include deleted accounts. False by default. | [optional] 

### Return type

[**Dbv0038AccountInfo**](Dbv0038AccountInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_accounts**
> Dbv0038AccountInfo slurmdb_v0038_get_accounts(with_deleted=with_deleted)

Get account list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_account_info import Dbv0038AccountInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    with_deleted = True # bool | Include deleted accounts. False by default. (optional)

    try:
        # Get account list
        api_response = api_instance.slurmdb_v0038_get_accounts(with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0038_get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_deleted** | **bool**| Include deleted accounts. False by default. | [optional] 

### Return type

[**Dbv0038AccountInfo**](Dbv0038AccountInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_association**
> Dbv0038AssociationsInfo slurmdb_v0038_get_association(cluster=cluster, account=account, user=user, partition=partition)

Get association info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_associations_info import Dbv0038AssociationsInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    account = 'account_example' # str | Account name (optional)
    user = 'user_example' # str | User name (optional)
    partition = 'partition_example' # str | Partition Name (optional)

    try:
        # Get association info
        api_response = api_instance.slurmdb_v0038_get_association(cluster=cluster, account=account, user=user, partition=partition)
        print("The response of SlurmApi->slurmdb_v0038_get_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **account** | **str**| Account name | [optional] 
 **user** | **str**| User name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0038AssociationsInfo**](Dbv0038AssociationsInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_associations**
> Dbv0038AssociationsInfo slurmdb_v0038_get_associations(cluster=cluster, account=account, user=user, partition=partition)

Get association list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_associations_info import Dbv0038AssociationsInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    account = 'account_example' # str | Account name (optional)
    user = 'user_example' # str | User name (optional)
    partition = 'partition_example' # str | Partition Name (optional)

    try:
        # Get association list
        api_response = api_instance.slurmdb_v0038_get_associations(cluster=cluster, account=account, user=user, partition=partition)
        print("The response of SlurmApi->slurmdb_v0038_get_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **account** | **str**| Account name | [optional] 
 **user** | **str**| User name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0038AssociationsInfo**](Dbv0038AssociationsInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_cluster**
> Dbv0038ClusterInfo slurmdb_v0038_get_cluster(cluster_name)

Get cluster info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_cluster_info import Dbv0038ClusterInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster_name = 'cluster_name_example' # str | Slurm cluster name

    try:
        # Get cluster info
        api_response = api_instance.slurmdb_v0038_get_cluster(cluster_name)
        print("The response of SlurmApi->slurmdb_v0038_get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name | 

### Return type

[**Dbv0038ClusterInfo**](Dbv0038ClusterInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_clusters**
> Dbv0038ClusterInfo slurmdb_v0038_get_clusters()

Get cluster list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_cluster_info import Dbv0038ClusterInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0038_get_clusters()
        print("The response of SlurmApi->slurmdb_v0038_get_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_clusters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0038ClusterInfo**](Dbv0038ClusterInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_config**
> Dbv0038ConfigInfo slurmdb_v0038_get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_config_info import Dbv0038ConfigInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Dump all configuration information
        api_response = api_instance.slurmdb_v0038_get_config()
        print("The response of SlurmApi->slurmdb_v0038_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0038ConfigInfo**](Dbv0038ConfigInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | Unable to dump config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_job**
> Dbv0038JobInfo slurmdb_v0038_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_job_info import Dbv0038JobInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm JobID

    try:
        # Get job info
        api_response = api_instance.slurmdb_v0038_get_job(job_id)
        print("The response of SlurmApi->slurmdb_v0038_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Slurm JobID | 

### Return type

[**Dbv0038JobInfo**](Dbv0038JobInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Unable to find job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_jobs**
> Dbv0038JobInfo slurmdb_v0038_get_jobs(submit_time=submit_time, start_time=start_time, end_time=end_time, account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, skip_steps=skip_steps, disable_wait_for_result=disable_wait_for_result, exit_code=exit_code, format=format, group=group, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, state=state, step=step, node=node, wckey=wckey)

Get job list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_job_info import Dbv0038JobInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    submit_time = 'submit_time_example' # str | Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    start_time = 'start_time_example' # str | Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    end_time = 'end_time_example' # str | Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    account = 'account_example' # str | Comma delimited list of accounts to match (optional)
    association = 'association_example' # str | Comma delimited list of associations to match (optional)
    cluster = 'cluster_example' # str | Comma delimited list of cluster to match (optional)
    constraints = 'constraints_example' # str | Comma delimited list of constraints to match (optional)
    cpus_max = 'cpus_max_example' # str | Number of CPUs high range (optional)
    cpus_min = 'cpus_min_example' # str | Number of CPUs low range (optional)
    skip_steps = True # bool | Report job step information (optional)
    disable_wait_for_result = True # bool | Disable waiting for result from slurmdbd (optional)
    exit_code = 'exit_code_example' # str | Exit code of job (optional)
    format = 'format_example' # str | Comma delimited list of formats to match (optional)
    group = 'group_example' # str | Comma delimited list of groups to match (optional)
    job_name = 'job_name_example' # str | Comma delimited list of job names to match (optional)
    nodes_max = 'nodes_max_example' # str | Number of nodes high range (optional)
    nodes_min = 'nodes_min_example' # str | Number of nodes low range (optional)
    partition = 'partition_example' # str | Comma delimited list of partitions to match (optional)
    qos = 'qos_example' # str | Comma delimited list of QOS to match (optional)
    reason = 'reason_example' # str | Comma delimited list of job reasons to match (optional)
    reservation = 'reservation_example' # str | Comma delimited list of reservations to match (optional)
    state = 'state_example' # str | Comma delimited list of states to match (optional)
    step = 'step_example' # str | Comma delimited list of job steps to match (optional)
    node = 'node_example' # str | Comma delimited list of used nodes to match (optional)
    wckey = 'wckey_example' # str | Comma delimited list of wckeys to match (optional)

    try:
        # Get job list
        api_response = api_instance.slurmdb_v0038_get_jobs(submit_time=submit_time, start_time=start_time, end_time=end_time, account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, skip_steps=skip_steps, disable_wait_for_result=disable_wait_for_result, exit_code=exit_code, format=format, group=group, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, state=state, step=step, node=node, wckey=wckey)
        print("The response of SlurmApi->slurmdb_v0038_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_time** | **str**| Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional] 
 **start_time** | **str**| Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional] 
 **end_time** | **str**| Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional] 
 **account** | **str**| Comma delimited list of accounts to match | [optional] 
 **association** | **str**| Comma delimited list of associations to match | [optional] 
 **cluster** | **str**| Comma delimited list of cluster to match | [optional] 
 **constraints** | **str**| Comma delimited list of constraints to match | [optional] 
 **cpus_max** | **str**| Number of CPUs high range | [optional] 
 **cpus_min** | **str**| Number of CPUs low range | [optional] 
 **skip_steps** | **bool**| Report job step information | [optional] 
 **disable_wait_for_result** | **bool**| Disable waiting for result from slurmdbd | [optional] 
 **exit_code** | **str**| Exit code of job | [optional] 
 **format** | **str**| Comma delimited list of formats to match | [optional] 
 **group** | **str**| Comma delimited list of groups to match | [optional] 
 **job_name** | **str**| Comma delimited list of job names to match | [optional] 
 **nodes_max** | **str**| Number of nodes high range | [optional] 
 **nodes_min** | **str**| Number of nodes low range | [optional] 
 **partition** | **str**| Comma delimited list of partitions to match | [optional] 
 **qos** | **str**| Comma delimited list of QOS to match | [optional] 
 **reason** | **str**| Comma delimited list of job reasons to match | [optional] 
 **reservation** | **str**| Comma delimited list of reservations to match | [optional] 
 **state** | **str**| Comma delimited list of states to match | [optional] 
 **step** | **str**| Comma delimited list of job steps to match | [optional] 
 **node** | **str**| Comma delimited list of used nodes to match | [optional] 
 **wckey** | **str**| Comma delimited list of wckeys to match | [optional] 

### Return type

[**Dbv0038JobInfo**](Dbv0038JobInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | Unable to query jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_qos**
> Dbv0038QosInfo slurmdb_v0038_get_qos(with_deleted=with_deleted)

Get QOS list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_qos_info import Dbv0038QosInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    with_deleted = True # bool | Include deleted QOSs. False by default. (optional)

    try:
        # Get QOS list
        api_response = api_instance.slurmdb_v0038_get_qos(with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0038_get_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_deleted** | **bool**| Include deleted QOSs. False by default. | [optional] 

### Return type

[**Dbv0038QosInfo**](Dbv0038QosInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS&#39; |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_single_qos**
> Dbv0038QosInfo slurmdb_v0038_get_single_qos(qos_name, with_deleted=with_deleted)

Get QOS info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_qos_info import Dbv0038QosInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    qos_name = 'qos_name_example' # str | Slurm QOS Name
    with_deleted = True # bool | Include deleted QOSs. False by default. (optional)

    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0038_get_single_qos(qos_name, with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0038_get_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name | 
 **with_deleted** | **bool**| Include deleted QOSs. False by default. | [optional] 

### Return type

[**Dbv0038QosInfo**](Dbv0038QosInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_tres**
> Dbv0038TresInfo slurmdb_v0038_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_tres_info import Dbv0038TresInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Get TRES info
        api_response = api_instance.slurmdb_v0038_get_tres()
        print("The response of SlurmApi->slurmdb_v0038_get_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_tres: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0038TresInfo**](Dbv0038TresInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to retrieve TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_user**
> Dbv0038UserInfo slurmdb_v0038_get_user(user_name, with_deleted=with_deleted)

Get user info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_user_info import Dbv0038UserInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    user_name = 'user_name_example' # str | Slurm User Name
    with_deleted = True # bool | Include deleted users. False by default. (optional)

    try:
        # Get user info
        api_response = api_instance.slurmdb_v0038_get_user(user_name, with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0038_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name | 
 **with_deleted** | **bool**| Include deleted users. False by default. | [optional] 

### Return type

[**Dbv0038UserInfo**](Dbv0038UserInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_users**
> Dbv0038UserInfo slurmdb_v0038_get_users(with_deleted=with_deleted)

Get user list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_user_info import Dbv0038UserInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    with_deleted = True # bool | Include deleted users. False by default. (optional)

    try:
        # Get user list
        api_response = api_instance.slurmdb_v0038_get_users(with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0038_get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_deleted** | **bool**| Include deleted users. False by default. | [optional] 

### Return type

[**Dbv0038UserInfo**](Dbv0038UserInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_wckey**
> Dbv0038WckeyInfo slurmdb_v0038_get_wckey(wckey)

Get wckey info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_wckey_info import Dbv0038WckeyInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    wckey = 'wckey_example' # str | Slurm wckey name

    try:
        # Get wckey info
        api_response = api_instance.slurmdb_v0038_get_wckey(wckey)
        print("The response of SlurmApi->slurmdb_v0038_get_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name | 

### Return type

[**Dbv0038WckeyInfo**](Dbv0038WckeyInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckey |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_get_wckeys**
> Dbv0038WckeyInfo slurmdb_v0038_get_wckeys()

Get wckey list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_wckey_info import Dbv0038WckeyInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Get wckey list
        api_response = api_instance.slurmdb_v0038_get_wckeys()
        print("The response of SlurmApi->slurmdb_v0038_get_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_wckeys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0038WckeyInfo**](Dbv0038WckeyInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_set_config**
> Dbv0038ConfigResponse slurmdb_v0038_set_config(dbv0038_set_config=dbv0038_set_config)

Load all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_config_response import Dbv0038ConfigResponse
from openapi_client.models.dbv0038_set_config import Dbv0038SetConfig
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0038_set_config = openapi_client.Dbv0038SetConfig() # Dbv0038SetConfig | Add or update config (optional)

    try:
        # Load all configuration information
        api_response = api_instance.slurmdb_v0038_set_config(dbv0038_set_config=dbv0038_set_config)
        print("The response of SlurmApi->slurmdb_v0038_set_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_set_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0038_set_config** | [**Dbv0038SetConfig**](Dbv0038SetConfig.md)| Add or update config | [optional] 

### Return type

[**Dbv0038ConfigResponse**](Dbv0038ConfigResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Load config |  -  |
**0** | Unable to set config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_update_account**
> Dbv0038AccountResponse slurmdb_v0038_update_account(dbv0038_update_account)

Update accounts

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_account_response import Dbv0038AccountResponse
from openapi_client.models.dbv0038_update_account import Dbv0038UpdateAccount
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0038_update_account = openapi_client.Dbv0038UpdateAccount() # Dbv0038UpdateAccount | update/create accounts

    try:
        # Update accounts
        api_response = api_instance.slurmdb_v0038_update_account(dbv0038_update_account)
        print("The response of SlurmApi->slurmdb_v0038_update_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0038_update_account** | [**Dbv0038UpdateAccount**](Dbv0038UpdateAccount.md)| update/create accounts | 

### Return type

[**Dbv0038AccountResponse**](Dbv0038AccountResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add/update list of accounts |  -  |
**0** | Unable to add or update accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_update_associations**
> Dbv0038ResponseAssociations slurmdb_v0038_update_associations(dbv0038_associations_info)

Set associations info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_associations_info import Dbv0038AssociationsInfo
from openapi_client.models.dbv0038_response_associations import Dbv0038ResponseAssociations
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0038_associations_info = openapi_client.Dbv0038AssociationsInfo() # Dbv0038AssociationsInfo | Add or update associations

    try:
        # Set associations info
        api_response = api_instance.slurmdb_v0038_update_associations(dbv0038_associations_info)
        print("The response of SlurmApi->slurmdb_v0038_update_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0038_associations_info** | [**Dbv0038AssociationsInfo**](Dbv0038AssociationsInfo.md)| Add or update associations | 

### Return type

[**Dbv0038ResponseAssociations**](Dbv0038ResponseAssociations.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | status of associations update |  -  |
**0** | Unable to update associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_update_qos**
> Dbv0038ResponseQos slurmdb_v0038_update_qos(dbv0038_update_qos)

Set QOS info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_qos import Dbv0038ResponseQos
from openapi_client.models.dbv0038_update_qos import Dbv0038UpdateQos
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0038_update_qos = openapi_client.Dbv0038UpdateQos() # Dbv0038UpdateQos | Add or update QOSs

    try:
        # Set QOS info
        api_response = api_instance.slurmdb_v0038_update_qos(dbv0038_update_qos)
        print("The response of SlurmApi->slurmdb_v0038_update_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0038_update_qos** | [**Dbv0038UpdateQos**](Dbv0038UpdateQos.md)| Add or update QOSs | 

### Return type

[**Dbv0038ResponseQos**](Dbv0038ResponseQos.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS update response |  -  |
**0** | Unable to update QOSs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_update_tres**
> Dbv0038ResponseTres slurmdb_v0038_update_tres(dbv0038_tres_update)

Set TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_tres import Dbv0038ResponseTres
from openapi_client.models.dbv0038_tres_update import Dbv0038TresUpdate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0038_tres_update = openapi_client.Dbv0038TresUpdate() # Dbv0038TresUpdate | Add or Update TRES

    try:
        # Set TRES info
        api_response = api_instance.slurmdb_v0038_update_tres(dbv0038_tres_update)
        print("The response of SlurmApi->slurmdb_v0038_update_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_tres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0038_tres_update** | [**Dbv0038TresUpdate**](Dbv0038TresUpdate.md)| Add or Update TRES | 

### Return type

[**Dbv0038ResponseTres**](Dbv0038ResponseTres.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to update TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0038_update_users**
> Dbv0038ResponseUserUpdate slurmdb_v0038_update_users(dbv0038_update_users)

Update user

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0038_response_user_update import Dbv0038ResponseUserUpdate
from openapi_client.models.dbv0038_update_users import Dbv0038UpdateUsers
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0038_update_users = openapi_client.Dbv0038UpdateUsers() # Dbv0038UpdateUsers | add or update user

    try:
        # Update user
        api_response = api_instance.slurmdb_v0038_update_users(dbv0038_update_users)
        print("The response of SlurmApi->slurmdb_v0038_update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0038_update_users** | [**Dbv0038UpdateUsers**](Dbv0038UpdateUsers.md)| add or update user | 

### Return type

[**Dbv0038ResponseUserUpdate**](Dbv0038ResponseUserUpdate.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update users |  -  |
**0** | User not found or not able to update user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_add_clusters**
> Status slurmdb_v0039_add_clusters(dbv0039_clusters_info)

Add clusters

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_clusters_info import Dbv0039ClustersInfo
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0039_clusters_info = openapi_client.Dbv0039ClustersInfo() # Dbv0039ClustersInfo | Add or update clusters

    try:
        # Add clusters
        api_response = api_instance.slurmdb_v0039_add_clusters(dbv0039_clusters_info)
        print("The response of SlurmApi->slurmdb_v0039_add_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_add_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0039_clusters_info** | [**Dbv0039ClustersInfo**](Dbv0039ClustersInfo.md)| Add or update clusters | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Unable to add cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_add_wckeys**
> Status slurmdb_v0039_add_wckeys(dbv0039_wckey_info=dbv0039_wckey_info)

Add wckeys

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_wckey_info import Dbv0039WckeyInfo
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0039_wckey_info = openapi_client.Dbv0039WckeyInfo() # Dbv0039WckeyInfo | add wckeys (optional)

    try:
        # Add wckeys
        api_response = api_instance.slurmdb_v0039_add_wckeys(dbv0039_wckey_info=dbv0039_wckey_info)
        print("The response of SlurmApi->slurmdb_v0039_add_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_add_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0039_wckey_info** | [**Dbv0039WckeyInfo**](Dbv0039WckeyInfo.md)| add wckeys | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | Unable to add wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_delete_account**
> Status slurmdb_v0039_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    account_name = 'account_name_example' # str | Slurm Account Name

    try:
        # Delete account
        api_response = api_instance.slurmdb_v0039_delete_account(account_name)
        print("The response of SlurmApi->slurmdb_v0039_delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete account |  -  |
**0** | Unable to delete account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_delete_association**
> Dbv0039ResponseAssociationsDelete slurmdb_v0039_delete_association(cluster=cluster, account=account, user=user, partition=partition)

Delete association

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_response_associations_delete import Dbv0039ResponseAssociationsDelete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    account = 'account_example' # str | Account name (optional)
    user = 'user_example' # str | User name (optional)
    partition = 'partition_example' # str | Partition Name (optional)

    try:
        # Delete association
        api_response = api_instance.slurmdb_v0039_delete_association(cluster=cluster, account=account, user=user, partition=partition)
        print("The response of SlurmApi->slurmdb_v0039_delete_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **account** | **str**| Account name | [optional] 
 **user** | **str**| User name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0039ResponseAssociationsDelete**](Dbv0039ResponseAssociationsDelete.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete associations |  -  |
**0** | Association not found or unable to delete association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_delete_associations**
> Dbv0039ResponseAssociationsDelete slurmdb_v0039_delete_associations(cluster=cluster, account=account, user=user, partition=partition)

Delete associations

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_response_associations_delete import Dbv0039ResponseAssociationsDelete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    account = 'account_example' # str | Account name (optional)
    user = 'user_example' # str | User name (optional)
    partition = 'partition_example' # str | Partition Name (optional)

    try:
        # Delete associations
        api_response = api_instance.slurmdb_v0039_delete_associations(cluster=cluster, account=account, user=user, partition=partition)
        print("The response of SlurmApi->slurmdb_v0039_delete_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **account** | **str**| Account name | [optional] 
 **user** | **str**| User name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0039ResponseAssociationsDelete**](Dbv0039ResponseAssociationsDelete.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete associations |  -  |
**0** | Associations not found or unable to delete association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_delete_cluster**
> Status slurmdb_v0039_delete_cluster(cluster_name)

Delete cluster

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster_name = 'cluster_name_example' # str | Slurm cluster name

    try:
        # Delete cluster
        api_response = api_instance.slurmdb_v0039_delete_cluster(cluster_name)
        print("The response of SlurmApi->slurmdb_v0039_delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete cluster |  -  |
**0** | Cluster not found or unable to delete cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_delete_qos**
> Status slurmdb_v0039_delete_qos(qos_name)

Delete QOS

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    qos_name = 'qos_name_example' # str | Slurm QOS Name

    try:
        # Delete QOS
        api_response = api_instance.slurmdb_v0039_delete_qos(qos_name)
        print("The response of SlurmApi->slurmdb_v0039_delete_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete qos |  -  |
**0** | Unable to delete QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_delete_user**
> Status slurmdb_v0039_delete_user(user_name)

Delete user

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    user_name = 'user_name_example' # str | Slurm User Name

    try:
        # Delete user
        api_response = api_instance.slurmdb_v0039_delete_user(user_name)
        print("The response of SlurmApi->slurmdb_v0039_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User deleted |  -  |
**0** | User not found or unable to delete user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_delete_wckey**
> Status slurmdb_v0039_delete_wckey(wckey)

Delete wckey

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    wckey = 'wckey_example' # str | Slurm wckey name

    try:
        # Delete wckey
        api_response = api_instance.slurmdb_v0039_delete_wckey(wckey)
        print("The response of SlurmApi->slurmdb_v0039_delete_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete wckey |  -  |
**0** | wckey not found or unable to delete wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_diag**
> Dbv0039Diag slurmdb_v0039_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_diag import Dbv0039Diag
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdb_v0039_diag()
        print("The response of SlurmApi->slurmdb_v0039_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0039Diag**](Dbv0039Diag.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Unable to query diagnostics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_account**
> Dbv0039AccountInfo slurmdb_v0039_get_account(account_name, with_deleted=with_deleted)

Get account info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_account_info import Dbv0039AccountInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    account_name = 'account_name_example' # str | Slurm Account Name
    with_deleted = false # str | Include deleted accounts. False by default. (optional) (default to false)

    try:
        # Get account info
        api_response = api_instance.slurmdb_v0039_get_account(account_name, with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0039_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name | 
 **with_deleted** | **str**| Include deleted accounts. False by default. | [optional] [default to false]

### Return type

[**Dbv0039AccountInfo**](Dbv0039AccountInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_accounts**
> Dbv0039AccountInfo slurmdb_v0039_get_accounts(with_deleted=with_deleted)

Get account list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_account_info import Dbv0039AccountInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    with_deleted = false # str | Include deleted accounts. False by default. (optional) (default to false)

    try:
        # Get account list
        api_response = api_instance.slurmdb_v0039_get_accounts(with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0039_get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_deleted** | **str**| Include deleted accounts. False by default. | [optional] [default to false]

### Return type

[**Dbv0039AccountInfo**](Dbv0039AccountInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_association**
> Dbv0039AssociationsInfo slurmdb_v0039_get_association(cluster=cluster, account=account, user=user, partition=partition)

Get association info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_associations_info import Dbv0039AssociationsInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    account = 'account_example' # str | Account name (optional)
    user = 'user_example' # str | User name (optional)
    partition = 'partition_example' # str | Partition Name (optional)

    try:
        # Get association info
        api_response = api_instance.slurmdb_v0039_get_association(cluster=cluster, account=account, user=user, partition=partition)
        print("The response of SlurmApi->slurmdb_v0039_get_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **account** | **str**| Account name | [optional] 
 **user** | **str**| User name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0039AssociationsInfo**](Dbv0039AssociationsInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_associations**
> Dbv0039AssociationsInfo slurmdb_v0039_get_associations(cluster=cluster, account=account, user=user, partition=partition)

Get association list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_associations_info import Dbv0039AssociationsInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    account = 'account_example' # str | Account name (optional)
    user = 'user_example' # str | User name (optional)
    partition = 'partition_example' # str | Partition Name (optional)

    try:
        # Get association list
        api_response = api_instance.slurmdb_v0039_get_associations(cluster=cluster, account=account, user=user, partition=partition)
        print("The response of SlurmApi->slurmdb_v0039_get_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **account** | **str**| Account name | [optional] 
 **user** | **str**| User name | [optional] 
 **partition** | **str**| Partition Name | [optional] 

### Return type

[**Dbv0039AssociationsInfo**](Dbv0039AssociationsInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_cluster**
> Dbv0039ClustersInfo slurmdb_v0039_get_cluster(cluster_name)

Get cluster info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_clusters_info import Dbv0039ClustersInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    cluster_name = 'cluster_name_example' # str | Slurm cluster name

    try:
        # Get cluster info
        api_response = api_instance.slurmdb_v0039_get_cluster(cluster_name)
        print("The response of SlurmApi->slurmdb_v0039_get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name | 

### Return type

[**Dbv0039ClustersInfo**](Dbv0039ClustersInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_clusters**
> Dbv0039ClustersInfo slurmdb_v0039_get_clusters()

Get cluster list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_clusters_info import Dbv0039ClustersInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0039_get_clusters()
        print("The response of SlurmApi->slurmdb_v0039_get_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_clusters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0039ClustersInfo**](Dbv0039ClustersInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_config**
> Dbv0039ConfigInfo slurmdb_v0039_get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_config_info import Dbv0039ConfigInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Dump all configuration information
        api_response = api_instance.slurmdb_v0039_get_config()
        print("The response of SlurmApi->slurmdb_v0039_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0039ConfigInfo**](Dbv0039ConfigInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | Unable to dump config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_job**
> Dbv0039JobInfo slurmdb_v0039_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_job_info import Dbv0039JobInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm JobID

    try:
        # Get job info
        api_response = api_instance.slurmdb_v0039_get_job(job_id)
        print("The response of SlurmApi->slurmdb_v0039_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Slurm JobID | 

### Return type

[**Dbv0039JobInfo**](Dbv0039JobInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Unable to find job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_jobs**
> Dbv0039JobInfo slurmdb_v0039_get_jobs(users=users, submit_time=submit_time, start_time=start_time, end_time=end_time, account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, skip_steps=skip_steps, disable_wait_for_result=disable_wait_for_result, exit_code=exit_code, format=format, group=group, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, state=state, step=step, node=node, wckey=wckey)

Get job list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_job_info import Dbv0039JobInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    users = 'users_example' # str | Filter by comma delimited list of user names (optional)
    submit_time = 'submit_time_example' # str | Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    start_time = 'start_time_example' # str | Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    end_time = 'end_time_example' # str | Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    account = 'account_example' # str | Comma delimited list of accounts to match (optional)
    association = 'association_example' # str | Comma delimited list of associations to match (optional)
    cluster = 'cluster_example' # str | Comma delimited list of cluster to match (optional)
    constraints = 'constraints_example' # str | Comma delimited list of constraints to match (optional)
    cpus_max = 'cpus_max_example' # str | Number of CPUs high range (optional)
    cpus_min = 'cpus_min_example' # str | Number of CPUs low range (optional)
    skip_steps = false # str | Report job step information (optional) (default to false)
    disable_wait_for_result = false # str | Disable waiting for result from slurmdbd (optional) (default to false)
    exit_code = 'exit_code_example' # str | Exit code of job (optional)
    format = 'format_example' # str | Comma delimited list of formats to match (optional)
    group = 'group_example' # str | Comma delimited list of groups to match (optional)
    job_name = 'job_name_example' # str | Comma delimited list of job names to match (optional)
    nodes_max = 'nodes_max_example' # str | Number of nodes high range (optional)
    nodes_min = 'nodes_min_example' # str | Number of nodes low range (optional)
    partition = 'partition_example' # str | Comma delimited list of partitions to match (optional)
    qos = 'qos_example' # str | Comma delimited list of QOS to match (optional)
    reason = 'reason_example' # str | Comma delimited list of job reasons to match (optional)
    reservation = 'reservation_example' # str | Comma delimited list of reservations to match (optional)
    state = 'state_example' # str | Comma delimited list of states to match (optional)
    step = 'step_example' # str | Comma delimited list of job steps to match (optional)
    node = 'node_example' # str | Comma delimited list of used nodes to match (optional)
    wckey = 'wckey_example' # str | Comma delimited list of wckeys to match (optional)

    try:
        # Get job list
        api_response = api_instance.slurmdb_v0039_get_jobs(users=users, submit_time=submit_time, start_time=start_time, end_time=end_time, account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, skip_steps=skip_steps, disable_wait_for_result=disable_wait_for_result, exit_code=exit_code, format=format, group=group, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, state=state, step=step, node=node, wckey=wckey)
        print("The response of SlurmApi->slurmdb_v0039_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users** | **str**| Filter by comma delimited list of user names | [optional] 
 **submit_time** | **str**| Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional] 
 **start_time** | **str**| Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional] 
 **end_time** | **str**| Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional] 
 **account** | **str**| Comma delimited list of accounts to match | [optional] 
 **association** | **str**| Comma delimited list of associations to match | [optional] 
 **cluster** | **str**| Comma delimited list of cluster to match | [optional] 
 **constraints** | **str**| Comma delimited list of constraints to match | [optional] 
 **cpus_max** | **str**| Number of CPUs high range | [optional] 
 **cpus_min** | **str**| Number of CPUs low range | [optional] 
 **skip_steps** | **str**| Report job step information | [optional] [default to false]
 **disable_wait_for_result** | **str**| Disable waiting for result from slurmdbd | [optional] [default to false]
 **exit_code** | **str**| Exit code of job | [optional] 
 **format** | **str**| Comma delimited list of formats to match | [optional] 
 **group** | **str**| Comma delimited list of groups to match | [optional] 
 **job_name** | **str**| Comma delimited list of job names to match | [optional] 
 **nodes_max** | **str**| Number of nodes high range | [optional] 
 **nodes_min** | **str**| Number of nodes low range | [optional] 
 **partition** | **str**| Comma delimited list of partitions to match | [optional] 
 **qos** | **str**| Comma delimited list of QOS to match | [optional] 
 **reason** | **str**| Comma delimited list of job reasons to match | [optional] 
 **reservation** | **str**| Comma delimited list of reservations to match | [optional] 
 **state** | **str**| Comma delimited list of states to match | [optional] 
 **step** | **str**| Comma delimited list of job steps to match | [optional] 
 **node** | **str**| Comma delimited list of used nodes to match | [optional] 
 **wckey** | **str**| Comma delimited list of wckeys to match | [optional] 

### Return type

[**Dbv0039JobInfo**](Dbv0039JobInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | Unable to query jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_qos**
> Dbv0039QosInfo slurmdb_v0039_get_qos(with_deleted=with_deleted)

Get QOS list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_qos_info import Dbv0039QosInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    with_deleted = false # str | Include deleted QOSs. False by default. (optional) (default to false)

    try:
        # Get QOS list
        api_response = api_instance.slurmdb_v0039_get_qos(with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0039_get_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_deleted** | **str**| Include deleted QOSs. False by default. | [optional] [default to false]

### Return type

[**Dbv0039QosInfo**](Dbv0039QosInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS&#39; |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_single_qos**
> Dbv0039QosInfo slurmdb_v0039_get_single_qos(qos_name, with_deleted=with_deleted)

Get QOS info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_qos_info import Dbv0039QosInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    qos_name = 'qos_name_example' # str | Slurm QOS Name
    with_deleted = false # str | Include deleted QOSs. False by default. (optional) (default to false)

    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0039_get_single_qos(qos_name, with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0039_get_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name | 
 **with_deleted** | **str**| Include deleted QOSs. False by default. | [optional] [default to false]

### Return type

[**Dbv0039QosInfo**](Dbv0039QosInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_tres**
> Dbv0039TresInfo slurmdb_v0039_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_tres_info import Dbv0039TresInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Get TRES info
        api_response = api_instance.slurmdb_v0039_get_tres()
        print("The response of SlurmApi->slurmdb_v0039_get_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_tres: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0039TresInfo**](Dbv0039TresInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to retrieve TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_user**
> Dbv0039UserInfo slurmdb_v0039_get_user(user_name, with_deleted=with_deleted)

Get user info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_user_info import Dbv0039UserInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    user_name = 'user_name_example' # str | Slurm User Name
    with_deleted = false # str | Include deleted users. False by default. (optional) (default to false)

    try:
        # Get user info
        api_response = api_instance.slurmdb_v0039_get_user(user_name, with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0039_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name | 
 **with_deleted** | **str**| Include deleted users. False by default. | [optional] [default to false]

### Return type

[**Dbv0039UserInfo**](Dbv0039UserInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_users**
> Dbv0039UserInfo slurmdb_v0039_get_users(with_deleted=with_deleted)

Get user list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_user_info import Dbv0039UserInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    with_deleted = false # str | Include deleted users. False by default. (optional) (default to false)

    try:
        # Get user list
        api_response = api_instance.slurmdb_v0039_get_users(with_deleted=with_deleted)
        print("The response of SlurmApi->slurmdb_v0039_get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_deleted** | **str**| Include deleted users. False by default. | [optional] [default to false]

### Return type

[**Dbv0039UserInfo**](Dbv0039UserInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_wckey**
> Dbv0039WckeyInfo slurmdb_v0039_get_wckey(wckey)

Get wckey info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_wckey_info import Dbv0039WckeyInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    wckey = 'wckey_example' # str | Slurm wckey name

    try:
        # Get wckey info
        api_response = api_instance.slurmdb_v0039_get_wckey(wckey)
        print("The response of SlurmApi->slurmdb_v0039_get_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name | 

### Return type

[**Dbv0039WckeyInfo**](Dbv0039WckeyInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckey |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_get_wckeys**
> Dbv0039WckeyInfo slurmdb_v0039_get_wckeys()

Get wckey list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_wckey_info import Dbv0039WckeyInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # Get wckey list
        api_response = api_instance.slurmdb_v0039_get_wckeys()
        print("The response of SlurmApi->slurmdb_v0039_get_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_wckeys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dbv0039WckeyInfo**](Dbv0039WckeyInfo.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_set_config**
> Status slurmdb_v0039_set_config(dbv0039_set_config=dbv0039_set_config)

Load all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_set_config import Dbv0039SetConfig
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0039_set_config = openapi_client.Dbv0039SetConfig() # Dbv0039SetConfig | Add or update config (optional)

    try:
        # Load all configuration information
        api_response = api_instance.slurmdb_v0039_set_config(dbv0039_set_config=dbv0039_set_config)
        print("The response of SlurmApi->slurmdb_v0039_set_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_set_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0039_set_config** | [**Dbv0039SetConfig**](Dbv0039SetConfig.md)| Add or update config | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Load config |  -  |
**0** | Unable to set config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_update_accounts**
> Status slurmdb_v0039_update_accounts(dbv0039_account_info)

Update accounts

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_account_info import Dbv0039AccountInfo
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0039_account_info = openapi_client.Dbv0039AccountInfo() # Dbv0039AccountInfo | update/create accounts

    try:
        # Update accounts
        api_response = api_instance.slurmdb_v0039_update_accounts(dbv0039_account_info)
        print("The response of SlurmApi->slurmdb_v0039_update_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0039_account_info** | [**Dbv0039AccountInfo**](Dbv0039AccountInfo.md)| update/create accounts | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add/update list of accounts |  -  |
**0** | Unable to add or update accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_update_associations**
> Status slurmdb_v0039_update_associations(dbv0039_associations_info)

Set associations info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_associations_info import Dbv0039AssociationsInfo
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0039_associations_info = openapi_client.Dbv0039AssociationsInfo() # Dbv0039AssociationsInfo | Add or update associations

    try:
        # Set associations info
        api_response = api_instance.slurmdb_v0039_update_associations(dbv0039_associations_info)
        print("The response of SlurmApi->slurmdb_v0039_update_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0039_associations_info** | [**Dbv0039AssociationsInfo**](Dbv0039AssociationsInfo.md)| Add or update associations | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | status of associations update |  -  |
**0** | Unable to update associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_update_qos**
> Status slurmdb_v0039_update_qos(dbv0039_update_qos)

Set QOS info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_update_qos import Dbv0039UpdateQos
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0039_update_qos = openapi_client.Dbv0039UpdateQos() # Dbv0039UpdateQos | Add or update QOSs

    try:
        # Set QOS info
        api_response = api_instance.slurmdb_v0039_update_qos(dbv0039_update_qos)
        print("The response of SlurmApi->slurmdb_v0039_update_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0039_update_qos** | [**Dbv0039UpdateQos**](Dbv0039UpdateQos.md)| Add or update QOSs | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS update response |  -  |
**0** | Unable to update QOSs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_update_tres**
> Status slurmdb_v0039_update_tres(dbv0039_tres_update)

Set TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_tres_update import Dbv0039TresUpdate
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0039_tres_update = openapi_client.Dbv0039TresUpdate() # Dbv0039TresUpdate | Add or Update TRES

    try:
        # Set TRES info
        api_response = api_instance.slurmdb_v0039_update_tres(dbv0039_tres_update)
        print("The response of SlurmApi->slurmdb_v0039_update_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_tres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0039_tres_update** | [**Dbv0039TresUpdate**](Dbv0039TresUpdate.md)| Add or Update TRES | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to update TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0039_update_users**
> Status slurmdb_v0039_update_users(dbv0039_update_users)

Update user

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.dbv0039_update_users import Dbv0039UpdateUsers
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    dbv0039_update_users = openapi_client.Dbv0039UpdateUsers() # Dbv0039UpdateUsers | add or update user

    try:
        # Update user
        api_response = api_instance.slurmdb_v0039_update_users(dbv0039_update_users)
        print("The response of SlurmApi->slurmdb_v0039_update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbv0039_update_users** | [**Dbv0039UpdateUsers**](Dbv0039UpdateUsers.md)| add or update user | 

### Return type

[**Status**](Status.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update users |  -  |
**0** | User not found or not able to update user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

