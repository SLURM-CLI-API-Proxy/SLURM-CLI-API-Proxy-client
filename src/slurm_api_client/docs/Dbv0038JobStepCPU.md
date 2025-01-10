# Dbv0038JobStepCPU

CPU properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_frequency** | [**Dbv0038JobStepCPURequestedFrequency**](Dbv0038JobStepCPURequestedFrequency.md) |  | [optional] 
**governor** | **List[str]** | CPU governor | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_step_cpu import Dbv0038JobStepCPU

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobStepCPU from a JSON string
dbv0038_job_step_cpu_instance = Dbv0038JobStepCPU.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobStepCPU.to_json())

# convert the object into a dict
dbv0038_job_step_cpu_dict = dbv0038_job_step_cpu_instance.to_dict()
# create an instance of Dbv0038JobStepCPU from a dict
dbv0038_job_step_cpu_from_dict = Dbv0038JobStepCPU.from_dict(dbv0038_job_step_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


