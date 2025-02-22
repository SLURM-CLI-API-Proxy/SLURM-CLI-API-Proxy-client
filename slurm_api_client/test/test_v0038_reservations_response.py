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

from openapi_client.models.v0038_reservations_response import V0038ReservationsResponse

class TestV0038ReservationsResponse(unittest.TestCase):
    """V0038ReservationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038ReservationsResponse:
        """Test V0038ReservationsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038ReservationsResponse`
        """
        model = V0038ReservationsResponse()
        if include_optional:
            return V0038ReservationsResponse(
                meta = openapi_client.models.v0/0/38_meta.v0.0.38_meta(
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
                    openapi_client.models.v0/0/38_error.v0.0.38_error(
                        error = '', 
                        error_number = 56, )
                    ],
                reservations = [
                    openapi_client.models.v0/0/38_reservation.v0.0.38_reservation(
                        accounts = '', 
                        burst_buffer = '', 
                        core_count = 56, 
                        core_spec_cnt = 56, 
                        end_time = 56, 
                        features = '', 
                        flags = [
                            ''
                            ], 
                        groups = '', 
                        licenses = '', 
                        max_start_delay = 56, 
                        name = '', 
                        node_count = 56, 
                        node_list = '', 
                        partition = '', 
                        purge_completed = openapi_client.models.v0_0_38_reservation_purge_completed.v0_0_38_reservation_purge_completed(
                            time = 56, ), 
                        start_time = 56, 
                        watts = 56, 
                        tres = '', 
                        users = '', )
                    ]
            )
        else:
            return V0038ReservationsResponse(
        )
        """

    def testV0038ReservationsResponse(self):
        """Test V0038ReservationsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
