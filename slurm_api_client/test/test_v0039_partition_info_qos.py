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

from openapi_client.models.v0039_partition_info_qos import V0039PartitionInfoQos

class TestV0039PartitionInfoQos(unittest.TestCase):
    """V0039PartitionInfoQos unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039PartitionInfoQos:
        """Test V0039PartitionInfoQos
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039PartitionInfoQos`
        """
        model = V0039PartitionInfoQos()
        if include_optional:
            return V0039PartitionInfoQos(
                allowed = '',
                deny = '',
                assigned = ''
            )
        else:
            return V0039PartitionInfoQos(
        )
        """

    def testV0039PartitionInfoQos(self):
        """Test V0039PartitionInfoQos"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
