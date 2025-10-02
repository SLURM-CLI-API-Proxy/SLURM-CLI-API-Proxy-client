# V0042UserShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminlevel** | **List[str]** |  | [optional] 
**defaultaccount** | **str** | Default account | [optional] 
**defaultwckey** | **str** | Default WCKey | [optional] 

## Example

```python
from openapi_client.models.v0042_user_short import V0042UserShort

# TODO update the JSON string below
json = "{}"
# create an instance of V0042UserShort from a JSON string
v0042_user_short_instance = V0042UserShort.from_json(json)
# print the JSON string representation of the object
print(V0042UserShort.to_json())

# convert the object into a dict
v0042_user_short_dict = v0042_user_short_instance.to_dict()
# create an instance of V0042UserShort from a dict
v0042_user_short_from_dict = V0042UserShort.from_dict(v0042_user_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


