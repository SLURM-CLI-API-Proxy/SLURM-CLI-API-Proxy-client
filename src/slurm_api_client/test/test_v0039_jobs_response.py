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

from openapi_client.models.v0039_jobs_response import V0039JobsResponse

class TestV0039JobsResponse(unittest.TestCase):
    """V0039JobsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039JobsResponse:
        """Test V0039JobsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039JobsResponse`
        """
        model = V0039JobsResponse()
        if include_optional:
            return V0039JobsResponse(
                meta = openapi_client.models.v0/0/39_meta.v0.0.39_meta(
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
                    openapi_client.models.v0/0/39_error.v0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    openapi_client.models.v0/0/39_warning.v0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                jobs = [
                    openapi_client.models.v0/0/39_job_info.v0.0.39_job_info(
                        account = '', 
                        accrue_time = 56, 
                        admin_comment = '', 
                        allocating_node = '', 
                        array_job_id = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        array_task_id = openapi_client.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        array_max_tasks = , 
                        array_task_string = '', 
                        association_id = 56, 
                        batch_features = '', 
                        batch_flag = True, 
                        batch_host = '', 
                        flags = [
                            'KILL_INVALID_DEPENDENCY'
                            ], 
                        burst_buffer = '', 
                        burst_buffer_state = '', 
                        cluster = '', 
                        cluster_features = '', 
                        command = '', 
                        comment = '', 
                        container = '', 
                        container_id = '', 
                        contiguous = True, 
                        core_spec = 56, 
                        thread_spec = 56, 
                        cores_per_socket = openapi_client.models.v0/0/39_uint16_no_val.v0.0.39_uint16_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        billable_tres = openapi_client.models.v0/0/39_float64_no_val.v0.0.39_float64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), 
                        cpus_per_task = openapi_client.models.v0/0/39_uint16_no_val.v0.0.39_uint16_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        cpu_frequency_minimum = , 
                        cpu_frequency_maximum = , 
                        cpu_frequency_governor = , 
                        cpus_per_tres = '', 
                        cron = '', 
                        deadline = 56, 
                        delay_boot = , 
                        dependency = '', 
                        derived_exit_code = , 
                        eligible_time = 56, 
                        end_time = 56, 
                        excluded_nodes = '', 
                        exit_code = , 
                        extra = '', 
                        failed_node = '', 
                        features = '', 
                        federation_origin = '', 
                        federation_siblings_active = '', 
                        federation_siblings_viable = '', 
                        gres_detail = [
                            ''
                            ], 
                        group_id = 56, 
                        group_name = '', 
                        het_job_id = , 
                        het_job_id_set = '', 
                        het_job_offset = , 
                        job_id = 56, 
                        job_resources = openapi_client.models.v0/0/39_job_res.v0.0.39_job_res(
                            nodes = '', 
                            allocated_cores = 56, 
                            allocated_cpus = 56, 
                            allocated_hosts = 56, 
                            allocated_nodes = [
                                null
                                ], ), 
                        job_size_str = [
                            ''
                            ], 
                        job_state = '', 
                        last_sched_evaluation = 56, 
                        licenses = '', 
                        mail_type = [
                            'BEGIN'
                            ], 
                        mail_user = '', 
                        max_cpus = , 
                        max_nodes = , 
                        mcs_label = '', 
                        memory_per_tres = '', 
                        name = '', 
                        network = '', 
                        nodes = '', 
                        nice = 56, 
                        tasks_per_core = , 
                        tasks_per_tres = , 
                        tasks_per_node = , 
                        tasks_per_socket = , 
                        tasks_per_board = , 
                        cpus = , 
                        node_count = , 
                        tasks = , 
                        partition = '', 
                        prefer = '', 
                        memory_per_cpu = openapi_client.models.v0/0/39_uint64_no_val.v0.0.39_uint64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        memory_per_node = openapi_client.models.v0/0/39_uint64_no_val.v0.0.39_uint64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        minimum_cpus_per_node = , 
                        minimum_tmp_disk_per_node = , 
                        power = openapi_client.models.v0_0_39_job_info_power.v0_0_39_job_info_power(), 
                        preempt_time = 56, 
                        preemptable_time = 56, 
                        pre_sus_time = 56, 
                        hold = True, 
                        priority = , 
                        profile = [
                            'NOT_SET'
                            ], 
                        qos = '', 
                        reboot = True, 
                        required_nodes = '', 
                        minimum_switches = 56, 
                        requeue = True, 
                        resize_time = 56, 
                        restart_cnt = 56, 
                        resv_name = '', 
                        scheduled_nodes = '', 
                        selinux_context = '', 
                        shared = [
                            'none'
                            ], 
                        exclusive = [
                            'true'
                            ], 
                        oversubscribe = True, 
                        show_flags = [
                            'ALL'
                            ], 
                        sockets_per_board = 56, 
                        sockets_per_node = , 
                        start_time = 56, 
                        state_description = '', 
                        state_reason = '', 
                        standard_error = '', 
                        standard_input = '', 
                        standard_output = '', 
                        submit_time = 56, 
                        suspend_time = 56, 
                        system_comment = '', 
                        time_limit = , 
                        time_minimum = , 
                        threads_per_core = , 
                        tres_bind = '', 
                        tres_freq = '', 
                        tres_per_job = '', 
                        tres_per_node = '', 
                        tres_per_socket = '', 
                        tres_per_task = '', 
                        tres_req_str = '', 
                        tres_alloc_str = '', 
                        user_id = 56, 
                        user_name = '', 
                        maximum_switch_wait_time = 56, 
                        wckey = '', 
                        current_working_directory = '', )
                    ]
            )
        else:
            return V0039JobsResponse(
        )
        """

    def testV0039JobsResponse(self):
        """Test V0039JobsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
