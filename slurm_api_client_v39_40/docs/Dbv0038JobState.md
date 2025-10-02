# Dbv0038JobState

State properties of job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **str** | Current state of job | [optional] 
**reason** | **str** | Last reason job didn&#39;t run | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_state import Dbv0038JobState

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobState from a JSON string
dbv0038_job_state_instance = Dbv0038JobState.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobState.to_json())

# convert the object into a dict
dbv0038_job_state_dict = dbv0038_job_state_instance.to_dict()
# create an instance of Dbv0038JobState from a dict
dbv0038_job_state_from_dict = Dbv0038JobState.from_dict(dbv0038_job_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


