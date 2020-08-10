# PCA Analysis Using TRACE
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
  
## Notes

Your VCF must have coordinates aligned to b37. b37 is broad insitutes version of GRCh37. hg19 contigs are not compatible.

**If you have a vcf that was aligned to a reference other than b37 (broad institute version of GRCh37), you will have to convert the coordinates to b37. If you used hg19, you will first have to convert to hg38 before b37.**

Conversion of hg38 to b37 [Convert hg38 to b37](./liftover_hg38_to_b37.md).

Differences between GRCh37 builds: [GRCh37 Builds and their Naming Conventions](https://gatk.broadinstitute.org/hc/en-us/articles/360035890711-GRCh37-hg19-b37-humanG1Kv37-Human-Reference-Discrepancies) *The naming convention of hg19 and hg38 differs from b37.

*There doesn't seem to be a chain file that converts hg19 to b37 coordinates. If your vcf was produced with alignment to hg19, you will have to do two liftOvers.*
  - Liftover hg19 to hg38
  - Liftover hg38 to b37-[Convert hg38 to b37](./liftover_hg38_to_b37.md)


## Protocol
