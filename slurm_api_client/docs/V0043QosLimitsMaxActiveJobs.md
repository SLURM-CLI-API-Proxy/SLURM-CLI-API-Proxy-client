# V0043QosLimitsMaxActiveJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accruing** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**count** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_qos_limits_max_active_jobs import V0043QosLimitsMaxActiveJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0043QosLimitsMaxActiveJobs from a JSON string
v0043_qos_limits_max_active_jobs_instance = V0043QosLimitsMaxActiveJobs.from_json(json)
# print the JSON string representation of the object
print(V0043QosLimitsMaxActiveJobs.to_json())

# convert the object into a dict
v0043_qos_limits_max_active_jobs_dict = v0043_qos_limits_max_active_jobs_instance.to_dict()
# create an instance of V0043QosLimitsMaxActiveJobs from a dict
v0043_qos_limits_max_active_jobs_from_dict = V0043QosLimitsMaxActiveJobs.from_dict(v0043_qos_limits_max_active_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


