# V0041JobSubmitReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | Deprecated; Populate script field in jobs[0] or job | [optional] 
**jobs** | [**List[V0041JobDescMsg]**](V0041JobDescMsg.md) | HetJob description | [optional] 
**job** | [**V0041JobDescMsg**](V0041JobDescMsg.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_job_submit_req import V0041JobSubmitReq

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobSubmitReq from a JSON string
v0041_job_submit_req_instance = V0041JobSubmitReq.from_json(json)
# print the JSON string representation of the object
print(V0041JobSubmitReq.to_json())

# convert the object into a dict
v0041_job_submit_req_dict = v0041_job_submit_req_instance.to_dict()
# create an instance of V0041JobSubmitReq from a dict
v0041_job_submit_req_from_dict = V0041JobSubmitReq.from_dict(v0041_job_submit_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


