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

from openapi_client.models.v0040_assoc_max import V0040AssocMax

class TestV0040AssocMax(unittest.TestCase):
    """V0040AssocMax unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040AssocMax:
        """Test V0040AssocMax
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040AssocMax`
        """
        model = V0040AssocMax()
        if include_optional:
            return V0040AssocMax(
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
                    total = [
                        openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    group = openapi_client.models.v0_0_40_assoc_max_tres_group.v0_0_40_assoc_max_tres_group(
                        minutes = [
                            openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], 
                        active = , ), 
                    minutes = openapi_client.models.v0_0_40_assoc_max_tres_minutes.v0_0_40_assoc_max_tres_minutes(
                        total = , 
                        per = openapi_client.models.v0_0_40_qos_limits_min_tres_per.v0_0_40_qos_limits_min_tres_per(
                            job = , ), ), 
                    per = openapi_client.models.v0_0_40_assoc_max_tres_per.v0_0_40_assoc_max_tres_per(
                        job = , 
                        node = , ), ),
                per = openapi_client.models.v0_0_40_assoc_max_per.v0_0_40_assoc_max_per(
                    account = openapi_client.models.v0_0_40_assoc_max_per_account.v0_0_40_assoc_max_per_account(
                        wall_clock = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), ), )
            )
        else:
            return V0040AssocMax(
        )
        """

    def testV0040AssocMax(self):
        """Test V0040AssocMax"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
