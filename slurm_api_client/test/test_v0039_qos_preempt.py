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

from openapi_client.models.v0039_qos_preempt import V0039QosPreempt

class TestV0039QosPreempt(unittest.TestCase):
    """V0039QosPreempt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039QosPreempt:
        """Test V0039QosPreempt
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039QosPreempt`
        """
        model = V0039QosPreempt()
        if include_optional:
            return V0039QosPreempt(
                list = [
                    ''
                    ],
                mode = [
                    'DISABLED'
                    ],
                exempt_time = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0039QosPreempt(
        )
        """

    def testV0039QosPreempt(self):
        """Test V0039QosPreempt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
