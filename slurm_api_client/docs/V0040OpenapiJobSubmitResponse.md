# V0040OpenapiJobSubmitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**V0040JobSubmitResponseMsg**](V0040JobSubmitResponseMsg.md) |  | [optional] 
**job_id** | **int** | Submitted Job ID | [optional] 
**step_id** | **str** | Submitted Step ID | [optional] 
**job_submit_user_msg** | **str** | job submission user message | [optional] 
**meta** | [**V0040OpenapiMeta**](V0040OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0040OpenapiError]**](V0040OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0040OpenapiWarning]**](V0040OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_job_submit_response import V0040OpenapiJobSubmitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiJobSubmitResponse from a JSON string
v0040_openapi_job_submit_response_instance = V0040OpenapiJobSubmitResponse.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiJobSubmitResponse.to_json())

# convert the object into a dict
v0040_openapi_job_submit_response_dict = v0040_openapi_job_submit_response_instance.to_dict()
# create an instance of V0040OpenapiJobSubmitResponse from a dict
v0040_openapi_job_submit_response_from_dict = V0040OpenapiJobSubmitResponse.from_dict(v0040_openapi_job_submit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


