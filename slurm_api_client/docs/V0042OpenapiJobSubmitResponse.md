# V0042OpenapiJobSubmitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | submitted Job ID | [optional] 
**step_id** | **str** | submitted Step ID | [optional] 
**job_submit_user_msg** | **str** | Job submission user message | [optional] 
**meta** | [**V0042OpenapiMeta**](V0042OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0042OpenapiError]**](V0042OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0042OpenapiWarning]**](V0042OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_openapi_job_submit_response import V0042OpenapiJobSubmitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0042OpenapiJobSubmitResponse from a JSON string
v0042_openapi_job_submit_response_instance = V0042OpenapiJobSubmitResponse.from_json(json)
# print the JSON string representation of the object
print(V0042OpenapiJobSubmitResponse.to_json())

# convert the object into a dict
v0042_openapi_job_submit_response_dict = v0042_openapi_job_submit_response_instance.to_dict()
# create an instance of V0042OpenapiJobSubmitResponse from a dict
v0042_openapi_job_submit_response_from_dict = V0042OpenapiJobSubmitResponse.from_dict(v0042_openapi_job_submit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


