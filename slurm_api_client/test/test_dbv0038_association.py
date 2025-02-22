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

from openapi_client.models.dbv0038_association import Dbv0038Association

class TestDbv0038Association(unittest.TestCase):
    """Dbv0038Association unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038Association:
        """Test Dbv0038Association
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038Association`
        """
        model = Dbv0038Association()
        if include_optional:
            return Dbv0038Association(
                account = '',
                cluster = '',
                default = openapi_client.models.dbv0_0_38_association_default.dbv0_0_38_association_default(
                    qos = '', ),
                flags = [
                    ''
                    ],
                max = openapi_client.models.dbv0_0_38_association_max.dbv0_0_38_association_max(
                    jobs = openapi_client.models.dbv0_0_38_association_max_jobs.dbv0_0_38_association_max_jobs(
                        per = openapi_client.models.dbv0_0_38_association_max_jobs_per.dbv0_0_38_association_max_jobs_per(
                            wall_clock = 56, ), ), 
                    per = openapi_client.models.dbv0_0_38_association_max_per.dbv0_0_38_association_max_per(
                        account = openapi_client.models.dbv0_0_38_association_max_per_account.dbv0_0_38_association_max_per_account(
                            wall_clock = 56, ), ), 
                    tres = openapi_client.models.dbv0_0_38_association_max_tres.dbv0_0_38_association_max_tres(
                        total = [
                            openapi_client.models.dbv0_0_38_tres_list_inner.dbv0_0_38_tres_list_inner(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], 
                        minutes = openapi_client.models.dbv0_0_38_association_max_tres_minutes.dbv0_0_38_association_max_tres_minutes(), ), ),
                min = openapi_client.models.dbv0_0_38_association_min.dbv0_0_38_association_min(
                    priority_threshold = 56, ),
                parent_account = '',
                partition = '',
                priority = 56,
                shares_raw = 56,
                usage = openapi_client.models.dbv0_0_38_association_usage.dbv0_0_38_association_usage(
                    accrue_job_count = 56, 
                    group_used_wallclock = 1.337, 
                    fairshare_factor = 1.337, 
                    fairshare_shares = 56, 
                    normalized_priority = 56, 
                    normalized_shares = 1.337, 
                    effective_normalized_usage = 1.337, 
                    raw_usage = 56, 
                    job_count = 56, 
                    fairshare_level = 1.337, ),
                user = '',
                qos = [
                    ''
                    ]
            )
        else:
            return Dbv0038Association(
        )
        """

    def testDbv0038Association(self):
        """Test Dbv0038Association"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
