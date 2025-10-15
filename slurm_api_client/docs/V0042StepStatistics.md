# V0042StepStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0040StepStatisticsCPU**](V0040StepStatisticsCPU.md) |  | [optional] 
**energy** | [**V0042StepStatisticsEnergy**](V0042StepStatisticsEnergy.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_step_statistics import V0042StepStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StepStatistics from a JSON string
v0042_step_statistics_instance = V0042StepStatistics.from_json(json)
# print the JSON string representation of the object
print(V0042StepStatistics.to_json())

# convert the object into a dict
v0042_step_statistics_dict = v0042_step_statistics_instance.to_dict()
# create an instance of V0042StepStatistics from a dict
v0042_step_statistics_from_dict = V0042StepStatistics.from_dict(v0042_step_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


