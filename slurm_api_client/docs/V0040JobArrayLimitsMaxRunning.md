# V0040JobArrayLimitsMaxRunning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks** | **int** | Maximum number of simultaneously running tasks, 0 if no limit | [optional] 

## Example

```python
from openapi_client.models.v0040_job_array_limits_max_running import V0040JobArrayLimitsMaxRunning

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobArrayLimitsMaxRunning from a JSON string
v0040_job_array_limits_max_running_instance = V0040JobArrayLimitsMaxRunning.from_json(json)
# print the JSON string representation of the object
print(V0040JobArrayLimitsMaxRunning.to_json())

# convert the object into a dict
v0040_job_array_limits_max_running_dict = v0040_job_array_limits_max_running_instance.to_dict()
# create an instance of V0040JobArrayLimitsMaxRunning from a dict
v0040_job_array_limits_max_running_from_dict = V0040JobArrayLimitsMaxRunning.from_dict(v0040_job_array_limits_max_running_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


