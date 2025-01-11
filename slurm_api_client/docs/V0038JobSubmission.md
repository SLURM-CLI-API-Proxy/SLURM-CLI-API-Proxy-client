# V0038JobSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | Executable script (full contents) to run in batch step | 
**job** | [**V0038JobProperties**](V0038JobProperties.md) |  | [optional] 
**jobs** | [**List[V0038JobProperties]**](V0038JobProperties.md) | Properties of an HetJob | [optional] 

## Example

```python
from openapi_client.models.v0038_job_submission import V0038JobSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of V0038JobSubmission from a JSON string
v0038_job_submission_instance = V0038JobSubmission.from_json(json)
# print the JSON string representation of the object
print(V0038JobSubmission.to_json())

# convert the object into a dict
v0038_job_submission_dict = v0038_job_submission_instance.to_dict()
# create an instance of V0038JobSubmission from a dict
v0038_job_submission_from_dict = V0038JobSubmission.from_dict(v0038_job_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


