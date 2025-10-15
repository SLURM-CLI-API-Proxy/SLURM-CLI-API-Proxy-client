# V0043AssocMaxJobsPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**accruing** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**submitted** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**wall_clock** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_assoc_max_jobs_per import V0043AssocMaxJobsPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0043AssocMaxJobsPer from a JSON string
v0043_assoc_max_jobs_per_instance = V0043AssocMaxJobsPer.from_json(json)
# print the JSON string representation of the object
print(V0043AssocMaxJobsPer.to_json())

# convert the object into a dict
v0043_assoc_max_jobs_per_dict = v0043_assoc_max_jobs_per_instance.to_dict()
# create an instance of V0043AssocMaxJobsPer from a dict
v0043_assoc_max_jobs_per_from_dict = V0043AssocMaxJobsPer.from_dict(v0043_assoc_max_jobs_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


