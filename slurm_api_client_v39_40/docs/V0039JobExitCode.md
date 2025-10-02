# V0039JobExitCode

job exit details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | exit status | [optional] 
**return_code** | **int** | return code (numeric) | [optional] 
**signal** | [**V0039JobExitCodeSignal**](V0039JobExitCodeSignal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_job_exit_code import V0039JobExitCode

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobExitCode from a JSON string
v0039_job_exit_code_instance = V0039JobExitCode.from_json(json)
# print the JSON string representation of the object
print(V0039JobExitCode.to_json())

# convert the object into a dict
v0039_job_exit_code_dict = v0039_job_exit_code_instance.to_dict()
# create an instance of V0039JobExitCode from a dict
v0039_job_exit_code_from_dict = V0039JobExitCode.from_dict(v0039_job_exit_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


