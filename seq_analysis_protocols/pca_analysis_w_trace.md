# PCA Analysis Using TRACE
8-10-20

This protocol uses the LASER web utility produced at the University of Michigan. 

TRACE is a sub-utility that uses genotype data instead of sequencing data to trace genetic ancestry.

[LASER Server](https://laser.sph.umich.edu/index.html#!run/trace%401.03)

[Laser Info](http://csg.sph.umich.edu/chaolong/LASER/)

## Requirements
- VCF with genotype calls
  - Jinlab whole exome sequencing pipeline produces this after joint-calling
  - **NOTE: VCF must have coordinates aligned to b37. b37 is broad insitutes version of GRCh37. hg19 contigs are not compatible.**
- TRACE
  - You will need to create an account in order to run pca analysis on your target vcf
  - After you login, go to the TRACE webpage to upload and run data. https://laser.sph.umich.edu/index.html#!run/trace%401.03
  
