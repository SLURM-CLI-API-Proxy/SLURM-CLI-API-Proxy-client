# Dbv0038Job

Single job description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account charged by job | [optional] 
**comment** | [**Dbv0038JobComment**](Dbv0038JobComment.md) |  | [optional] 
**allocation_nodes** | **str** | Nodes allocated to job | [optional] 
**array** | [**Dbv0038JobArray**](Dbv0038JobArray.md) |  | [optional] 
**time** | [**Dbv0038JobTime**](Dbv0038JobTime.md) |  | [optional] 
**association** | [**Dbv0038AssociationShortInfo**](Dbv0038AssociationShortInfo.md) |  | [optional] 
**cluster** | **str** | Assigned cluster | [optional] 
**constraints** | **str** | Constraints on job | [optional] 
**derived_exit_code** | [**Dbv0038JobExitCode**](Dbv0038JobExitCode.md) |  | [optional] 
**exit_code** | [**Dbv0038JobExitCode**](Dbv0038JobExitCode.md) |  | [optional] 
**flags** | **List[str]** | List of properties of job | [optional] 
**group** | **str** | User&#39;s group to run job | [optional] 
**het** | [**Dbv0038JobHet**](Dbv0038JobHet.md) |  | [optional] 
**job_id** | **int** | Job id | [optional] 
**name** | **str** | Assigned job name | [optional] 
**mcs** | [**Dbv0038JobMcs**](Dbv0038JobMcs.md) |  | [optional] 
**nodes** | **str** | List of nodes allocated for job | [optional] 
**partition** | **str** | Assigned job&#39;s partition | [optional] 
**priority** | **int** | Priority | [optional] 
**qos** | **str** | Assigned qos name | [optional] 
**required** | [**Dbv0038JobRequired**](Dbv0038JobRequired.md) |  | [optional] 
**kill_request_user** | **str** | User who requested job killed | [optional] 
**reservation** | [**Dbv0038JobReservation**](Dbv0038JobReservation.md) |  | [optional] 
**state** | [**Dbv0038JobState**](Dbv0038JobState.md) |  | [optional] 
**steps** | [**List[Dbv0038JobStep]**](Dbv0038JobStep.md) | Job step description | [optional] 
**tres** | [**Dbv0038JobTres**](Dbv0038JobTres.md) |  | [optional] 
**user** | **str** | Job user | [optional] 
**wckey** | [**Dbv0038JobWckey**](Dbv0038JobWckey.md) |  | [optional] 
**working_directory** | **str** | Directory where job was initially started | [optional] 
**container** | **str** | absolute path to OCI container bundle | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job import Dbv0038Job

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038Job from a JSON string
dbv0038_job_instance = Dbv0038Job.from_json(json)
# print the JSON string representation of the object
print(Dbv0038Job.to_json())

# convert the object into a dict
dbv0038_job_dict = dbv0038_job_instance.to_dict()
# create an instance of Dbv0038Job from a dict
dbv0038_job_from_dict = Dbv0038Job.from_dict(dbv0038_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


