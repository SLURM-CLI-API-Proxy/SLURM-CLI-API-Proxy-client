# V0040Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[V0040AssocShort]**](V0040AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0040Coord]**](V0040Coord.md) |  | [optional] 
**description** | **str** | Arbitrary string describing the account | 
**name** | **str** | Account name | 
**organization** | **str** | Organization to which the account belongs | 
**flags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0040_account import V0040Account

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Account from a JSON string
v0040_account_instance = V0040Account.from_json(json)
# print the JSON string representation of the object
print(V0040Account.to_json())

# convert the object into a dict
v0040_account_dict = v0040_account_instance.to_dict()
# create an instance of V0040Account from a dict
v0040_account_from_dict = V0040Account.from_dict(v0040_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


