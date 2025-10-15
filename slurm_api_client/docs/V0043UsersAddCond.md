# V0043UsersAddCond


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **List[str]** |  | [optional] 
**association** | [**V0043AssocRecSet**](V0043AssocRecSet.md) |  | [optional] 
**clusters** | **List[str]** |  | [optional] 
**partitions** | **List[str]** |  | [optional] 
**users** | **List[str]** |  | 
**wckeys** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0043_users_add_cond import V0043UsersAddCond

# TODO update the JSON string below
json = "{}"
# create an instance of V0043UsersAddCond from a JSON string
v0043_users_add_cond_instance = V0043UsersAddCond.from_json(json)
# print the JSON string representation of the object
print(V0043UsersAddCond.to_json())

# convert the object into a dict
v0043_users_add_cond_dict = v0043_users_add_cond_instance.to_dict()
# create an instance of V0043UsersAddCond from a dict
v0043_users_add_cond_from_dict = V0043UsersAddCond.from_dict(v0043_users_add_cond_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


