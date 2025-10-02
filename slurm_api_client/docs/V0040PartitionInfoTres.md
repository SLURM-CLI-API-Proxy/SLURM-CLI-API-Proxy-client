# V0040PartitionInfoTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_weights** | **str** | TRESBillingWeights | [optional] 
**configured** | **str** | TRES | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info_tres import V0040PartitionInfoTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfoTres from a JSON string
v0040_partition_info_tres_instance = V0040PartitionInfoTres.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfoTres.to_json())

# convert the object into a dict
v0040_partition_info_tres_dict = v0040_partition_info_tres_instance.to_dict()
# create an instance of V0040PartitionInfoTres from a dict
v0040_partition_info_tres_from_dict = V0040PartitionInfoTres.from_dict(v0040_partition_info_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


