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

from openapi_client.models.v0040_step_tres_requested import V0040StepTresRequested

class TestV0040StepTresRequested(unittest.TestCase):
    """V0040StepTresRequested unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040StepTresRequested:
        """Test V0040StepTresRequested
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040StepTresRequested`
        """
        model = V0040StepTresRequested()
        if include_optional:
            return V0040StepTresRequested(
                max = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                min = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                average = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                total = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0040StepTresRequested(
        )
        """

    def testV0040StepTresRequested(self):
        """Test V0040StepTresRequested"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
