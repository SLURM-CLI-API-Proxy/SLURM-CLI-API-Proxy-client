# V0041OpenapiSlurmdbdConfigRespInstancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** | Cluster name | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**instance_id** | **str** | Cloud instance ID | [optional] 
**instance_type** | **str** | Cloud instance type | [optional] 
**node_name** | **str** | NodeName | [optional] 
**time** | [**V0040InstanceTime**](V0040InstanceTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_instances_inner import V0041OpenapiSlurmdbdConfigRespInstancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespInstancesInner from a JSON string
v0041_openapi_slurmdbd_config_resp_instances_inner_instance = V0041OpenapiSlurmdbdConfigRespInstancesInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespInstancesInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_instances_inner_dict = v0041_openapi_slurmdbd_config_resp_instances_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespInstancesInner from a dict
v0041_openapi_slurmdbd_config_resp_instances_inner_from_dict = V0041OpenapiSlurmdbdConfigRespInstancesInner.from_dict(v0041_openapi_slurmdbd_config_resp_instances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


