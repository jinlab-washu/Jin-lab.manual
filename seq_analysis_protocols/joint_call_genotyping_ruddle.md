# Joint-Call Genotyping on Ruddle
As of 8-17-2020
## Notes
* Must have .g.vcf produced by haplotype caller for each sample
* Must correct data structure format for rms
  * $sample_dir/$sample.g.vcf,$sample.g.vcf.tbi
* Script location: /home/bioinfo/software/knightlab/bin_Apr2019/gatkExomeCall.rms
  * Most up to date version as of date listed above
## Protocol

If you have fastq files, you will need to run the pre-processing steps necessary to produce the aligned, base recalibrated bam and the haplotypecalled .g.vcf file.
See here(./

If you have aligned and base recalibrated (BQSR) bam files, you can go directly to joint-calling without having to run a separate pre-processing step. 
