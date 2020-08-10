# PCA Analysis Using TRACE
8-10-20

This protocol uses the LASER web utility produced at the University of Michigan. 

TRACE is a sub-utility that uses genotype data instead of sequencing data to trace genetic ancestry.

[LASER Server](https://laser.sph.umich.edu/index.html#!run/trace%401.03) - Utility to run pca analysis

[Laser Documentation](http://csg.sph.umich.edu/chaolong/LASER/) - Information Regarding TRACE and LASER pca analysis

## Requirements
- VCF with genotype calls
  - Jinlab whole exome sequencing pipeline produces this after joint-calling
  - **NOTE: VCF must have coordinates aligned to b37. b37 is broad insitutes version of GRCh37. hg19 contigs are not compatible.**
- TRACE
  - You will need to create an account in order to run pca analysis on your target vcf
  - After you login, select the TRACE button under dropdown menu labeled "RUN" at the top of the screen.
  
  
## Protocol

If you have a file produced by GRCh38
