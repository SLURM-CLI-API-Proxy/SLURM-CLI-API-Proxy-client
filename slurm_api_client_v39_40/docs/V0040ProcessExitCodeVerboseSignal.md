# V0040ProcessExitCodeVerboseSignal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**V0040Uint16NoVal**](V0040Uint16NoVal.md) |  | [optional] 
**name** | **str** | Signal sent to process | [optional] 

## Example

```python
from openapi_client.models.v0040_process_exit_code_verbose_signal import V0040ProcessExitCodeVerboseSignal

# TODO update the JSON string below
json = "{}"
# create an instance of V0040ProcessExitCodeVerboseSignal from a JSON string
v0040_process_exit_code_verbose_signal_instance = V0040ProcessExitCodeVerboseSignal.from_json(json)
# print the JSON string representation of the object
print(V0040ProcessExitCodeVerboseSignal.to_json())

# convert the object into a dict
v0040_process_exit_code_verbose_signal_dict = v0040_process_exit_code_verbose_signal_instance.to_dict()
# create an instance of V0040ProcessExitCodeVerboseSignal from a dict
v0040_process_exit_code_verbose_signal_from_dict = V0040ProcessExitCodeVerboseSignal.from_dict(v0040_process_exit_code_verbose_signal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


