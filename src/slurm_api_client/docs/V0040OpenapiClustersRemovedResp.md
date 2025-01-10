# V0040OpenapiClustersRemovedResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_clusters** | **List[str]** |  | 
**meta** | [**V0040OpenapiMeta**](V0040OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0040OpenapiError]**](V0040OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0040OpenapiWarning]**](V0040OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_clusters_removed_resp import V0040OpenapiClustersRemovedResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiClustersRemovedResp from a JSON string
v0040_openapi_clusters_removed_resp_instance = V0040OpenapiClustersRemovedResp.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiClustersRemovedResp.to_json())

# convert the object into a dict
v0040_openapi_clusters_removed_resp_dict = v0040_openapi_clusters_removed_resp_instance.to_dict()
# create an instance of V0040OpenapiClustersRemovedResp from a dict
v0040_openapi_clusters_removed_resp_from_dict = V0040OpenapiClustersRemovedResp.from_dict(v0040_openapi_clusters_removed_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


