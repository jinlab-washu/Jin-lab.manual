# Whole Exome Sequencing Processing on Ruddle
>WORK IN PROGRESS

> Purpose: To produce a multi-sample vcf ready for downstream variant analysis<br>

> Workflow:
>> Pre-processing: FASTQ/bam preprocessing<br>
>> Alignment: bwa-mem<br>
>> Variant Processing: Base Recalibration-BQSR, HaplotypeCaller, Cohort Joint-Call Genotyping-GenotypeGVCFs, Variant Filtering-VQSR<br>

### Workflow Versions as of 7-12-20
- GATK3 Newest: /home/bioinfo/software/knightlab/bin_Apr2019/gatkExome.rms
  - Should work with fastq and bam files
- GATK4 Newest: /home/jk2269/pipelines/gatkExome4.rms

## Notes
- Fastq files have to follow a naming convention.
  - Such as `mDZ038_74777_R1_001.fastq.gz` or `KMM_5-2_AHW3JKDSXX_L001_R1_001`
  - Common Error:  `rms /home/jk2269/pipelines/gatkExome.rms -19 /home/sp2349/scratch60/moyamoya_texas_scratch/rms_dir/* ERROR - FASTQ file name not in a parsable format: GVD_44_37789_R1.fastq.gz`
- Data must have a particular structure. Bam and fastq files have unique data structures, that must not be mixed.
  - FASTQ: $sample/Unaligned/$sample.fastq.gz or $sample.fastq.qp
  - BAM: $sample/$sample.bam,$sample.bai
  - Either move data to fit correct structure or link files from a different location
  
## Protocol

1. Create the data structure required for rms GATKExome.rms

    Bams and Fastq file inputs have different data structures that are required for input into Exome rms scripts. *Bam and fastq files should have separate data structures. DO NOT MIX*
    
    **FASTQ FILE INPUT**<br>
    If you are using Fastq files, the data structure format is `$sample/Unaligned/$sample.fastq.gz or $sample.fastq.qp` where each sample has its own directory. Each sample directory should have an `unaligned` folder that contains the fastq.gz or fastq.qp reads. Fastq names must have a specific format. 
    
    - If you need to convert bam's to fastq, use /home/jk2269/pipelines/bam2splitfastq.rms . 
      - bam2splitfastq.rms creates the data structure for you in your current working directory
    - If you have fastq files, the data structure can be created with /home/jk2269/binpy/ycgaFastq
    
    **BAM FILE INPUT**<br>
    If you are using Bam Files, data structure format is `$sample/$sample.bam,$sample.bai` where each sample has its own directory, `$sample`, containing a bam file and its index.
    

2. Run the rms script in your directory containing the data structure

    2a. Open a new tmux session `tmux new -s $myproject` where `$myproject` is the name you give it<br>
    2b. Move to the directory containing your data `cd /path_to_data`<br>
    2c. Run `rms /home/bioinfo/software/knightlab/bin_Apr2019/gatkExome.rms $-19 $sample_dir` where `$-19` specifies the reference and `$sample_dir` tells the script where to look for the data. If you are in the directory containing your data (followed step 2b), you should use a `*` here to tell the script to look at everything in the current directory.<br>
    
      - For example, `rms /home/bioinfo/software/knightlab/bin_Apr2019/gatkExome.rms -19 ./*` will run the script on every sample in your current directory<br>
      - Use `-38` for hg38 reference instead of hg19
      
3. Check for exome_calls.vcf.gz and exome_calls.vcf.gz.tbi output

    If the pipeline ran successfully, you should have the files, exome_calls.vcf.gz and exome_calls.vcf.gz.tbi, in the directory which you ran the command in step 2. 
    
    Additionally, each sample directory should have the following files: .g.vcf.gz, .bam, .bai, exomMetrics.txt
