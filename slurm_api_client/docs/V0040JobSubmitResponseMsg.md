# V0040JobSubmitResponseMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | New job ID | [optional] 
**step_id** | **str** | New job step ID | [optional] 
**error_code** | **int** | Error code | [optional] 
**error** | **str** | Error message | [optional] 
**job_submit_user_msg** | **str** | Message to user from job_submit plugin | [optional] 

## Example

```python
from openapi_client.models.v0040_job_submit_response_msg import V0040JobSubmitResponseMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobSubmitResponseMsg from a JSON string
v0040_job_submit_response_msg_instance = V0040JobSubmitResponseMsg.from_json(json)
# print the JSON string representation of the object
print(V0040JobSubmitResponseMsg.to_json())

# convert the object into a dict
v0040_job_submit_response_msg_dict = v0040_job_submit_response_msg_instance.to_dict()
# create an instance of V0040JobSubmitResponseMsg from a dict
v0040_job_submit_response_msg_from_dict = V0040JobSubmitResponseMsg.from_dict(v0040_job_submit_response_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


