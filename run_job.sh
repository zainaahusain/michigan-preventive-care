#!/bin/bash


# AI Assistance Documentation
# Tool: OpenAI ChatGPT (GPT-6)
# Date: November 9, 2026
#
# ChatGPT assisted with writing the SLURM batch script,
# including resource requests, job output paths, and
# selecting the Python interpreter from the project environment.
#
# I submitted the job on Great Lakes, checked its completion
# status using sacct, and saved the job logs and results.


#SBATCH --job-name=mi-checkups
#SBATCH --account=compfor203f26s001_class
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:10:00
#SBATCH --output=logs/checkups-%j.out
#SBATCH --error=logs/checkups-%j.err

set -e

echo "Job ID: $SLURM_JOB_ID"
echo "Compute node: $(hostname)"

# Load Python environment tools
module load mamba/py3.12

# Run the analysis using the project environment
/home/zainahu/.conda/envs/michigan-preventive-care/bin/python src/analyze.py

echo "Analysis completed."
