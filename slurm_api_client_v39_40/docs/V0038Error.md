# V0038Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | error message | [optional] 
**error_number** | **int** | Slurm internal error number | [optional] 

## Example

```python
from openapi_client.models.v0038_error import V0038Error

# TODO update the JSON string below
json = "{}"
# create an instance of V0038Error from a JSON string
v0038_error_instance = V0038Error.from_json(json)
# print the JSON string representation of the object
print(V0038Error.to_json())

# convert the object into a dict
v0038_error_dict = v0038_error_instance.to_dict()
# create an instance of V0038Error from a dict
v0038_error_from_dict = V0038Error.from_dict(v0038_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


