# V0043QosLimitsMax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_jobs** | [**V0043QosLimitsMaxActiveJobs**](V0043QosLimitsMaxActiveJobs.md) |  | [optional] 
**jobs** | [**V0043QosLimitsMaxJobs**](V0043QosLimitsMaxJobs.md) |  | [optional] 
**tres** | [**V0043QosLimitsMaxTres**](V0043QosLimitsMaxTres.md) |  | [optional] 
**wall_clock** | [**V0043QosLimitsMaxWallClock**](V0043QosLimitsMaxWallClock.md) |  | [optional] 
**accruing** | [**V0043QosLimitsMaxJobsActiveJobs**](V0043QosLimitsMaxJobsActiveJobs.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_qos_limits_max import V0043QosLimitsMax

# TODO update the JSON string below
json = "{}"
# create an instance of V0043QosLimitsMax from a JSON string
v0043_qos_limits_max_instance = V0043QosLimitsMax.from_json(json)
# print the JSON string representation of the object
print(V0043QosLimitsMax.to_json())

# convert the object into a dict
v0043_qos_limits_max_dict = v0043_qos_limits_max_instance.to_dict()
# create an instance of V0043QosLimitsMax from a dict
v0043_qos_limits_max_from_dict = V0043QosLimitsMax.from_dict(v0043_qos_limits_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


