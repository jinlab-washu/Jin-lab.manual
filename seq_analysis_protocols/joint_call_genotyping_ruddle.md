# Joint-Call Genotyping on Ruddle
As of 8-17-2020
## Notes
* Must have .g.vcf produced by haplotype caller for each sample
* Must correct data structure format for rms
  * $sample_dir/$sample.g.vcf,$sample.g.vcf.tbi
* Script locations 
  * GATK4: /home/jk2269/pipelines/gatkExomeCall4.rms
  * GATK3: /home/bioinfo/software/knightlab/bin_Apr2019/gatkExomeCall.rms
## Protocol

*If you have fastq files or unaligned bams, you will need to run the pre-processing steps necessary to produce the aligned, base recalibrated `bam` and the haplotypecalled `.g.vcf` file.
See protocol [here](./ruddle_exome.md)

*If you have aligned and base recalibrated (BQSR) bam files, you can go directly to joint-calling without having to run a separate pre-processing step. 


1. Check data structure is correct.

   Check that each of your samples has a directory that contains the gvcf(`.g.vcf.gz`), its index (`.g.vcf.gz.tbi`), the final bam (`.bam`), and its index (`.bai`).
   
2. Change your directory to the directory containing your data. 

    ``cd path_to_data``
    
3. Run the rms script.

 
    ```rms /home/bioinfo/software/knightlab/bin_Apr2019/gatkExomeCall.rms ./*```
    
    *This command will output the RMS logs in the current working directory.*
