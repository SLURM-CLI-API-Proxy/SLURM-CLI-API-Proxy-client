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

from openapi_client.models.dbv0039_config_info import Dbv0039ConfigInfo

class TestDbv0039ConfigInfo(unittest.TestCase):
    """Dbv0039ConfigInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039ConfigInfo:
        """Test Dbv0039ConfigInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039ConfigInfo`
        """
        model = Dbv0039ConfigInfo()
        if include_optional:
            return Dbv0039ConfigInfo(
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
                errors = [
                    openapi_client.models.dbv0/0/39_error.dbv0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    openapi_client.models.dbv0/0/39_warning.dbv0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                tres = [
                    openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                accounts = [
                    openapi_client.models.v0/0/39_account.v0.0.39_account(
                        associations = [
                            openapi_client.models.v0/0/39_assoc_short.v0.0.39_assoc_short(
                                account = '', 
                                cluster = '', 
                                partition = '', 
                                user = '', )
                            ], 
                        coordinators = [
                            openapi_client.models.v0/0/39_coord.v0.0.39_coord(
                                name = '', 
                                direct = True, )
                            ], 
                        description = '', 
                        name = '', 
                        organization = '', 
                        flags = [
                            'DELETED'
                            ], )
                    ],
                associations = [
                    openapi_client.models.v0/0/39_assoc.v0.0.39_assoc(
                        account = '', 
                        cluster = '', 
                        default = openapi_client.models.v0_0_39_assoc_default.v0_0_39_assoc_default(
                            qos = '', ), 
                        flags = [
                            'DELETED'
                            ], 
                        max = openapi_client.models.v0_0_39_assoc_max.v0_0_39_assoc_max(
                            jobs = openapi_client.models.v0_0_39_assoc_max_jobs.v0_0_39_assoc_max_jobs(
                                per = openapi_client.models.v0_0_39_assoc_max_jobs_per.v0_0_39_assoc_max_jobs_per(
                                    count = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    accruing = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    submitted = , 
                                    wall_clock = , ), 
                                active = , 
                                accruing = , 
                                total = , ), 
                            tres = openapi_client.models.v0_0_39_assoc_max_tres.v0_0_39_assoc_max_tres(
                                minutes = openapi_client.models.v0_0_39_assoc_max_tres_minutes.v0_0_39_assoc_max_tres_minutes(), 
                                group = openapi_client.models.v0_0_39_assoc_max_tres_group.v0_0_39_assoc_max_tres_group(), ), 
                            per = openapi_client.models.v0_0_39_assoc_max_per.v0_0_39_assoc_max_per(
                                account = openapi_client.models.v0_0_39_assoc_max_per_account.v0_0_39_assoc_max_per_account(), ), ), 
                        is_default = True, 
                        min = openapi_client.models.v0_0_39_assoc_min.v0_0_39_assoc_min(
                            priority_threshold = , ), 
                        parent_account = '', 
                        partition = '', 
                        priority = , 
                        qos = [
                            ''
                            ], 
                        shares_raw = 56, 
                        usage = openapi_client.models.v0/0/39_assoc_usage.v0.0.39_assoc_usage(
                            accrue_job_count = 56, 
                            group_used_wallclock = 1.337, 
                            fairshare_factor = 1.337, 
                            fairshare_shares = 56, 
                            normalized_priority = 1.337, 
                            normalized_shares = 1.337, 
                            effective_normalized_usage = 1.337, 
                            normalized_usage = 1.337, 
                            raw_usage = 1.337, 
                            active_jobs = 56, 
                            job_count = 56, 
                            fairshare_level = 1.337, ), 
                        user = '', )
                    ],
                users = [
                    openapi_client.models.v0/0/39_user.v0.0.39_user(
                        administrator_level = [
                            'Not Set'
                            ], 
                        associations = [
                            openapi_client.models.v0/0/39_assoc_short.v0.0.39_assoc_short(
                                account = '', 
                                cluster = '', 
                                partition = '', 
                                user = '', )
                            ], 
                        coordinators = [
                            openapi_client.models.v0/0/39_coord.v0.0.39_coord(
                                name = '', 
                                direct = True, )
                            ], 
                        default = openapi_client.models.v0_0_39_user_default.v0_0_39_user_default(
                            account = '', 
                            wckey = '', ), 
                        flags = [
                            'NONE'
                            ], 
                        name = '', 
                        old_name = '', 
                        wckeys = [
                            openapi_client.models.v0/0/39_wckey.v0.0.39_wckey(
                                accounting = [
                                    openapi_client.models.v0/0/39_accounting.v0.0.39_accounting(
                                        allocated = openapi_client.models.v0_0_39_accounting_allocated.v0_0_39_accounting_allocated(
                                            seconds = 56, ), 
                                        id = 56, 
                                        start = 56, 
                                        tres = openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                                            type = '', 
                                            name = '', 
                                            id = 56, 
                                            count = 56, ), )
                                    ], 
                                cluster = '', 
                                id = 56, 
                                name = '', 
                                user = '', )
                            ], )
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
                    ],
                wckeys = [
                    openapi_client.models.v0/0/39_wckey.v0.0.39_wckey(
                        accounting = [
                            openapi_client.models.v0/0/39_accounting.v0.0.39_accounting(
                                allocated = openapi_client.models.v0_0_39_accounting_allocated.v0_0_39_accounting_allocated(
                                    seconds = 56, ), 
                                id = 56, 
                                start = 56, 
                                tres = openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                                    type = '', 
                                    name = '', 
                                    id = 56, 
                                    count = 56, ), )
                            ], 
                        cluster = '', 
                        id = 56, 
                        name = '', 
                        user = '', 
                        flags = [
                            'DELETED'
                            ], )
                    ],
                clusters = [
                    openapi_client.models.v0/0/39_cluster_rec.v0.0.39_cluster_rec(
                        controller = openapi_client.models.v0_0_39_cluster_rec_controller.v0_0_39_cluster_rec_controller(
                            host = '', 
                            port = 56, ), 
                        flags = [
                            'REGISTERING'
                            ], 
                        name = '', 
                        nodes = '', 
                        select_plugin = '', 
                        associations = openapi_client.models.v0_0_39_cluster_rec_associations.v0_0_39_cluster_rec_associations(
                            root = openapi_client.models.v0/0/39_assoc_short.v0.0.39_assoc_short(
                                account = '', 
                                cluster = '', 
                                partition = '', 
                                user = '', ), ), 
                        rpc_version = 56, 
                        tres = [
                            openapi_client.models.v0/0/39_tres.v0.0.39_tres(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], )
                    ]
            )
        else:
            return Dbv0039ConfigInfo(
        )
        """

    def testDbv0039ConfigInfo(self):
        """Test Dbv0039ConfigInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
