# V0042OpenapiJobPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[V0042JobArrayResponseMsgEntry]**](V0042JobArrayResponseMsgEntry.md) |  | [optional] 
**meta** | [**V0042OpenapiMeta**](V0042OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0042OpenapiError]**](V0042OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0042OpenapiWarning]**](V0042OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_openapi_job_post_response import V0042OpenapiJobPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0042OpenapiJobPostResponse from a JSON string
v0042_openapi_job_post_response_instance = V0042OpenapiJobPostResponse.from_json(json)
# print the JSON string representation of the object
print(V0042OpenapiJobPostResponse.to_json())

# convert the object into a dict
v0042_openapi_job_post_response_dict = v0042_openapi_job_post_response_instance.to_dict()
# create an instance of V0042OpenapiJobPostResponse from a dict
v0042_openapi_job_post_response_from_dict = V0042OpenapiJobPostResponse.from_dict(v0042_openapi_job_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


