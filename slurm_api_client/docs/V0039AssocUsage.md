# V0039AssocUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrue_job_count** | **int** |  | [optional] 
**group_used_wallclock** | **float** |  | [optional] 
**fairshare_factor** | **float** |  | [optional] 
**fairshare_shares** | **int** |  | [optional] 
**normalized_priority** | **float** |  | [optional] 
**normalized_shares** | **float** |  | [optional] 
**effective_normalized_usage** | **float** |  | [optional] 
**normalized_usage** | **float** |  | [optional] 
**raw_usage** | **float** |  | [optional] 
**active_jobs** | **int** |  | [optional] 
**job_count** | **int** |  | [optional] 
**fairshare_level** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_assoc_usage import V0039AssocUsage

# TODO update the JSON string below
json = "{}"
# create an instance of V0039AssocUsage from a JSON string
v0039_assoc_usage_instance = V0039AssocUsage.from_json(json)
# print the JSON string representation of the object
print(V0039AssocUsage.to_json())

# convert the object into a dict
v0039_assoc_usage_dict = v0039_assoc_usage_instance.to_dict()
# create an instance of V0039AssocUsage from a dict
v0039_assoc_usage_from_dict = V0039AssocUsage.from_dict(v0039_assoc_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


