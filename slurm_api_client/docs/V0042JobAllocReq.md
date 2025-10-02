# V0042JobAllocReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hetjob** | [**List[V0042JobDescMsg]**](V0042JobDescMsg.md) |  | [optional] 
**job** | [**V0042JobDescMsg**](V0042JobDescMsg.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_job_alloc_req import V0042JobAllocReq

# TODO update the JSON string below
json = "{}"
# create an instance of V0042JobAllocReq from a JSON string
v0042_job_alloc_req_instance = V0042JobAllocReq.from_json(json)
# print the JSON string representation of the object
print(V0042JobAllocReq.to_json())

# convert the object into a dict
v0042_job_alloc_req_dict = v0042_job_alloc_req_instance.to_dict()
# create an instance of V0042JobAllocReq from a dict
v0042_job_alloc_req_from_dict = V0042JobAllocReq.from_dict(v0042_job_alloc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


