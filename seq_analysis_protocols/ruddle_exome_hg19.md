# Whole Exome Sequencing Processing with Alignment to hg19
>WORK IN PROGRESS

> Purpose: To produce a multi-sample vcf ready for downstream variant analysis<br>

> Workflow:
>> Pre-processing: FASTQ preprocessing
>> Alignment: bwa-mem to hg19 reference<br>
>> Variant Processing: Base Recalibration-BQSR, HaplotypeCaller, Variant Filtering-VQSR, Cohort Joint-Call Genotyping-GenotypeGVCFs<br>
>> GATK Version: GATK3

### Requirements:
- Yale Ruddle hpc
- rms path added to .bashrc
- Compressed fastq files with bgzip (.fastq.gz) or qp (.qp)

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


- Open a new tmux seesion
`tmux new -s $myproject` where `$myproject` is the name you give it
