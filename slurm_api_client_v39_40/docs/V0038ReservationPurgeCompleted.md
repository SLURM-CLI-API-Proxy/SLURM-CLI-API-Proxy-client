# V0038ReservationPurgeCompleted

If PURGE_COMP flag is set the amount of seconds this reservation will sit idle until it is revoked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **int** | amount of seconds this reservation will sit idle until it is revoked | [optional] 

## Example

```python
from openapi_client.models.v0038_reservation_purge_completed import V0038ReservationPurgeCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of V0038ReservationPurgeCompleted from a JSON string
v0038_reservation_purge_completed_instance = V0038ReservationPurgeCompleted.from_json(json)
# print the JSON string representation of the object
print(V0038ReservationPurgeCompleted.to_json())

# convert the object into a dict
v0038_reservation_purge_completed_dict = v0038_reservation_purge_completed_instance.to_dict()
# create an instance of V0038ReservationPurgeCompleted from a dict
v0038_reservation_purge_completed_from_dict = V0038ReservationPurgeCompleted.from_dict(v0038_reservation_purge_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


