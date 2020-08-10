You can find the chain files here: [USCS hg19 Chain Files](http://hgdownload.soe.ucsc.edu/goldenPath/hg19/liftOver/)

The type of conversion you are doing will determine what chain file you need.

If you are starting from scratch (no chain files or references files downloaded), you will need the following:
- Chain file specific to the conversion you are doing
- Reference `.fasta` and accompanying `.dict` in the same directory

For example:
>**If you have a vcf with alignment to the hg19 reference, you will need the following:**
> - hg19ToHg38.over.chain.gz chain file
> - The hg19 reference fasta with an accompanying `.dict` file
  > - If you can only find the fasta online, you can create a sequnce dict with GATK's CreateSequenceDictionary tool. See here [GATK4 CreateSequence Dictionary](https://gatk.broadinstitute.org/hc/en-us/articles/360047217371-CreateSequenceDictionary-Picard-)
  
