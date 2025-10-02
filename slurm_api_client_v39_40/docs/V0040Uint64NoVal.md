# V0040Uint64NoVal

Integer number with flags

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] [default to False]
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from openapi_client.models.v0040_uint64_no_val import V0040Uint64NoVal

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Uint64NoVal from a JSON string
v0040_uint64_no_val_instance = V0040Uint64NoVal.from_json(json)
# print the JSON string representation of the object
print(V0040Uint64NoVal.to_json())

# convert the object into a dict
v0040_uint64_no_val_dict = v0040_uint64_no_val_instance.to_dict()
# create an instance of V0040Uint64NoVal from a dict
v0040_uint64_no_val_from_dict = V0040Uint64NoVal.from_dict(v0040_uint64_no_val_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


