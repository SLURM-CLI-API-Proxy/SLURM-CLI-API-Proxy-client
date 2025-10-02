# V0042ProcessExitCodeVerbose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **List[str]** |  | [optional] 
**return_code** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**signal** | [**V0042ProcessExitCodeVerboseSignal**](V0042ProcessExitCodeVerboseSignal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_process_exit_code_verbose import V0042ProcessExitCodeVerbose

# TODO update the JSON string below
json = "{}"
# create an instance of V0042ProcessExitCodeVerbose from a JSON string
v0042_process_exit_code_verbose_instance = V0042ProcessExitCodeVerbose.from_json(json)
# print the JSON string representation of the object
print(V0042ProcessExitCodeVerbose.to_json())

# convert the object into a dict
v0042_process_exit_code_verbose_dict = v0042_process_exit_code_verbose_instance.to_dict()
# create an instance of V0042ProcessExitCodeVerbose from a dict
v0042_process_exit_code_verbose_from_dict = V0042ProcessExitCodeVerbose.from_dict(v0042_process_exit_code_verbose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


