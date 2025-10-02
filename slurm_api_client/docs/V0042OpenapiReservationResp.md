# V0042OpenapiReservationResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservations** | [**List[V0042ReservationInfo]**](V0042ReservationInfo.md) |  | 
**last_update** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | 
**meta** | [**V0042OpenapiMeta**](V0042OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0042OpenapiError]**](V0042OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0042OpenapiWarning]**](V0042OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_openapi_reservation_resp import V0042OpenapiReservationResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0042OpenapiReservationResp from a JSON string
v0042_openapi_reservation_resp_instance = V0042OpenapiReservationResp.from_json(json)
# print the JSON string representation of the object
print(V0042OpenapiReservationResp.to_json())

# convert the object into a dict
v0042_openapi_reservation_resp_dict = v0042_openapi_reservation_resp_instance.to_dict()
# create an instance of V0042OpenapiReservationResp from a dict
v0042_openapi_reservation_resp_from_dict = V0042OpenapiReservationResp.from_dict(v0042_openapi_reservation_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


