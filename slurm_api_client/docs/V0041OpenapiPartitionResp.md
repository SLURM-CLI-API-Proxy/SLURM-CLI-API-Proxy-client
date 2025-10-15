# V0041OpenapiPartitionResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitions** | [**List[V0041OpenapiPartitionRespPartitionsInner]**](V0041OpenapiPartitionRespPartitionsInner.md) | List of partitions | 
**last_update** | [**V0041OpenapiPartitionRespLastUpdate**](V0041OpenapiPartitionRespLastUpdate.md) |  | 
**meta** | [**V0041OpenapiSharesRespMeta**](V0041OpenapiSharesRespMeta.md) |  | [optional] 
**errors** | [**List[V0041OpenapiSharesRespErrorsInner]**](V0041OpenapiSharesRespErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[V0041OpenapiSharesRespWarningsInner]**](V0041OpenapiSharesRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_partition_resp import V0041OpenapiPartitionResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionResp from a JSON string
v0041_openapi_partition_resp_instance = V0041OpenapiPartitionResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionResp.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_dict = v0041_openapi_partition_resp_instance.to_dict()
# create an instance of V0041OpenapiPartitionResp from a dict
v0041_openapi_partition_resp_from_dict = V0041OpenapiPartitionResp.from_dict(v0041_openapi_partition_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


