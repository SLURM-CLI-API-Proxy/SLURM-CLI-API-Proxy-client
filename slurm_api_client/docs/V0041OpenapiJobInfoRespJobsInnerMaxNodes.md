# V0041OpenapiJobInfoRespJobsInnerMaxNodes

Maximum number of nodes usable by the job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_max_nodes import V0041OpenapiJobInfoRespJobsInnerMaxNodes

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoRespJobsInnerMaxNodes from a JSON string
v0041_openapi_job_info_resp_jobs_inner_max_nodes_instance = V0041OpenapiJobInfoRespJobsInnerMaxNodes.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoRespJobsInnerMaxNodes.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_jobs_inner_max_nodes_dict = v0041_openapi_job_info_resp_jobs_inner_max_nodes_instance.to_dict()
# create an instance of V0041OpenapiJobInfoRespJobsInnerMaxNodes from a dict
v0041_openapi_job_info_resp_jobs_inner_max_nodes_from_dict = V0041OpenapiJobInfoRespJobsInnerMaxNodes.from_dict(v0041_openapi_job_info_resp_jobs_inner_max_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


