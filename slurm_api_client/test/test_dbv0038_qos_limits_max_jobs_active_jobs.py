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

from openapi_client.models.dbv0038_qos_limits_max_jobs_active_jobs import Dbv0038QosLimitsMaxJobsActiveJobs

class TestDbv0038QosLimitsMaxJobsActiveJobs(unittest.TestCase):
    """Dbv0038QosLimitsMaxJobsActiveJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038QosLimitsMaxJobsActiveJobs:
        """Test Dbv0038QosLimitsMaxJobsActiveJobs
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038QosLimitsMaxJobsActiveJobs`
        """
        model = Dbv0038QosLimitsMaxJobsActiveJobs()
        if include_optional:
            return Dbv0038QosLimitsMaxJobsActiveJobs(
                per = openapi_client.models.dbv0_0_38_qos_limits_max_jobs_active_jobs_per.dbv0_0_38_qos_limits_max_jobs_active_jobs_per(
                    account = 56, 
                    user = 56, )
            )
        else:
            return Dbv0038QosLimitsMaxJobsActiveJobs(
        )
        """

    def testDbv0038QosLimitsMaxJobsActiveJobs(self):
        """Test Dbv0038QosLimitsMaxJobsActiveJobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
