# Run Kinship Analysis on Whole Exome Sequencing Data
- Methods adopted from Xue Zeng scripts in Kahle lab at Yale University


Software Requirements:
- Docker

## Plink Identity by Descent

Interactive:

1. Load PLINK

  WashU Cluster: 
    
    Use Docker image: `sam16711/plink:latest`

    ```bsub -Is -q research-hpc -a 'docker(sam16711/plink:latest)' -R "select[mem>15000] rusage[mem=15000]" /bin/bash```
  
  Yale Ruddle:
   
    Start new tmux window with: `tmux attach -s new PLINK`
    
    Run interactive node in new window with: `srun srun --pty -t 4:00:00 --mem=8G -p interactive bash`

    *NOTE Time and memory limits may have to be modified based on input data size

    Load Plink: `module load PLINK`

2. Run plink command for kinship

    ```plink --vcf ./IDT_WES_hg38.vcf.gz --geno 0.01 --hwe 0.001 --maf 0.05 --genome --snps-only```

    ![plink_running](https://github.com/jinlab-washu/Plink/blob/master/plink_kinship.png)
    
## VCFtools Relatedness

Interactive:

1. Load VCFTools

  WashU Cluster:

    Load Docker Image biocontainers/vcftools:v0.1.16-1-deb_cv1

    ```bsub -Is -q research-hpc -R "select[mem>15000] rusage[mem=15000]" -a 'docker(biocontainers/vcftools:v0.1.16-1-deb_cv1@sha256:caa02f1a00f18e1509ff3097cabaebb37b3ab884082ca983b3d7b7b7d13c6744)' /bin/bash```
  
  Yale Ruddle:
    
    Load VCFtools with module: `moduel load VCFTools`

2. Run relatedness2

    ```vcftools --gzvcf $vcf.gz --relatedness2```
    
Output:

- out.relatedness2
- out.log
