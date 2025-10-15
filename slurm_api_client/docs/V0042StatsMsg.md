# V0042StatsMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts_packed** | **int** | Zero if only RPC statistic included | [optional] 
**req_time** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**req_time_start** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**server_thread_count** | **int** | Number of current active slurmctld threads | [optional] 
**agent_queue_size** | **int** | Number of enqueued outgoing RPC requests in an internal retry list | [optional] 
**agent_count** | **int** | Number of agent threads | [optional] 
**agent_thread_count** | **int** | Total number of active threads created by all agent threads | [optional] 
**dbd_agent_queue_size** | **int** | Number of messages for SlurmDBD that are queued | [optional] 
**gettimeofday_latency** | **int** | Latency of 1000 calls to the gettimeofday() syscall in microseconds, as measured at controller startup | [optional] 
**schedule_cycle_max** | **int** | Max time of any scheduling cycle in microseconds since last reset | [optional] 
**schedule_cycle_last** | **int** | Time in microseconds for last scheduling cycle | [optional] 
**schedule_cycle_sum** | **int** | Total run time in microseconds for all scheduling cycles since last reset | [optional] 
**schedule_cycle_total** | **int** | Number of scheduling cycles since last reset | [optional] 
**schedule_cycle_mean** | **int** | Mean time in microseconds for all scheduling cycles since last reset | [optional] 
**schedule_cycle_mean_depth** | **int** | Mean of the number of jobs processed in a scheduling cycle | [optional] 
**schedule_cycle_per_minute** | **int** | Number of scheduling executions per minute | [optional] 
**schedule_cycle_depth** | **int** | Total number of jobs processed in scheduling cycles | [optional] 
**schedule_exit** | [**V0042ScheduleExitFields**](V0042ScheduleExitFields.md) |  | [optional] 
**schedule_queue_length** | **int** | Number of jobs pending in queue | [optional] 
**jobs_submitted** | **int** | Number of jobs submitted since last reset | [optional] 
**jobs_started** | **int** | Number of jobs started since last reset | [optional] 
**jobs_completed** | **int** | Number of jobs completed since last reset | [optional] 
**jobs_canceled** | **int** | Number of jobs canceled since the last reset | [optional] 
**jobs_failed** | **int** | Number of jobs failed due to slurmd or other internal issues since last reset | [optional] 
**jobs_pending** | **int** | Number of jobs pending at the time of listed in job_state_ts | [optional] 
**jobs_running** | **int** | Number of jobs running at the time of listed in job_state_ts | [optional] 
**job_states_ts** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**bf_backfilled_jobs** | **int** | Number of jobs started through backfilling since last slurm start | [optional] 
**bf_last_backfilled_jobs** | **int** | Number of jobs started through backfilling since last reset | [optional] 
**bf_backfilled_het_jobs** | **int** | Number of heterogeneous job components started through backfilling since last Slurm start | [optional] 
**bf_cycle_counter** | **int** | Number of backfill scheduling cycles since last reset | [optional] 
**bf_cycle_mean** | **int** | Mean time in microseconds of backfilling scheduling cycles since last reset | [optional] 
**bf_depth_mean** | **int** | Mean number of eligible to run jobs processed during all backfilling scheduling cycles since last reset | [optional] 
**bf_depth_mean_try** | **int** | The subset of Depth Mean that the backfill scheduler attempted to schedule | [optional] 
**bf_cycle_sum** | **int** | Total time in microseconds of backfilling scheduling cycles since last reset | [optional] 
**bf_cycle_last** | **int** | Execution time in microseconds of last backfill scheduling cycle | [optional] 
**bf_cycle_max** | **int** | Execution time in microseconds of longest backfill scheduling cycle | [optional] 
**bf_exit** | [**V0042BfExitFields**](V0042BfExitFields.md) |  | [optional] 
**bf_last_depth** | **int** | Number of processed jobs during last backfilling scheduling cycle | [optional] 
**bf_last_depth_try** | **int** | Number of processed jobs during last backfilling scheduling cycle that had a chance to start using available resources | [optional] 
**bf_depth_sum** | **int** | Total number of jobs processed during all backfilling scheduling cycles since last reset | [optional] 
**bf_depth_try_sum** | **int** | Subset of bf_depth_sum that the backfill scheduler attempted to schedule | [optional] 
**bf_queue_len** | **int** | Number of jobs pending to be processed by backfilling algorithm | [optional] 
**bf_queue_len_mean** | **int** | Mean number of jobs pending to be processed by backfilling algorithm | [optional] 
**bf_queue_len_sum** | **int** | Total number of jobs pending to be processed by backfilling algorithm since last reset | [optional] 
**bf_table_size** | **int** | Number of different time slots tested by the backfill scheduler in its last iteration | [optional] 
**bf_table_size_sum** | **int** | Total number of different time slots tested by the backfill scheduler | [optional] 
**bf_table_size_mean** | **int** | Mean number of different time slots tested by the backfill scheduler | [optional] 
**bf_when_last_cycle** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**bf_active** | **bool** | Backfill scheduler currently running | [optional] 
**rpcs_by_message_type** | [**List[V0042StatsMsgRpcType]**](V0042StatsMsgRpcType.md) | RPCs by type | [optional] 
**rpcs_by_user** | [**List[V0042StatsMsgRpcUser]**](V0042StatsMsgRpcUser.md) | RPCs by user | [optional] 
**pending_rpcs** | [**List[V0042StatsMsgRpcQueue]**](V0042StatsMsgRpcQueue.md) | Pending RPCs | [optional] 
**pending_rpcs_by_hostlist** | [**List[V0042StatsMsgRpcDump]**](V0042StatsMsgRpcDump.md) | Pending RPCs by hostlist | [optional] 

## Example

```python
from openapi_client.models.v0042_stats_msg import V0042StatsMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StatsMsg from a JSON string
v0042_stats_msg_instance = V0042StatsMsg.from_json(json)
# print the JSON string representation of the object
print(V0042StatsMsg.to_json())

# convert the object into a dict
v0042_stats_msg_dict = v0042_stats_msg_instance.to_dict()
# create an instance of V0042StatsMsg from a dict
v0042_stats_msg_from_dict = V0042StatsMsg.from_dict(v0042_stats_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


