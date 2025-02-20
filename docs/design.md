# Developer documentation

!!! warning "Under Development"
    
    This tool is under active development. The documentation is not complete yet. If you have any 
    questions, please contact us via [GitHub Issues](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/issues)

## Architectural drivers

- Slurm WLM has a reduced set of commands, but the number of optional arguments required by each one is significantly large
- The OpenAPI specification of slurmrest changes significantly on each new version, as well as the supported arguments by each wlm version.
- A wlm can provide support to multiple OpenAPI specification versions
- Each OpenApi specifaction may significantly differ from each other

Client:

https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/SlurmApi.md



### References

- Schmed's [Slurm REST API documentation](https://slurm.schedmd.com/rest_api.html)
- Schmed's [Slurm command line documentation](https://slurm.schedmd.com/sbatch.html)
- [Slurm version vs supported API versions](https://slurm.schedmd.com/upgrades.html#openapi_changes)



```mermaid
graph TD;
    
    
    Users -->|SSH| sinfo[sinfo];
    Users -->|SSH| sbatch[sbatch];
    Users -->|SSH| squeue[squeue];
    Users -->|SSH| scontrol[scontrol];
    
    subgraph "Head Node"
        slurmctld --> slurmdbd[slurmdbd];
        sinfo --> slurmctld;
        sbatch --> slurmctld;
        squeue --> slurmctld;
        scontrol --> slurmctld;
    end
    
    subgraph "Compute Node"
        slurmd1[slurmd] 
    end
    
    subgraph "Compute Node"
        slurmd2[slurmd]
    end
    
    slurmctld --> slurmd1;
    slurmctld --> slurmd2;
    
    slurmdbd --> Database["Slurm Accounting Database"];
```


```mermaid
graph TD;
    

    LocalScript --> sinfop
    LocalScript --> sbatchp
    LocalScript --> squeuep
    LocalScript --> scontrolp

    
    Users -->|SSH| sinfo[sinfo];
    Users -->|SSH| sbatch[sbatch];
    Users -->|SSH| squeue[squeue];
    Users -->|SSH| scontrol[scontrol];
    Users --> sinfop
    Users --> sbatchp
    Users --> squeuep
    Users --> scontrolp

    sinfop[sinfo*] --> |HTTP Request| slurmrestd;
    sbatchp[sbatch*] --> |HTTP Request| slurmrestd;
    squeuep[squeue*] --> |HTTP Request| slurmrestd;
    scontrolp[scontrolp*] --> |HTTP Request| slurmrestd;
    

    subgraph "Slurm controller"
        slurmrestd --> slurmctld[slurmctld];
        slurmctld --> slurmdbd[slurmdbd];
        sinfo --> slurmctld;
        sbatch --> slurmctld;
        squeue --> slurmctld;
        scontrol --> slurmctld;
    end
    
    subgraph "Compute Node"
        slurmd1[slurmd] 
    end
    
    subgraph "Compute Node"
        slurmd2[slurmd]
    end
    
    slurmctld --> slurmd1;
    slurmctld --> slurmd2;
    
    slurmdbd --> Database["Slurm Accounting Database"];
```