# V0043QosLimitsMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**active_jobs** | [**V0043QosLimitsMaxJobsActiveJobs**](V0043QosLimitsMaxJobsActiveJobs.md) |  | [optional] 
**per** | [**V0043QosLimitsMaxJobsActiveJobsPer**](V0043QosLimitsMaxJobsActiveJobsPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_qos_limits_max_jobs import V0043QosLimitsMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0043QosLimitsMaxJobs from a JSON string
v0043_qos_limits_max_jobs_instance = V0043QosLimitsMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0043QosLimitsMaxJobs.to_json())

# convert the object into a dict
v0043_qos_limits_max_jobs_dict = v0043_qos_limits_max_jobs_instance.to_dict()
# create an instance of V0043QosLimitsMaxJobs from a dict
v0043_qos_limits_max_jobs_from_dict = V0043QosLimitsMaxJobs.from_dict(v0043_qos_limits_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


