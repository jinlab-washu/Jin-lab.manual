#!/bin/bash
#SBATCH --job-name=gnomad_case_control
#SBATCH --out="slurm-%j.out"
#SBATCH --time=4:00:00
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=1
#SBATCH --mem-per-cpu=8G
#SBATCH --mail-type=ALL

module load miniconda
conda activate hail2

python /gpfs/ycga/project/kahle/sp2349/weilai_gnomad/code/gnomad_combined_case_control.py 
