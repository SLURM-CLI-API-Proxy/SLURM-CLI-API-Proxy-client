# V0041OpenapiSlurmdbdJobsRespJobsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account the job ran under | [optional] 
**comment** | [**V0040JobComment**](V0040JobComment.md) |  | [optional] 
**allocation_nodes** | **int** | List of nodes allocated to the job | [optional] 
**array** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArray**](V0041OpenapiSlurmdbdJobsRespJobsInnerArray.md) |  | [optional] 
**association** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation**](V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.md) |  | [optional] 
**block** | **str** | The name of the block to be used (used with Blue Gene systems) | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**constraints** | **str** | Feature(s) the job requested as a constraint | [optional] 
**container** | **str** | Absolute path to OCI container bundle | [optional] 
**derived_exit_code** | [**V0041OpenapiJobInfoRespJobsInnerDerivedExitCode**](V0041OpenapiJobInfoRespJobsInnerDerivedExitCode.md) |  | [optional] 
**time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerTime**](V0041OpenapiSlurmdbdJobsRespJobsInnerTime.md) |  | [optional] 
**exit_code** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerExitCode**](V0041OpenapiSlurmdbdJobsRespJobsInnerExitCode.md) |  | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**failed_node** | **str** | Name of node that caused job failure | [optional] 
**flags** | **List[str]** | Flags associated with the job | [optional] 
**group** | **str** | Group ID of the user that owns the job | [optional] 
**het** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerHet**](V0041OpenapiSlurmdbdJobsRespJobsInnerHet.md) |  | [optional] 
**job_id** | **int** | Job ID | [optional] 
**name** | **str** | Job name | [optional] 
**licenses** | **str** | License(s) required by the job | [optional] 
**mcs** | [**V0040JobMcs**](V0040JobMcs.md) |  | [optional] 
**nodes** | **str** | Node(s) allocated to the job | [optional] 
**partition** | **str** | Partition assigned to the job | [optional] 
**hold** | **bool** | Hold (true) or release (false) job | [optional] 
**priority** | [**V0041JobDescMsgPriority**](V0041JobDescMsgPriority.md) |  | [optional] 
**qos** | **str** | Quality of Service assigned to the job | [optional] 
**required** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequired**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequired.md) |  | [optional] 
**kill_request_user** | **str** | User ID that requested termination of the job | [optional] 
**reservation** | [**V0040JobReservation**](V0040JobReservation.md) |  | [optional] 
**script** | **str** | Job batch script; only the first component in a HetJob is populated or honored | [optional] 
**stdin_expanded** | **str** | Job stdin with expanded fields | [optional] 
**stdout_expanded** | **str** | Job stdout with expanded fields | [optional] 
**stderr_expanded** | **str** | Job stderr with expanded fields | [optional] 
**stdout** | **str** | Path to stdout file | [optional] 
**stderr** | **str** | Path to stderr file | [optional] 
**stdin** | **str** | Path to stdin file | [optional] 
**state** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerState**](V0041OpenapiSlurmdbdJobsRespJobsInnerState.md) |  | [optional] 
**steps** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner.md) | Individual steps in the job | [optional] 
**submit_line** | **str** | Command used to submit the job | [optional] 
**tres** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerTres**](V0041OpenapiSlurmdbdJobsRespJobsInnerTres.md) |  | [optional] 
**used_gres** | **str** | Generic resources used by job | [optional] 
**user** | **str** | User that owns the job | [optional] 
**wckey** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerWckey**](V0041OpenapiSlurmdbdJobsRespJobsInnerWckey.md) |  | [optional] 
**working_directory** | **str** | Path to current working directory | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner import V0041OpenapiSlurmdbdJobsRespJobsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInner from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_instance = V0041OpenapiSlurmdbdJobsRespJobsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInner from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInner.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


