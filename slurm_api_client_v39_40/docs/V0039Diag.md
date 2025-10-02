# V0039Diag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0039Meta**](V0039Meta.md) |  | [optional] 
**errors** | [**List[V0039Error]**](V0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[V0039Warning]**](V0039Warning.md) | Slurm warnings | [optional] 
**statistics** | [**V0039StatsMsg**](V0039StatsMsg.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_diag import V0039Diag

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Diag from a JSON string
v0039_diag_instance = V0039Diag.from_json(json)
# print the JSON string representation of the object
print(V0039Diag.to_json())

# convert the object into a dict
v0039_diag_dict = v0039_diag_instance.to_dict()
# create an instance of V0039Diag from a dict
v0039_diag_from_dict = V0039Diag.from_dict(v0039_diag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


