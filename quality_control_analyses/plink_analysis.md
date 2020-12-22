# Run Kinship Analysis on Whole Exome Sequencing Data
- Methods adopted from Xue Zeng scripts in Kahle lab at Yale University

*WORK_IN_PROGRESS*

Software Requirements:
- Docker

## Method 1-Plink
Use Docker image: ```sam16711/plink:latest```

Interactive:

1. Load Docker Image

    ```bsub -Is -q research-hpc -a 'docker(sam16711/plink:latest)' -R "select[mem>15000] rusage[mem=15000]" /bin/bash```

1. Run plink command for kinship

    ```plink --vcf ./IDT_WES_hg38.vcf.gz --geno 0.01 --hwe 0.001 --maf 0.05 --genome --snps-only```

    ![plink_running](https://github.com/jinlab-washu/Plink/blob/master/plink_kinship.png)
    
## Method2-VCFtools

Interactive:

1. Load Docker Image biocontainers/vcftools:v0.1.16-1-deb_cv1

    ```bsub -Is -q research-hpc -R "select[mem>15000] rusage[mem=15000]" -a 'docker(biocontainers/vcftools:v0.1.16-1-deb_cv1@sha256:caa02f1a00f18e1509ff3097cabaebb37b3ab884082ca983b3d7b7b7d13c6744)' /bin/bash```

2. Run relatedness2

    ```vcftools --gzvcf $vcf.gz --relatedness2```
    
Output:

- out.relatedness2
- out.log
