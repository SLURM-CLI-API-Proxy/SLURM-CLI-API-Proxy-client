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

from openapi_client.models.v0040_partition_info_timeouts import V0040PartitionInfoTimeouts

class TestV0040PartitionInfoTimeouts(unittest.TestCase):
    """V0040PartitionInfoTimeouts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040PartitionInfoTimeouts:
        """Test V0040PartitionInfoTimeouts
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040PartitionInfoTimeouts`
        """
        model = V0040PartitionInfoTimeouts()
        if include_optional:
            return V0040PartitionInfoTimeouts(
                resume = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                suspend = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0040PartitionInfoTimeouts(
        )
        """

    def testV0040PartitionInfoTimeouts(self):
        """Test V0040PartitionInfoTimeouts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
