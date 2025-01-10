# V0040PartitionInfoTimeouts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resume** | [**V0040Uint16NoVal**](V0040Uint16NoVal.md) |  | [optional] 
**suspend** | [**V0040Uint16NoVal**](V0040Uint16NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info_timeouts import V0040PartitionInfoTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfoTimeouts from a JSON string
v0040_partition_info_timeouts_instance = V0040PartitionInfoTimeouts.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfoTimeouts.to_json())

# convert the object into a dict
v0040_partition_info_timeouts_dict = v0040_partition_info_timeouts_instance.to_dict()
# create an instance of V0040PartitionInfoTimeouts from a dict
v0040_partition_info_timeouts_from_dict = V0040PartitionInfoTimeouts.from_dict(v0040_partition_info_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


