# V0040User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_level** | **List[str]** |  | [optional] 
**associations** | [**List[V0040AssocShort]**](V0040AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0040Coord]**](V0040Coord.md) |  | [optional] 
**default** | [**V0040UserDefault**](V0040UserDefault.md) |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**name** | **str** | User name | 
**old_name** | **str** | Previous user name | [optional] 
**wckeys** | [**List[V0040Wckey]**](V0040Wckey.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_user import V0040User

# TODO update the JSON string below
json = "{}"
# create an instance of V0040User from a JSON string
v0040_user_instance = V0040User.from_json(json)
# print the JSON string representation of the object
print(V0040User.to_json())

# convert the object into a dict
v0040_user_dict = v0040_user_instance.to_dict()
# create an instance of V0040User from a dict
v0040_user_from_dict = V0040User.from_dict(v0040_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


