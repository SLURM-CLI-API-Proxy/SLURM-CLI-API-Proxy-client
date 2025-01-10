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

from openapi_client.models.v0039_job_array_limits_max import V0039JobArrayLimitsMax

class TestV0039JobArrayLimitsMax(unittest.TestCase):
    """V0039JobArrayLimitsMax unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039JobArrayLimitsMax:
        """Test V0039JobArrayLimitsMax
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039JobArrayLimitsMax`
        """
        model = V0039JobArrayLimitsMax()
        if include_optional:
            return V0039JobArrayLimitsMax(
                running = openapi_client.models.v0_0_39_job_array_limits_max_running.v0_0_39_job_array_limits_max_running(
                    tasks = 56, )
            )
        else:
            return V0039JobArrayLimitsMax(
        )
        """

    def testV0039JobArrayLimitsMax(self):
        """Test V0039JobArrayLimitsMax"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
