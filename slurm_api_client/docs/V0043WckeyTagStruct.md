# V0043WckeyTagStruct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wckey** | **str** | WCKey name | 
**flags** | **List[str]** | Active flags | 

## Example

```python
from openapi_client.models.v0043_wckey_tag_struct import V0043WckeyTagStruct

# TODO update the JSON string below
json = "{}"
# create an instance of V0043WckeyTagStruct from a JSON string
v0043_wckey_tag_struct_instance = V0043WckeyTagStruct.from_json(json)
# print the JSON string representation of the object
print(V0043WckeyTagStruct.to_json())

# convert the object into a dict
v0043_wckey_tag_struct_dict = v0043_wckey_tag_struct_instance.to_dict()
# create an instance of V0043WckeyTagStruct from a dict
v0043_wckey_tag_struct_from_dict = V0043WckeyTagStruct.from_dict(v0043_wckey_tag_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


