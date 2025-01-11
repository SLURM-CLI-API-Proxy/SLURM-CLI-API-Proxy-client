# V0040QosLimitsMax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_jobs** | [**V0040QosLimitsMaxActiveJobs**](V0040QosLimitsMaxActiveJobs.md) |  | [optional] 
**tres** | [**V0040QosLimitsMaxTres**](V0040QosLimitsMaxTres.md) |  | [optional] 
**wall_clock** | [**V0040QosLimitsMaxWallClock**](V0040QosLimitsMaxWallClock.md) |  | [optional] 
**jobs** | [**V0040QosLimitsMaxJobs**](V0040QosLimitsMaxJobs.md) |  | [optional] 
**accruing** | [**V0040QosLimitsMaxJobsActiveJobs**](V0040QosLimitsMaxJobsActiveJobs.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_qos_limits_max import V0040QosLimitsMax

# TODO update the JSON string below
json = "{}"
# create an instance of V0040QosLimitsMax from a JSON string
v0040_qos_limits_max_instance = V0040QosLimitsMax.from_json(json)
# print the JSON string representation of the object
print(V0040QosLimitsMax.to_json())

# convert the object into a dict
v0040_qos_limits_max_dict = v0040_qos_limits_max_instance.to_dict()
# create an instance of V0040QosLimitsMax from a dict
v0040_qos_limits_max_from_dict = V0040QosLimitsMax.from_dict(v0040_qos_limits_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


