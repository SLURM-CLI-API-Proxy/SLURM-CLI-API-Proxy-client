# V0042Tres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | TRES type (CPU, MEM, etc) | 
**name** | **str** | TRES name (if applicable) | [optional] 
**id** | **int** | ID used in the database | [optional] 
**count** | **int** | TRES count (0 if listed generically) | [optional] 

## Example

```python
from openapi_client.models.v0042_tres import V0042Tres

# TODO update the JSON string below
json = "{}"
# create an instance of V0042Tres from a JSON string
v0042_tres_instance = V0042Tres.from_json(json)
# print the JSON string representation of the object
print(V0042Tres.to_json())

# convert the object into a dict
v0042_tres_dict = v0042_tres_instance.to_dict()
# create an instance of V0042Tres from a dict
v0042_tres_from_dict = V0042Tres.from_dict(v0042_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


