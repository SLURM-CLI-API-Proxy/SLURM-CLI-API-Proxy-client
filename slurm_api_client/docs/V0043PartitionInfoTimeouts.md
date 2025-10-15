# V0043PartitionInfoTimeouts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resume** | [**V0043Uint16NoValStruct**](V0043Uint16NoValStruct.md) |  | [optional] 
**suspend** | [**V0043Uint16NoValStruct**](V0043Uint16NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_partition_info_timeouts import V0043PartitionInfoTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of V0043PartitionInfoTimeouts from a JSON string
v0043_partition_info_timeouts_instance = V0043PartitionInfoTimeouts.from_json(json)
# print the JSON string representation of the object
print(V0043PartitionInfoTimeouts.to_json())

# convert the object into a dict
v0043_partition_info_timeouts_dict = v0043_partition_info_timeouts_instance.to_dict()
# create an instance of V0043PartitionInfoTimeouts from a dict
v0043_partition_info_timeouts_from_dict = V0043PartitionInfoTimeouts.from_dict(v0043_partition_info_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


