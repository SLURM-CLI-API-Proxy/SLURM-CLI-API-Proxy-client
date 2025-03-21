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

from openapi_client.models.dbv0038_association_usage import Dbv0038AssociationUsage

class TestDbv0038AssociationUsage(unittest.TestCase):
    """Dbv0038AssociationUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038AssociationUsage:
        """Test Dbv0038AssociationUsage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038AssociationUsage`
        """
        model = Dbv0038AssociationUsage()
        if include_optional:
            return Dbv0038AssociationUsage(
                accrue_job_count = 56,
                group_used_wallclock = 1.337,
                fairshare_factor = 1.337,
                fairshare_shares = 56,
                normalized_priority = 56,
                normalized_shares = 1.337,
                effective_normalized_usage = 1.337,
                raw_usage = 56,
                job_count = 56,
                fairshare_level = 1.337
            )
        else:
            return Dbv0038AssociationUsage(
        )
        """

    def testDbv0038AssociationUsage(self):
        """Test Dbv0038AssociationUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
