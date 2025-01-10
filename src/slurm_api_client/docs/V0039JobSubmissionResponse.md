# V0039JobSubmissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0039Meta**](V0039Meta.md) |  | [optional] 
**errors** | [**List[V0039Error]**](V0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[V0039Warning]**](V0039Warning.md) | Slurm warnings | [optional] 
**job_id** | **int** | new job ID | [optional] 
**step_id** | **str** | new job step ID | [optional] 
**job_submit_user_msg** | **str** | Message to user from job_submit plugin | [optional] 

## Example

```python
from openapi_client.models.v0039_job_submission_response import V0039JobSubmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobSubmissionResponse from a JSON string
v0039_job_submission_response_instance = V0039JobSubmissionResponse.from_json(json)
# print the JSON string representation of the object
print(V0039JobSubmissionResponse.to_json())

# convert the object into a dict
v0039_job_submission_response_dict = v0039_job_submission_response_instance.to_dict()
# create an instance of V0039JobSubmissionResponse from a dict
v0039_job_submission_response_from_dict = V0039JobSubmissionResponse.from_dict(v0039_job_submission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


