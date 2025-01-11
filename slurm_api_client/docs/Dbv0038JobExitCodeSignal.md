# Dbv0038JobExitCodeSignal

Signal details (if signaled)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signal_id** | **int** | Signal number process received | [optional] 
**name** | **str** | Name of signal received | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_exit_code_signal import Dbv0038JobExitCodeSignal

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobExitCodeSignal from a JSON string
dbv0038_job_exit_code_signal_instance = Dbv0038JobExitCodeSignal.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobExitCodeSignal.to_json())

# convert the object into a dict
dbv0038_job_exit_code_signal_dict = dbv0038_job_exit_code_signal_instance.to_dict()
# create an instance of Dbv0038JobExitCodeSignal from a dict
dbv0038_job_exit_code_signal_from_dict = Dbv0038JobExitCodeSignal.from_dict(dbv0038_job_exit_code_signal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


