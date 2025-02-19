#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <username> <server>"
else

    USERNAME=$1
    SERVER=$2

    # Execute the SSH command and capture the output
    OUTPUT=$(ssh "$USERNAME@$SERVER" "scontrol token")
    EXIT_CODE=$?

    # Only export if the previous command succeeded
    if [ $EXIT_CODE -eq 0 ]; then
        export $(echo "$OUTPUT")
        echo SLURM_JWT variable updated
    else
        echo "Error executing scontrol token command (exit code: $EXIT_CODE)"
        exit $EXIT_CODE
    fi
fi