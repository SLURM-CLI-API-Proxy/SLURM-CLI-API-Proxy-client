# Command-line interface proxy for SLURM REST API


!!! warning "Under Development"
    
    This tool is under active development. The documentation is not complete yet. If you have any 
    questions, please contact us via [GitHub Issues](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/issues)


The SLURM CLI-API Proxy client is a tool designed to bridge existing applications and scripts that rely on the SLURM CLI. The tool mimics traditional SLURM CLI commands (like sbatch), translating them into REST API calls. This enables seamless integration of existing tools with external SLURM workload managers.

An application from the biomedical domain would be a Galaxy Pulsar server that forwards jobs to an HPC backend through SLURM.

Another key use case for this tool is Arvados, an open-source platform designed for managing and processing large biomedical data.

But in fact, anywhere where a setup assumes the SLURM CLI to be available on a host, the SLURM CLI-API Proxy could help to offload job processing to a more powerful system.

Galaxy
A Galaxy Pulsar server can be configured to pick up compute jobs by itself. But it can also be configured to forward them through a SLURM CLI. However, on public HPC Systems like the Dutch Snellius supercomputer, the SLURM CLI is only available on nodes that are not intended for running services like Galaxy Pulsar on them. “Mocking” the CLI can be a solution. The proxy picks up issued SLURM CLI commands and translates them into SLURM REST API calls. These calls are sent to the public HPC system’s REST-API endpoint.

Arvados
One of the key components of Arvados, the Arvados-SLURM dispatcher, is designed to provide access to a local SLURM workload manager, using a CLI-based integration (i.e., using sbatch and related commands under the hood). While this allows Arvados to leverage SLURM for job scheduling and resource management, it requires Arvados nodes to run within the HPC infrastructure where these commands are available. Therefore, when a connection between Arvados and an external SLURM workload manager is needed, setting up the Arvados-SLURM dispatcher requires multiple networking/tunneling tweaks, something that is not desirable on an HPC research infrastructure. For instance, in SURF’s infrastructure, an Arvados cluster deployed on the SURF Research Cloud would require these 'tweaks' to offload computing tasks to Snellius, despite both being offered by SURF.

While refactoring Arvados to integrate directly with the SLURM REST API would be an option to address this challenge, the complexity and scale of its codebase makes the SLURM CLI-API Proxy client a more cost-effective solution. Based on the SLURM REST API, this proxy integrates seamlessly with Arvados without requiring any modifications to its existing codebase.

