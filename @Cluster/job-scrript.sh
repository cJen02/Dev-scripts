#!/bin/bash
#SBATCH --job-name=test_job 	# Job name
#SBATCH --partition=sabarmati	# Run "sinfo" command to see the list of available partition
#SBATCH --nodes=1 				# Run all processes on a single node
#SBATCH --ntasks=1 				# Run a single task
#SBATCH --cpus-per-task=4 		# Number of CPU cores per task
#SBATCH --gres=gpu 				# Include gpu for the task (optional only for GPU jobs)
#SBATCH --mem=6gb 				# Total memory limit (optional)
#SBATCH --time=00:05:00 		# Time limit hrs:min:sec (optional)
#SBATCH --output=first_%j.log 	# Standard output and error log
date;hostname;pwd


module load openmpi4

<Executable PATH> INPUT OUTPUT
