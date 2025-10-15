# V0042AccountShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Arbitrary string describing the account | [optional] 
**organization** | **str** | Organization to which the account belongs | [optional] 

## Example

```python
from openapi_client.models.v0042_account_short import V0042AccountShort

# TODO update the JSON string below
json = "{}"
# create an instance of V0042AccountShort from a JSON string
v0042_account_short_instance = V0042AccountShort.from_json(json)
# print the JSON string representation of the object
print(V0042AccountShort.to_json())

# convert the object into a dict
v0042_account_short_dict = v0042_account_short_instance.to_dict()
# create an instance of V0042AccountShort from a dict
v0042_account_short_from_dict = V0042AccountShort.from_dict(v0042_account_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


