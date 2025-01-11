# V0039ReservationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **str** |  | [optional] 
**burst_buffer** | **str** |  | [optional] 
**core_count** | **int** |  | [optional] 
**core_specializations** | [**List[V0039ReservationCoreSpec]**](V0039ReservationCoreSpec.md) |  | [optional] 
**end_time** | **int** |  | [optional] 
**features** | **str** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**groups** | **str** |  | [optional] 
**licenses** | **str** |  | [optional] 
**max_start_delay** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**node_count** | **int** |  | [optional] 
**node_list** | **str** |  | [optional] 
**partition** | **str** |  | [optional] 
**purge_completed** | [**V0039ReservationInfoPurgeCompleted**](V0039ReservationInfoPurgeCompleted.md) |  | [optional] 
**start_time** | **int** |  | [optional] 
**watts** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**tres** | **str** |  | [optional] 
**users** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_reservation_info import V0039ReservationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0039ReservationInfo from a JSON string
v0039_reservation_info_instance = V0039ReservationInfo.from_json(json)
# print the JSON string representation of the object
print(V0039ReservationInfo.to_json())

# convert the object into a dict
v0039_reservation_info_dict = v0039_reservation_info_instance.to_dict()
# create an instance of V0039ReservationInfo from a dict
v0039_reservation_info_from_dict = V0039ReservationInfo.from_dict(v0039_reservation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


