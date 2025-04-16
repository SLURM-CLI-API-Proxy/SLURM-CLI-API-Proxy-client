# Supporting alternative SLURM API versions

As described in the previous sections, this application's core is decoupled from any particular version of API client. All the implemented command handlers make reference to an abstract `SlurmAPIClientWrapper`, and the specific implementation to be used is defined at runtime depending on what's defined on the used YAML configuration files.

Given this, adding support for an alternative version of the SLURM API would require, in principle:

1. Creating a new class that implements the `SlurmAPIClientWrapper` interface.
2. Implementing all of its methods, which could be, for the most part, based on the existing implementations.
3. Redefining new YAML files for each command, changing the mappings according to the new API specifications, and changing the `wrapper_class` accordingly.

```mermaid
---
title: Client wrapper abstraction
---
classDiagram

    class V41SlurmAPIClientWrapper {
        + sbatch_post_request(self, request, conf, slurmrestd_token) SbatchResponse
        + scontrol_update_request(self, target_job_id, request, conf, slurmrestd_token) ScontrolResponse
        + squeue_get_request(self, cli_arguments, conf, slurmrestd_token) SqueueResponse
        + sinfo_get_request(self, cli_arguments, conf, slurmrestd_token) SinfoResponse
    }

    class V39SlurmAPIClientWrapper {
        + sbatch_post_request(self, request, conf, slurmrestd_token) SbatchResponse
        + scontrol_update_request(self, target_job_id, request, conf, slurmrestd_token) ScontrolResponse
        + squeue_get_request(self, cli_arguments, conf, slurmrestd_token) SqueueResponse
        + sinfo_get_request(self, cli_arguments, conf, slurmrestd_token) SinfoResponse
    }


    class SlurmAPIClientWrapper {
        + sbatch_post_request(self, request, conf, slurmrestd_token) SbatchResponse
        + squeue_get_request(self, cli_arguments, conf, slurmrestd_token) SqueueResponse
        + sinfo_get_request(self, cli_arguments, conf, slurmrestd_token) SinfoResponse
        + scontrol_update_request(self, target_job_id, request, conf, slurmrestd_token) ScontrolResponse
    }

    SlurmAPIClientWrapper <|-- V39SlurmAPIClientWrapper
    SlurmAPIClientWrapper <|-- V41SlurmAPIClientWrapper
```

However, the scenario of adding support for new versions has not been explored in detail, and it may require further refinements on the tool design.