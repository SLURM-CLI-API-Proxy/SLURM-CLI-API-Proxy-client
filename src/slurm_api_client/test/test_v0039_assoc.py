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

from openapi_client.models.v0039_assoc import V0039Assoc

class TestV0039Assoc(unittest.TestCase):
    """V0039Assoc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039Assoc:
        """Test V0039Assoc
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039Assoc`
        """
        model = V0039Assoc()
        if include_optional:
            return V0039Assoc(
                account = '',
                cluster = '',
                default = openapi_client.models.v0_0_39_assoc_default.v0_0_39_assoc_default(
                    qos = '', ),
                flags = [
                    'DELETED'
                    ],
                max = openapi_client.models.v0_0_39_assoc_max.v0_0_39_assoc_max(
                    jobs = openapi_client.models.v0_0_39_assoc_max_jobs.v0_0_39_assoc_max_jobs(
                        per = openapi_client.models.v0_0_39_assoc_max_jobs_per.v0_0_39_assoc_max_jobs_per(
                            count = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            accruing = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            submitted = , 
                            wall_clock = , ), 
                        active = , 
                        accruing = , 
                        total = , ), 
                    tres = openapi_client.models.v0_0_39_assoc_max_tres.v0_0_39_assoc_max_tres(
                        minutes = openapi_client.models.v0_0_39_assoc_max_tres_minutes.v0_0_39_assoc_max_tres_minutes(), 
                        group = openapi_client.models.v0_0_39_assoc_max_tres_group.v0_0_39_assoc_max_tres_group(), ), 
                    per = openapi_client.models.v0_0_39_assoc_max_per.v0_0_39_assoc_max_per(
                        account = openapi_client.models.v0_0_39_assoc_max_per_account.v0_0_39_assoc_max_per_account(), ), ),
                is_default = True,
                min = openapi_client.models.v0_0_39_assoc_min.v0_0_39_assoc_min(
                    priority_threshold = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                parent_account = '',
                partition = '',
                priority = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                qos = [
                    ''
                    ],
                shares_raw = 56,
                usage = openapi_client.models.v0/0/39_assoc_usage.v0.0.39_assoc_usage(
                    accrue_job_count = 56, 
                    group_used_wallclock = 1.337, 
                    fairshare_factor = 1.337, 
                    fairshare_shares = 56, 
                    normalized_priority = 1.337, 
                    normalized_shares = 1.337, 
                    effective_normalized_usage = 1.337, 
                    normalized_usage = 1.337, 
                    raw_usage = 1.337, 
                    active_jobs = 56, 
                    job_count = 56, 
                    fairshare_level = 1.337, ),
                user = ''
            )
        else:
            return V0039Assoc(
                user = '',
        )
        """

    def testV0039Assoc(self):
        """Test V0039Assoc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
