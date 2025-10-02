# V0039SlurmStepId

step details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | JobID | [optional] 
**step_het_component** | **int** | HetStep | [optional] 
**step_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_slurm_step_id import V0039SlurmStepId

# TODO update the JSON string below
json = "{}"
# create an instance of V0039SlurmStepId from a JSON string
v0039_slurm_step_id_instance = V0039SlurmStepId.from_json(json)
# print the JSON string representation of the object
print(V0039SlurmStepId.to_json())

# convert the object into a dict
v0039_slurm_step_id_dict = v0039_slurm_step_id_instance.to_dict()
# create an instance of V0039SlurmStepId from a dict
v0039_slurm_step_id_from_dict = V0039SlurmStepId.from_dict(v0039_slurm_step_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


