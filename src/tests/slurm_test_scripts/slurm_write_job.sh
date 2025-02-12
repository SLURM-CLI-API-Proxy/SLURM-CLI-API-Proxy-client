#!/bin/bash
#SBATCH --job-name=file_writer
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err
#SBATCH --time=1:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1

# Write content to a file
echo "Running Slurm job $SLURM_JOB_ID!"
sleep 10
echo "Hello from Slurm job $SLURM_JOB_ID!" >> /tmp/output.txt