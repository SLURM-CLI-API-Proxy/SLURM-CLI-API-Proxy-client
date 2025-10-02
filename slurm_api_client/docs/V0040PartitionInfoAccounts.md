# V0040PartitionInfoAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **str** | AllowAccounts | [optional] 
**deny** | **str** | DenyAccounts | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info_accounts import V0040PartitionInfoAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfoAccounts from a JSON string
v0040_partition_info_accounts_instance = V0040PartitionInfoAccounts.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfoAccounts.to_json())

# convert the object into a dict
v0040_partition_info_accounts_dict = v0040_partition_info_accounts_instance.to_dict()
# create an instance of V0040PartitionInfoAccounts from a dict
v0040_partition_info_accounts_from_dict = V0040PartitionInfoAccounts.from_dict(v0040_partition_info_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


