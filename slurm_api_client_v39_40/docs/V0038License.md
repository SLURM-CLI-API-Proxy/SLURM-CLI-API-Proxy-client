# V0038License


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_name** | **str** | name of license | [optional] 
**total** | **int** | total number of licenses | [optional] 
**used** | **int** | number of licenses in use | [optional] 
**free** | **int** | number of licenses available | [optional] 
**reserved** | **int** | number of licenses reserved | [optional] 
**remote** | **bool** | license is remote | [optional] 

## Example

```python
from openapi_client.models.v0038_license import V0038License

# TODO update the JSON string below
json = "{}"
# create an instance of V0038License from a JSON string
v0038_license_instance = V0038License.from_json(json)
# print the JSON string representation of the object
print(V0038License.to_json())

# convert the object into a dict
v0038_license_dict = v0038_license_instance.to_dict()
# create an instance of V0038License from a dict
v0038_license_from_dict = V0038License.from_dict(v0038_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


