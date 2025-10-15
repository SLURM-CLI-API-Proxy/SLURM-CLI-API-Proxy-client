# V0043OpenapiJobPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[V0043JobArrayResponseMsgEntry]**](V0043JobArrayResponseMsgEntry.md) |  | [optional] 
**meta** | [**V0043OpenapiMeta**](V0043OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0043OpenapiError]**](V0043OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0043OpenapiWarning]**](V0043OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_openapi_job_post_response import V0043OpenapiJobPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0043OpenapiJobPostResponse from a JSON string
v0043_openapi_job_post_response_instance = V0043OpenapiJobPostResponse.from_json(json)
# print the JSON string representation of the object
print(V0043OpenapiJobPostResponse.to_json())

# convert the object into a dict
v0043_openapi_job_post_response_dict = v0043_openapi_job_post_response_instance.to_dict()
# create an instance of V0043OpenapiJobPostResponse from a dict
v0043_openapi_job_post_response_from_dict = V0043OpenapiJobPostResponse.from_dict(v0043_openapi_job_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


