# V0040SharesRespMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**List[V0040AssocSharesObjWrap]**](V0040AssocSharesObjWrap.md) |  | [optional] 
**total_shares** | **int** | Total number of shares | [optional] 

## Example

```python
from openapi_client.models.v0040_shares_resp_msg import V0040SharesRespMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0040SharesRespMsg from a JSON string
v0040_shares_resp_msg_instance = V0040SharesRespMsg.from_json(json)
# print the JSON string representation of the object
print(V0040SharesRespMsg.to_json())

# convert the object into a dict
v0040_shares_resp_msg_dict = v0040_shares_resp_msg_instance.to_dict()
# create an instance of V0040SharesRespMsg from a dict
v0040_shares_resp_msg_from_dict = V0040SharesRespMsg.from_dict(v0040_shares_resp_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


