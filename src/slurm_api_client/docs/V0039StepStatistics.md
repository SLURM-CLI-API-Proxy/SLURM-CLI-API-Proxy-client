# V0039StepStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0039StepStatisticsCPU**](V0039StepStatisticsCPU.md) |  | [optional] 
**energy** | [**V0039StepStatisticsEnergy**](V0039StepStatisticsEnergy.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_step_statistics import V0039StepStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of V0039StepStatistics from a JSON string
v0039_step_statistics_instance = V0039StepStatistics.from_json(json)
# print the JSON string representation of the object
print(V0039StepStatistics.to_json())

# convert the object into a dict
v0039_step_statistics_dict = v0039_step_statistics_instance.to_dict()
# create an instance of V0039StepStatistics from a dict
v0039_step_statistics_from_dict = V0039StepStatistics.from_dict(v0039_step_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


