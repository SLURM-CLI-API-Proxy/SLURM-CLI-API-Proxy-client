# V0040OpenapiMetaClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Client source description | [optional] 
**user** | **str** | Client user (if known) | [optional] 
**group** | **str** | Client group (if known) | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_meta_client import V0040OpenapiMetaClient

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiMetaClient from a JSON string
v0040_openapi_meta_client_instance = V0040OpenapiMetaClient.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiMetaClient.to_json())

# convert the object into a dict
v0040_openapi_meta_client_dict = v0040_openapi_meta_client_instance.to_dict()
# create an instance of V0040OpenapiMetaClient from a dict
v0040_openapi_meta_client_from_dict = V0040OpenapiMetaClient.from_dict(v0040_openapi_meta_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


