# V0042AssocMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per** | [**V0042AssocMaxJobsPer**](V0042AssocMaxJobsPer.md) |  | [optional] 
**active** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**accruing** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**total** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_assoc_max_jobs import V0042AssocMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0042AssocMaxJobs from a JSON string
v0042_assoc_max_jobs_instance = V0042AssocMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0042AssocMaxJobs.to_json())

# convert the object into a dict
v0042_assoc_max_jobs_dict = v0042_assoc_max_jobs_instance.to_dict()
# create an instance of V0042AssocMaxJobs from a dict
v0042_assoc_max_jobs_from_dict = V0042AssocMaxJobs.from_dict(v0042_assoc_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


