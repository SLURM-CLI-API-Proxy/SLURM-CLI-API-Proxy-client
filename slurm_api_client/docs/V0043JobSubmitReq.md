# V0043JobSubmitReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | Deprecated; Populate script field in jobs[0] or job | [optional] 
**jobs** | [**List[V0043JobDescMsg]**](V0043JobDescMsg.md) |  | [optional] 
**job** | [**V0043JobDescMsg**](V0043JobDescMsg.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_job_submit_req import V0043JobSubmitReq

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobSubmitReq from a JSON string
v0043_job_submit_req_instance = V0043JobSubmitReq.from_json(json)
# print the JSON string representation of the object
print(V0043JobSubmitReq.to_json())

# convert the object into a dict
v0043_job_submit_req_dict = v0043_job_submit_req_instance.to_dict()
# create an instance of V0043JobSubmitReq from a dict
v0043_job_submit_req_from_dict = V0043JobSubmitReq.from_dict(v0043_job_submit_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


