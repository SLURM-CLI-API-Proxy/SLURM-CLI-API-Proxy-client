# V0038Node


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | computer architecture | [optional] 
**burstbuffer_network_address** | **str** | BcastAddr | [optional] 
**boards** | **int** | total number of boards per node | [optional] 
**boot_time** | **int** | timestamp of node boot | [optional] 
**cores** | **int** | number of cores per socket | [optional] 
**cpu_binding** | **int** | Default task binding | [optional] 
**cpu_load** | **int** | CPU load * 100 | [optional] 
**free_memory** | **int** | free memory in MiB | [optional] 
**cpus** | **int** | configured count of cpus running on the node | [optional] 
**features** | **str** |  | [optional] 
**active_features** | **str** | list of a node&#39;s available features | [optional] 
**gres** | **str** | list of a node&#39;s generic resources | [optional] 
**gres_drained** | **str** | list of drained GRES | [optional] 
**gres_used** | **str** | list of GRES in current use | [optional] 
**mcs_label** | **str** | mcs label if mcs plugin in use | [optional] 
**name** | **str** | node name to slurm | [optional] 
**next_state_after_reboot** | **str** | state after reboot | [optional] 
**next_state_after_reboot_flags** | **List[str]** | node state flags | [optional] 
**address** | **str** | state after reboot | [optional] 
**hostname** | **str** | node&#39;s hostname | [optional] 
**state** | **str** | current node state | [optional] 
**state_flags** | **List[str]** | node state flags | [optional] 
**operating_system** | **str** | operating system | [optional] 
**owner** | **str** | User allowed to use this node | [optional] 
**partitions** | **List[str]** | assigned partitions | [optional] 
**port** | **int** | TCP port number of the slurmd | [optional] 
**real_memory** | **int** | configured MB of real memory on the node | [optional] 
**reason** | **str** | reason for node being DOWN or DRAINING | [optional] 
**reason_changed_at** | **int** | Time stamp when reason was set | [optional] 
**reason_set_by_user** | **str** | User that set the reason | [optional] 
**slurmd_start_time** | **int** | timestamp of slurmd startup | [optional] 
**sockets** | **int** | total number of sockets per node | [optional] 
**threads** | **int** | number of threads per core | [optional] 
**temporary_disk** | **int** | configured MB of total disk in TMP_FS | [optional] 
**weight** | **int** | arbitrary priority of node for scheduling | [optional] 
**tres** | **str** | TRES on node | [optional] 
**tres_used** | **str** | TRES used on node | [optional] 
**tres_weighted** | **float** | TRES weight used on node | [optional] 
**slurmd_version** | **str** | Slurmd version | [optional] 
**alloc_cpus** | **int** | Allocated CPUs | [optional] 
**idle_cpus** | **int** | Idle CPUs | [optional] 
**alloc_memory** | **int** | Allocated memory (MB) | [optional] 

## Example

```python
from openapi_client.models.v0038_node import V0038Node

# TODO update the JSON string below
json = "{}"
# create an instance of V0038Node from a JSON string
v0038_node_instance = V0038Node.from_json(json)
# print the JSON string representation of the object
print(V0038Node.to_json())

# convert the object into a dict
v0038_node_dict = v0038_node_instance.to_dict()
# create an instance of V0038Node from a dict
v0038_node_from_dict = V0038Node.from_dict(v0038_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


