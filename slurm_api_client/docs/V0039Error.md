# V0039Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_number** | **int** | Slurm internal error number | [optional] 
**error** | **str** | Error message | [optional] 
**source** | **str** | Where error occurred in the source | [optional] 
**description** | **str** | Explanation of cause of error | [optional] 

## Example

```python
from openapi_client.models.v0039_error import V0039Error

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Error from a JSON string
v0039_error_instance = V0039Error.from_json(json)
# print the JSON string representation of the object
print(V0039Error.to_json())

# convert the object into a dict
v0039_error_dict = v0039_error_instance.to_dict()
# create an instance of V0039Error from a dict
v0039_error_from_dict = V0039Error.from_dict(v0039_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


