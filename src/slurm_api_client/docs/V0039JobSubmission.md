# V0039JobSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | Executable script (full contents) to run in batch step for all job components | [optional] 
**job** | [**V0039JobDescMsg**](V0039JobDescMsg.md) |  | [optional] 
**jobs** | [**List[V0039JobDescMsg]**](V0039JobDescMsg.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_job_submission import V0039JobSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobSubmission from a JSON string
v0039_job_submission_instance = V0039JobSubmission.from_json(json)
# print the JSON string representation of the object
print(V0039JobSubmission.to_json())

# convert the object into a dict
v0039_job_submission_dict = v0039_job_submission_instance.to_dict()
# create an instance of V0039JobSubmission from a dict
v0039_job_submission_from_dict = V0039JobSubmission.from_dict(v0039_job_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


