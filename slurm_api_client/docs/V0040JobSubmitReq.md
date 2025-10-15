# V0040JobSubmitReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | Batch job script; must be specified in first component of jobs or in job if this field is not populated | [optional] 
**jobs** | [**List[V0040JobDescMsg]**](V0040JobDescMsg.md) |  | [optional] 
**job** | [**V0040JobDescMsg**](V0040JobDescMsg.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_job_submit_req import V0040JobSubmitReq

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobSubmitReq from a JSON string
v0040_job_submit_req_instance = V0040JobSubmitReq.from_json(json)
# print the JSON string representation of the object
print(V0040JobSubmitReq.to_json())

# convert the object into a dict
v0040_job_submit_req_dict = v0040_job_submit_req_instance.to_dict()
# create an instance of V0040JobSubmitReq from a dict
v0040_job_submit_req_from_dict = V0040JobSubmitReq.from_dict(v0040_job_submit_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


