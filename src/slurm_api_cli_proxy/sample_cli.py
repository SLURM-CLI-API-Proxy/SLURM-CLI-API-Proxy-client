import openapi_client

from openapi_client.rest import ApiException
from pprint import pprint

configuration = openapi_client.Configuration(

    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = '12345' # str | Slurm JobID

    try:
        # get job info
        api_response = api_instance.slurm_v0038_get_job(job_id)
        print("The response of SlurmApi->slurm_v0038_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_job: %s\n" % e)