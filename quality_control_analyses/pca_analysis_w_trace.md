# PCA Analysis Using TRACE (Laser Web Tool)
8-10-20

This protocol uses the LASER web utility produced at the University of Michigan. 

TRACE is a sub-utility that uses genotype data instead of sequencing data to trace genetic ancestry.

[LASER Server](https://laser.sph.umich.edu/index.html#!run/trace%401.03) - Utility to run pca analysis

[Laser Documentation](http://csg.sph.umich.edu/chaolong/LASER/) - Information Regarding TRACE and LASER pca analysis

## Requirements
- *VCF with genotype calls
  - Jinlab whole exome sequencing pipeline produces this after joint-calling
  - **SEE NOTES**
- TRACE
  - You will need to create an account in order to run pca analysis on your target vcf
  - After you login, select the TRACE button under dropdown menu labeled "RUN" at the top of the screen.
- USCS Chain file, reference `.fasta`, and reference `.dict` 
  - We have the necessary files for conversion of hg38 to b37 and hg19 to hg38 on compute0
  - See here for downloading chain files: [Download Chain Files and References](./download_chain_files_and_refs.md)
  
## Notes

Your VCF must have coordinates aligned to b37. b37 is broad insitutes version of GRCh37. hg19 contigs are not compatible.

**If you have a vcf that was aligned to a reference other than b37 (broad institute version of GRCh37), you will have to convert the coordinates to b37. If you used hg19, you will first have to convert to hg38 before b37.**

Conversion of hg38/h19 to b37 [Convert hg38/hg19 to b37](./liftover_hg38_to_b37.md).

Differences between GRCh37 builds: [GRCh37 Builds and their Naming Conventions](https://gatk.broadinstitute.org/hc/en-us/articles/360035890711-GRCh37-hg19-b37-humanG1Kv37-Human-Reference-Discrepancies) *The naming convention of hg19 and hg38 differs from b37.

*There doesn't seem to be a chain file that converts hg19 to b37 coordinates. If your vcf was produced with alignment to hg19, you will have to do two liftOvers.*
  - Liftover hg19 to hg38
  - Liftover hg38 to b37

## Protocol

1. Create an account (if you have not already done so)

2. Click the run tab at the top of the screen and select TRACE from the dropdown menu
![Trace Dropdown](./trace_dropdwn.png)
3. Give your job a name and upload the vcf. 
  - If you would like to visualize groups of variants, you can create a "study groups" file and upload it. If you do this, **EVERY** individual in the study must have a group. See the website instructions for more information on the format.
4. Change the number of principal components from 3 to 10. 
  - This increases the number of ways the data can be visualized. Sometimes ethnicities overlap and it is hard to determine which background a sample belongs too. By increasing the number of principal components, you can separate closely populated ethnicities by displaying different variations of the principal components (e.g. PC1 vs PC7 instead of PC1 vs PC2)
5. Submit the job by clicking the button at the bottom of the screen. This can take up to several hours to run, depending upon the size of your vcf and number of individuals in the study.
6. You can view the results of your study by selecting the "Jobs" tab at the top of the screen. Then select your job of interest.
