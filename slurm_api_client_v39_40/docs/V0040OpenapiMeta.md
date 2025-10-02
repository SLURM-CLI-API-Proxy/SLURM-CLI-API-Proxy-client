# V0040OpenapiMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | [**V0040OpenapiMetaPlugin**](V0040OpenapiMetaPlugin.md) |  | [optional] 
**client** | [**V0040OpenapiMetaClient**](V0040OpenapiMetaClient.md) |  | [optional] 
**command** | **List[str]** |  | [optional] 
**slurm** | [**V0040OpenapiMetaSlurm**](V0040OpenapiMetaSlurm.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_meta import V0040OpenapiMeta

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiMeta from a JSON string
v0040_openapi_meta_instance = V0040OpenapiMeta.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiMeta.to_json())

# convert the object into a dict
v0040_openapi_meta_dict = v0040_openapi_meta_instance.to_dict()
# create an instance of V0040OpenapiMeta from a dict
v0040_openapi_meta_from_dict = V0040OpenapiMeta.from_dict(v0040_openapi_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


