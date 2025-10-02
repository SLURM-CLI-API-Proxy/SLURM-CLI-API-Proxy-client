# V0043PartitionInfoAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **str** | AllowAccounts - Comma-separated list of accounts which may execute jobs in the partition | [optional] 
**deny** | **str** | DenyAccounts - Comma-separated list of accounts which may not execute jobs in the partition | [optional] 

## Example

```python
from openapi_client.models.v0043_partition_info_accounts import V0043PartitionInfoAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of V0043PartitionInfoAccounts from a JSON string
v0043_partition_info_accounts_instance = V0043PartitionInfoAccounts.from_json(json)
# print the JSON string representation of the object
print(V0043PartitionInfoAccounts.to_json())

# convert the object into a dict
v0043_partition_info_accounts_dict = v0043_partition_info_accounts_instance.to_dict()
# create an instance of V0043PartitionInfoAccounts from a dict
v0043_partition_info_accounts_from_dict = V0043PartitionInfoAccounts.from_dict(v0043_partition_info_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


