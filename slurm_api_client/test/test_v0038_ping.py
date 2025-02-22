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

from openapi_client.models.v0038_ping import V0038Ping

class TestV0038Ping(unittest.TestCase):
    """V0038Ping unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038Ping:
        """Test V0038Ping
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038Ping`
        """
        model = V0038Ping()
        if include_optional:
            return V0038Ping(
                hostname = '',
                ping = 'UP',
                mode = '',
                status = 56
            )
        else:
            return V0038Ping(
        )
        """

    def testV0038Ping(self):
        """Test V0038Ping"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
