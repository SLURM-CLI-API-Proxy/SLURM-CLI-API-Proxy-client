# V0042OpenapiKillJobsResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**List[V0042KillJobsRespJob]**](V0042KillJobsRespJob.md) | List of jobs signal responses | 
**meta** | [**V0042OpenapiMeta**](V0042OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0042OpenapiError]**](V0042OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0042OpenapiWarning]**](V0042OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_openapi_kill_jobs_resp import V0042OpenapiKillJobsResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0042OpenapiKillJobsResp from a JSON string
v0042_openapi_kill_jobs_resp_instance = V0042OpenapiKillJobsResp.from_json(json)
# print the JSON string representation of the object
print(V0042OpenapiKillJobsResp.to_json())

# convert the object into a dict
v0042_openapi_kill_jobs_resp_dict = v0042_openapi_kill_jobs_resp_instance.to_dict()
# create an instance of V0042OpenapiKillJobsResp from a dict
v0042_openapi_kill_jobs_resp_from_dict = V0042OpenapiKillJobsResp.from_dict(v0042_openapi_kill_jobs_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


