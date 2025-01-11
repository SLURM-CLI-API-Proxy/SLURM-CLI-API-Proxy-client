# V0039JobDescMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**account_gather_frequency** | **str** |  | [optional] 
**admin_comment** | **str** |  | [optional] 
**allocation_node_list** | **str** |  | [optional] 
**allocation_node_port** | **int** |  | [optional] 
**argv** | **List[str]** |  | [optional] 
**array** | **str** |  | [optional] 
**batch_features** | **str** |  | [optional] 
**begin_time** | **int** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**burst_buffer** | **str** |  | [optional] 
**clusters** | **str** |  | [optional] 
**cluster_constraint** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**contiguous** | **bool** |  | [optional] 
**container** | **str** |  | [optional] 
**container_id** | **str** |  | [optional] 
**core_specification** | **int** |  | [optional] 
**thread_specification** | **int** |  | [optional] 
**cpu_binding** | **str** |  | [optional] 
**cpu_binding_flags** | **List[str]** |  | [optional] 
**cpu_frequency** | **str** |  | [optional] 
**cpus_per_tres** | **str** |  | [optional] 
**crontab** | [**V0039CronEntry**](V0039CronEntry.md) |  | [optional] 
**deadline** | **int** |  | [optional] 
**delay_boot** | **int** |  | [optional] 
**dependency** | **str** |  | [optional] 
**end_time** | **int** |  | [optional] 
**environment** | **List[str]** |  | 
**excluded_nodes** | **List[str]** |  | [optional] 
**extra** | **str** |  | [optional] 
**constraints** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**hetjob_group** | **int** |  | [optional] 
**immediate** | **bool** |  | [optional] 
**job_id** | **int** |  | [optional] 
**kill_on_node_fail** | **bool** |  | [optional] 
**licenses** | **str** |  | [optional] 
**mail_type** | **List[str]** |  | [optional] 
**mail_user** | **str** |  | [optional] 
**mcs_label** | **str** |  | [optional] 
**memory_binding** | **str** |  | [optional] 
**memory_binding_type** | **List[str]** |  | [optional] 
**memory_per_tres** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**nice** | **int** |  | [optional] 
**tasks** | **int** |  | [optional] 
**open_mode** | **List[str]** |  | [optional] 
**reserve_ports** | **int** |  | [optional] 
**overcommit** | **bool** |  | [optional] 
**partition** | **str** |  | [optional] 
**distribution_plane_size** | **int** |  | [optional] 
**power_flags** | **List[str]** |  | [optional] 
**prefer** | **str** |  | [optional] 
**hold** | **bool** | Hold (true) or release (false) job | [optional] 
**priority** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**profile** | **List[str]** |  | [optional] 
**qos** | **str** |  | [optional] 
**reboot** | **bool** |  | [optional] 
**required_nodes** | **List[str]** |  | [optional] 
**requeue** | **bool** |  | [optional] 
**reservation** | **str** |  | [optional] 
**script** | **str** |  | [optional] 
**shared** | **List[str]** |  | [optional] 
**exclusive** | **List[str]** |  | [optional] 
**oversubscribe** | **bool** |  | [optional] 
**site_factor** | **int** |  | [optional] 
**spank_environment** | **List[str]** |  | [optional] 
**distribution** | **str** |  | [optional] 
**time_limit** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**time_minimum** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**tres_bind** | **str** |  | [optional] 
**tres_freq** | **str** |  | [optional] 
**tres_per_job** | **str** |  | [optional] 
**tres_per_node** | **str** |  | [optional] 
**tres_per_socket** | **str** |  | [optional] 
**tres_per_task** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**wait_all_nodes** | **bool** |  | [optional] 
**kill_warning_flags** | **List[str]** |  | [optional] 
**kill_warning_signal** | **str** |  | [optional] 
**kill_warning_delay** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**current_working_directory** | **str** |  | [optional] 
**cpus_per_task** | **int** |  | [optional] 
**minimum_cpus** | **int** |  | [optional] 
**maximum_cpus** | **int** |  | [optional] 
**nodes** | **str** |  | [optional] 
**minimum_nodes** | **int** |  | [optional] 
**maximum_nodes** | **int** |  | [optional] 
**minimum_boards_per_node** | **int** |  | [optional] 
**minimum_sockets_per_board** | **int** |  | [optional] 
**sockets_per_node** | **int** |  | [optional] 
**threads_per_core** | **int** |  | [optional] 
**tasks_per_node** | **int** |  | [optional] 
**tasks_per_socket** | **int** |  | [optional] 
**tasks_per_core** | **int** |  | [optional] 
**tasks_per_board** | **int** |  | [optional] 
**ntasks_per_tres** | **int** |  | [optional] 
**minimum_cpus_per_node** | **int** |  | [optional] 
**memory_per_cpu** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**memory_per_node** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**temporary_disk_per_node** | **int** |  | [optional] 
**selinux_context** | **str** |  | [optional] 
**required_switches** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**standard_error** | **str** |  | [optional] 
**standard_input** | **str** |  | [optional] 
**standard_output** | **str** |  | [optional] 
**wait_for_switch** | **int** |  | [optional] 
**wckey** | **str** |  | [optional] 
**x11** | **List[str]** |  | [optional] 
**x11_magic_cookie** | **str** |  | [optional] 
**x11_target_host** | **str** |  | [optional] 
**x11_target_port** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_job_desc_msg import V0039JobDescMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobDescMsg from a JSON string
v0039_job_desc_msg_instance = V0039JobDescMsg.from_json(json)
# print the JSON string representation of the object
print(V0039JobDescMsg.to_json())

# convert the object into a dict
v0039_job_desc_msg_dict = v0039_job_desc_msg_instance.to_dict()
# create an instance of V0039JobDescMsg from a dict
v0039_job_desc_msg_from_dict = V0039JobDescMsg.from_dict(v0039_job_desc_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


