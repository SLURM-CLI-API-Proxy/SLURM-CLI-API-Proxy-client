# V0039JobExitCodeSignal

Job exited due to signal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signal_id** | **int** | signal numeric ID | [optional] 
**name** | **str** | signal name | [optional] 

## Example

```python
from openapi_client.models.v0039_job_exit_code_signal import V0039JobExitCodeSignal

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobExitCodeSignal from a JSON string
v0039_job_exit_code_signal_instance = V0039JobExitCodeSignal.from_json(json)
# print the JSON string representation of the object
print(V0039JobExitCodeSignal.to_json())

# convert the object into a dict
v0039_job_exit_code_signal_dict = v0039_job_exit_code_signal_instance.to_dict()
# create an instance of V0039JobExitCodeSignal from a dict
v0039_job_exit_code_signal_from_dict = V0039JobExitCodeSignal.from_dict(v0039_job_exit_code_signal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


