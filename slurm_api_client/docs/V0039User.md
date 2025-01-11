# V0039User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_level** | **List[str]** |  | [optional] 
**associations** | [**List[V0039AssocShort]**](V0039AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0039Coord]**](V0039Coord.md) |  | [optional] 
**default** | [**V0039UserDefault**](V0039UserDefault.md) |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**old_name** | **str** |  | [optional] 
**wckeys** | [**List[V0039Wckey]**](V0039Wckey.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_user import V0039User

# TODO update the JSON string below
json = "{}"
# create an instance of V0039User from a JSON string
v0039_user_instance = V0039User.from_json(json)
# print the JSON string representation of the object
print(V0039User.to_json())

# convert the object into a dict
v0039_user_dict = v0039_user_instance.to_dict()
# create an instance of V0039User from a dict
v0039_user_from_dict = V0039User.from_dict(v0039_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


