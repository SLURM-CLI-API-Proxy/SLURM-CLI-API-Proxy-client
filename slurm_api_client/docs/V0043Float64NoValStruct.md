# V0043Float64NoValStruct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **float** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0043_float64_no_val_struct import V0043Float64NoValStruct

# TODO update the JSON string below
json = "{}"
# create an instance of V0043Float64NoValStruct from a JSON string
v0043_float64_no_val_struct_instance = V0043Float64NoValStruct.from_json(json)
# print the JSON string representation of the object
print(V0043Float64NoValStruct.to_json())

# convert the object into a dict
v0043_float64_no_val_struct_dict = v0043_float64_no_val_struct_instance.to_dict()
# create an instance of V0043Float64NoValStruct from a dict
v0043_float64_no_val_struct_from_dict = V0043Float64NoValStruct.from_dict(v0043_float64_no_val_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


