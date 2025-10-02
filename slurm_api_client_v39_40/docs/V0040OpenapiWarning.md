# V0040OpenapiWarning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Long form warning description | [optional] 
**source** | **str** | Source of warning or where warning was first detected | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_warning import V0040OpenapiWarning

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiWarning from a JSON string
v0040_openapi_warning_instance = V0040OpenapiWarning.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiWarning.to_json())

# convert the object into a dict
v0040_openapi_warning_dict = v0040_openapi_warning_instance.to_dict()
# create an instance of V0040OpenapiWarning from a dict
v0040_openapi_warning_from_dict = V0040OpenapiWarning.from_dict(v0040_openapi_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


