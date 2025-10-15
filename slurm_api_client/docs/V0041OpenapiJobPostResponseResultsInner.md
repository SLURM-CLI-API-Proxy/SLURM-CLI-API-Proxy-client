# V0041OpenapiJobPostResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Job ID for updated job | [optional] 
**step_id** | **str** | Step ID for updated job | [optional] 
**error** | **str** | Verbose update status or error | [optional] 
**error_code** | **int** | Verbose update status or error | [optional] 
**why** | **str** | Update response message | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_job_post_response_results_inner import V0041OpenapiJobPostResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobPostResponseResultsInner from a JSON string
v0041_openapi_job_post_response_results_inner_instance = V0041OpenapiJobPostResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobPostResponseResultsInner.to_json())

# convert the object into a dict
v0041_openapi_job_post_response_results_inner_dict = v0041_openapi_job_post_response_results_inner_instance.to_dict()
# create an instance of V0041OpenapiJobPostResponseResultsInner from a dict
v0041_openapi_job_post_response_results_inner_from_dict = V0041OpenapiJobPostResponseResultsInner.from_dict(v0041_openapi_job_post_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


