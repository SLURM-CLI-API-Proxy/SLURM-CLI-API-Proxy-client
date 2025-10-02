# V0038JobProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Charge resources used by this job to specified account. | [optional] 
**account_gather_frequency** | **str** | Define the job accounting and profiling sampling intervals. | [optional] 
**argv** | **List[str]** | Arguments to the script. | [optional] 
**array** | **str** | Submit a job array, multiple jobs to be executed with identical parameters. The indexes specification identifies what array index values should be used. | [optional] 
**batch_features** | **str** | features required for batch script&#39;s node | [optional] 
**begin_time** | **int** | Submit the batch script to the Slurm controller immediately, like normal, but tell the controller to defer the allocation of the job until the specified time. | [optional] 
**burst_buffer** | **str** | Burst buffer specification. | [optional] 
**cluster_constraint** | **str** | Specifies features that a federated cluster must have to have a sibling job submitted to it. | [optional] 
**comment** | **str** | An arbitrary comment. | [optional] 
**constraints** | **str** | node features required by job. | [optional] 
**container** | **str** | absolute path to OCI container bundle | [optional] 
**core_specification** | **int** | Count of specialized threads per node reserved by the job for system operations and not used by the application. | [optional] 
**cores_per_socket** | **int** | Restrict node selection to nodes with at least the specified number of cores per socket. | [optional] 
**cpu_binding** | **str** | Cpu binding | [optional] 
**cpu_binding_hint** | **str** | Cpu binding hint | [optional] 
**cpu_frequency** | **str** | Request that job steps initiated by srun commands inside this sbatch script be run at some requested frequency if possible, on the CPUs selected for the step on the compute node(s). | [optional] 
**cpus_per_gpu** | **str** | Number of CPUs requested per allocated GPU. | [optional] 
**cpus_per_task** | **int** | Advise the Slurm controller that ensuing job steps will require ncpus number of processors per task. | [optional] 
**current_working_directory** | **str** | Instruct Slurm to connect the batch script&#39;s standard output directly to the file name. | [optional] 
**deadline** | **str** | Remove the job if no ending is possible before this deadline (start &gt; (deadline - time[-min])). | [optional] 
**delay_boot** | **int** | Do not reboot nodes in order to satisfied this job&#39;s feature specification if the job has been eligible to run for less than this time period. | [optional] 
**dependency** | **str** | Defer the start of this job until the specified dependencies have been satisfied completed. | [optional] 
**distribution** | **str** | Specify alternate distribution methods for remote processes. | [optional] 
**environment** | **object** | Dictionary of environment entries. | 
**exclusive** | **str** | The job allocation can share nodes just other users with the \&quot;user\&quot; option or with the \&quot;mcs\&quot; option). | [optional] 
**get_user_environment** | **bool** | Load new login environment for user on job node. | [optional] 
**gres** | **str** | Specifies a comma delimited list of generic consumable resources. | [optional] 
**gres_flags** | **str** | Specify generic resource task binding options. | [optional] 
**gpu_binding** | **str** | Requested binding of tasks to GPU. | [optional] 
**gpu_frequency** | **str** | Requested GPU frequency. | [optional] 
**gpus** | **str** | GPUs per job. | [optional] 
**gpus_per_node** | **str** | GPUs per node. | [optional] 
**gpus_per_socket** | **str** | GPUs per socket. | [optional] 
**gpus_per_task** | **str** | GPUs per task. | [optional] 
**hold** | **bool** | Specify the job is to be submitted in a held state (priority of zero). | [optional] 
**kill_on_invalid_dependency** | **bool** | If a job has an invalid dependency, then Slurm is to terminate it. | [optional] 
**licenses** | **str** | Specification of licenses (or other resources available on all nodes of the cluster) which must be allocated to this job. | [optional] 
**mail_type** | **str** | Notify user by email when certain event types occur. | [optional] 
**mail_user** | **str** | User to receive email notification of state changes as defined by mail_type. | [optional] 
**mcs_label** | **str** | This parameter is a group among the groups of the user. | [optional] 
**memory_binding** | **str** | Bind tasks to memory. | [optional] 
**memory_per_cpu** | **int** | Minimum real memory per cpu (MB). | [optional] 
**memory_per_gpu** | **int** | Minimum memory required per allocated GPU. | [optional] 
**memory_per_node** | **int** | Minimum real memory per node (MB). | [optional] 
**minimum_cpus_per_node** | **int** | Minimum number of CPUs per node. | [optional] 
**minimum_nodes** | **bool** | If a range of node counts is given, prefer the smaller count. | [optional] 
**name** | **str** | Specify a name for the job allocation. | [optional] 
**nice** | **int** | Run the job with an adjusted scheduling priority within Slurm. | [optional] 
**no_kill** | **bool** | Do not automatically terminate a job if one of the nodes it has been allocated fails. | [optional] 
**nodes** | **List[int]** | Request that a minimum of minnodes nodes and a maximum node count. | [optional] 
**open_mode** | **str** | Open the output and error files using append or truncate mode as specified. | [optional] [default to 'append']
**oversubscribe** | **bool** | The job allocation can over-subscribe resources with other running jobs. | [optional] [default to False]
**partition** | **str** | Request a specific partition for the resource allocation. | [optional] 
**prefer** | **str** | Comma delimited list of features for scheduler to prefer but not a strict requirement like a constraint. Value can be used for job submission but is only displayed for PENDING jobs. | [optional] 
**priority** | **str** | Request a specific job priority. | [optional] 
**qos** | **str** | Request a quality of service for the job. | [optional] 
**requeue** | **bool** | Specifies that the batch job should eligible to being requeue. | [optional] 
**reservation** | **str** | Allocate resources for the job from the named reservation. | [optional] 
**signal** | **str** | When a job is within sig_time seconds of its end time, send it the signal sig_num. | [optional] 
**sockets_per_node** | **int** | Restrict node selection to nodes with at least the specified number of sockets. | [optional] 
**spread_job** | **bool** | Spread the job allocation over as many nodes as possible and attempt to evenly distribute tasks across the allocated nodes. | [optional] 
**standard_error** | **str** | Instruct Slurm to connect the batch script&#39;s standard error directly to the file name. | [optional] 
**standard_input** | **str** | Instruct Slurm to connect the batch script&#39;s standard input directly to the file name specified. | [optional] 
**standard_output** | **str** | Instruct Slurm to connect the batch script&#39;s standard output directly to the file name. | [optional] 
**tasks** | **int** | Advises the Slurm controller that job steps run within the allocation will launch a maximum of number tasks and to provide for sufficient resources. | [optional] 
**tasks_per_core** | **int** | Request the maximum ntasks be invoked on each core. | [optional] 
**tasks_per_node** | **int** | Request the maximum ntasks be invoked on each node. | [optional] 
**tasks_per_socket** | **int** | Request the maximum ntasks be invoked on each socket. | [optional] 
**thread_specification** | **int** | Count of specialized threads per node reserved by the job for system operations and not used by the application. | [optional] 
**threads_per_core** | **int** | Restrict node selection to nodes with at least the specified number of threads per core. | [optional] 
**time_limit** | **int** | Step time limit in minutes. | [optional] 
**time_minimum** | **int** | Minimum run time in minutes. | [optional] 
**wait_all_nodes** | **bool** | Do not begin execution until all nodes are ready for use. | [optional] 
**wckey** | **str** | Specify wckey to be used with job. | [optional] 

## Example

```python
from openapi_client.models.v0038_job_properties import V0038JobProperties

# TODO update the JSON string below
json = "{}"
# create an instance of V0038JobProperties from a JSON string
v0038_job_properties_instance = V0038JobProperties.from_json(json)
# print the JSON string representation of the object
print(V0038JobProperties.to_json())

# convert the object into a dict
v0038_job_properties_dict = v0038_job_properties_instance.to_dict()
# create an instance of V0038JobProperties from a dict
v0038_job_properties_from_dict = V0038JobProperties.from_dict(v0038_job_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


