# V0040License


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_name** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**used** | **int** |  | [optional] 
**free** | **int** |  | [optional] 
**remote** | **bool** |  | [optional] 
**reserved** | **int** |  | [optional] 
**last_consumed** | **int** |  | [optional] 
**last_deficit** | **int** |  | [optional] 
**last_update** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.v0040_license import V0040License

# TODO update the JSON string below
json = "{}"
# create an instance of V0040License from a JSON string
v0040_license_instance = V0040License.from_json(json)
# print the JSON string representation of the object
print(V0040License.to_json())

# convert the object into a dict
v0040_license_dict = v0040_license_instance.to_dict()
# create an instance of V0040License from a dict
v0040_license_from_dict = V0040License.from_dict(v0040_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


