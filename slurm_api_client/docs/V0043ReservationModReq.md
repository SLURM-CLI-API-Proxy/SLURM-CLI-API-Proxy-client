# V0043ReservationModReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservations** | [**List[V0043ReservationDescMsg]**](V0043ReservationDescMsg.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_reservation_mod_req import V0043ReservationModReq

# TODO update the JSON string below
json = "{}"
# create an instance of V0043ReservationModReq from a JSON string
v0043_reservation_mod_req_instance = V0043ReservationModReq.from_json(json)
# print the JSON string representation of the object
print(V0043ReservationModReq.to_json())

# convert the object into a dict
v0043_reservation_mod_req_dict = v0043_reservation_mod_req_instance.to_dict()
# create an instance of V0043ReservationModReq from a dict
v0043_reservation_mod_req_from_dict = V0043ReservationModReq.from_dict(v0043_reservation_mod_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


