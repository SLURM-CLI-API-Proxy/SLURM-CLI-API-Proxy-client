# V0040QosLimitsMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_jobs** | [**V0040QosLimitsMaxJobsActiveJobs**](V0040QosLimitsMaxJobsActiveJobs.md) |  | [optional] 
**per** | [**V0040QosLimitsMaxJobsActiveJobsPer**](V0040QosLimitsMaxJobsActiveJobsPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_qos_limits_max_jobs import V0040QosLimitsMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0040QosLimitsMaxJobs from a JSON string
v0040_qos_limits_max_jobs_instance = V0040QosLimitsMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0040QosLimitsMaxJobs.to_json())

# convert the object into a dict
v0040_qos_limits_max_jobs_dict = v0040_qos_limits_max_jobs_instance.to_dict()
# create an instance of V0040QosLimitsMaxJobs from a dict
v0040_qos_limits_max_jobs_from_dict = V0040QosLimitsMaxJobs.from_dict(v0040_qos_limits_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


