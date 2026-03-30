#!/bin/sh
#SBATCH --job-name=assignment1-1_8
#SBATCH --output=slurm-%j-%x.out
#SBATCH --error=slurm-%j-%x.out
#SBATCH --time=01:00:00     #(hrs:min:sec until )
#SBATCH --nodes=1           #(no. of nodes to run on)
#SBATCH --ntasks=8          #(no. of tasks IN TOTAL to run)
#SBATCH --ntasks-per-node=8 #(no. of tasks per node to run)
#SBATCH --cpus-per-task=1   #(CPU cores per task)
#Load required modules
module purge
module load GCC/11.3.0
module load OpenMPI/4.1.4
module load mpi4py/3.1.4

if [ -z "$1" ]; then
    echo "Please provide the path to the NDJSON file!"
    exit 1
fi

mpirun python src/assignment1.py "$1"
