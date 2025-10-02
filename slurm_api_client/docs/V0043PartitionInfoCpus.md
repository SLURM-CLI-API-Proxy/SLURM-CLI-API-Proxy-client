# V0043PartitionInfoCpus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_binding** | **int** | CpuBind - Default method controlling how tasks are bound to allocated resources | [optional] 
**total** | **int** | TotalCPUs - Number of CPUs available in this partition | [optional] 

## Example

```python
from openapi_client.models.v0043_partition_info_cpus import V0043PartitionInfoCpus

# TODO update the JSON string below
json = "{}"
# create an instance of V0043PartitionInfoCpus from a JSON string
v0043_partition_info_cpus_instance = V0043PartitionInfoCpus.from_json(json)
# print the JSON string representation of the object
print(V0043PartitionInfoCpus.to_json())

# convert the object into a dict
v0043_partition_info_cpus_dict = v0043_partition_info_cpus_instance.to_dict()
# create an instance of V0043PartitionInfoCpus from a dict
v0043_partition_info_cpus_from_dict = V0043PartitionInfoCpus.from_dict(v0043_partition_info_cpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


