# Status


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0039Meta**](V0039Meta.md) |  | [optional] 
**errors** | [**List[V0039Error]**](V0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[V0039Warning]**](V0039Warning.md) | Slurm warnings | [optional] 

## Example

```python
from openapi_client.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print(Status.to_json())

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_from_dict = Status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


