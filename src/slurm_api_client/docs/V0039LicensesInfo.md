# V0039LicensesInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0039Meta**](V0039Meta.md) |  | [optional] 
**errors** | [**List[V0039Error]**](V0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[V0039Warning]**](V0039Warning.md) | Slurm warnings | [optional] 
**licenses** | [**List[V0039License]**](V0039License.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_licenses_info import V0039LicensesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0039LicensesInfo from a JSON string
v0039_licenses_info_instance = V0039LicensesInfo.from_json(json)
# print the JSON string representation of the object
print(V0039LicensesInfo.to_json())

# convert the object into a dict
v0039_licenses_info_dict = v0039_licenses_info_instance.to_dict()
# create an instance of V0039LicensesInfo from a dict
v0039_licenses_info_from_dict = V0039LicensesInfo.from_dict(v0039_licenses_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


