# V0040UserShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminlevel** | **List[str]** |  | [optional] 
**defaultaccount** | **str** | Default account | [optional] 
**defaultwckey** | **str** | Default WCKey | [optional] 

## Example

```python
from openapi_client.models.v0040_user_short import V0040UserShort

# TODO update the JSON string below
json = "{}"
# create an instance of V0040UserShort from a JSON string
v0040_user_short_instance = V0040UserShort.from_json(json)
# print the JSON string representation of the object
print(V0040UserShort.to_json())

# convert the object into a dict
v0040_user_short_dict = v0040_user_short_instance.to_dict()
# create an instance of V0040UserShort from a dict
v0040_user_short_from_dict = V0040UserShort.from_dict(v0040_user_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


