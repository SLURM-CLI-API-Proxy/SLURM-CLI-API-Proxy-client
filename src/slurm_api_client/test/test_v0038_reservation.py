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

from openapi_client.models.v0038_reservation import V0038Reservation

class TestV0038Reservation(unittest.TestCase):
    """V0038Reservation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038Reservation:
        """Test V0038Reservation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038Reservation`
        """
        model = V0038Reservation()
        if include_optional:
            return V0038Reservation(
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
                users = ''
            )
        else:
            return V0038Reservation(
        )
        """

    def testV0038Reservation(self):
        """Test V0038Reservation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
