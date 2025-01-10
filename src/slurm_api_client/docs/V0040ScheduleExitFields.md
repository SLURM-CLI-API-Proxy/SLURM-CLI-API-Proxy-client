# V0040ScheduleExitFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_job_queue** | **int** |  | [optional] 
**default_queue_depth** | **int** |  | [optional] 
**max_job_start** | **int** |  | [optional] 
**max_rpc_cnt** | **int** |  | [optional] 
**max_sched_time** | **int** |  | [optional] 
**licenses** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.v0040_schedule_exit_fields import V0040ScheduleExitFields

# TODO update the JSON string below
json = "{}"
# create an instance of V0040ScheduleExitFields from a JSON string
v0040_schedule_exit_fields_instance = V0040ScheduleExitFields.from_json(json)
# print the JSON string representation of the object
print(V0040ScheduleExitFields.to_json())

# convert the object into a dict
v0040_schedule_exit_fields_dict = v0040_schedule_exit_fields_instance.to_dict()
# create an instance of V0040ScheduleExitFields from a dict
v0040_schedule_exit_fields_from_dict = V0040ScheduleExitFields.from_dict(v0040_schedule_exit_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


