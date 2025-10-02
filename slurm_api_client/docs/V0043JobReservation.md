# V0043JobReservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of requested reservation | [optional] 
**name** | **str** | Name of reservation to use | [optional] 
**requested** | **str** | Comma-separated list of requested reservation names | [optional] 

## Example

```python
from openapi_client.models.v0043_job_reservation import V0043JobReservation

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobReservation from a JSON string
v0043_job_reservation_instance = V0043JobReservation.from_json(json)
# print the JSON string representation of the object
print(V0043JobReservation.to_json())

# convert the object into a dict
v0043_job_reservation_dict = v0043_job_reservation_instance.to_dict()
# create an instance of V0043JobReservation from a dict
v0043_job_reservation_from_dict = V0043JobReservation.from_dict(v0043_job_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


