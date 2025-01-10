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

from openapi_client.models.v0038_node_allocation_sockets import V0038NodeAllocationSockets

class TestV0038NodeAllocationSockets(unittest.TestCase):
    """V0038NodeAllocationSockets unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038NodeAllocationSockets:
        """Test V0038NodeAllocationSockets
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038NodeAllocationSockets`
        """
        model = V0038NodeAllocationSockets()
        if include_optional:
            return V0038NodeAllocationSockets(
                cores = openapi_client.models.cores.cores()
            )
        else:
            return V0038NodeAllocationSockets(
        )
        """

    def testV0038NodeAllocationSockets(self):
        """Test V0038NodeAllocationSockets"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
