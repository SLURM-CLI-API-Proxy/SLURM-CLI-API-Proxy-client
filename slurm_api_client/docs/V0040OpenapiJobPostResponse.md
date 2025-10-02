# V0040OpenapiJobPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[V0040JobArrayResponseMsgEntry]**](V0040JobArrayResponseMsgEntry.md) |  | [optional] 
**job_id** | **str** | First updated Job ID - Use results instead | [optional] 
**step_id** | **str** | First updated Step ID - Use results instead | [optional] 
**job_submit_user_msg** | **str** | First updated Job submission user message - Use results instead | [optional] 
**meta** | [**V0040OpenapiMeta**](V0040OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0040OpenapiError]**](V0040OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0040OpenapiWarning]**](V0040OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_job_post_response import V0040OpenapiJobPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiJobPostResponse from a JSON string
v0040_openapi_job_post_response_instance = V0040OpenapiJobPostResponse.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiJobPostResponse.to_json())

# convert the object into a dict
v0040_openapi_job_post_response_dict = v0040_openapi_job_post_response_instance.to_dict()
# create an instance of V0040OpenapiJobPostResponse from a dict
v0040_openapi_job_post_response_from_dict = V0040OpenapiJobPostResponse.from_dict(v0040_openapi_job_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


