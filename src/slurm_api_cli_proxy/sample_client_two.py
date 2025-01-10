import openapi_client
import os

from openapi_client.rest import ApiException
from pprint import pprint

configuration = openapi_client.Configuration(

    #host = "http://localhost:8080/hcadavid6/slurm-rest_api_ro/0.0.38"
    host = "http://localhost:6820/slurm/v0.0.40"

    #host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzY1MjI2NDAsImlhdCI6MTczNjUyMDg0MCwic3VuIjoieGVub24ifQ.dj12i_cGAXw862_VFVA6p5QVBHxE4IPQPFD6YUIST-0"
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = token

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = token

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = '12345' # str | Slurm JobID

    print(api_instance)

    # try:
    #     # get job info
    #     api_response = api_instance.slurm_v0038_get_job(job_id)
    #     print("The response of SlurmApi->slurm_v0038_get_job:\n")
    #     pprint(api_response)
    # except Exception as e:
    #     print("Exception when calling SlurmApi->slurm_v0038_get_job: %s\n" % e)

