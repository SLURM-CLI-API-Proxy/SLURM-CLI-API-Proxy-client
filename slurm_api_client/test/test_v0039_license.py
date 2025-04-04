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

from openapi_client.models.v0039_license import V0039License

class TestV0039License(unittest.TestCase):
    """V0039License unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039License:
        """Test V0039License
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039License`
        """
        model = V0039License()
        if include_optional:
            return V0039License(
                license_name = '',
                total = 56,
                used = 56,
                free = 56,
                remote = True,
                reserved = 56,
                last_consumed = 56,
                last_deficit = 56,
                last_update = 56
            )
        else:
            return V0039License(
        )
        """

    def testV0039License(self):
        """Test V0039License"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
