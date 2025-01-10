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

from openapi_client.models.dbv0038_job_step_time import Dbv0038JobStepTime

class TestDbv0038JobStepTime(unittest.TestCase):
    """Dbv0038JobStepTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038JobStepTime:
        """Test Dbv0038JobStepTime
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038JobStepTime`
        """
        model = Dbv0038JobStepTime()
        if include_optional:
            return Dbv0038JobStepTime(
                elapsed = 56,
                end = 56,
                start = 56,
                suspended = 56,
                system = openapi_client.models.dbv0_0_38_job_time_system.dbv0_0_38_job_time_system(
                    seconds = 56, 
                    microseconds = 56, ),
                total = openapi_client.models.dbv0_0_38_job_time_total.dbv0_0_38_job_time_total(
                    seconds = 56, 
                    microseconds = 56, ),
                user = openapi_client.models.dbv0_0_38_job_time_user.dbv0_0_38_job_time_user(
                    seconds = 56, 
                    microseconds = 56, )
            )
        else:
            return Dbv0038JobStepTime(
        )
        """

    def testDbv0038JobStepTime(self):
        """Test Dbv0038JobStepTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
