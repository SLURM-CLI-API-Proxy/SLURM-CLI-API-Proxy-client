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

from openapi_client.models.dbv0038_qos_limits_max_tres_per import Dbv0038QosLimitsMaxTresPer

class TestDbv0038QosLimitsMaxTresPer(unittest.TestCase):
    """Dbv0038QosLimitsMaxTresPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038QosLimitsMaxTresPer:
        """Test Dbv0038QosLimitsMaxTresPer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038QosLimitsMaxTresPer`
        """
        model = Dbv0038QosLimitsMaxTresPer()
        if include_optional:
            return Dbv0038QosLimitsMaxTresPer(
                account = [
                    openapi_client.models.dbv0_0_38_tres_list_inner.dbv0_0_38_tres_list_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                job = [
                    openapi_client.models.dbv0_0_38_tres_list_inner.dbv0_0_38_tres_list_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                node = [
                    openapi_client.models.dbv0_0_38_tres_list_inner.dbv0_0_38_tres_list_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                user = [
                    openapi_client.models.dbv0_0_38_tres_list_inner.dbv0_0_38_tres_list_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return Dbv0038QosLimitsMaxTresPer(
        )
        """

    def testDbv0038QosLimitsMaxTresPer(self):
        """Test Dbv0038QosLimitsMaxTresPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
