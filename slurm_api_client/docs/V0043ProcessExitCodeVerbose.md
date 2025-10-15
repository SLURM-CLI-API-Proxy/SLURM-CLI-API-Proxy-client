# V0043ProcessExitCodeVerbose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **List[str]** | Status given by return code | [optional] 
**return_code** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**signal** | [**V0043ProcessExitCodeVerboseSignal**](V0043ProcessExitCodeVerboseSignal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_process_exit_code_verbose import V0043ProcessExitCodeVerbose

# TODO update the JSON string below
json = "{}"
# create an instance of V0043ProcessExitCodeVerbose from a JSON string
v0043_process_exit_code_verbose_instance = V0043ProcessExitCodeVerbose.from_json(json)
# print the JSON string representation of the object
print(V0043ProcessExitCodeVerbose.to_json())

# convert the object into a dict
v0043_process_exit_code_verbose_dict = v0043_process_exit_code_verbose_instance.to_dict()
# create an instance of V0043ProcessExitCodeVerbose from a dict
v0043_process_exit_code_verbose_from_dict = V0043ProcessExitCodeVerbose.from_dict(v0043_process_exit_code_verbose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


