# V0040ProcessExitCodeVerbose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **List[str]** | Status given by return code | [optional] 
**return_code** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**signal** | [**V0040ProcessExitCodeVerboseSignal**](V0040ProcessExitCodeVerboseSignal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_process_exit_code_verbose import V0040ProcessExitCodeVerbose

# TODO update the JSON string below
json = "{}"
# create an instance of V0040ProcessExitCodeVerbose from a JSON string
v0040_process_exit_code_verbose_instance = V0040ProcessExitCodeVerbose.from_json(json)
# print the JSON string representation of the object
print(V0040ProcessExitCodeVerbose.to_json())

# convert the object into a dict
v0040_process_exit_code_verbose_dict = v0040_process_exit_code_verbose_instance.to_dict()
# create an instance of V0040ProcessExitCodeVerbose from a dict
v0040_process_exit_code_verbose_from_dict = V0040ProcessExitCodeVerbose.from_dict(v0040_process_exit_code_verbose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


