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

from openapi_client.models.dbv0038_response_tres import Dbv0038ResponseTres

class TestDbv0038ResponseTres(unittest.TestCase):
    """Dbv0038ResponseTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038ResponseTres:
        """Test Dbv0038ResponseTres
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038ResponseTres`
        """
        model = Dbv0038ResponseTres()
        if include_optional:
            return Dbv0038ResponseTres(
                meta = openapi_client.models.dbv0/0/38_meta.dbv0.0.38_meta(
                    plugin = openapi_client.models.dbv0_0_38_meta_plugin.dbv0_0_38_meta_plugin(
                        type = '', 
                        name = '', ), 
                    slurm = openapi_client.models.dbv0_0_38_meta_slurm.dbv0_0_38_meta_Slurm(
                        version = openapi_client.models.dbv0_0_38_meta_slurm_version.dbv0_0_38_meta_Slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', ), ),
                errors = [
                    openapi_client.models.dbv0/0/38_error.dbv0.0.38_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ]
            )
        else:
            return Dbv0038ResponseTres(
        )
        """

    def testDbv0038ResponseTres(self):
        """Test Dbv0038ResponseTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
