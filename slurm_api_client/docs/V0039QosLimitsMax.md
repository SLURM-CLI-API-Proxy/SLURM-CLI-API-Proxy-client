# V0039QosLimitsMax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_jobs** | [**V0039QosLimitsMaxActiveJobs**](V0039QosLimitsMaxActiveJobs.md) |  | [optional] 
**tres** | [**V0039QosLimitsMaxTres**](V0039QosLimitsMaxTres.md) |  | [optional] 
**wall_clock** | [**V0039QosLimitsMaxWallClock**](V0039QosLimitsMaxWallClock.md) |  | [optional] 
**jobs** | [**V0039QosLimitsMaxJobs**](V0039QosLimitsMaxJobs.md) |  | [optional] 
**accruing** | [**V0039QosLimitsMaxJobsActiveJobs**](V0039QosLimitsMaxJobsActiveJobs.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_qos_limits_max import V0039QosLimitsMax

# TODO update the JSON string below
json = "{}"
# create an instance of V0039QosLimitsMax from a JSON string
v0039_qos_limits_max_instance = V0039QosLimitsMax.from_json(json)
# print the JSON string representation of the object
print(V0039QosLimitsMax.to_json())

# convert the object into a dict
v0039_qos_limits_max_dict = v0039_qos_limits_max_instance.to_dict()
# create an instance of V0039QosLimitsMax from a dict
v0039_qos_limits_max_from_dict = V0039QosLimitsMax.from_dict(v0039_qos_limits_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


