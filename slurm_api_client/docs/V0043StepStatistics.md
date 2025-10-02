# V0043StepStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0040StepStatisticsCPU**](V0040StepStatisticsCPU.md) |  | [optional] 
**energy** | [**V0043StepStatisticsEnergy**](V0043StepStatisticsEnergy.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_step_statistics import V0043StepStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of V0043StepStatistics from a JSON string
v0043_step_statistics_instance = V0043StepStatistics.from_json(json)
# print the JSON string representation of the object
print(V0043StepStatistics.to_json())

# convert the object into a dict
v0043_step_statistics_dict = v0043_step_statistics_instance.to_dict()
# create an instance of V0043StepStatistics from a dict
v0043_step_statistics_from_dict = V0043StepStatistics.from_dict(v0043_step_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


