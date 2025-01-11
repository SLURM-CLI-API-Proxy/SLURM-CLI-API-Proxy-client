# V0039JobTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** |  | [optional] 
**eligible** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**start** | **int** |  | [optional] 
**submission** | **int** |  | [optional] 
**suspended** | **int** |  | [optional] 
**system** | [**V0039JobTimeSystem**](V0039JobTimeSystem.md) |  | [optional] 
**limit** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**total** | [**V0039JobTimeSystem**](V0039JobTimeSystem.md) |  | [optional] 
**user** | [**V0039JobTimeSystem**](V0039JobTimeSystem.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_job_time import V0039JobTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobTime from a JSON string
v0039_job_time_instance = V0039JobTime.from_json(json)
# print the JSON string representation of the object
print(V0039JobTime.to_json())

# convert the object into a dict
v0039_job_time_dict = v0039_job_time_instance.to_dict()
# create an instance of V0039JobTime from a dict
v0039_job_time_from_dict = V0039JobTime.from_dict(v0039_job_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


