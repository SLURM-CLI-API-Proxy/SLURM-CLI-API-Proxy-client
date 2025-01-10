# openapi_client.SlurmdbApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurmdb_v0040_delete_account**](SlurmdbApi.md#slurmdb_v0040_delete_account) | **DELETE** /slurmdb/v0.0.40/account/{account_name} | Delete account
[**slurmdb_v0040_delete_association**](SlurmdbApi.md#slurmdb_v0040_delete_association) | **DELETE** /slurmdb/v0.0.40/association | Delete association
[**slurmdb_v0040_delete_associations**](SlurmdbApi.md#slurmdb_v0040_delete_associations) | **DELETE** /slurmdb/v0.0.40/associations | Delete associations
[**slurmdb_v0040_delete_cluster**](SlurmdbApi.md#slurmdb_v0040_delete_cluster) | **DELETE** /slurmdb/v0.0.40/cluster/{cluster_name} | Delete cluster
[**slurmdb_v0040_delete_single_qos**](SlurmdbApi.md#slurmdb_v0040_delete_single_qos) | **DELETE** /slurmdb/v0.0.40/qos/{qos} | Delete QOS
[**slurmdb_v0040_delete_user**](SlurmdbApi.md#slurmdb_v0040_delete_user) | **DELETE** /slurmdb/v0.0.40/user/{name} | Delete user
[**slurmdb_v0040_delete_wckey**](SlurmdbApi.md#slurmdb_v0040_delete_wckey) | **DELETE** /slurmdb/v0.0.40/wckey/{id} | Delete wckey
[**slurmdb_v0040_get_account**](SlurmdbApi.md#slurmdb_v0040_get_account) | **GET** /slurmdb/v0.0.40/account/{account_name} | Get account info
[**slurmdb_v0040_get_accounts**](SlurmdbApi.md#slurmdb_v0040_get_accounts) | **GET** /slurmdb/v0.0.40/accounts | Get account list
[**slurmdb_v0040_get_association**](SlurmdbApi.md#slurmdb_v0040_get_association) | **GET** /slurmdb/v0.0.40/association | Get association info
[**slurmdb_v0040_get_associations**](SlurmdbApi.md#slurmdb_v0040_get_associations) | **GET** /slurmdb/v0.0.40/associations | Get association list
[**slurmdb_v0040_get_cluster**](SlurmdbApi.md#slurmdb_v0040_get_cluster) | **GET** /slurmdb/v0.0.40/cluster/{cluster_name} | Get cluster info
[**slurmdb_v0040_get_clusters**](SlurmdbApi.md#slurmdb_v0040_get_clusters) | **GET** /slurmdb/v0.0.40/clusters | Get cluster list
[**slurmdb_v0040_get_config**](SlurmdbApi.md#slurmdb_v0040_get_config) | **GET** /slurmdb/v0.0.40/config | Dump all configuration information
[**slurmdb_v0040_get_diag**](SlurmdbApi.md#slurmdb_v0040_get_diag) | **GET** /slurmdb/v0.0.40/diag | Get slurmdb diagnostics
[**slurmdb_v0040_get_instance**](SlurmdbApi.md#slurmdb_v0040_get_instance) | **GET** /slurmdb/v0.0.40/instance | Get instance info
[**slurmdb_v0040_get_instances**](SlurmdbApi.md#slurmdb_v0040_get_instances) | **GET** /slurmdb/v0.0.40/instances | Get instance list
[**slurmdb_v0040_get_job**](SlurmdbApi.md#slurmdb_v0040_get_job) | **GET** /slurmdb/v0.0.40/job/{job_id} | Get job info
[**slurmdb_v0040_get_jobs**](SlurmdbApi.md#slurmdb_v0040_get_jobs) | **GET** /slurmdb/v0.0.40/jobs | Get job list
[**slurmdb_v0040_get_qos**](SlurmdbApi.md#slurmdb_v0040_get_qos) | **GET** /slurmdb/v0.0.40/qos | Get QOS list
[**slurmdb_v0040_get_single_qos**](SlurmdbApi.md#slurmdb_v0040_get_single_qos) | **GET** /slurmdb/v0.0.40/qos/{qos} | Get QOS info
[**slurmdb_v0040_get_tres**](SlurmdbApi.md#slurmdb_v0040_get_tres) | **GET** /slurmdb/v0.0.40/tres | Get TRES info
[**slurmdb_v0040_get_user**](SlurmdbApi.md#slurmdb_v0040_get_user) | **GET** /slurmdb/v0.0.40/user/{name} | Get user info
[**slurmdb_v0040_get_users**](SlurmdbApi.md#slurmdb_v0040_get_users) | **GET** /slurmdb/v0.0.40/users | Get user list
[**slurmdb_v0040_get_wckey**](SlurmdbApi.md#slurmdb_v0040_get_wckey) | **GET** /slurmdb/v0.0.40/wckey/{id} | Get wckey info
[**slurmdb_v0040_get_wckeys**](SlurmdbApi.md#slurmdb_v0040_get_wckeys) | **GET** /slurmdb/v0.0.40/wckeys | Get wckey list
[**slurmdb_v0040_post_accounts**](SlurmdbApi.md#slurmdb_v0040_post_accounts) | **POST** /slurmdb/v0.0.40/accounts | Update accounts
[**slurmdb_v0040_post_accounts_association**](SlurmdbApi.md#slurmdb_v0040_post_accounts_association) | **POST** /slurmdb/v0.0.40/accounts_association | Add accounts with conditional association
[**slurmdb_v0040_post_associations**](SlurmdbApi.md#slurmdb_v0040_post_associations) | **POST** /slurmdb/v0.0.40/associations | Set associations info
[**slurmdb_v0040_post_clusters**](SlurmdbApi.md#slurmdb_v0040_post_clusters) | **POST** /slurmdb/v0.0.40/clusters | update clusters
[**slurmdb_v0040_post_config**](SlurmdbApi.md#slurmdb_v0040_post_config) | **POST** /slurmdb/v0.0.40/config | Load all configuration information
[**slurmdb_v0040_post_qos**](SlurmdbApi.md#slurmdb_v0040_post_qos) | **POST** /slurmdb/v0.0.40/qos | Set QOS info
[**slurmdb_v0040_post_tres**](SlurmdbApi.md#slurmdb_v0040_post_tres) | **POST** /slurmdb/v0.0.40/tres | Set TRES info
[**slurmdb_v0040_post_users**](SlurmdbApi.md#slurmdb_v0040_post_users) | **POST** /slurmdb/v0.0.40/users | Update user
[**slurmdb_v0040_post_users_association**](SlurmdbApi.md#slurmdb_v0040_post_users_association) | **POST** /slurmdb/v0.0.40/users_association | Add users with conditional association
[**slurmdb_v0040_post_wckeys**](SlurmdbApi.md#slurmdb_v0040_post_wckeys) | **POST** /slurmdb/v0.0.40/wckeys | Add wckeys


# **slurmdb_v0040_delete_account**
> V0040OpenapiAccountsRemovedResp slurmdb_v0040_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_accounts_removed_resp import V0040OpenapiAccountsRemovedResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name

    try:
        # Delete account
        api_response = api_instance.slurmdb_v0040_delete_account(account_name)
        print("The response of SlurmdbApi->slurmdb_v0040_delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 

### Return type

[**V0040OpenapiAccountsRemovedResp**](V0040OpenapiAccountsRemovedResp.md)

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

# **slurmdb_v0040_delete_association**
> V0040OpenapiAssocsRemovedResp slurmdb_v0040_delete_association(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)

Delete association

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_assocs_removed_resp import V0040OpenapiAssocsRemovedResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    format = 'format_example' # str | CSV format list (optional)
    id = 'id_example' # str | CSV id list (optional)
    only_defaults = 'only_defaults_example' # str | filter to only defaults (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | usage end UNIX timestamp (optional)
    usage_start = 'usage_start_example' # str | usage start UNIX timestamp (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | fill in usage (optional)
    with_deleted = 'with_deleted_example' # str | return deleted associations (optional)
    with_raw_qos = 'with_raw_qos_example' # str | return a raw qos or delta_qos (optional)
    with_sub_accts = 'with_sub_accts_example' # str | return sub acct information also (optional)
    without_parent_info = 'without_parent_info_example' # str | don't give me parent id/name (optional)
    without_parent_limits = 'without_parent_limits_example' # str | don't give me limits from parents (optional)

    try:
        # Delete association
        api_response = api_instance.slurmdb_v0040_delete_association(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)
        print("The response of SlurmdbApi->slurmdb_v0040_delete_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_delete_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **format** | **str**| CSV format list | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **only_defaults** | **str**| filter to only defaults | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| usage end UNIX timestamp | [optional] 
 **usage_start** | **str**| usage start UNIX timestamp | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| fill in usage | [optional] 
 **with_deleted** | **str**| return deleted associations | [optional] 
 **with_raw_qos** | **str**| return a raw qos or delta_qos | [optional] 
 **with_sub_accts** | **str**| return sub acct information also | [optional] 
 **without_parent_info** | **str**| don&#39;t give me parent id/name | [optional] 
 **without_parent_limits** | **str**| don&#39;t give me limits from parents | [optional] 

### Return type

[**V0040OpenapiAssocsRemovedResp**](V0040OpenapiAssocsRemovedResp.md)

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

# **slurmdb_v0040_delete_associations**
> V0040OpenapiAssocsRemovedResp slurmdb_v0040_delete_associations(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)

Delete associations

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_assocs_removed_resp import V0040OpenapiAssocsRemovedResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    format = 'format_example' # str | CSV format list (optional)
    id = 'id_example' # str | CSV id list (optional)
    only_defaults = 'only_defaults_example' # str | filter to only defaults (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | usage end UNIX timestamp (optional)
    usage_start = 'usage_start_example' # str | usage start UNIX timestamp (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | fill in usage (optional)
    with_deleted = 'with_deleted_example' # str | return deleted associations (optional)
    with_raw_qos = 'with_raw_qos_example' # str | return a raw qos or delta_qos (optional)
    with_sub_accts = 'with_sub_accts_example' # str | return sub acct information also (optional)
    without_parent_info = 'without_parent_info_example' # str | don't give me parent id/name (optional)
    without_parent_limits = 'without_parent_limits_example' # str | don't give me limits from parents (optional)

    try:
        # Delete associations
        api_response = api_instance.slurmdb_v0040_delete_associations(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)
        print("The response of SlurmdbApi->slurmdb_v0040_delete_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_delete_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **format** | **str**| CSV format list | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **only_defaults** | **str**| filter to only defaults | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| usage end UNIX timestamp | [optional] 
 **usage_start** | **str**| usage start UNIX timestamp | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| fill in usage | [optional] 
 **with_deleted** | **str**| return deleted associations | [optional] 
 **with_raw_qos** | **str**| return a raw qos or delta_qos | [optional] 
 **with_sub_accts** | **str**| return sub acct information also | [optional] 
 **without_parent_info** | **str**| don&#39;t give me parent id/name | [optional] 
 **without_parent_limits** | **str**| don&#39;t give me limits from parents | [optional] 

### Return type

[**V0040OpenapiAssocsRemovedResp**](V0040OpenapiAssocsRemovedResp.md)

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

# **slurmdb_v0040_delete_cluster**
> V0040OpenapiClustersRemovedResp slurmdb_v0040_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Delete cluster

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_clusters_removed_resp import V0040OpenapiClustersRemovedResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str |  (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str |  (optional)
    format = 'format_example' # str | CSV format list (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end UNIX timestamp (seconds) (optional)
    usage_start = 'usage_start_example' # str | Usage start UNIX timestamp (seconds) (optional)
    with_deleted = 'with_deleted_example' # str | include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | query usage (optional)

    try:
        # Delete cluster
        api_response = api_instance.slurmdb_v0040_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0040_delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**|  | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**|  | [optional] 
 **format** | **str**| CSV format list | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end UNIX timestamp (seconds) | [optional] 
 **usage_start** | **str**| Usage start UNIX timestamp (seconds) | [optional] 
 **with_deleted** | **str**| include deleted clusters | [optional] 
 **with_usage** | **str**| query usage | [optional] 

### Return type

[**V0040OpenapiClustersRemovedResp**](V0040OpenapiClustersRemovedResp.md)

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

# **slurmdb_v0040_delete_single_qos**
> V0040OpenapiSlurmdbdQosRemovedResp slurmdb_v0040_delete_single_qos(qos)

Delete QOS

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_slurmdbd_qos_removed_resp import V0040OpenapiSlurmdbdQosRemovedResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name

    try:
        # Delete QOS
        api_response = api_instance.slurmdb_v0040_delete_single_qos(qos)
        print("The response of SlurmdbApi->slurmdb_v0040_delete_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_delete_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 

### Return type

[**V0040OpenapiSlurmdbdQosRemovedResp**](V0040OpenapiSlurmdbdQosRemovedResp.md)

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

# **slurmdb_v0040_delete_user**
> V0040OpenapiResp slurmdb_v0040_delete_user(name)

Delete user

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
    api_instance = openapi_client.SlurmdbApi(api_client)
    name = 'name_example' # str | User name

    try:
        # Delete user
        api_response = api_instance.slurmdb_v0040_delete_user(name)
        print("The response of SlurmdbApi->slurmdb_v0040_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 

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
**200** | User deleted |  -  |
**0** | User not found or unable to delete user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_delete_wckey**
> V0040OpenapiWckeyRemovedResp slurmdb_v0040_delete_wckey(id)

Delete wckey

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_wckey_removed_resp import V0040OpenapiWckeyRemovedResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    id = 'id_example' # str | wckey id

    try:
        # Delete wckey
        api_response = api_instance.slurmdb_v0040_delete_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0040_delete_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_delete_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| wckey id | 

### Return type

[**V0040OpenapiWckeyRemovedResp**](V0040OpenapiWckeyRemovedResp.md)

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

# **slurmdb_v0040_get_account**
> V0040OpenapiAccountsResp slurmdb_v0040_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)

Get account info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_accounts_resp import V0040OpenapiAccountsResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name
    with_assocs = 'with_assocs_example' # str | include associations (optional)
    with_coords = 'with_coords_example' # str | include coordinators (optional)
    with_deleted = 'with_deleted_example' # str | include deleted (optional)

    try:
        # Get account info
        api_response = api_instance.slurmdb_v0040_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0040_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 
 **with_assocs** | **str**| include associations | [optional] 
 **with_coords** | **str**| include coordinators | [optional] 
 **with_deleted** | **str**| include deleted | [optional] 

### Return type

[**V0040OpenapiAccountsResp**](V0040OpenapiAccountsResp.md)

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

# **slurmdb_v0040_get_accounts**
> V0040OpenapiAccountsResp slurmdb_v0040_get_accounts(description=description, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)

Get account list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_accounts_resp import V0040OpenapiAccountsResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    with_assocs = 'with_assocs_example' # str | include associations (optional)
    with_coords = 'with_coords_example' # str | include coordinators (optional)
    with_deleted = 'with_deleted_example' # str | include deleted accounts (optional)

    try:
        # Get account list
        api_response = api_instance.slurmdb_v0040_get_accounts(description=description, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0040_get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **with_assocs** | **str**| include associations | [optional] 
 **with_coords** | **str**| include coordinators | [optional] 
 **with_deleted** | **str**| include deleted accounts | [optional] 

### Return type

[**V0040OpenapiAccountsResp**](V0040OpenapiAccountsResp.md)

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

# **slurmdb_v0040_get_association**
> V0040OpenapiAssocsResp slurmdb_v0040_get_association(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)

Get association info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_assocs_resp import V0040OpenapiAssocsResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    format = 'format_example' # str | CSV format list (optional)
    id = 'id_example' # str | CSV id list (optional)
    only_defaults = 'only_defaults_example' # str | filter to only defaults (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | usage end UNIX timestamp (optional)
    usage_start = 'usage_start_example' # str | usage start UNIX timestamp (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | fill in usage (optional)
    with_deleted = 'with_deleted_example' # str | return deleted associations (optional)
    with_raw_qos = 'with_raw_qos_example' # str | return a raw qos or delta_qos (optional)
    with_sub_accts = 'with_sub_accts_example' # str | return sub acct information also (optional)
    without_parent_info = 'without_parent_info_example' # str | don't give me parent id/name (optional)
    without_parent_limits = 'without_parent_limits_example' # str | don't give me limits from parents (optional)

    try:
        # Get association info
        api_response = api_instance.slurmdb_v0040_get_association(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)
        print("The response of SlurmdbApi->slurmdb_v0040_get_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **format** | **str**| CSV format list | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **only_defaults** | **str**| filter to only defaults | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| usage end UNIX timestamp | [optional] 
 **usage_start** | **str**| usage start UNIX timestamp | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| fill in usage | [optional] 
 **with_deleted** | **str**| return deleted associations | [optional] 
 **with_raw_qos** | **str**| return a raw qos or delta_qos | [optional] 
 **with_sub_accts** | **str**| return sub acct information also | [optional] 
 **without_parent_info** | **str**| don&#39;t give me parent id/name | [optional] 
 **without_parent_limits** | **str**| don&#39;t give me limits from parents | [optional] 

### Return type

[**V0040OpenapiAssocsResp**](V0040OpenapiAssocsResp.md)

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

# **slurmdb_v0040_get_associations**
> V0040OpenapiAssocsResp slurmdb_v0040_get_associations(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)

Get association list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_assocs_resp import V0040OpenapiAssocsResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    format = 'format_example' # str | CSV format list (optional)
    id = 'id_example' # str | CSV id list (optional)
    only_defaults = 'only_defaults_example' # str | filter to only defaults (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | usage end UNIX timestamp (optional)
    usage_start = 'usage_start_example' # str | usage start UNIX timestamp (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | fill in usage (optional)
    with_deleted = 'with_deleted_example' # str | return deleted associations (optional)
    with_raw_qos = 'with_raw_qos_example' # str | return a raw qos or delta_qos (optional)
    with_sub_accts = 'with_sub_accts_example' # str | return sub acct information also (optional)
    without_parent_info = 'without_parent_info_example' # str | don't give me parent id/name (optional)
    without_parent_limits = 'without_parent_limits_example' # str | don't give me limits from parents (optional)

    try:
        # Get association list
        api_response = api_instance.slurmdb_v0040_get_associations(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)
        print("The response of SlurmdbApi->slurmdb_v0040_get_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **format** | **str**| CSV format list | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **only_defaults** | **str**| filter to only defaults | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| usage end UNIX timestamp | [optional] 
 **usage_start** | **str**| usage start UNIX timestamp | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| fill in usage | [optional] 
 **with_deleted** | **str**| return deleted associations | [optional] 
 **with_raw_qos** | **str**| return a raw qos or delta_qos | [optional] 
 **with_sub_accts** | **str**| return sub acct information also | [optional] 
 **without_parent_info** | **str**| don&#39;t give me parent id/name | [optional] 
 **without_parent_limits** | **str**| don&#39;t give me limits from parents | [optional] 

### Return type

[**V0040OpenapiAssocsResp**](V0040OpenapiAssocsResp.md)

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

# **slurmdb_v0040_get_cluster**
> V0040OpenapiClustersResp slurmdb_v0040_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Get cluster info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_clusters_resp import V0040OpenapiClustersResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str |  (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str |  (optional)
    format = 'format_example' # str | CSV format list (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end UNIX timestamp (seconds) (optional)
    usage_start = 'usage_start_example' # str | Usage start UNIX timestamp (seconds) (optional)
    with_deleted = 'with_deleted_example' # str | include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | query usage (optional)

    try:
        # Get cluster info
        api_response = api_instance.slurmdb_v0040_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0040_get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**|  | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**|  | [optional] 
 **format** | **str**| CSV format list | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end UNIX timestamp (seconds) | [optional] 
 **usage_start** | **str**| Usage start UNIX timestamp (seconds) | [optional] 
 **with_deleted** | **str**| include deleted clusters | [optional] 
 **with_usage** | **str**| query usage | [optional] 

### Return type

[**V0040OpenapiClustersResp**](V0040OpenapiClustersResp.md)

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

# **slurmdb_v0040_get_clusters**
> V0040OpenapiClustersResp slurmdb_v0040_get_clusters(classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Get cluster list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_clusters_resp import V0040OpenapiClustersResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    classification = 'classification_example' # str |  (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str |  (optional)
    format = 'format_example' # str | CSV format list (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end UNIX timestamp (seconds) (optional)
    usage_start = 'usage_start_example' # str | Usage start UNIX timestamp (seconds) (optional)
    with_deleted = 'with_deleted_example' # str | include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | query usage (optional)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0040_get_clusters(classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0040_get_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification** | **str**|  | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**|  | [optional] 
 **format** | **str**| CSV format list | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end UNIX timestamp (seconds) | [optional] 
 **usage_start** | **str**| Usage start UNIX timestamp (seconds) | [optional] 
 **with_deleted** | **str**| include deleted clusters | [optional] 
 **with_usage** | **str**| query usage | [optional] 

### Return type

[**V0040OpenapiClustersResp**](V0040OpenapiClustersResp.md)

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

# **slurmdb_v0040_get_config**
> V0040OpenapiSlurmdbdConfigResp slurmdb_v0040_get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_slurmdbd_config_resp import V0040OpenapiSlurmdbdConfigResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)

    try:
        # Dump all configuration information
        api_response = api_instance.slurmdb_v0040_get_config()
        print("The response of SlurmdbApi->slurmdb_v0040_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0040OpenapiSlurmdbdConfigResp**](V0040OpenapiSlurmdbdConfigResp.md)

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

# **slurmdb_v0040_get_diag**
> V0040OpenapiSlurmdbdStatsResp slurmdb_v0040_get_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_slurmdbd_stats_resp import V0040OpenapiSlurmdbdStatsResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)

    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdb_v0040_get_diag()
        print("The response of SlurmdbApi->slurmdb_v0040_get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0040OpenapiSlurmdbdStatsResp**](V0040OpenapiSlurmdbdStatsResp.md)

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

# **slurmdb_v0040_get_instance**
> V0040OpenapiInstancesResp slurmdb_v0040_get_instance(cluster=cluster, extra=extra, instance_id=instance_id, instance_type=instance_type)

Get instance info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_instances_resp import V0040OpenapiInstancesResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    extra = 'extra_example' # str | Arbitrary string (optional)
    instance_id = 'instance_id_example' # str | Cloud instance ID (optional)
    instance_type = 'instance_type_example' # str | Cloud instance type (optional)

    try:
        # Get instance info
        api_response = api_instance.slurmdb_v0040_get_instance(cluster=cluster, extra=extra, instance_id=instance_id, instance_type=instance_type)
        print("The response of SlurmdbApi->slurmdb_v0040_get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **extra** | **str**| Arbitrary string | [optional] 
 **instance_id** | **str**| Cloud instance ID | [optional] 
 **instance_type** | **str**| Cloud instance type | [optional] 

### Return type

[**V0040OpenapiInstancesResp**](V0040OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | Instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_get_instances**
> V0040OpenapiInstancesResp slurmdb_v0040_get_instances(cluster=cluster, extra=extra, instance_id=instance_id, instance_type=instance_type)

Get instance list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_instances_resp import V0040OpenapiInstancesResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | Cluster name (optional)
    extra = 'extra_example' # str | Arbitrary string (optional)
    instance_id = 'instance_id_example' # str | Cloud instance ID (optional)
    instance_type = 'instance_type_example' # str | Cloud instance type (optional)

    try:
        # Get instance list
        api_response = api_instance.slurmdb_v0040_get_instances(cluster=cluster, extra=extra, instance_id=instance_id, instance_type=instance_type)
        print("The response of SlurmdbApi->slurmdb_v0040_get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional] 
 **extra** | **str**| Arbitrary string | [optional] 
 **instance_id** | **str**| Cloud instance ID | [optional] 
 **instance_type** | **str**| Cloud instance type | [optional] 

### Return type

[**V0040OpenapiInstancesResp**](V0040OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | Instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_get_job**
> V0040OpenapiSlurmdbdJobsResp slurmdb_v0040_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_slurmdbd_jobs_resp import V0040OpenapiSlurmdbdJobsResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    job_id = 'job_id_example' # str | Job id

    try:
        # Get job info
        api_response = api_instance.slurmdb_v0040_get_job(job_id)
        print("The response of SlurmdbApi->slurmdb_v0040_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job id | 

### Return type

[**V0040OpenapiSlurmdbdJobsResp**](V0040OpenapiSlurmdbdJobsResp.md)

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

# **slurmdb_v0040_get_jobs**
> V0040OpenapiSlurmdbdJobsResp slurmdb_v0040_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, timelimit_max=timelimit_max, timelimit_min=timelimit_min, end_time=end_time, start_time=start_time, submit_time=submit_time, node=node, users=users, wckey=wckey)

Get job list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_slurmdbd_jobs_resp import V0040OpenapiSlurmdbdJobsResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV account list (optional)
    association = 'association_example' # str | CSV association list (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    constraints = 'constraints_example' # str | CSV constraint list (optional)
    cpus_max = 'cpus_max_example' # str | number of cpus high range (optional)
    cpus_min = 'cpus_min_example' # str | number of cpus low range (optional)
    scheduler_unset = 'scheduler_unset_example' # str |  (optional)
    scheduled_on_submit = 'scheduled_on_submit_example' # str |  (optional)
    scheduled_by_main = 'scheduled_by_main_example' # str |  (optional)
    scheduled_by_backfill = 'scheduled_by_backfill_example' # str |  (optional)
    job_started = 'job_started_example' # str |  (optional)
    exit_code = 'exit_code_example' # str | job exit code (numeric) (optional)
    show_duplicates = 'show_duplicates_example' # str |  (optional)
    skip_steps = 'skip_steps_example' # str |  (optional)
    disable_truncate_usage_time = 'disable_truncate_usage_time_example' # str |  (optional)
    whole_hetjob = 'whole_hetjob_example' # str |  (optional)
    disable_whole_hetjob = 'disable_whole_hetjob_example' # str |  (optional)
    disable_wait_for_result = 'disable_wait_for_result_example' # str |  (optional)
    usage_time_as_submit_time = 'usage_time_as_submit_time_example' # str |  (optional)
    show_batch_script = 'show_batch_script_example' # str |  (optional)
    show_job_environment = 'show_job_environment_example' # str |  (optional)
    format = 'format_example' # str | CSV format list (optional)
    groups = 'groups_example' # str | CSV group list (optional)
    job_name = 'job_name_example' # str | CSV job name list (optional)
    nodes_max = 'nodes_max_example' # str | number of nodes high range (optional)
    nodes_min = 'nodes_min_example' # str | number of nodes low range (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS name list (optional)
    reason = 'reason_example' # str | CSV reason list (optional)
    reservation = 'reservation_example' # str | CSV reservation name list (optional)
    reservation_id = 'reservation_id_example' # str | CSV reservation ID list (optional)
    state = 'state_example' # str | CSV state list (optional)
    step = 'step_example' # str | CSV step id list (optional)
    timelimit_max = 'timelimit_max_example' # str | maximum timelimit (seconds) (optional)
    timelimit_min = 'timelimit_min_example' # str | minimum timelimit (seconds) (optional)
    end_time = 'end_time_example' # str | usage end timestamp (optional)
    start_time = 'start_time_example' # str | usage start timestamp (optional)
    submit_time = 'submit_time_example' # str | submit time timestamp (optional)
    node = 'node_example' # str | ranged node string where jobs ran (optional)
    users = 'users_example' # str | CSV user name list (optional)
    wckey = 'wckey_example' # str | CSV wckey list (optional)

    try:
        # Get job list
        api_response = api_instance.slurmdb_v0040_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, timelimit_max=timelimit_max, timelimit_min=timelimit_min, end_time=end_time, start_time=start_time, submit_time=submit_time, node=node, users=users, wckey=wckey)
        print("The response of SlurmdbApi->slurmdb_v0040_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV account list | [optional] 
 **association** | **str**| CSV association list | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **constraints** | **str**| CSV constraint list | [optional] 
 **cpus_max** | **str**| number of cpus high range | [optional] 
 **cpus_min** | **str**| number of cpus low range | [optional] 
 **scheduler_unset** | **str**|  | [optional] 
 **scheduled_on_submit** | **str**|  | [optional] 
 **scheduled_by_main** | **str**|  | [optional] 
 **scheduled_by_backfill** | **str**|  | [optional] 
 **job_started** | **str**|  | [optional] 
 **exit_code** | **str**| job exit code (numeric) | [optional] 
 **show_duplicates** | **str**|  | [optional] 
 **skip_steps** | **str**|  | [optional] 
 **disable_truncate_usage_time** | **str**|  | [optional] 
 **whole_hetjob** | **str**|  | [optional] 
 **disable_whole_hetjob** | **str**|  | [optional] 
 **disable_wait_for_result** | **str**|  | [optional] 
 **usage_time_as_submit_time** | **str**|  | [optional] 
 **show_batch_script** | **str**|  | [optional] 
 **show_job_environment** | **str**|  | [optional] 
 **format** | **str**| CSV format list | [optional] 
 **groups** | **str**| CSV group list | [optional] 
 **job_name** | **str**| CSV job name list | [optional] 
 **nodes_max** | **str**| number of nodes high range | [optional] 
 **nodes_min** | **str**| number of nodes low range | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS name list | [optional] 
 **reason** | **str**| CSV reason list | [optional] 
 **reservation** | **str**| CSV reservation name list | [optional] 
 **reservation_id** | **str**| CSV reservation ID list | [optional] 
 **state** | **str**| CSV state list | [optional] 
 **step** | **str**| CSV step id list | [optional] 
 **timelimit_max** | **str**| maximum timelimit (seconds) | [optional] 
 **timelimit_min** | **str**| minimum timelimit (seconds) | [optional] 
 **end_time** | **str**| usage end timestamp | [optional] 
 **start_time** | **str**| usage start timestamp | [optional] 
 **submit_time** | **str**| submit time timestamp | [optional] 
 **node** | **str**| ranged node string where jobs ran | [optional] 
 **users** | **str**| CSV user name list | [optional] 
 **wckey** | **str**| CSV wckey list | [optional] 

### Return type

[**V0040OpenapiSlurmdbdJobsResp**](V0040OpenapiSlurmdbdJobsResp.md)

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

# **slurmdb_v0040_get_qos**
> V0040OpenapiSlurmdbdQosResp slurmdb_v0040_get_qos(description=description, id=id, format=format, name=name, preempt_mode=preempt_mode, with_deleted=with_deleted)

Get QOS list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_slurmdbd_qos_resp import V0040OpenapiSlurmdbdQosResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    format = 'format_example' # str | CSV format list (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str |  (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted QOS (optional)

    try:
        # Get QOS list
        api_response = api_instance.slurmdb_v0040_get_qos(description=description, id=id, format=format, name=name, preempt_mode=preempt_mode, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0040_get_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **format** | **str**| CSV format list | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**|  | [optional] 
 **with_deleted** | **str**| Include deleted QOS | [optional] 

### Return type

[**V0040OpenapiSlurmdbdQosResp**](V0040OpenapiSlurmdbdQosResp.md)

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

# **slurmdb_v0040_get_single_qos**
> V0040OpenapiSlurmdbdQosResp slurmdb_v0040_get_single_qos(qos, with_deleted=with_deleted)

Get QOS info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_slurmdbd_qos_resp import V0040OpenapiSlurmdbdQosResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name
    with_deleted = 'with_deleted_example' # str | Query includes deleted QOS (optional)

    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0040_get_single_qos(qos, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0040_get_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 
 **with_deleted** | **str**| Query includes deleted QOS | [optional] 

### Return type

[**V0040OpenapiSlurmdbdQosResp**](V0040OpenapiSlurmdbdQosResp.md)

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

# **slurmdb_v0040_get_tres**
> V0040OpenapiTresResp slurmdb_v0040_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_tres_resp import V0040OpenapiTresResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)

    try:
        # Get TRES info
        api_response = api_instance.slurmdb_v0040_get_tres()
        print("The response of SlurmdbApi->slurmdb_v0040_get_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_tres: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0040OpenapiTresResp**](V0040OpenapiTresResp.md)

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

# **slurmdb_v0040_get_user**
> V0040OpenapiUsersResp slurmdb_v0040_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)

Get user info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_users_resp import V0040OpenapiUsersResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    name = 'name_example' # str | User name
    with_deleted = 'with_deleted_example' # str | Include deleted users (optional)
    with_assocs = 'with_assocs_example' # str | Include assocations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_wckeys = 'with_wckeys_example' # str | Include wckeys (optional)

    try:
        # Get user info
        api_response = api_instance.slurmdb_v0040_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)
        print("The response of SlurmdbApi->slurmdb_v0040_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 
 **with_deleted** | **str**| Include deleted users | [optional] 
 **with_assocs** | **str**| Include assocations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_wckeys** | **str**| Include wckeys | [optional] 

### Return type

[**V0040OpenapiUsersResp**](V0040OpenapiUsersResp.md)

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

# **slurmdb_v0040_get_users**
> V0040OpenapiUsersResp slurmdb_v0040_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)

Get user list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_users_resp import V0040OpenapiUsersResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    admin_level = 'admin_level_example' # str | Administrator level (optional)
    default_account = 'default_account_example' # str | CSV default account list (optional)
    default_wckey = 'default_wckey_example' # str | CSV default wckey list (optional)
    with_assocs = 'with_assocs_example' # str | With associations (optional)
    with_coords = 'with_coords_example' # str | With coordinators (optional)
    with_deleted = 'with_deleted_example' # str | With deleted (optional)
    with_wckeys = 'with_wckeys_example' # str | With wckeys (optional)
    without_defaults = 'without_defaults_example' # str | Exclude defaults (optional)

    try:
        # Get user list
        api_response = api_instance.slurmdb_v0040_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)
        print("The response of SlurmdbApi->slurmdb_v0040_get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_level** | **str**| Administrator level | [optional] 
 **default_account** | **str**| CSV default account list | [optional] 
 **default_wckey** | **str**| CSV default wckey list | [optional] 
 **with_assocs** | **str**| With associations | [optional] 
 **with_coords** | **str**| With coordinators | [optional] 
 **with_deleted** | **str**| With deleted | [optional] 
 **with_wckeys** | **str**| With wckeys | [optional] 
 **without_defaults** | **str**| Exclude defaults | [optional] 

### Return type

[**V0040OpenapiUsersResp**](V0040OpenapiUsersResp.md)

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

# **slurmdb_v0040_get_wckey**
> V0040OpenapiWckeyResp slurmdb_v0040_get_wckey(id)

Get wckey info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_wckey_resp import V0040OpenapiWckeyResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    id = 'id_example' # str | wckey id

    try:
        # Get wckey info
        api_response = api_instance.slurmdb_v0040_get_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0040_get_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| wckey id | 

### Return type

[**V0040OpenapiWckeyResp**](V0040OpenapiWckeyResp.md)

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

# **slurmdb_v0040_get_wckeys**
> V0040OpenapiWckeyResp slurmdb_v0040_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)

Get wckey list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_wckey_resp import V0040OpenapiWckeyResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    format = 'format_example' # str | CSV format name list (optional)
    id = 'id_example' # str | CSV id list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | only query defaults (optional)
    usage_end = 'usage_end_example' # str | usage end UNIX timestamp (seconds) (optional)
    usage_start = 'usage_start_example' # str | usage start UNIX timestamp (seconds) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | include usage with query (optional)
    with_deleted = 'with_deleted_example' # str | include deleted wckeys with query (optional)

    try:
        # Get wckey list
        api_response = api_instance.slurmdb_v0040_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0040_get_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_get_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **format** | **str**| CSV format name list | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| only query defaults | [optional] 
 **usage_end** | **str**| usage end UNIX timestamp (seconds) | [optional] 
 **usage_start** | **str**| usage start UNIX timestamp (seconds) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| include usage with query | [optional] 
 **with_deleted** | **str**| include deleted wckeys with query | [optional] 

### Return type

[**V0040OpenapiWckeyResp**](V0040OpenapiWckeyResp.md)

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

# **slurmdb_v0040_post_accounts**
> V0040OpenapiResp slurmdb_v0040_post_accounts(v0040_openapi_accounts_resp)

Update accounts

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_accounts_resp import V0040OpenapiAccountsResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_accounts_resp = openapi_client.V0040OpenapiAccountsResp() # V0040OpenapiAccountsResp | update/create accounts

    try:
        # Update accounts
        api_response = api_instance.slurmdb_v0040_post_accounts(v0040_openapi_accounts_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_accounts_resp** | [**V0040OpenapiAccountsResp**](V0040OpenapiAccountsResp.md)| update/create accounts | 

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
**200** | Add/update list of accounts |  -  |
**0** | Unable to add or update accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_post_accounts_association**
> V0040OpenapiAccountsAddCondRespStr slurmdb_v0040_post_accounts_association(v0040_openapi_accounts_add_cond_resp)

Add accounts with conditional association

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_accounts_add_cond_resp import V0040OpenapiAccountsAddCondResp
from openapi_client.models.v0040_openapi_accounts_add_cond_resp_str import V0040OpenapiAccountsAddCondRespStr
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_accounts_add_cond_resp = openapi_client.V0040OpenapiAccountsAddCondResp() # V0040OpenapiAccountsAddCondResp | Create accounts with conditional association

    try:
        # Add accounts with conditional association
        api_response = api_instance.slurmdb_v0040_post_accounts_association(v0040_openapi_accounts_add_cond_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_accounts_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_accounts_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_accounts_add_cond_resp** | [**V0040OpenapiAccountsAddCondResp**](V0040OpenapiAccountsAddCondResp.md)| Create accounts with conditional association | 

### Return type

[**V0040OpenapiAccountsAddCondRespStr**](V0040OpenapiAccountsAddCondRespStr.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add list of accounts with conditional association |  -  |
**0** | Unable to add accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_post_associations**
> V0040OpenapiResp slurmdb_v0040_post_associations(v0040_openapi_assocs_resp)

Set associations info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_assocs_resp import V0040OpenapiAssocsResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_assocs_resp = openapi_client.V0040OpenapiAssocsResp() # V0040OpenapiAssocsResp | Add or update associations

    try:
        # Set associations info
        api_response = api_instance.slurmdb_v0040_post_associations(v0040_openapi_assocs_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_assocs_resp** | [**V0040OpenapiAssocsResp**](V0040OpenapiAssocsResp.md)| Add or update associations | 

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
**200** | status of associations update |  -  |
**0** | Unable to update associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_post_clusters**
> V0040OpenapiResp slurmdb_v0040_post_clusters(v0040_openapi_clusters_resp)

update clusters

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_clusters_resp import V0040OpenapiClustersResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_clusters_resp = openapi_client.V0040OpenapiClustersResp() # V0040OpenapiClustersResp | Add or modify clusters

    try:
        # update clusters
        api_response = api_instance.slurmdb_v0040_post_clusters(v0040_openapi_clusters_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_clusters_resp** | [**V0040OpenapiClustersResp**](V0040OpenapiClustersResp.md)| Add or modify clusters | 

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
**200** | Modify clusters response |  -  |
**0** | Unable to add cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_post_config**
> V0040OpenapiResp slurmdb_v0040_post_config(v0040_openapi_slurmdbd_config_resp=v0040_openapi_slurmdbd_config_resp)

Load all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.models.v0040_openapi_slurmdbd_config_resp import V0040OpenapiSlurmdbdConfigResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_slurmdbd_config_resp = openapi_client.V0040OpenapiSlurmdbdConfigResp() # V0040OpenapiSlurmdbdConfigResp | Add or update config (optional)

    try:
        # Load all configuration information
        api_response = api_instance.slurmdb_v0040_post_config(v0040_openapi_slurmdbd_config_resp=v0040_openapi_slurmdbd_config_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_slurmdbd_config_resp** | [**V0040OpenapiSlurmdbdConfigResp**](V0040OpenapiSlurmdbdConfigResp.md)| Add or update config | [optional] 

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
**200** | Load config |  -  |
**0** | Unable to set config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_post_qos**
> V0040OpenapiResp slurmdb_v0040_post_qos(v0040_openapi_slurmdbd_qos_resp)

Set QOS info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.models.v0040_openapi_slurmdbd_qos_resp import V0040OpenapiSlurmdbdQosResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_slurmdbd_qos_resp = openapi_client.V0040OpenapiSlurmdbdQosResp() # V0040OpenapiSlurmdbdQosResp | Add or update QOSs

    try:
        # Set QOS info
        api_response = api_instance.slurmdb_v0040_post_qos(v0040_openapi_slurmdbd_qos_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_slurmdbd_qos_resp** | [**V0040OpenapiSlurmdbdQosResp**](V0040OpenapiSlurmdbdQosResp.md)| Add or update QOSs | 

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
**200** | QOS update response |  -  |
**0** | Unable to update QOSs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_post_tres**
> V0040OpenapiResp slurmdb_v0040_post_tres(v0040_openapi_tres_resp)

Set TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.models.v0040_openapi_tres_resp import V0040OpenapiTresResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_tres_resp = openapi_client.V0040OpenapiTresResp() # V0040OpenapiTresResp | Add or Update TRES

    try:
        # Set TRES info
        api_response = api_instance.slurmdb_v0040_post_tres(v0040_openapi_tres_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_tres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_tres_resp** | [**V0040OpenapiTresResp**](V0040OpenapiTresResp.md)| Add or Update TRES | 

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
**200** | List of TRES |  -  |
**0** | Unable to update TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_post_users**
> V0040OpenapiResp slurmdb_v0040_post_users(v0040_openapi_users_resp)

Update user

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.models.v0040_openapi_users_resp import V0040OpenapiUsersResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_users_resp = openapi_client.V0040OpenapiUsersResp() # V0040OpenapiUsersResp | add or update user

    try:
        # Update user
        api_response = api_instance.slurmdb_v0040_post_users(v0040_openapi_users_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_users_resp** | [**V0040OpenapiUsersResp**](V0040OpenapiUsersResp.md)| add or update user | 

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
**200** | Update users |  -  |
**0** | User not found or not able to update user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_post_users_association**
> V0040OpenapiUsersAddCondRespStr slurmdb_v0040_post_users_association(v0040_openapi_users_add_cond_resp)

Add users with conditional association

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_users_add_cond_resp import V0040OpenapiUsersAddCondResp
from openapi_client.models.v0040_openapi_users_add_cond_resp_str import V0040OpenapiUsersAddCondRespStr
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_users_add_cond_resp = openapi_client.V0040OpenapiUsersAddCondResp() # V0040OpenapiUsersAddCondResp | Create users with conditional association

    try:
        # Add users with conditional association
        api_response = api_instance.slurmdb_v0040_post_users_association(v0040_openapi_users_add_cond_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_users_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_users_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_users_add_cond_resp** | [**V0040OpenapiUsersAddCondResp**](V0040OpenapiUsersAddCondResp.md)| Create users with conditional association | 

### Return type

[**V0040OpenapiUsersAddCondRespStr**](V0040OpenapiUsersAddCondRespStr.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add list of users with conditional association |  -  |
**0** | Unable to add accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0040_post_wckeys**
> V0040OpenapiResp slurmdb_v0040_post_wckeys(v0040_openapi_wckey_resp=v0040_openapi_wckey_resp)

Add wckeys

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.models.v0040_openapi_wckey_resp import V0040OpenapiWckeyResp
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
    api_instance = openapi_client.SlurmdbApi(api_client)
    v0040_openapi_wckey_resp = openapi_client.V0040OpenapiWckeyResp() # V0040OpenapiWckeyResp | add wckeys (optional)

    try:
        # Add wckeys
        api_response = api_instance.slurmdb_v0040_post_wckeys(v0040_openapi_wckey_resp=v0040_openapi_wckey_resp)
        print("The response of SlurmdbApi->slurmdb_v0040_post_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0040_post_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_openapi_wckey_resp** | [**V0040OpenapiWckeyResp**](V0040OpenapiWckeyResp.md)| add wckeys | [optional] 

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
**200** | List of wckeys |  -  |
**0** | Unable to add wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

