# V0039StatsMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts_packed** | **int** |  | [optional] 
**req_time** | **int** |  | [optional] 
**req_time_start** | **int** |  | [optional] 
**server_thread_count** | **int** |  | [optional] 
**agent_queue_size** | **int** |  | [optional] 
**agent_count** | **int** |  | [optional] 
**agent_thread_count** | **int** |  | [optional] 
**dbd_agent_queue_size** | **int** |  | [optional] 
**gettimeofday_latency** | **int** |  | [optional] 
**schedule_cycle_max** | **int** |  | [optional] 
**schedule_cycle_last** | **int** |  | [optional] 
**schedule_cycle_total** | **int** |  | [optional] 
**schedule_cycle_mean** | **int** |  | [optional] 
**schedule_cycle_mean_depth** | **int** |  | [optional] 
**schedule_cycle_per_minute** | **int** |  | [optional] 
**schedule_queue_length** | **int** |  | [optional] 
**jobs_submitted** | **int** |  | [optional] 
**jobs_started** | **int** |  | [optional] 
**jobs_completed** | **int** |  | [optional] 
**jobs_canceled** | **int** |  | [optional] 
**jobs_failed** | **int** |  | [optional] 
**jobs_pending** | **int** |  | [optional] 
**jobs_running** | **int** |  | [optional] 
**job_states_ts** | **int** |  | [optional] 
**bf_backfilled_jobs** | **int** |  | [optional] 
**bf_last_backfilled_jobs** | **int** |  | [optional] 
**bf_backfilled_het_jobs** | **int** |  | [optional] 
**bf_cycle_counter** | **int** |  | [optional] 
**bf_cycle_mean** | **int** |  | [optional] 
**bf_depth_mean** | **int** |  | [optional] 
**bf_depth_mean_try** | **int** |  | [optional] 
**bf_cycle_sum** | **int** |  | [optional] 
**bf_cycle_last** | **int** |  | [optional] 
**bf_last_depth** | **int** |  | [optional] 
**bf_last_depth_try** | **int** |  | [optional] 
**bf_depth_sum** | **int** |  | [optional] 
**bf_depth_try_sum** | **int** |  | [optional] 
**bf_queue_len** | **int** |  | [optional] 
**bf_queue_len_mean** | **int** |  | [optional] 
**bf_queue_len_sum** | **int** |  | [optional] 
**bf_table_size** | **int** |  | [optional] 
**bf_table_size_mean** | **int** |  | [optional] 
**bf_when_last_cycle** | **int** |  | [optional] 
**bf_active** | **bool** |  | [optional] 
**rpcs_by_message_type** | [**List[V0039StatsMsgRpcsByTypeInner]**](V0039StatsMsgRpcsByTypeInner.md) | RPCs by message type | [optional] 
**rpcs_by_user** | [**List[V0039StatsMsgRpcsByUserInner]**](V0039StatsMsgRpcsByUserInner.md) | RPCs by user | [optional] 

## Example

```python
from openapi_client.models.v0039_stats_msg import V0039StatsMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0039StatsMsg from a JSON string
v0039_stats_msg_instance = V0039StatsMsg.from_json(json)
# print the JSON string representation of the object
print(V0039StatsMsg.to_json())

# convert the object into a dict
v0039_stats_msg_dict = v0039_stats_msg_instance.to_dict()
# create an instance of V0039StatsMsg from a dict
v0039_stats_msg_from_dict = V0039StatsMsg.from_dict(v0039_stats_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


