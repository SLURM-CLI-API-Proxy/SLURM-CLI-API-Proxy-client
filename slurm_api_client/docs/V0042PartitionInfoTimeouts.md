# V0042PartitionInfoTimeouts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resume** | [**V0042Uint16NoValStruct**](V0042Uint16NoValStruct.md) |  | [optional] 
**suspend** | [**V0042Uint16NoValStruct**](V0042Uint16NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_partition_info_timeouts import V0042PartitionInfoTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of V0042PartitionInfoTimeouts from a JSON string
v0042_partition_info_timeouts_instance = V0042PartitionInfoTimeouts.from_json(json)
# print the JSON string representation of the object
print(V0042PartitionInfoTimeouts.to_json())

# convert the object into a dict
v0042_partition_info_timeouts_dict = v0042_partition_info_timeouts_instance.to_dict()
# create an instance of V0042PartitionInfoTimeouts from a dict
v0042_partition_info_timeouts_from_dict = V0042PartitionInfoTimeouts.from_dict(v0042_partition_info_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


