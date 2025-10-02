# V0043AssocShort


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
from openapi_client.models.v0043_assoc_short import V0043AssocShort

# TODO update the JSON string below
json = "{}"
# create an instance of V0043AssocShort from a JSON string
v0043_assoc_short_instance = V0043AssocShort.from_json(json)
# print the JSON string representation of the object
print(V0043AssocShort.to_json())

# convert the object into a dict
v0043_assoc_short_dict = v0043_assoc_short_instance.to_dict()
# create an instance of V0043AssocShort from a dict
v0043_assoc_short_from_dict = V0043AssocShort.from_dict(v0043_assoc_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


