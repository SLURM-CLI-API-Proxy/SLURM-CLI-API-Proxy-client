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

from openapi_client.models.v0040_openapi_clusters_resp import V0040OpenapiClustersResp

class TestV0040OpenapiClustersResp(unittest.TestCase):
    """V0040OpenapiClustersResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiClustersResp:
        """Test V0040OpenapiClustersResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiClustersResp`
        """
        model = V0040OpenapiClustersResp()
        if include_optional:
            return V0040OpenapiClustersResp(
                clusters = [
                    openapi_client.models.v0/0/40_cluster_rec.v0.0.40_cluster_rec(
                        controller = openapi_client.models.v0_0_39_cluster_rec_controller.v0_0_39_cluster_rec_controller(
                            host = '', 
                            port = 56, ), 
                        flags = [
                            'REGISTERING'
                            ], 
                        name = '', 
                        nodes = '', 
                        select_plugin = '', 
                        associations = openapi_client.models.v0_0_40_cluster_rec_associations.v0_0_40_cluster_rec_associations(
                            root = openapi_client.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                                account = '', 
                                cluster = '', 
                                partition = '', 
                                user = '', 
                                id = 56, ), ), 
                        rpc_version = 56, 
                        tres = [
                            openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], )
                    ],
                meta = openapi_client.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
                    plugin = openapi_client.models.v0_0_40_openapi_meta_plugin.v0_0_40_openapi_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = openapi_client.models.v0_0_40_openapi_meta_client.v0_0_40_openapi_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = openapi_client.models.v0_0_40_openapi_meta_slurm.v0_0_40_openapi_meta_slurm(
                        version = openapi_client.models.v0_0_40_openapi_meta_slurm_version.v0_0_40_openapi_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    openapi_client.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    openapi_client.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiClustersResp(
                clusters = [
                    openapi_client.models.v0/0/40_cluster_rec.v0.0.40_cluster_rec(
                        controller = openapi_client.models.v0_0_39_cluster_rec_controller.v0_0_39_cluster_rec_controller(
                            host = '', 
                            port = 56, ), 
                        flags = [
                            'REGISTERING'
                            ], 
                        name = '', 
                        nodes = '', 
                        select_plugin = '', 
                        associations = openapi_client.models.v0_0_40_cluster_rec_associations.v0_0_40_cluster_rec_associations(
                            root = openapi_client.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                                account = '', 
                                cluster = '', 
                                partition = '', 
                                user = '', 
                                id = 56, ), ), 
                        rpc_version = 56, 
                        tres = [
                            openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], )
                    ],
        )
        """

    def testV0040OpenapiClustersResp(self):
        """Test V0040OpenapiClustersResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
