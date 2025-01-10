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

from openapi_client.models.v0040_assoc_rec_set import V0040AssocRecSet

class TestV0040AssocRecSet(unittest.TestCase):
    """V0040AssocRecSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040AssocRecSet:
        """Test V0040AssocRecSet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040AssocRecSet`
        """
        model = V0040AssocRecSet()
        if include_optional:
            return V0040AssocRecSet(
                comment = '',
                defaultqos = '',
                grpjobs = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                grpjobsaccrue = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                grpsubmitjobs = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                grptres = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                grptresmins = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                grptresrunmins = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                grpwall = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                maxjobs = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                maxjobsaccrue = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                maxsubmitjobs = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                maxtresminsperjob = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                maxtresrunmins = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                maxtresperjob = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                maxtrespernode = [
                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                maxwalldurationperjob = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                minpriothresh = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                parent = '',
                priority = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                qoslevel = [
                    ''
                    ],
                fairshare = 56
            )
        else:
            return V0040AssocRecSet(
        )
        """

    def testV0040AssocRecSet(self):
        """Test V0040AssocRecSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
