# V0040OpenapiMetaSlurm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**V0040OpenapiMetaSlurmVersion**](V0040OpenapiMetaSlurmVersion.md) |  | [optional] 
**release** | **str** | Slurm release string | [optional] 
**cluster** | **str** | Slurm cluster name | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_meta_slurm import V0040OpenapiMetaSlurm

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiMetaSlurm from a JSON string
v0040_openapi_meta_slurm_instance = V0040OpenapiMetaSlurm.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiMetaSlurm.to_json())

# convert the object into a dict
v0040_openapi_meta_slurm_dict = v0040_openapi_meta_slurm_instance.to_dict()
# create an instance of V0040OpenapiMetaSlurm from a dict
v0040_openapi_meta_slurm_from_dict = V0040OpenapiMetaSlurm.from_dict(v0040_openapi_meta_slurm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


