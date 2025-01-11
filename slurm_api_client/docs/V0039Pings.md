# V0039Pings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0039Meta**](V0039Meta.md) |  | [optional] 
**errors** | [**List[V0039Error]**](V0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[V0039Warning]**](V0039Warning.md) | Slurm warnings | [optional] 
**pings** | [**List[V0039ControllerPing]**](V0039ControllerPing.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_pings import V0039Pings

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Pings from a JSON string
v0039_pings_instance = V0039Pings.from_json(json)
# print the JSON string representation of the object
print(V0039Pings.to_json())

# convert the object into a dict
v0039_pings_dict = v0039_pings_instance.to_dict()
# create an instance of V0039Pings from a dict
v0039_pings_from_dict = V0039Pings.from_dict(v0039_pings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


