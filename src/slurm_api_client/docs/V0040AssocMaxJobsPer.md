# V0040AssocMaxJobsPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**accruing** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**submitted** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**wall_clock** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_assoc_max_jobs_per import V0040AssocMaxJobsPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0040AssocMaxJobsPer from a JSON string
v0040_assoc_max_jobs_per_instance = V0040AssocMaxJobsPer.from_json(json)
# print the JSON string representation of the object
print(V0040AssocMaxJobsPer.to_json())

# convert the object into a dict
v0040_assoc_max_jobs_per_dict = v0040_assoc_max_jobs_per_instance.to_dict()
# create an instance of V0040AssocMaxJobsPer from a dict
v0040_assoc_max_jobs_per_from_dict = V0040AssocMaxJobsPer.from_dict(v0040_assoc_max_jobs_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


