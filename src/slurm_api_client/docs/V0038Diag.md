# V0038Diag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0038Meta**](V0038Meta.md) |  | [optional] 
**errors** | [**List[V0038Error]**](V0038Error.md) | slurm errors | [optional] 
**statistics** | [**V0038DiagStatistics**](V0038DiagStatistics.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0038_diag import V0038Diag

# TODO update the JSON string below
json = "{}"
# create an instance of V0038Diag from a JSON string
v0038_diag_instance = V0038Diag.from_json(json)
# print the JSON string representation of the object
print(V0038Diag.to_json())

# convert the object into a dict
v0038_diag_dict = v0038_diag_instance.to_dict()
# create an instance of V0038Diag from a dict
v0038_diag_from_dict = V0038Diag.from_dict(v0038_diag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


