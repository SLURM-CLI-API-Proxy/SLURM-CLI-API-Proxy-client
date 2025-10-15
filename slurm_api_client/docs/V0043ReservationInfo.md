# V0043ReservationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **str** | Comma-separated list of permitted accounts | [optional] 
**burst_buffer** | **str** | BurstBuffer - Burst buffer resources reserved | [optional] 
**core_count** | **int** | CoreCnt - Number of cores reserved | [optional] 
**core_specializations** | [**List[V0043ReservationCoreSpec]**](V0043ReservationCoreSpec.md) |  | [optional] 
**end_time** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**features** | **str** | Features - Expression describing the reservation&#39;s required node features | [optional] 
**flags** | **List[str]** | Flags associated with this reservation | [optional] 
**groups** | **str** | Groups - Comma-separated list of permitted groups | [optional] 
**licenses** | **str** | Licenses - Comma-separated list of licenses reserved | [optional] 
**max_start_delay** | **int** | MaxStartDelay - Maximum time an eligible job not requesting this reservation can delay a job requesting it in seconds | [optional] 
**name** | **str** | ReservationName - Name of the reservation | [optional] 
**node_count** | **int** | NodeCnt - Number of nodes reserved | [optional] 
**node_list** | **str** | Nodes - Comma-separated list of node names and/or node ranges reserved | [optional] 
**partition** | **str** | PartitionName - Partition used to reserve nodes from | [optional] 
**purge_completed** | [**V0043ReservationInfoPurgeCompleted**](V0043ReservationInfoPurgeCompleted.md) |  | [optional] 
**start_time** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**watts** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**tres** | **str** | Comma-separated list of required TRES | [optional] 
**users** | **str** | Comma-separated list of permitted users | [optional] 

## Example

```python
from openapi_client.models.v0043_reservation_info import V0043ReservationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0043ReservationInfo from a JSON string
v0043_reservation_info_instance = V0043ReservationInfo.from_json(json)
# print the JSON string representation of the object
print(V0043ReservationInfo.to_json())

# convert the object into a dict
v0043_reservation_info_dict = v0043_reservation_info_instance.to_dict()
# create an instance of V0043ReservationInfo from a dict
v0043_reservation_info_from_dict = V0043ReservationInfo.from_dict(v0043_reservation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


