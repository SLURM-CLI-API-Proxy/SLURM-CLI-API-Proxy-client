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

from openapi_client.models.dbv0038_association_max_jobs import Dbv0038AssociationMaxJobs

class TestDbv0038AssociationMaxJobs(unittest.TestCase):
    """Dbv0038AssociationMaxJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038AssociationMaxJobs:
        """Test Dbv0038AssociationMaxJobs
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038AssociationMaxJobs`
        """
        model = Dbv0038AssociationMaxJobs()
        if include_optional:
            return Dbv0038AssociationMaxJobs(
                per = openapi_client.models.dbv0_0_38_association_max_jobs_per.dbv0_0_38_association_max_jobs_per(
                    wall_clock = 56, )
            )
        else:
            return Dbv0038AssociationMaxJobs(
        )
        """

    def testDbv0038AssociationMaxJobs(self):
        """Test Dbv0038AssociationMaxJobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
