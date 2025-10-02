# V0040OpenapiPartitionResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitions** | [**List[V0040PartitionInfo]**](V0040PartitionInfo.md) |  | 
**last_update** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | 
**meta** | [**V0040OpenapiMeta**](V0040OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0040OpenapiError]**](V0040OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0040OpenapiWarning]**](V0040OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_partition_resp import V0040OpenapiPartitionResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiPartitionResp from a JSON string
v0040_openapi_partition_resp_instance = V0040OpenapiPartitionResp.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiPartitionResp.to_json())

# convert the object into a dict
v0040_openapi_partition_resp_dict = v0040_openapi_partition_resp_instance.to_dict()
# create an instance of V0040OpenapiPartitionResp from a dict
v0040_openapi_partition_resp_from_dict = V0040OpenapiPartitionResp.from_dict(v0040_openapi_partition_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


