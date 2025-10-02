# V0038ReservationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0038Meta**](V0038Meta.md) |  | [optional] 
**errors** | [**List[V0038Error]**](V0038Error.md) | slurm errors | [optional] 
**reservations** | [**List[V0038Reservation]**](V0038Reservation.md) | reservation info | [optional] 

## Example

```python
from openapi_client.models.v0038_reservations_response import V0038ReservationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0038ReservationsResponse from a JSON string
v0038_reservations_response_instance = V0038ReservationsResponse.from_json(json)
# print the JSON string representation of the object
print(V0038ReservationsResponse.to_json())

# convert the object into a dict
v0038_reservations_response_dict = v0038_reservations_response_instance.to_dict()
# create an instance of V0038ReservationsResponse from a dict
v0038_reservations_response_from_dict = V0038ReservationsResponse.from_dict(v0038_reservations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


