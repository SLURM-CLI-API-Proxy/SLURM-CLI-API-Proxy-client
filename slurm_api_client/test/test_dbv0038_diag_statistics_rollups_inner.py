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

from openapi_client.models.dbv0038_diag_statistics_rollups_inner import Dbv0038DiagStatisticsRollupsInner

class TestDbv0038DiagStatisticsRollupsInner(unittest.TestCase):
    """Dbv0038DiagStatisticsRollupsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038DiagStatisticsRollupsInner:
        """Test Dbv0038DiagStatisticsRollupsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038DiagStatisticsRollupsInner`
        """
        model = Dbv0038DiagStatisticsRollupsInner()
        if include_optional:
            return Dbv0038DiagStatisticsRollupsInner(
                type = '',
                last_run = 56,
                last_cycle = 56,
                max_cycle = 56,
                total_time = 56,
                mean_cycles = 56
            )
        else:
            return Dbv0038DiagStatisticsRollupsInner(
        )
        """

    def testDbv0038DiagStatisticsRollupsInner(self):
        """Test Dbv0038DiagStatisticsRollupsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
