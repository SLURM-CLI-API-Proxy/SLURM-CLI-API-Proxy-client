# V0038Licenses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[V0038Error]**](V0038Error.md) | slurm errors | [optional] 
**licenses** | [**List[V0038License]**](V0038License.md) | licenses info | [optional] 

## Example

```python
from openapi_client.models.v0038_licenses import V0038Licenses

# TODO update the JSON string below
json = "{}"
# create an instance of V0038Licenses from a JSON string
v0038_licenses_instance = V0038Licenses.from_json(json)
# print the JSON string representation of the object
print(V0038Licenses.to_json())

# convert the object into a dict
v0038_licenses_dict = v0038_licenses_instance.to_dict()
# create an instance of V0038Licenses from a dict
v0038_licenses_from_dict = V0038Licenses.from_dict(v0038_licenses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


