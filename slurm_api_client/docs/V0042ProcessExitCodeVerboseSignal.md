# V0042ProcessExitCodeVerboseSignal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**V0042Uint16NoValStruct**](V0042Uint16NoValStruct.md) |  | [optional] 
**name** | **str** | Signal sent to process (name) | [optional] 

## Example

```python
from openapi_client.models.v0042_process_exit_code_verbose_signal import V0042ProcessExitCodeVerboseSignal

# TODO update the JSON string below
json = "{}"
# create an instance of V0042ProcessExitCodeVerboseSignal from a JSON string
v0042_process_exit_code_verbose_signal_instance = V0042ProcessExitCodeVerboseSignal.from_json(json)
# print the JSON string representation of the object
print(V0042ProcessExitCodeVerboseSignal.to_json())

# convert the object into a dict
v0042_process_exit_code_verbose_signal_dict = v0042_process_exit_code_verbose_signal_instance.to_dict()
# create an instance of V0042ProcessExitCodeVerboseSignal from a dict
v0042_process_exit_code_verbose_signal_from_dict = V0042ProcessExitCodeVerboseSignal.from_dict(v0042_process_exit_code_verbose_signal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


