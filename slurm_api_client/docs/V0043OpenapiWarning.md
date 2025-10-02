# V0043OpenapiWarning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Long form warning description | [optional] 
**source** | **str** | Source of warning or where warning was first detected | [optional] 

## Example

```python
from openapi_client.models.v0043_openapi_warning import V0043OpenapiWarning

# TODO update the JSON string below
json = "{}"
# create an instance of V0043OpenapiWarning from a JSON string
v0043_openapi_warning_instance = V0043OpenapiWarning.from_json(json)
# print the JSON string representation of the object
print(V0043OpenapiWarning.to_json())

# convert the object into a dict
v0043_openapi_warning_dict = v0043_openapi_warning_instance.to_dict()
# create an instance of V0043OpenapiWarning from a dict
v0043_openapi_warning_from_dict = V0043OpenapiWarning.from_dict(v0043_openapi_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


