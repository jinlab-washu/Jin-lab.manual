#!/bin/bash
#SBATCH --job-name=combine_gnomad_tables
#SBATCH --out="combine_gnomad_tables_slurm-%j.out"
#SBATCH --time=72:00:00
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=1
#SBATCH --mem-per-cpu=16G
#SBATCH --mail-type=ALL

module load miniconda
conda activate hail2

python /gpfs/ycga/project/kahle/sp2349/weilai_gnomad/code/combine_weilai_gnomad_tables.py 
