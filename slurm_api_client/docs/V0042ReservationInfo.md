# V0042ReservationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **str** | Comma separated list of permitted accounts | [optional] 
**burst_buffer** | **str** | BurstBuffer | [optional] 
**core_count** | **int** | CoreCnt | [optional] 
**core_specializations** | [**List[V0042ReservationCoreSpec]**](V0042ReservationCoreSpec.md) |  | [optional] 
**end_time** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**features** | **str** | Features | [optional] 
**flags** | **List[str]** |  | [optional] 
**groups** | **str** | Groups | [optional] 
**licenses** | **str** | Licenses | [optional] 
**max_start_delay** | **int** | MaxStartDelay in seconds | [optional] 
**name** | **str** | ReservationName | [optional] 
**node_count** | **int** | NodeCnt | [optional] 
**node_list** | **str** | Nodes | [optional] 
**partition** | **str** | PartitionName | [optional] 
**purge_completed** | [**V0042ReservationInfoPurgeCompleted**](V0042ReservationInfoPurgeCompleted.md) |  | [optional] 
**start_time** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**watts** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**tres** | **str** | Comma separated list of required TRES | [optional] 
**users** | **str** | Comma separated list of permitted users | [optional] 

## Example

```python
from openapi_client.models.v0042_reservation_info import V0042ReservationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0042ReservationInfo from a JSON string
v0042_reservation_info_instance = V0042ReservationInfo.from_json(json)
# print the JSON string representation of the object
print(V0042ReservationInfo.to_json())

# convert the object into a dict
v0042_reservation_info_dict = v0042_reservation_info_instance.to_dict()
# create an instance of V0042ReservationInfo from a dict
v0042_reservation_info_from_dict = V0042ReservationInfo.from_dict(v0042_reservation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


