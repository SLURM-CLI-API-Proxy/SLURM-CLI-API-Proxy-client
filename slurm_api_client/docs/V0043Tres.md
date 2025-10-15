# V0043Tres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | TRES type (CPU, MEM, etc) | 
**name** | **str** | TRES name (if applicable) | [optional] 
**id** | **int** | ID used in the database | [optional] 
**count** | **int** | TRES count (0 if listed generically) | [optional] 

## Example

```python
from openapi_client.models.v0043_tres import V0043Tres

# TODO update the JSON string below
json = "{}"
# create an instance of V0043Tres from a JSON string
v0043_tres_instance = V0043Tres.from_json(json)
# print the JSON string representation of the object
print(V0043Tres.to_json())

# convert the object into a dict
v0043_tres_dict = v0043_tres_instance.to_dict()
# create an instance of V0043Tres from a dict
v0043_tres_from_dict = V0043Tres.from_dict(v0043_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


