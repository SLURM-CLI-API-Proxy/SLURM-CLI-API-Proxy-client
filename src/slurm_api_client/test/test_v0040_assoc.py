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

from openapi_client.models.v0040_assoc import V0040Assoc

class TestV0040Assoc(unittest.TestCase):
    """V0040Assoc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040Assoc:
        """Test V0040Assoc
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040Assoc`
        """
        model = V0040Assoc()
        if include_optional:
            return V0040Assoc(
                accounting = [
                    openapi_client.models.v0/0/40_accounting.v0.0.40_accounting(
                        allocated = openapi_client.models.v0_0_39_accounting_allocated.v0_0_39_accounting_allocated(
                            seconds = 56, ), 
                        id = 56, 
                        start = 56, 
                        tres = openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, ), )
                    ],
                account = '',
                cluster = '',
                comment = '',
                default = openapi_client.models.v0_0_39_assoc_default.v0_0_39_assoc_default(
                    qos = '', ),
                flags = [
                    'DELETED'
                    ],
                max = openapi_client.models.v0_0_40_assoc_max.v0_0_40_assoc_max(
                    jobs = openapi_client.models.v0_0_40_assoc_max_jobs.v0_0_40_assoc_max_jobs(
                        per = openapi_client.models.v0_0_40_assoc_max_jobs_per.v0_0_40_assoc_max_jobs_per(
                            count = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            accruing = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            submitted = , 
                            wall_clock = , ), 
                        active = , 
                        accruing = , 
                        total = , ), 
                    tres = openapi_client.models.v0_0_40_assoc_max_tres.v0_0_40_assoc_max_tres(
                        group = openapi_client.models.v0_0_40_assoc_max_tres_group.v0_0_40_assoc_max_tres_group(
                            minutes = [
                                openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '', 
                                    name = '', 
                                    id = 56, )
                                ], ), 
                        minutes = openapi_client.models.v0_0_40_assoc_max_tres_minutes.v0_0_40_assoc_max_tres_minutes(), ), 
                    per = openapi_client.models.v0_0_40_assoc_max_per.v0_0_40_assoc_max_per(
                        account = openapi_client.models.v0_0_40_assoc_max_per_account.v0_0_40_assoc_max_per_account(), ), ),
                id = openapi_client.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                    account = '', 
                    cluster = '', 
                    partition = '', 
                    user = '', ),
                is_default = True,
                lineage = '',
                min = openapi_client.models.v0_0_40_assoc_min.v0_0_40_assoc_min(
                    priority_threshold = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                parent_account = '',
                partition = '',
                priority = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                qos = [
                    ''
                    ],
                shares_raw = 56,
                user = ''
            )
        else:
            return V0040Assoc(
                user = '',
        )
        """

    def testV0040Assoc(self):
        """Test V0040Assoc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
