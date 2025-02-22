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

from openapi_client.models.dbv0038_job_step import Dbv0038JobStep

class TestDbv0038JobStep(unittest.TestCase):
    """Dbv0038JobStep unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0038JobStep:
        """Test Dbv0038JobStep
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0038JobStep`
        """
        model = Dbv0038JobStep()
        if include_optional:
            return Dbv0038JobStep(
                time = openapi_client.models.dbv0_0_38_job_step_time.dbv0_0_38_job_step_time(
                    elapsed = 56, 
                    end = 56, 
                    start = 56, 
                    suspended = 56, 
                    system = openapi_client.models.dbv0_0_38_job_time_system.dbv0_0_38_job_time_system(
                        seconds = 56, 
                        microseconds = 56, ), 
                    total = openapi_client.models.dbv0_0_38_job_time_total.dbv0_0_38_job_time_total(
                        seconds = 56, 
                        microseconds = 56, ), 
                    user = openapi_client.models.dbv0_0_38_job_time_user.dbv0_0_38_job_time_user(
                        seconds = 56, 
                        microseconds = 56, ), ),
                exit_code = openapi_client.models.dbv0/0/38_job_exit_code.dbv0.0.38_job_exit_code(
                    status = '', 
                    return_code = 56, 
                    signal = openapi_client.models.dbv0_0_38_job_exit_code_signal.dbv0_0_38_job_exit_code_signal(
                        signal_id = 56, 
                        name = '', ), ),
                nodes = openapi_client.models.dbv0_0_38_job_step_nodes.dbv0_0_38_job_step_nodes(
                    count = 56, 
                    range = '', ),
                tasks = openapi_client.models.dbv0_0_38_job_step_tasks.dbv0_0_38_job_step_tasks(
                    count = 56, ),
                pid = '',
                cpu = openapi_client.models.dbv0_0_38_job_step_cpu.dbv0_0_38_job_step_CPU(
                    requested_frequency = openapi_client.models.dbv0_0_38_job_step_cpu_requested_frequency.dbv0_0_38_job_step_CPU_requested_frequency(
                        min = 56, 
                        max = 56, ), 
                    governor = [
                        ''
                        ], ),
                kill_request_user = '',
                state = '',
                statistics = openapi_client.models.dbv0_0_38_job_step_statistics.dbv0_0_38_job_step_statistics(
                    cpu = openapi_client.models.dbv0_0_38_job_step_statistics_cpu.dbv0_0_38_job_step_statistics_CPU(
                        actual_frequency = 56, ), 
                    energy = openapi_client.models.dbv0_0_38_job_step_statistics_energy.dbv0_0_38_job_step_statistics_energy(
                        consumed = 56, ), ),
                step = openapi_client.models.dbv0_0_38_job_step_step.dbv0_0_38_job_step_step(
                    job_id = 56, 
                    het = openapi_client.models.dbv0_0_38_job_step_step_het.dbv0_0_38_job_step_step_het(
                        component = 56, ), 
                    id = '', 
                    name = '', ),
                task = '',
                tres = openapi_client.models.dbv0_0_38_job_step_tres.dbv0_0_38_job_step_tres(
                    requested = openapi_client.models.dbv0_0_38_job_step_tres_requested.dbv0_0_38_job_step_tres_requested(
                        average = [
                            openapi_client.models.dbv0_0_38_tres_list_inner.dbv0_0_38_tres_list_inner(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], 
                        max = [
                            openapi_client.models.dbv0_0_38_tres_list_inner.dbv0_0_38_tres_list_inner(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], 
                        min = , 
                        total = , ), 
                    consumed = openapi_client.models.dbv0_0_38_job_step_tres_requested.dbv0_0_38_job_step_tres_requested(), 
                    allocated = , )
            )
        else:
            return Dbv0038JobStep(
        )
        """

    def testDbv0038JobStep(self):
        """Test Dbv0038JobStep"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
