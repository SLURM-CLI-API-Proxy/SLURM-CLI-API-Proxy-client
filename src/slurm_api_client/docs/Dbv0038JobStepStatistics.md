# Dbv0038JobStepStatistics

Statistics of job step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**Dbv0038JobStepStatisticsCPU**](Dbv0038JobStepStatisticsCPU.md) |  | [optional] 
**energy** | [**Dbv0038JobStepStatisticsEnergy**](Dbv0038JobStepStatisticsEnergy.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_step_statistics import Dbv0038JobStepStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobStepStatistics from a JSON string
dbv0038_job_step_statistics_instance = Dbv0038JobStepStatistics.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobStepStatistics.to_json())

# convert the object into a dict
dbv0038_job_step_statistics_dict = dbv0038_job_step_statistics_instance.to_dict()
# create an instance of Dbv0038JobStepStatistics from a dict
dbv0038_job_step_statistics_from_dict = Dbv0038JobStepStatistics.from_dict(dbv0038_job_step_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


