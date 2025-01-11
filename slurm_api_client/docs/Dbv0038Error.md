# Dbv0038Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_number** | **int** | Slurm internal error number | [optional] 
**error** | **str** | Error message | [optional] 
**source** | **str** | Where error occurred in the source | [optional] 
**description** | **str** | Explanation of cause of error | [optional] 

## Example

```python
from openapi_client.models.dbv0038_error import Dbv0038Error

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038Error from a JSON string
dbv0038_error_instance = Dbv0038Error.from_json(json)
# print the JSON string representation of the object
print(Dbv0038Error.to_json())

# convert the object into a dict
dbv0038_error_dict = dbv0038_error_instance.to_dict()
# create an instance of Dbv0038Error from a dict
dbv0038_error_from_dict = Dbv0038Error.from_dict(dbv0038_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


