# Run Kinship Analysis on Whole Exome Sequencing Data
- Methods adopted from Xue Zeng scripts in Kahle lab at Yale University

## Plink Identity by Descent

### 1. Load PLINK  
    
#### WashU Cluster: 

Use Docker image: `sam16711/plink:latest`

```bsub -Is -q research-hpc -a 'docker(sam16711/plink:latest)' -R "select[mem>15000] rusage[mem=15000]" /bin/bash```
  
#### Yale Ruddle:
   
Start new tmux window with: `tmux new -s PLINK`

Run interactive node in new window with: `srun --pty -t 4:00:00 --mem=8G -p interactive bash`

*NOTE Time and memory limits may have to be modified based on input data size

Load Plink: `module load PLINK`

### 2. Run plink command for kinship

```plink --vcf ./IDT_WES_hg38.vcf.gz --geno 0.01 --hwe 0.001 --maf 0.05 --genome --snps-only```

![plink_running](https://github.com/jinlab-washu/Plink/blob/master/plink_kinship.png)
    
## VCFtools Relatedness

### 1. Load VCFTools

#### WashU Cluster:

Load Docker Image biocontainers/vcftools:v0.1.16-1-deb_cv1

```bsub -Is -q research-hpc -R "select[mem>15000] rusage[mem=15000]" -a 'docker(biocontainers/vcftools:v0.1.16-1-deb_cv1@sha256:caa02f1a00f18e1509ff3097cabaebb37b3ab884082ca983b3d7b7b7d13c6744)' /bin/bash```

#### Yale Ruddle:

Load VCFtools with module: `module load VCFTools`

### 2. Run relatedness2

```vcftools --gzvcf $vcf.gz --relatedness2```
    
### Output:

- out.relatedness2
- out.log

## Running Plink for gender check

### 1. Load PLINK  

#### WashU Cluster: 

Use Docker image: `sam16711/plink:latest`

```bsub -Is -q research-hpc -a 'docker(sam16711/plink:latest)' -R "select[mem>15000] rusage[mem=15000]" /bin/bash```

#### Yale Ruddle 

Start new tmux window with: `tmux new -s gender_check`

Run interactive node in new window with: `srun --pty -t 4:00:00 --mem=8G -p interactive bash`

*NOTE Time and memory limits may have to be modified based on input data size

Load Plink: `module load PLINK`


### 2. Run the following commands:

```plink --vcf ../exome_calls.vcf.gz --out exome_calls_data```

```plink --bfile exome_calls_data --split-x b37 --make-bed --out exome_calls_data_split```

```plink --bfile exome_calls_data_split --impute-sex ycount --make-bed --out exome_calls_out```
