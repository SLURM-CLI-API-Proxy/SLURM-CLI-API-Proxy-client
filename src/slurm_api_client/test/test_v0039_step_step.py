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

from openapi_client.models.v0039_step_step import V0039StepStep

class TestV0039StepStep(unittest.TestCase):
    """V0039StepStep unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039StepStep:
        """Test V0039StepStep
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039StepStep`
        """
        model = V0039StepStep()
        if include_optional:
            return V0039StepStep(
                id = openapi_client.models.v0/0/39_slurm_step_id.v0.0.39_slurm_step_id(
                    job_id = 56, 
                    step_het_component = 56, 
                    step_id = '', ),
                name = ''
            )
        else:
            return V0039StepStep(
        )
        """

    def testV0039StepStep(self):
        """Test V0039StepStep"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
