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

from openapi_client.models.v0038_job_submission import V0038JobSubmission

class TestV0038JobSubmission(unittest.TestCase):
    """V0038JobSubmission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0038JobSubmission:
        """Test V0038JobSubmission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0038JobSubmission`
        """
        model = V0038JobSubmission()
        if include_optional:
            return V0038JobSubmission(
                script = '',
                job = openapi_client.models.v0/0/38_job_properties.v0.0.38_job_properties(
                    account = '', 
                    account_gather_frequency = '', 
                    argv = [
                        ''
                        ], 
                    array = '', 
                    batch_features = '', 
                    begin_time = 56, 
                    burst_buffer = '', 
                    cluster_constraint = '', 
                    comment = '', 
                    constraints = '', 
                    container = '', 
                    core_specification = 56, 
                    cores_per_socket = 56, 
                    cpu_binding = '', 
                    cpu_binding_hint = '', 
                    cpu_frequency = '', 
                    cpus_per_gpu = '', 
                    cpus_per_task = 56, 
                    current_working_directory = '', 
                    deadline = '', 
                    delay_boot = 56, 
                    dependency = '', 
                    distribution = '', 
                    environment = openapi_client.models.environment.environment(), 
                    exclusive = 'user', 
                    get_user_environment = True, 
                    gres = '', 
                    gres_flags = 'disable-binding', 
                    gpu_binding = '', 
                    gpu_frequency = '', 
                    gpus = '', 
                    gpus_per_node = '', 
                    gpus_per_socket = '', 
                    gpus_per_task = '', 
                    hold = True, 
                    kill_on_invalid_dependency = True, 
                    licenses = '', 
                    mail_type = '', 
                    mail_user = '', 
                    mcs_label = '', 
                    memory_binding = '', 
                    memory_per_cpu = 56, 
                    memory_per_gpu = 56, 
                    memory_per_node = 56, 
                    minimum_cpus_per_node = 56, 
                    minimum_nodes = True, 
                    name = '', 
                    nice = 56, 
                    no_kill = True, 
                    nodes = [
                        56
                        ], 
                    open_mode = 'append', 
                    oversubscribe = True, 
                    partition = '', 
                    prefer = '', 
                    priority = '', 
                    qos = '', 
                    requeue = True, 
                    reservation = '', 
                    signal = 'sig_num', 
                    sockets_per_node = 56, 
                    spread_job = True, 
                    standard_error = '', 
                    standard_input = '', 
                    standard_output = '', 
                    tasks = 56, 
                    tasks_per_core = 56, 
                    tasks_per_node = 56, 
                    tasks_per_socket = 56, 
                    thread_specification = 56, 
                    threads_per_core = 56, 
                    time_limit = 56, 
                    time_minimum = 56, 
                    wait_all_nodes = True, 
                    wckey = '', ),
                jobs = [
                    openapi_client.models.v0/0/38_job_properties.v0.0.38_job_properties(
                        account = '', 
                        account_gather_frequency = '', 
                        argv = [
                            ''
                            ], 
                        array = '', 
                        batch_features = '', 
                        begin_time = 56, 
                        burst_buffer = '', 
                        cluster_constraint = '', 
                        comment = '', 
                        constraints = '', 
                        container = '', 
                        core_specification = 56, 
                        cores_per_socket = 56, 
                        cpu_binding = '', 
                        cpu_binding_hint = '', 
                        cpu_frequency = '', 
                        cpus_per_gpu = '', 
                        cpus_per_task = 56, 
                        current_working_directory = '', 
                        deadline = '', 
                        delay_boot = 56, 
                        dependency = '', 
                        distribution = '', 
                        environment = openapi_client.models.environment.environment(), 
                        exclusive = 'user', 
                        get_user_environment = True, 
                        gres = '', 
                        gres_flags = 'disable-binding', 
                        gpu_binding = '', 
                        gpu_frequency = '', 
                        gpus = '', 
                        gpus_per_node = '', 
                        gpus_per_socket = '', 
                        gpus_per_task = '', 
                        hold = True, 
                        kill_on_invalid_dependency = True, 
                        licenses = '', 
                        mail_type = '', 
                        mail_user = '', 
                        mcs_label = '', 
                        memory_binding = '', 
                        memory_per_cpu = 56, 
                        memory_per_gpu = 56, 
                        memory_per_node = 56, 
                        minimum_cpus_per_node = 56, 
                        minimum_nodes = True, 
                        name = '', 
                        nice = 56, 
                        no_kill = True, 
                        nodes = [
                            56
                            ], 
                        open_mode = 'append', 
                        oversubscribe = True, 
                        partition = '', 
                        prefer = '', 
                        priority = '', 
                        qos = '', 
                        requeue = True, 
                        reservation = '', 
                        signal = 'sig_num', 
                        sockets_per_node = 56, 
                        spread_job = True, 
                        standard_error = '', 
                        standard_input = '', 
                        standard_output = '', 
                        tasks = 56, 
                        tasks_per_core = 56, 
                        tasks_per_node = 56, 
                        tasks_per_socket = 56, 
                        thread_specification = 56, 
                        threads_per_core = 56, 
                        time_limit = 56, 
                        time_minimum = 56, 
                        wait_all_nodes = True, 
                        wckey = '', )
                    ]
            )
        else:
            return V0038JobSubmission(
                script = '',
        )
        """

    def testV0038JobSubmission(self):
        """Test V0038JobSubmission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
