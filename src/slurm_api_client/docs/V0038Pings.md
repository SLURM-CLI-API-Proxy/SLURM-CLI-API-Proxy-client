# V0038Pings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0038Meta**](V0038Meta.md) |  | [optional] 
**errors** | [**List[V0038Error]**](V0038Error.md) | slurm errors | [optional] 
**pings** | [**List[V0038Ping]**](V0038Ping.md) | slurm controller pings | [optional] 

## Example

```python
from openapi_client.models.v0038_pings import V0038Pings

# TODO update the JSON string below
json = "{}"
# create an instance of V0038Pings from a JSON string
v0038_pings_instance = V0038Pings.from_json(json)
# print the JSON string representation of the object
print(V0038Pings.to_json())

# convert the object into a dict
v0038_pings_dict = v0038_pings_instance.to_dict()
# create an instance of V0038Pings from a dict
v0038_pings_from_dict = V0038Pings.from_dict(v0038_pings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


