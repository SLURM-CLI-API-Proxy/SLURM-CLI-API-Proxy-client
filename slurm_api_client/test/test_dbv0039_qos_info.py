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

from openapi_client.models.dbv0039_qos_info import Dbv0039QosInfo

class TestDbv0039QosInfo(unittest.TestCase):
    """Dbv0039QosInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039QosInfo:
        """Test Dbv0039QosInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039QosInfo`
        """
        model = Dbv0039QosInfo()
        if include_optional:
            return Dbv0039QosInfo(
                meta = openapi_client.models.dbv0/0/39_meta.dbv0.0.39_meta(
                    plugin = openapi_client.models.dbv0_0_38_meta_plugin.dbv0_0_38_meta_plugin(
                        type = '', 
                        name = '', ), 
                    slurm = openapi_client.models.dbv0_0_39_meta_slurm.dbv0_0_39_meta_Slurm(
                        version = openapi_client.models.dbv0_0_39_meta_slurm_version.dbv0_0_39_meta_Slurm_version(
                            major = 56, 
                            micro = 56, 
                            minor = 56, ), 
                        release = '', ), ),
                warnings = [
                    openapi_client.models.dbv0/0/39_warning.dbv0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                errors = [
                    openapi_client.models.dbv0/0/39_error.dbv0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
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
            return Dbv0039QosInfo(
        )
        """

    def testDbv0039QosInfo(self):
        """Test Dbv0039QosInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
