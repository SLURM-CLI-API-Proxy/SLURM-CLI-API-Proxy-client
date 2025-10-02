# V0043AccountShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Arbitrary string describing the account | [optional] 
**organization** | **str** | Organization to which the account belongs | [optional] 

## Example

```python
from openapi_client.models.v0043_account_short import V0043AccountShort

# TODO update the JSON string below
json = "{}"
# create an instance of V0043AccountShort from a JSON string
v0043_account_short_instance = V0043AccountShort.from_json(json)
# print the JSON string representation of the object
print(V0043AccountShort.to_json())

# convert the object into a dict
v0043_account_short_dict = v0043_account_short_instance.to_dict()
# create an instance of V0043AccountShort from a dict
v0043_account_short_from_dict = V0043AccountShort.from_dict(v0043_account_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


