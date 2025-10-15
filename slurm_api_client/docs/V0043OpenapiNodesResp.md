# V0043OpenapiNodesResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[V0043Node]**](V0043Node.md) |  | 
**last_update** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | 
**meta** | [**V0043OpenapiMeta**](V0043OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0043OpenapiError]**](V0043OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0043OpenapiWarning]**](V0043OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_openapi_nodes_resp import V0043OpenapiNodesResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0043OpenapiNodesResp from a JSON string
v0043_openapi_nodes_resp_instance = V0043OpenapiNodesResp.from_json(json)
# print the JSON string representation of the object
print(V0043OpenapiNodesResp.to_json())

# convert the object into a dict
v0043_openapi_nodes_resp_dict = v0043_openapi_nodes_resp_instance.to_dict()
# create an instance of V0043OpenapiNodesResp from a dict
v0043_openapi_nodes_resp_from_dict = V0043OpenapiNodesResp.from_dict(v0043_openapi_nodes_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


