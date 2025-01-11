# V0039Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[V0039AssocShort]**](V0039AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0039Coord]**](V0039Coord.md) |  | [optional] 
**description** | **str** |  | 
**name** | **str** |  | 
**organization** | **str** |  | 
**flags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_account import V0039Account

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Account from a JSON string
v0039_account_instance = V0039Account.from_json(json)
# print the JSON string representation of the object
print(V0039Account.to_json())

# convert the object into a dict
v0039_account_dict = v0039_account_instance.to_dict()
# create an instance of V0039Account from a dict
v0039_account_from_dict = V0039Account.from_dict(v0039_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


