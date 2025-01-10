# Dbv0038JobExitCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Job exit status | [optional] 
**return_code** | **int** | Return code from parent process | [optional] 
**signal** | [**Dbv0038JobExitCodeSignal**](Dbv0038JobExitCodeSignal.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_exit_code import Dbv0038JobExitCode

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobExitCode from a JSON string
dbv0038_job_exit_code_instance = Dbv0038JobExitCode.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobExitCode.to_json())

# convert the object into a dict
dbv0038_job_exit_code_dict = dbv0038_job_exit_code_instance.to_dict()
# create an instance of Dbv0038JobExitCode from a dict
dbv0038_job_exit_code_from_dict = Dbv0038JobExitCode.from_dict(dbv0038_job_exit_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


