# V0041OpenapiReservationRespReservationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **str** | Comma separated list of permitted accounts | [optional] 
**burst_buffer** | **str** | BurstBuffer | [optional] 
**core_count** | **int** | CoreCnt | [optional] 
**core_specializations** | [**List[V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner]**](V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner.md) | Reserved cores specification | [optional] 
**end_time** | [**V0041OpenapiReservationRespReservationsInnerEndTime**](V0041OpenapiReservationRespReservationsInnerEndTime.md) |  | [optional] 
**features** | **str** | Features | [optional] 
**flags** | **List[str]** | Flags associated with the reservation | [optional] 
**groups** | **str** | Groups | [optional] 
**licenses** | **str** | Licenses | [optional] 
**max_start_delay** | **int** | MaxStartDelay in seconds | [optional] 
**name** | **str** | ReservationName | [optional] 
**node_count** | **int** | NodeCnt | [optional] 
**node_list** | **str** | Nodes | [optional] 
**partition** | **str** | PartitionName | [optional] 
**purge_completed** | [**V0041OpenapiReservationRespReservationsInnerPurgeCompleted**](V0041OpenapiReservationRespReservationsInnerPurgeCompleted.md) |  | [optional] 
**start_time** | [**V0041OpenapiReservationRespReservationsInnerStartTime**](V0041OpenapiReservationRespReservationsInnerStartTime.md) |  | [optional] 
**watts** | [**V0041OpenapiReservationRespReservationsInnerWatts**](V0041OpenapiReservationRespReservationsInnerWatts.md) |  | [optional] 
**tres** | **str** | Comma separated list of required TRES | [optional] 
**users** | **str** | Comma separated list of permitted users | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_reservation_resp_reservations_inner import V0041OpenapiReservationRespReservationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiReservationRespReservationsInner from a JSON string
v0041_openapi_reservation_resp_reservations_inner_instance = V0041OpenapiReservationRespReservationsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiReservationRespReservationsInner.to_json())

# convert the object into a dict
v0041_openapi_reservation_resp_reservations_inner_dict = v0041_openapi_reservation_resp_reservations_inner_instance.to_dict()
# create an instance of V0041OpenapiReservationRespReservationsInner from a dict
v0041_openapi_reservation_resp_reservations_inner_from_dict = V0041OpenapiReservationRespReservationsInner.from_dict(v0041_openapi_reservation_resp_reservations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


