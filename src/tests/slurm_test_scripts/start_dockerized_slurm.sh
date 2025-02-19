
#!/bin/bash 

# Call this script with 'source' so the SLURM_JWT variable is exported to the current shell


CONTAINER_ID=$(docker ps -q -f name=testslurm)
if [ -n "$CONTAINER_ID" ]; then
    echo "Container testslurm is already running, only updating the token"
    TEST_CLUSTER_TOKEN=$(docker exec testslurm scontrol token)
    export $TEST_CLUSTER_TOKEN
    echo $SLURM_JWT

else
    echo "Starting slurm test container"
    #Dockerized slurm server from the xenon-middleware project.
    docker run -p 10022:22  -p 6821:6820 --name testslurm --privileged  ghcr.io/xenon-middleware/slurm:23 -d &

    # Wait for container to become healthy
    while ! docker exec testslurm scontrol ping > /dev/null 2>&1; do
        echo "Waiting for Slurm to initialize..."
        sleep 5
    done

    TEST_CLUSTER_TOKEN=$(docker exec testslurm scontrol token)
    export $TEST_CLUSTER_TOKEN
    echo $SLURM_JWT

    read -t 0

fi




