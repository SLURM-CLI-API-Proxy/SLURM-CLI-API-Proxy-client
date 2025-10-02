# V0042AssocShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account name | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**partition** | **str** | Partition name | [optional] 
**user** | **str** | User name | 
**id** | **int** | Numeric association ID | [optional] 

## Example

```python
from openapi_client.models.v0042_assoc_short import V0042AssocShort

# TODO update the JSON string below
json = "{}"
# create an instance of V0042AssocShort from a JSON string
v0042_assoc_short_instance = V0042AssocShort.from_json(json)
# print the JSON string representation of the object
print(V0042AssocShort.to_json())

# convert the object into a dict
v0042_assoc_short_dict = v0042_assoc_short_instance.to_dict()
# create an instance of V0042AssocShort from a dict
v0042_assoc_short_from_dict = V0042AssocShort.from_dict(v0042_assoc_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


