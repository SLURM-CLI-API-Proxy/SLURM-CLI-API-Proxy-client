# V0040PartitionInfoCpus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_binding** | **int** | CpuBind | [optional] 
**total** | **int** | TotalCPUs | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info_cpus import V0040PartitionInfoCpus

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfoCpus from a JSON string
v0040_partition_info_cpus_instance = V0040PartitionInfoCpus.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfoCpus.to_json())

# convert the object into a dict
v0040_partition_info_cpus_dict = v0040_partition_info_cpus_instance.to_dict()
# create an instance of V0040PartitionInfoCpus from a dict
v0040_partition_info_cpus_from_dict = V0040PartitionInfoCpus.from_dict(v0040_partition_info_cpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


