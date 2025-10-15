# V0043PartitionInfoQos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **str** | AllowQOS - Comma-separated list of Qos which may execute jobs in the partition | [optional] 
**deny** | **str** | DenyQOS - Comma-separated list of Qos which may not execute jobs in the partition | [optional] 
**assigned** | **str** | QOS - QOS name containing limits that will apply to all jobs in this partition | [optional] 

## Example

```python
from openapi_client.models.v0043_partition_info_qos import V0043PartitionInfoQos

# TODO update the JSON string below
json = "{}"
# create an instance of V0043PartitionInfoQos from a JSON string
v0043_partition_info_qos_instance = V0043PartitionInfoQos.from_json(json)
# print the JSON string representation of the object
print(V0043PartitionInfoQos.to_json())

# convert the object into a dict
v0043_partition_info_qos_dict = v0043_partition_info_qos_instance.to_dict()
# create an instance of V0043PartitionInfoQos from a dict
v0043_partition_info_qos_from_dict = V0043PartitionInfoQos.from_dict(v0043_partition_info_qos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


