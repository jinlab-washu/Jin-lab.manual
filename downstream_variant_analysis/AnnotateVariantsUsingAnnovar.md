# Annotate Variants using Annovar

[Annovar Documentation - official website](https://annovar.openbioinformatics.org/en/latest/user-guide/download/)

If you want to download Annovar yourself, please see the link above! For more detail, please visit Annovar official website.

### Requirement:

1. Variant call file (vcf): ie, `exome_calls.vcf.gz`
2. RMS and RMS file:
    **For hg19:**
    
    [`/gpfs/ycga/home/pf374/programsDir/scripts/Preprocessing_hg19.rms`](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/downstream_variant_analysis/Preprocessing_hg19.rms)
    
    **For hg38:**
    
    [`/gpfs/ycga/home/pf374/programsDir/scripts/Preprocessing_hg38.rms`](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/downstream_variant_analysis/Preprocessing_hg38.rms)

    The `Preprocessing_hg*.rms` files were modified from the example below:

    ```
    # Preprocess raw vcf file (see "/ycga-gpfs/project/kahle/Kahle-Projects/Arachnoid_Cyst/Jointcalling_04262020/Preprocessing.rms")
    rms Preprocessing.rms exome_calls.vcf.gz
    ```

### How to run it?

Usage: `rms Preprocessing_hg[19|38].rms <VCF file>`

An example of running `Preprocessing_hg19.rms`:

```
$ rms Preprocessing_hg19.rms exome_calls.vcf.gz
Input:  1 row, 1 column
Commands:  1 command to be executed.
[Wed Mar 31, 3:17pm]:Pipeline execution starting.
[Wed Mar 31, 3:17pm, 1 worker]:     ProcessVCF[1]: 0q,1r,0f,0c 
...


```

### Steps of processing:

1. Start a new interactive session on Ruddle `[netid@ruddle1 ~]$ srun --pty -p interactive --mem=8g bash`
2. Create a new folder annotation
3. `ln -s` the VCF file into the new folder: 

    ie, `exome_calls.vcf.gz`
    
4. Using RMS script `Preprocessing_hg[19|38].rms` to process VCF file: 

    ie, `rms Preprocessing_hg19.rms exome_calls.vcf.gz`

### Output files:

```
exome_calls_pass_step2_normalized_anno.avinput
exome_calls_pass_step2_normalized_anno.hg19_multianno.txt
exome_calls_pass_step2_normalized_anno.hg19_multianno.vcf

```

------------

### Annovar - Quick start:

[Official tutorial](https://annovar.openbioinformatics.org/en/latest/user-guide/startup/)

If you don't want to download Annovar, here is the ready-to-use program on Ruddle: `/gpfs/ycga/project/kahle/pf374/annovar_20191024/`

**Usage: `perl /gpfs/ycga/project/kahle/pf374/annovar_20191024/table_annovar.pl --help`**

> humandb path: `/gpfs/ycga/project/kahle/pf374/annovar_20191024/humandb/`

1. An example of using hg19 database to annotate:

```

$ perl /gpfs/ycga/project/kahle/pf374/annovar_20191024/table_annovar.pl --vcfinput exome_calls_pass_step2_normalized.vcf /gpfs/ycga/project/kahle/pf374/annovar_20191024/humandb/ -buildver hg19 -out exome_calls_pass_step2_normalized_anno -remove -protocol refGene,genomicSuperDups,snp138,1000g2015aug_all,avsnp150,exac03,exac03nontcga,gnomad_exome,gnomad_genome,gnomad211_exome,gnomad211_genome,dbnsfp41a,dbscsnv11,clinvar_20210123,bravo,mcap,revel -operation g,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f -nastring .

```

2. An example of hg38 database to annotate:

```

$ perl /gpfs/ycga/project/kahle/pf374/annovar_20191024/table_annovar.pl --vcfinput exome_calls_pass_step2_normalized.vcf /gpfs/ycga/project/kahle/pf374/annovar_20191024/humandb/ -buildver hg38 -out exome_calls_pass_step2_normalized_anno -remove -protocol refGene,genomicSuperDups,snp138,1000g2015aug_all,avsnp150,exac03,exac03nontcga,gnomad_exome,gnomad_genome,gnomad211_exome,gnomad211_genome,dbnsfp41a,dbscsnv11,clinvar_20210123,bravo,mcap,revel -operation g,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f -nastring .

```

### How to download annotate database?

**Usage: `perl /gpfs/ycga/project/kahle/pf374/annovar_20191024/annotate_variation.pl --help`**

> humandb path: `/gpfs/ycga/project/kahle/pf374/annovar_20191024/humandb/`
> 

An example of downloading 1000g2015aug for hg19:

```
(base) [pf374@c18n07 humandb]$ perl /gpfs/ycga/project/kahle/pf374/annovar_20191024/annotate_variation.pl --downdb 1000g2015aug -buildver hg19 /gpfs/ycga/project/kahle/pf374/annovar_20191024/humandb/ -webfrom annovar
NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
----------------------------UPDATE AVAILABLE------------------------------
--------------------------------------------------------------------------
WARNING: A new version of ANNOVAR (dated 2020-06-07) is available!
         Download from http://www.openbioinformatics.org/annovar/
Changes made in the 2020-06-07 version:
         * increase compatibility to run table_annovar.pl in Windows Powershell
--------------------------------------------------------------------------
--------------------------------------------------------------------------
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_1000g2015aug.zip ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the '/gpfs/ycga/project/kahle/pf374/annovar_20191024/humandb' directory

```

