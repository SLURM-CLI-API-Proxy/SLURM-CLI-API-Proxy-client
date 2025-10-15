# V0041JobAllocReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hetjob** | [**List[V0041JobDescMsg]**](V0041JobDescMsg.md) | HetJob description | [optional] 
**job** | [**V0041JobDescMsg**](V0041JobDescMsg.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_job_alloc_req import V0041JobAllocReq

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobAllocReq from a JSON string
v0041_job_alloc_req_instance = V0041JobAllocReq.from_json(json)
# print the JSON string representation of the object
print(V0041JobAllocReq.to_json())

# convert the object into a dict
v0041_job_alloc_req_dict = v0041_job_alloc_req_instance.to_dict()
# create an instance of V0041JobAllocReq from a dict
v0041_job_alloc_req_from_dict = V0041JobAllocReq.from_dict(v0041_job_alloc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


