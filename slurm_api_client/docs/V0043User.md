# V0043User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_level** | **List[str]** | AdminLevel granted to the user | [optional] 
**associations** | [**List[V0043AssocShort]**](V0043AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0043Coord]**](V0043Coord.md) |  | [optional] 
**default** | [**V0042UserDefault**](V0042UserDefault.md) |  | [optional] 
**flags** | **List[str]** | Flags associated with this user | [optional] 
**name** | **str** | User name | 
**old_name** | **str** | Previous user name | [optional] 
**wckeys** | [**List[V0043Wckey]**](V0043Wckey.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_user import V0043User

# TODO update the JSON string below
json = "{}"
# create an instance of V0043User from a JSON string
v0043_user_instance = V0043User.from_json(json)
# print the JSON string representation of the object
print(V0043User.to_json())

# convert the object into a dict
v0043_user_dict = v0043_user_instance.to_dict()
# create an instance of V0043User from a dict
v0043_user_from_dict = V0043User.from_dict(v0043_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


