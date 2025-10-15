# V0041KillJobsMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Filter jobs to a specific account | [optional] 
**flags** | **List[str]** | Filter jobs according to flags | [optional] 
**job_name** | **str** | Filter jobs to a specific name | [optional] 
**jobs** | **List[str]** | List of jobs to signal | [optional] 
**partition** | **str** | Filter jobs to a specific partition | [optional] 
**qos** | **str** | Filter jobs to a specific QOS | [optional] 
**reservation** | **str** | Filter jobs to a specific reservation | [optional] 
**signal** | **str** | Signal to send to jobs | [optional] 
**job_state** | **List[str]** | Filter jobs to a specific state | [optional] 
**user_id** | **str** | Filter jobs to a specific numeric user id | [optional] 
**user_name** | **str** | Filter jobs to a specific user name | [optional] 
**wckey** | **str** | Filter jobs to a specific wckey | [optional] 
**nodes** | **List[str]** | Filter jobs to a set of nodes | [optional] 

## Example

```python
from openapi_client.models.v0041_kill_jobs_msg import V0041KillJobsMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0041KillJobsMsg from a JSON string
v0041_kill_jobs_msg_instance = V0041KillJobsMsg.from_json(json)
# print the JSON string representation of the object
print(V0041KillJobsMsg.to_json())

# convert the object into a dict
v0041_kill_jobs_msg_dict = v0041_kill_jobs_msg_instance.to_dict()
# create an instance of V0041KillJobsMsg from a dict
v0041_kill_jobs_msg_from_dict = V0041KillJobsMsg.from_dict(v0041_kill_jobs_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


