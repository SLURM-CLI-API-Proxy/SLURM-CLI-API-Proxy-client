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

from openapi_client.models.v0039_qos_limits_max_tres import V0039QosLimitsMaxTres

class TestV0039QosLimitsMaxTres(unittest.TestCase):
    """V0039QosLimitsMaxTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039QosLimitsMaxTres:
        """Test V0039QosLimitsMaxTres
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039QosLimitsMaxTres`
        """
        model = V0039QosLimitsMaxTres()
        if include_optional:
            return V0039QosLimitsMaxTres(
                total = [
                    openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                minutes = openapi_client.models.v0_0_39_qos_limits_max_tres_minutes.v0_0_39_qos_limits_max_tres_minutes(
                    per = openapi_client.models.v0_0_39_qos_limits_max_tres_minutes_per.v0_0_39_qos_limits_max_tres_minutes_per(
                        qos = [
                            openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], 
                        job = [
                            openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], 
                        account = , 
                        user = , ), ),
                per = openapi_client.models.v0_0_39_qos_limits_max_tres_per.v0_0_39_qos_limits_max_tres_per(
                    account = [
                        openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    job = [
                        openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    node = , 
                    user = , )
            )
        else:
            return V0039QosLimitsMaxTres(
        )
        """

    def testV0039QosLimitsMaxTres(self):
        """Test V0039QosLimitsMaxTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
