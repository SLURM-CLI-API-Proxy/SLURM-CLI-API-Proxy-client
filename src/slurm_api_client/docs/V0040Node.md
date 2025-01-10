# V0040Node


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** |  | [optional] 
**burstbuffer_network_address** | **str** |  | [optional] 
**boards** | **int** |  | [optional] 
**boot_time** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**cores** | **int** |  | [optional] 
**specialized_cores** | **int** |  | [optional] 
**cpu_binding** | **int** |  | [optional] 
**cpu_load** | **int** |  | [optional] 
**free_mem** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**cpus** | **int** |  | [optional] 
**effective_cpus** | **int** |  | [optional] 
**specialized_cpus** | **str** |  | [optional] 
**energy** | [**V0040AcctGatherEnergy**](V0040AcctGatherEnergy.md) |  | [optional] 
**external_sensors** | [**V0040ExtSensorsData**](V0040ExtSensorsData.md) |  | [optional] 
**extra** | **str** |  | [optional] 
**power** | [**V0040PowerMgmtData**](V0040PowerMgmtData.md) |  | [optional] 
**features** | **List[str]** |  | [optional] 
**active_features** | **List[str]** |  | [optional] 
**gres** | **str** |  | [optional] 
**gres_drained** | **str** |  | [optional] 
**gres_used** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**last_busy** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**mcs_label** | **str** |  | [optional] 
**specialized_memory** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**next_state_after_reboot** | **List[str]** |  | [optional] 
**address** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**state** | **List[str]** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**partitions** | **List[str]** |  | [optional] 
**port** | **int** |  | [optional] 
**real_memory** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**reason_changed_at** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**reason_set_by_user** | **str** |  | [optional] 
**resume_after** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**reservation** | **str** |  | [optional] 
**alloc_memory** | **int** |  | [optional] 
**alloc_cpus** | **int** |  | [optional] 
**alloc_idle_cpus** | **int** |  | [optional] 
**tres_used** | **str** |  | [optional] 
**tres_weighted** | **float** |  | [optional] 
**slurmd_start_time** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**sockets** | **int** |  | [optional] 
**threads** | **int** |  | [optional] 
**temporary_disk** | **int** |  | [optional] 
**weight** | **int** |  | [optional] 
**tres** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v0040_node import V0040Node

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Node from a JSON string
v0040_node_instance = V0040Node.from_json(json)
# print the JSON string representation of the object
print(V0040Node.to_json())

# convert the object into a dict
v0040_node_dict = v0040_node_instance.to_dict()
# create an instance of V0040Node from a dict
v0040_node_from_dict = V0040Node.from_dict(v0040_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


