# Dbv0039WckeyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0039Meta**](Dbv0039Meta.md) |  | [optional] 
**errors** | [**List[Dbv0039Error]**](Dbv0039Error.md) | Slurm errors | [optional] 
**wckeys** | [**List[V0039Wckey]**](V0039Wckey.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0039_wckey_info import Dbv0039WckeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0039WckeyInfo from a JSON string
dbv0039_wckey_info_instance = Dbv0039WckeyInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0039WckeyInfo.to_json())

# convert the object into a dict
dbv0039_wckey_info_dict = dbv0039_wckey_info_instance.to_dict()
# create an instance of Dbv0039WckeyInfo from a dict
dbv0039_wckey_info_from_dict = Dbv0039WckeyInfo.from_dict(dbv0039_wckey_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


