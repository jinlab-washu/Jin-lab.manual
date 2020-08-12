# Whole Exome Sequencing Processing on Ruddle
>WORK IN PROGRESS

> Purpose: To produce a multi-sample vcf ready for downstream variant analysis<br>

> Workflow:
>> Pre-processing: FASTQ preprocessing
>> Alignment: bwa-mem to hg19 reference<br>
>> Variant Processing: Base Recalibration-BQSR, HaplotypeCaller, Cohort Joint-Call Genotyping-GenotypeGVCFs, Variant Filtering-VQSR<br>

### Workflow Versions as of 7-12-20
- GATK3 Newest: /home/bioinfo/software/knightlab/bin_Apr2019/gatkExome.rms
  - Should work with fastq and bam files
- GATK4 Newest: /home/jk2269/pipelines/gatkExome4.rms

## Notes
- Fastq files have to follow a naming convention.
  - Such as `mDZ038_74777_R1_001.fastq.gz` or `KMM_5-2_AHW3JKDSXX_L001_R1_001`
  - Common Error:  `rms /home/jk2269/pipelines/gatkExome.rms -19 /home/sp2349/scratch60/moyamoya_texas_scratch/rms_dir/* ERROR - FASTQ file name not in a parsable format: GVD_44_37789_R1.fastq.gz`
- Data must have a particular structure
  - $sample/ $sample.bam $sample.bai Unaligned/ $sample.fastq.gz
    - Where sample is a directory possibly containing bam files and/or an Unaligned folder containing fastq.gz or fastq.qp files.
  - Either move data to fit correct structure or link files from a different location
  
## Protocol

1. Create data structure required for rms GATKExome.rms

    - can use ycga Fastq and provide a text sample. 

2. Run rms script in data directory

    2a. Open a new tmux session `tmux new -s $myproject` where `$myproject` is the name you give it<br>
    2b. Move to the directory containing your data `cd /path_to_data`<br>
    2c. Run `rms /home/bioinfo/software/knightlab/bin_Apr2019/gatkExome.rms $-19 $sample_dir` where `$-19` specifies the reference and `$sample_dir` tells the script where to look for the data. If you are in the directory containing your data (followed step 2b), you should use a `*` here to tell the script to look at everything in the current directory.<br>
    
      - For example, `rms /home/bioinfo/software/knightlab/bin_Apr2019/gatkExome.rms -19 *` will run the script on every sample in your current directory<br>
      - Use `-38` for hg38 reference instead of hg19
