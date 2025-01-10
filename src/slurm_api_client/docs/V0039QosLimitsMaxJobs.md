# V0039QosLimitsMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_jobs** | [**V0039QosLimitsMaxJobsActiveJobs**](V0039QosLimitsMaxJobsActiveJobs.md) |  | [optional] 
**per** | [**V0039QosLimitsMaxJobsActiveJobsPer**](V0039QosLimitsMaxJobsActiveJobsPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_qos_limits_max_jobs import V0039QosLimitsMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0039QosLimitsMaxJobs from a JSON string
v0039_qos_limits_max_jobs_instance = V0039QosLimitsMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0039QosLimitsMaxJobs.to_json())

# convert the object into a dict
v0039_qos_limits_max_jobs_dict = v0039_qos_limits_max_jobs_instance.to_dict()
# create an instance of V0039QosLimitsMaxJobs from a dict
v0039_qos_limits_max_jobs_from_dict = V0039QosLimitsMaxJobs.from_dict(v0039_qos_limits_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


