# Dbv0038JobStepCPURequestedFrequency

CPU frequency requested

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | Min CPU frequency | [optional] 
**max** | **int** | Max CPU frequency | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_step_cpu_requested_frequency import Dbv0038JobStepCPURequestedFrequency

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobStepCPURequestedFrequency from a JSON string
dbv0038_job_step_cpu_requested_frequency_instance = Dbv0038JobStepCPURequestedFrequency.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobStepCPURequestedFrequency.to_json())

# convert the object into a dict
dbv0038_job_step_cpu_requested_frequency_dict = dbv0038_job_step_cpu_requested_frequency_instance.to_dict()
# create an instance of Dbv0038JobStepCPURequestedFrequency from a dict
dbv0038_job_step_cpu_requested_frequency_from_dict = Dbv0038JobStepCPURequestedFrequency.from_dict(dbv0038_job_step_cpu_requested_frequency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


