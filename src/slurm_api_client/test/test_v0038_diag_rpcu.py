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

from openapi_client.models.v0038_diag_rpcu import V0038DiagRpcu

class TestV0038DiagRpcu(unittest.TestCase):
    """V0038DiagRpcu unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038DiagRpcu:
        """Test V0038DiagRpcu
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038DiagRpcu`
        """
        model = V0038DiagRpcu()
        if include_optional:
            return V0038DiagRpcu(
                user = '',
                user_id = 56,
                count = 56,
                average_time = 56,
                total_time = 56
            )
        else:
            return V0038DiagRpcu(
        )
        """

    def testV0038DiagRpcu(self):
        """Test V0038DiagRpcu"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
