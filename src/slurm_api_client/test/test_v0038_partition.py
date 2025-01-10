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

from openapi_client.models.v0038_partition import V0038Partition

class TestV0038Partition(unittest.TestCase):
    """V0038Partition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038Partition:
        """Test V0038Partition
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038Partition`
        """
        model = V0038Partition()
        if include_optional:
            return V0038Partition(
                flags = [
                    ''
                    ],
                preemption_mode = [
                    ''
                    ],
                allowed_allocation_nodes = '',
                allowed_accounts = '',
                allowed_groups = '',
                allowed_qos = '',
                alternative = '',
                billing_weights = '',
                default_memory_per_cpu = 56,
                default_time_limit = 56,
                denied_accounts = '',
                denied_qos = '',
                preemption_grace_time = 56,
                maximum_cpus_per_node = 56,
                maximum_memory_per_node = 56,
                maximum_nodes_per_job = 56,
                max_time_limit = 56,
                min_nodes_per_job = 56,
                name = '',
                nodes = '',
                over_time_limit = 56,
                priority_job_factor = 56,
                priority_tier = 56,
                qos = '',
                state = '',
                total_cpus = 56,
                total_nodes = 56,
                tres = '',
                maximum_memory_per_cpu = 56,
                default_memory_per_node = 56
            )
        else:
            return V0038Partition(
        )
        """

    def testV0038Partition(self):
        """Test V0038Partition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
