# V0042AssocMaxJobsPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**accruing** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**submitted** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**wall_clock** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_assoc_max_jobs_per import V0042AssocMaxJobsPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0042AssocMaxJobsPer from a JSON string
v0042_assoc_max_jobs_per_instance = V0042AssocMaxJobsPer.from_json(json)
# print the JSON string representation of the object
print(V0042AssocMaxJobsPer.to_json())

# convert the object into a dict
v0042_assoc_max_jobs_per_dict = v0042_assoc_max_jobs_per_instance.to_dict()
# create an instance of V0042AssocMaxJobsPer from a dict
v0042_assoc_max_jobs_per_from_dict = V0042AssocMaxJobsPer.from_dict(v0042_assoc_max_jobs_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


