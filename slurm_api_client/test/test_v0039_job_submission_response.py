# coding: utf-8

"""
    Slurm Rest API

    API to access and control Slurm DB.

    The version of the OpenAPI document: Slurm-23.11.4&openapi/dbv0.0.38&openapi/dbv0.0.39&openapi/v0.0.39&openapi/slurmctld&openapi/v0.0.38&openapi/slurmdbd
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v0039_job_submission_response import V0039JobSubmissionResponse

class TestV0039JobSubmissionResponse(unittest.TestCase):
    """V0039JobSubmissionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039JobSubmissionResponse:
        """Test V0039JobSubmissionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039JobSubmissionResponse`
        """
        model = V0039JobSubmissionResponse()
        if include_optional:
            return V0039JobSubmissionResponse(
                meta = openapi_client.models.v0/0/39_meta.v0.0.39_meta(
                    plugin = openapi_client.models.dbv0_0_38_meta_plugin.dbv0_0_38_meta_plugin(
                        type = '', 
                        name = '', ), 
                    slurm = openapi_client.models.dbv0_0_39_meta_slurm.dbv0_0_39_meta_Slurm(
                        version = openapi_client.models.dbv0_0_39_meta_slurm_version.dbv0_0_39_meta_Slurm_version(
                            major = 56, 
                            micro = 56, 
                            minor = 56, ), 
                        release = '', ), ),
                errors = [
                    openapi_client.models.v0/0/39_error.v0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    openapi_client.models.v0/0/39_warning.v0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                job_id = 56,
                step_id = '',
                job_submit_user_msg = ''
            )
        else:
            return V0039JobSubmissionResponse(
        )
        """

    def testV0039JobSubmissionResponse(self):
        """Test V0039JobSubmissionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
