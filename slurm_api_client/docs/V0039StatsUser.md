# V0039StatsUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**time** | [**V0039StatsRpcTime**](V0039StatsRpcTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_stats_user import V0039StatsUser

# TODO update the JSON string below
json = "{}"
# create an instance of V0039StatsUser from a JSON string
v0039_stats_user_instance = V0039StatsUser.from_json(json)
# print the JSON string representation of the object
print(V0039StatsUser.to_json())

# convert the object into a dict
v0039_stats_user_dict = v0039_stats_user_instance.to_dict()
# create an instance of V0039StatsUser from a dict
v0039_stats_user_from_dict = V0039StatsUser.from_dict(v0039_stats_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


