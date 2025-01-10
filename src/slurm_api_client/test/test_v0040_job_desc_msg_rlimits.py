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

from openapi_client.models.v0040_job_desc_msg_rlimits import V0040JobDescMsgRlimits

class TestV0040JobDescMsgRlimits(unittest.TestCase):
    """V0040JobDescMsgRlimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040JobDescMsgRlimits:
        """Test V0040JobDescMsgRlimits
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040JobDescMsgRlimits`
        """
        model = V0040JobDescMsgRlimits()
        if include_optional:
            return V0040JobDescMsgRlimits(
                cpu = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                fsize = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                data = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                stack = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                core = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                rss = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                nproc = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                nofile = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                memlock = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                var_as = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0040JobDescMsgRlimits(
        )
        """

    def testV0040JobDescMsgRlimits(self):
        """Test V0040JobDescMsgRlimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
