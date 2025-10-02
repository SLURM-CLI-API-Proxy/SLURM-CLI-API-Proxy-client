# V0043AssocMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per** | [**V0043AssocMaxJobsPer**](V0043AssocMaxJobsPer.md) |  | [optional] 
**active** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**accruing** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**total** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_assoc_max_jobs import V0043AssocMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0043AssocMaxJobs from a JSON string
v0043_assoc_max_jobs_instance = V0043AssocMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0043AssocMaxJobs.to_json())

# convert the object into a dict
v0043_assoc_max_jobs_dict = v0043_assoc_max_jobs_instance.to_dict()
# create an instance of V0043AssocMaxJobs from a dict
v0043_assoc_max_jobs_from_dict = V0043AssocMaxJobs.from_dict(v0043_assoc_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


