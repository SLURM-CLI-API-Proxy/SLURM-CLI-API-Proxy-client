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

from openapi_client.models.v0039_assoc_max_jobs import V0039AssocMaxJobs

class TestV0039AssocMaxJobs(unittest.TestCase):
    """V0039AssocMaxJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039AssocMaxJobs:
        """Test V0039AssocMaxJobs
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039AssocMaxJobs`
        """
        model = V0039AssocMaxJobs()
        if include_optional:
            return V0039AssocMaxJobs(
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
                active = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                accruing = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                total = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0039AssocMaxJobs(
        )
        """

    def testV0039AssocMaxJobs(self):
        """Test V0039AssocMaxJobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
