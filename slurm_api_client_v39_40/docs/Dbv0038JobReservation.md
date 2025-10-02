# Dbv0038JobReservation

Reservation usage details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Database id of reservation | [optional] 
**name** | **int** | Name of reservation | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_reservation import Dbv0038JobReservation

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobReservation from a JSON string
dbv0038_job_reservation_instance = Dbv0038JobReservation.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobReservation.to_json())

# convert the object into a dict
dbv0038_job_reservation_dict = dbv0038_job_reservation_instance.to_dict()
# create an instance of Dbv0038JobReservation from a dict
dbv0038_job_reservation_from_dict = Dbv0038JobReservation.from_dict(dbv0038_job_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


