# V0042QosLimitsMax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_jobs** | [**V0042QosLimitsMaxActiveJobs**](V0042QosLimitsMaxActiveJobs.md) |  | [optional] 
**jobs** | [**V0042QosLimitsMaxJobs**](V0042QosLimitsMaxJobs.md) |  | [optional] 
**tres** | [**V0042QosLimitsMaxTres**](V0042QosLimitsMaxTres.md) |  | [optional] 
**wall_clock** | [**V0042QosLimitsMaxWallClock**](V0042QosLimitsMaxWallClock.md) |  | [optional] 
**accruing** | [**V0042QosLimitsMaxJobsActiveJobs**](V0042QosLimitsMaxJobsActiveJobs.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_qos_limits_max import V0042QosLimitsMax

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosLimitsMax from a JSON string
v0042_qos_limits_max_instance = V0042QosLimitsMax.from_json(json)
# print the JSON string representation of the object
print(V0042QosLimitsMax.to_json())

# convert the object into a dict
v0042_qos_limits_max_dict = v0042_qos_limits_max_instance.to_dict()
# create an instance of V0042QosLimitsMax from a dict
v0042_qos_limits_max_from_dict = V0042QosLimitsMax.from_dict(v0042_qos_limits_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


