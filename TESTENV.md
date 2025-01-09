
Test SLURM server:

https://github.com/xenon-middleware/xenon-docker-images/tree/master/slurm-23

OpenAPI spec:

```
wget --header="X-SLURM-USER-TOKEN:${SLURM_JWT}" -S -O - http://localhost:6820/openapi.json
```

Sample sumbission
```
curl -X POST \                                                                                                                       ✔ 
     -H "Content-Type: application/json" \
     -d '{"job_name":"my_job", "partition":"all", "account":"def", "time":"01:00:00", "nodes":1, "ntasks_per_node":1, "cpus_per_task":1}' \
     -H "X-SLURM-USER-TOKEN:${SLURM_JWT}" \
     http://localhost:6820/slurm/v0.0.40/job/submit
```
