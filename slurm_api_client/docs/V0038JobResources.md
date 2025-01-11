# V0038JobResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **str** | list of assigned job nodes | [optional] 
**allocated_cpus** | **int** | number of assigned job cpus | [optional] 
**allocated_hosts** | **int** | number of assigned job hosts | [optional] 
**allocated_nodes** | [**List[V0038NodeAllocation]**](V0038NodeAllocation.md) | array of allocated nodes | [optional] 

## Example

```python
from openapi_client.models.v0038_job_resources import V0038JobResources

# TODO update the JSON string below
json = "{}"
# create an instance of V0038JobResources from a JSON string
v0038_job_resources_instance = V0038JobResources.from_json(json)
# print the JSON string representation of the object
print(V0038JobResources.to_json())

# convert the object into a dict
v0038_job_resources_dict = v0038_job_resources_instance.to_dict()
# create an instance of V0038JobResources from a dict
v0038_job_resources_from_dict = V0038JobResources.from_dict(v0038_job_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


