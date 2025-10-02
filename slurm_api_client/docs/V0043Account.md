# V0043Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[V0043AssocShort]**](V0043AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0043Coord]**](V0043Coord.md) |  | [optional] 
**description** | **str** | Arbitrary string describing the account | 
**name** | **str** | Account name | 
**organization** | **str** | Organization to which the account belongs | 
**flags** | **List[str]** | Flags associated with this account | [optional] 

## Example

```python
from openapi_client.models.v0043_account import V0043Account

# TODO update the JSON string below
json = "{}"
# create an instance of V0043Account from a JSON string
v0043_account_instance = V0043Account.from_json(json)
# print the JSON string representation of the object
print(V0043Account.to_json())

# convert the object into a dict
v0043_account_dict = v0043_account_instance.to_dict()
# create an instance of V0043Account from a dict
v0043_account_from_dict = V0043Account.from_dict(v0043_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


