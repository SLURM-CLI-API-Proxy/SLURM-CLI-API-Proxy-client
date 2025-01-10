# V0039Warning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warning** | **str** | Earning message | [optional] 
**source** | **str** | Where error occurred in the source | [optional] 
**description** | **str** | Explanation of cause of error | [optional] 

## Example

```python
from openapi_client.models.v0039_warning import V0039Warning

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Warning from a JSON string
v0039_warning_instance = V0039Warning.from_json(json)
# print the JSON string representation of the object
print(V0039Warning.to_json())

# convert the object into a dict
v0039_warning_dict = v0039_warning_instance.to_dict()
# create an instance of V0039Warning from a dict
v0039_warning_from_dict = V0039Warning.from_dict(v0039_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


