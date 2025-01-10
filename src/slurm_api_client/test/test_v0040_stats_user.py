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

from openapi_client.models.v0040_stats_user import V0040StatsUser

class TestV0040StatsUser(unittest.TestCase):
    """V0040StatsUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040StatsUser:
        """Test V0040StatsUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040StatsUser`
        """
        model = V0040StatsUser()
        if include_optional:
            return V0040StatsUser(
                user = '',
                count = 56,
                time = openapi_client.models.v0_0_39_stats_rpc_time.v0_0_39_stats_rpc_time(
                    average = 56, 
                    total = 56, )
            )
        else:
            return V0040StatsUser(
        )
        """

    def testV0040StatsUser(self):
        """Test V0040StatsUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
