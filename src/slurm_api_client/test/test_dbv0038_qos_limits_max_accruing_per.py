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

from openapi_client.models.dbv0038_qos_limits_max_accruing_per import Dbv0038QosLimitsMaxAccruingPer

class TestDbv0038QosLimitsMaxAccruingPer(unittest.TestCase):
    """Dbv0038QosLimitsMaxAccruingPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038QosLimitsMaxAccruingPer:
        """Test Dbv0038QosLimitsMaxAccruingPer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038QosLimitsMaxAccruingPer`
        """
        model = Dbv0038QosLimitsMaxAccruingPer()
        if include_optional:
            return Dbv0038QosLimitsMaxAccruingPer(
                account = 56,
                user = 56
            )
        else:
            return Dbv0038QosLimitsMaxAccruingPer(
        )
        """

    def testDbv0038QosLimitsMaxAccruingPer(self):
        """Test Dbv0038QosLimitsMaxAccruingPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
