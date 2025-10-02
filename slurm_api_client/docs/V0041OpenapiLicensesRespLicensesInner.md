# V0041OpenapiLicensesRespLicensesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_name** | **str** | Name of the license | [optional] 
**total** | **int** | Total number of licenses present | [optional] 
**used** | **int** | Number of licenses in use | [optional] 
**free** | **int** | Number of licenses currently available | [optional] 
**remote** | **bool** | Indicates whether licenses are served by the database | [optional] 
**reserved** | **int** | Number of licenses reserved | [optional] 
**last_consumed** | **int** | Last known number of licenses that were consumed in the license manager (Remote Only) | [optional] 
**last_deficit** | **int** | Number of \&quot;missing licenses\&quot; from the cluster&#39;s perspective | [optional] 
**last_update** | **int** | When the license information was last updated (UNIX Timestamp) | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_licenses_resp_licenses_inner import V0041OpenapiLicensesRespLicensesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiLicensesRespLicensesInner from a JSON string
v0041_openapi_licenses_resp_licenses_inner_instance = V0041OpenapiLicensesRespLicensesInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiLicensesRespLicensesInner.to_json())

# convert the object into a dict
v0041_openapi_licenses_resp_licenses_inner_dict = v0041_openapi_licenses_resp_licenses_inner_instance.to_dict()
# create an instance of V0041OpenapiLicensesRespLicensesInner from a dict
v0041_openapi_licenses_resp_licenses_inner_from_dict = V0041OpenapiLicensesRespLicensesInner.from_dict(v0041_openapi_licenses_resp_licenses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


