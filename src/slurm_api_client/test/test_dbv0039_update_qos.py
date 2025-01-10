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

from openapi_client.models.dbv0039_update_qos import Dbv0039UpdateQos

class TestDbv0039UpdateQos(unittest.TestCase):
    """Dbv0039UpdateQos unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039UpdateQos:
        """Test Dbv0039UpdateQos
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039UpdateQos`
        """
        model = Dbv0039UpdateQos()
        if include_optional:
            return Dbv0039UpdateQos(
                qos = [
                    openapi_client.models.v0/0/39_qos.v0.0.39_qos(
                        description = '', 
                        flags = [
                            'NOT_SET'
                            ], 
                        id = 56, 
                        limits = openapi_client.models.v0_0_39_qos_limits.v0_0_39_qos_limits(
                            grace_time = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            max = openapi_client.models.v0_0_39_qos_limits_max.v0_0_39_qos_limits_max(
                                active_jobs = openapi_client.models.v0_0_39_qos_limits_max_active_jobs.v0_0_39_qos_limits_max_active_jobs(
                                    accruing = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    count = , ), 
                                tres = openapi_client.models.v0_0_39_qos_limits_max_tres.v0_0_39_qos_limits_max_tres(
                                    total = [
                                        openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                                            type = '', 
                                            name = '', 
                                            id = 56, )
                                        ], 
                                    minutes = openapi_client.models.v0_0_39_qos_limits_max_tres_minutes.v0_0_39_qos_limits_max_tres_minutes(
                                        per = openapi_client.models.v0_0_39_qos_limits_max_tres_minutes_per.v0_0_39_qos_limits_max_tres_minutes_per(
                                            qos = [
                                                openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                                                    type = '', 
                                                    name = '', 
                                                    id = 56, )
                                                ], 
                                            job = , 
                                            account = , 
                                            user = , ), ), 
                                    per = openapi_client.models.v0_0_39_qos_limits_max_tres_per.v0_0_39_qos_limits_max_tres_per(
                                        node = , ), ), 
                                wall_clock = openapi_client.models.v0_0_39_qos_limits_max_wall_clock.v0_0_39_qos_limits_max_wall_clock(), 
                                jobs = openapi_client.models.v0_0_39_qos_limits_max_jobs.v0_0_39_qos_limits_max_jobs(), 
                                accruing = openapi_client.models.v0_0_39_qos_limits_max_jobs_active_jobs.v0_0_39_qos_limits_max_jobs_active_jobs(), ), 
                            factor = 1.337, 
                            min = openapi_client.models.v0_0_39_qos_limits_min.v0_0_39_qos_limits_min(
                                priority_threshold = , ), ), 
                        name = '', 
                        preempt = openapi_client.models.v0_0_39_qos_preempt.v0_0_39_qos_preempt(
                            list = [
                                ''
                                ], 
                            mode = [
                                'DISABLED'
                                ], 
                            exempt_time = , ), 
                        priority = , 
                        usage_factor = openapi_client.models.v0/0/39_float64_no_val.v0.0.39_float64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), 
                        usage_threshold = openapi_client.models.v0/0/39_float64_no_val.v0.0.39_float64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), )
                    ]
            )
        else:
            return Dbv0039UpdateQos(
        )
        """

    def testDbv0039UpdateQos(self):
        """Test Dbv0039UpdateQos"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
