# V0040JobState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **List[str]** |  | [optional] 
**reason** | **str** | Reason for previous Pending or Failed state | [optional] 

## Example

```python
from openapi_client.models.v0040_job_state import V0040JobState

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobState from a JSON string
v0040_job_state_instance = V0040JobState.from_json(json)
# print the JSON string representation of the object
print(V0040JobState.to_json())

# convert the object into a dict
v0040_job_state_dict = v0040_job_state_instance.to_dict()
# create an instance of V0040JobState from a dict
v0040_job_state_from_dict = V0040JobState.from_dict(v0040_job_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


