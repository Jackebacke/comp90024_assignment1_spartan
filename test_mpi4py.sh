#!/bin/sh
#SBATCH --job-name=test_mpi4py
#SBATCH --time=00:10:00     #(hrs:min:sec)
#SBATCH --nodes=1           #(run on a single server)
#SBATCH --ntasks=4          #(run 4 tasks)
#SBATCH --cpus-per-task=4   #(CPU cores per task)
#Load required modules
module purge
module load GCC/11.3.0
module load OpenMPI/4.1.4
module load mpi4py/3.1.4
mpirun python src/test_mpi4py.py
