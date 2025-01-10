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

from openapi_client.models.v0040_float64_no_val import V0040Float64NoVal

class TestV0040Float64NoVal(unittest.TestCase):
    """V0040Float64NoVal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040Float64NoVal:
        """Test V0040Float64NoVal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040Float64NoVal`
        """
        model = V0040Float64NoVal()
        if include_optional:
            return V0040Float64NoVal(
                set = True,
                infinite = True,
                number = 1.337
            )
        else:
            return V0040Float64NoVal(
        )
        """

    def testV0040Float64NoVal(self):
        """Test V0040Float64NoVal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
