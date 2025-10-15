# V0042PartPrio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | **str** | Partition name | [optional] 
**priority** | **int** | Prospective job priority if it runs in this partition | [optional] 

## Example

```python
from openapi_client.models.v0042_part_prio import V0042PartPrio

# TODO update the JSON string below
json = "{}"
# create an instance of V0042PartPrio from a JSON string
v0042_part_prio_instance = V0042PartPrio.from_json(json)
# print the JSON string representation of the object
print(V0042PartPrio.to_json())

# convert the object into a dict
v0042_part_prio_dict = v0042_part_prio_instance.to_dict()
# create an instance of V0042PartPrio from a dict
v0042_part_prio_from_dict = V0042PartPrio.from_dict(v0042_part_prio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


