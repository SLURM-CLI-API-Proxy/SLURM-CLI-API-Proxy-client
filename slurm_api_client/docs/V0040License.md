# V0040License


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_name** | **str** | Name of the license | [optional] 
**total** | **int** | Total number of licenses present | [optional] 
**used** | **int** | Number of licenses in use | [optional] 
**free** | **int** | Number of licenses currently available | [optional] 
**remote** | **bool** | Indicates whether licenses are served by the database | [optional] 
**reserved** | **int** | Number of licenses reserved | [optional] 
**last_consumed** | **int** | Last known number of licenses that were consumed in the license manager (Remote Only) | [optional] 
**last_deficit** | **int** | Number of \&quot;missing licenses\&quot; from the cluster&#39;s perspective | [optional] 
**last_update** | **int** | When the license information was last updated (UNIX Timestamp) | [optional] 

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


