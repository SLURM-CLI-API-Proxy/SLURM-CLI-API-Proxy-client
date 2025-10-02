# V0043PartitionInfoTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_weights** | **str** | TRESBillingWeights - Billing weights of each tracked TRES type that will be used in calculating the usage of a job | [optional] 
**configured** | **str** | TRES - Number of each applicable TRES type available in this partition | [optional] 

## Example

```python
from openapi_client.models.v0043_partition_info_tres import V0043PartitionInfoTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0043PartitionInfoTres from a JSON string
v0043_partition_info_tres_instance = V0043PartitionInfoTres.from_json(json)
# print the JSON string representation of the object
print(V0043PartitionInfoTres.to_json())

# convert the object into a dict
v0043_partition_info_tres_dict = v0043_partition_info_tres_instance.to_dict()
# create an instance of V0043PartitionInfoTres from a dict
v0043_partition_info_tres_from_dict = V0043PartitionInfoTres.from_dict(v0043_partition_info_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


