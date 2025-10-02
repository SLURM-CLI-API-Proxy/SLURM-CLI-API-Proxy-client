# V0043InstanceTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_end** | **int** | When the instance will end (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**time_start** | **int** | When the instance will start (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 

## Example

```python
from openapi_client.models.v0043_instance_time import V0043InstanceTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0043InstanceTime from a JSON string
v0043_instance_time_instance = V0043InstanceTime.from_json(json)
# print the JSON string representation of the object
print(V0043InstanceTime.to_json())

# convert the object into a dict
v0043_instance_time_dict = v0043_instance_time_instance.to_dict()
# create an instance of V0043InstanceTime from a dict
v0043_instance_time_from_dict = V0043InstanceTime.from_dict(v0043_instance_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


