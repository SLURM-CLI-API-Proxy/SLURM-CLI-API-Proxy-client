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

from openapi_client.models.v0039_partition_info import V0039PartitionInfo

class TestV0039PartitionInfo(unittest.TestCase):
    """V0039PartitionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039PartitionInfo:
        """Test V0039PartitionInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039PartitionInfo`
        """
        model = V0039PartitionInfo()
        if include_optional:
            return V0039PartitionInfo(
                nodes = openapi_client.models.v0_0_39_partition_info_nodes.v0_0_39_partition_info_nodes(
                    allowed_allocation = '', 
                    configured = '', 
                    total = 56, ),
                accounts = openapi_client.models.v0_0_39_partition_info_accounts.v0_0_39_partition_info_accounts(
                    allowed = '', 
                    deny = '', ),
                groups = openapi_client.models.v0_0_39_partition_info_groups.v0_0_39_partition_info_groups(
                    allowed = '', ),
                qos = openapi_client.models.v0_0_39_partition_info_qos.v0_0_39_partition_info_qos(
                    allowed = '', 
                    deny = '', 
                    assigned = '', ),
                alternate = '',
                tres = openapi_client.models.v0_0_39_partition_info_tres.v0_0_39_partition_info_tres(
                    billing_weights = '', 
                    configured = '', ),
                cluster = '',
                cpus = openapi_client.models.v0_0_39_partition_info_cpus.v0_0_39_partition_info_cpus(
                    task_binding = 56, 
                    total = 56, ),
                defaults = openapi_client.models.v0_0_39_partition_info_defaults.v0_0_39_partition_info_defaults(
                    memory_per_cpu = 56, 
                    time = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    job = '', ),
                grace_time = 56,
                maximums = openapi_client.models.v0_0_39_partition_info_maximums.v0_0_39_partition_info_maximums(
                    cpus_per_node = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    cpus_per_socket = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    memory_per_cpu = 56, 
                    nodes = , 
                    shares = 56, 
                    time = , 
                    over_time_limit = openapi_client.models.v0/0/39_uint16_no_val.v0.0.39_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                minimums = openapi_client.models.v0_0_39_partition_info_minimums.v0_0_39_partition_info_minimums(
                    nodes = 56, ),
                name = '',
                node_sets = '',
                priority = openapi_client.models.v0_0_39_partition_info_priority.v0_0_39_partition_info_priority(
                    job_factor = 56, 
                    tier = 56, ),
                timeouts = openapi_client.models.v0_0_39_partition_info_timeouts.v0_0_39_partition_info_timeouts(
                    resume = openapi_client.models.v0/0/39_uint16_no_val.v0.0.39_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    suspend = openapi_client.models.v0/0/39_uint16_no_val.v0.0.39_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                suspend_time = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0039PartitionInfo(
        )
        """

    def testV0039PartitionInfo(self):
        """Test V0039PartitionInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
