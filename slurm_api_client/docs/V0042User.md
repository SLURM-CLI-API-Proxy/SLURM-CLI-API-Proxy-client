# V0042User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_level** | **List[str]** |  | [optional] 
**associations** | [**List[V0042AssocShort]**](V0042AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0042Coord]**](V0042Coord.md) |  | [optional] 
**default** | [**V0042UserDefault**](V0042UserDefault.md) |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**name** | **str** | User name | 
**old_name** | **str** | Previous user name | [optional] 
**wckeys** | [**List[V0042Wckey]**](V0042Wckey.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_user import V0042User

# TODO update the JSON string below
json = "{}"
# create an instance of V0042User from a JSON string
v0042_user_instance = V0042User.from_json(json)
# print the JSON string representation of the object
print(V0042User.to_json())

# convert the object into a dict
v0042_user_dict = v0042_user_instance.to_dict()
# create an instance of V0042User from a dict
v0042_user_from_dict = V0042User.from_dict(v0042_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


