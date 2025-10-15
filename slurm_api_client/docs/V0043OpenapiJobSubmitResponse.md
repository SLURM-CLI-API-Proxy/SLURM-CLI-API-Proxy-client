# V0043OpenapiJobSubmitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | submitted Job ID | [optional] 
**step_id** | **str** | submitted Step ID | [optional] 
**job_submit_user_msg** | **str** | Job submission user message | [optional] 
**meta** | [**V0043OpenapiMeta**](V0043OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0043OpenapiError]**](V0043OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0043OpenapiWarning]**](V0043OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_openapi_job_submit_response import V0043OpenapiJobSubmitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0043OpenapiJobSubmitResponse from a JSON string
v0043_openapi_job_submit_response_instance = V0043OpenapiJobSubmitResponse.from_json(json)
# print the JSON string representation of the object
print(V0043OpenapiJobSubmitResponse.to_json())

# convert the object into a dict
v0043_openapi_job_submit_response_dict = v0043_openapi_job_submit_response_instance.to_dict()
# create an instance of V0043OpenapiJobSubmitResponse from a dict
v0043_openapi_job_submit_response_from_dict = V0043OpenapiJobSubmitResponse.from_dict(v0043_openapi_job_submit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


