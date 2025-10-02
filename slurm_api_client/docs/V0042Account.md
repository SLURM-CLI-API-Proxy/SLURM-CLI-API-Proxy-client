# V0042Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[V0042AssocShort]**](V0042AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0042Coord]**](V0042Coord.md) |  | [optional] 
**description** | **str** | Arbitrary string describing the account | 
**name** | **str** | Account name | 
**organization** | **str** | Organization to which the account belongs | 
**flags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0042_account import V0042Account

# TODO update the JSON string below
json = "{}"
# create an instance of V0042Account from a JSON string
v0042_account_instance = V0042Account.from_json(json)
# print the JSON string representation of the object
print(V0042Account.to_json())

# convert the object into a dict
v0042_account_dict = v0042_account_instance.to_dict()
# create an instance of V0042Account from a dict
v0042_account_from_dict = V0042Account.from_dict(v0042_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


