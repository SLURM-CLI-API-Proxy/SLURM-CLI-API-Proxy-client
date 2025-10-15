# V0040StepStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0040StepStatisticsCPU**](V0040StepStatisticsCPU.md) |  | [optional] 
**energy** | [**V0040StepStatisticsEnergy**](V0040StepStatisticsEnergy.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_step_statistics import V0040StepStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StepStatistics from a JSON string
v0040_step_statistics_instance = V0040StepStatistics.from_json(json)
# print the JSON string representation of the object
print(V0040StepStatistics.to_json())

# convert the object into a dict
v0040_step_statistics_dict = v0040_step_statistics_instance.to_dict()
# create an instance of V0040StepStatistics from a dict
v0040_step_statistics_from_dict = V0040StepStatistics.from_dict(v0040_step_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


