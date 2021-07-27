07-27-2021
# Run Kinship Analysis on Whole Exome Sequencing Data
- Methods adopted from Xue Zeng scripts in Kahle lab at Yale University

## Plink Identity by Descent

### 1. Load PLINK  
    
#### WashU Cluster: 

Use Docker image: `sam16711/plink:latest`

``` bsub -Is -q general-interactive -a 'docker(sam16711/plink:latest)' -R "select[mem>15000] rusage[mem=15000]" /bin/bash ```
``` /bin/plink --help ```

#### Yale Ruddle:
   
Start new tmux window with: `tmux new -s PLINK`

Run interactive node in new window with: `srun --pty -t 4:00:00 --mem=8G -p interactive bash`

*NOTE Time and memory limits may have to be modified based on input data size

Load Plink: `module load PLINK`

### 2. Run plink command for *kinship*

Move to a location where you want to store the plink kinship: `cd $your_path_here`

```
plink --geno 0.01 --hwe 0.001 --maf 0.05 --genome --snps-only --allow-extra-chr \
--vcf *_vqsr.vcf
--out {file_name} #----no need to indicate file type, but may use .txt or .tsv
```

![plink_running](https://github.com/jinlab-washu/Plink/blob/master/plink_kinship.png)
    
## VCFtools Relatedness

### 1. Load VCFTools

#### WashU Cluster:

Load Docker Image biocontainers/vcftools:v0.1.16-1-deb_cv1

```bsub -Is -q research-hpc -R "select[mem>15000] rusage[mem=15000]" -a 'docker(biocontainers/vcftools:v0.1.16-1-deb_cv1@sha256:caa02f1a00f18e1509ff3097cabaebb37b3ab884082ca983b3d7b7b7d13c6744)' /bin/bash```

#### Yale Ruddle:

Load VCFtools with module: `module load VCFTools`

### 2. Run relatedness2

Move to a location where you want to store the plink relatedness results: `cd $your_path_here`

```vcftools --gzvcf $vcf.gz --relatedness2```
    
### Output:

- out.relatedness2
- out.log

## Running Plink for *gender check*

### 1. Load PLINK  

#### WashU Cluster: 

Use Docker image: `sam16711/plink:latest`

```bsub -Is -q general-interactive -a 'docker(sam16711/plink:latest)' -R "select[mem>15000] rusage[mem=15000]" /bin/bash```

#### Yale Ruddle 

Start new tmux window with: `tmux new -s gender_check`

Run interactive node in new window with: `srun --pty -t 4:00:00 --mem=8G -p interactive bash`

*NOTE Time and memory limits may have to be modified based on input data size

Load Plink: `module load PLINK`

### 2. Run the following commands:

Move to a location where you want to store the plink gender results: `cd $your_path_here`

```
plink --double-id --allow-extra-chr --vcf-half-call m \
--vcf your_path/exome_calls.vcf \
--out exome_calls_data
```
Next command is build specific
    
  -For GRCH37:
    ```
    plink --split-x hg19 --make-bed --allow-extra-chr \ 
    --bfile exome_calls_data \
    --out exome_calls_data_split
    ```
  -For GRCh38: 
    ```
    plink --split-x hg38 --make-bed --allow-extra-chr \ 
    --bfile exome_calls_data \
    --out exome_calls_data_split
    ```
Finally, run: 

```
plink --impute-sex ycount --make-bed --allow-extra-chr \
--bfile exome_calls_data_split \
--out exome_calls_out
```

You should have an output file called `exome_calls_out.sexcheck` in your current directory that contains the gender calls.+
*SNPSEX	Imputed sex code (1 = male, 2 = female, 0 = unknown)*
***You may delete any other intermidiate file***
