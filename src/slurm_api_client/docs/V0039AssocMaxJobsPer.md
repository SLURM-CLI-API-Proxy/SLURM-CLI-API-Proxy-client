# V0039AssocMaxJobsPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**accruing** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**submitted** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**wall_clock** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_assoc_max_jobs_per import V0039AssocMaxJobsPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0039AssocMaxJobsPer from a JSON string
v0039_assoc_max_jobs_per_instance = V0039AssocMaxJobsPer.from_json(json)
# print the JSON string representation of the object
print(V0039AssocMaxJobsPer.to_json())

# convert the object into a dict
v0039_assoc_max_jobs_per_dict = v0039_assoc_max_jobs_per_instance.to_dict()
# create an instance of V0039AssocMaxJobsPer from a dict
v0039_assoc_max_jobs_per_from_dict = V0039AssocMaxJobsPer.from_dict(v0039_assoc_max_jobs_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


