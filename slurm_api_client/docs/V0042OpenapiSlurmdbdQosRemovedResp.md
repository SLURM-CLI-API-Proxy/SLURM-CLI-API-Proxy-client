# V0042OpenapiSlurmdbdQosRemovedResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**removed_qos** | **List[str]** |  | 
**meta** | [**V0042OpenapiMeta**](V0042OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0042OpenapiError]**](V0042OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0042OpenapiWarning]**](V0042OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_openapi_slurmdbd_qos_removed_resp import V0042OpenapiSlurmdbdQosRemovedResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0042OpenapiSlurmdbdQosRemovedResp from a JSON string
v0042_openapi_slurmdbd_qos_removed_resp_instance = V0042OpenapiSlurmdbdQosRemovedResp.from_json(json)
# print the JSON string representation of the object
print(V0042OpenapiSlurmdbdQosRemovedResp.to_json())

# convert the object into a dict
v0042_openapi_slurmdbd_qos_removed_resp_dict = v0042_openapi_slurmdbd_qos_removed_resp_instance.to_dict()
# create an instance of V0042OpenapiSlurmdbdQosRemovedResp from a dict
v0042_openapi_slurmdbd_qos_removed_resp_from_dict = V0042OpenapiSlurmdbdQosRemovedResp.from_dict(v0042_openapi_slurmdbd_qos_removed_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


