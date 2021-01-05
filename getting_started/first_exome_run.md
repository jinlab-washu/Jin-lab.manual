# Guide for Starting your First Whole Exome Sequence Analysis

Tasks
- [ ] Determine where you samples are located. WashU or Ruddle cluster. This will determine which pipeline you will be using.
- [ ] Gather fastq and/or bam files
- [ ] Transfer data (if necessary)
- [ ] Create Pedigree File (if necessary)
- [ ] Create folder structure (Either import into GMS or create structure according to compute cluster and pipeline)
  - Typically this will be `$sample/$fastq_files`
  
  
Outline
1. Organize samples and create Pedigree File using Excel 
Preprocess samples: Align and generate gvcfs per sample
2. Joint-call genotype: Genotype all gvcfs and produce a single multi-sample vcf
3. Check 8X Coverage with ExomeMetrics output 
4. Annotate multisample vcf
5. Run downstream analyses: Call De-novo Mutations, Filter for Rare Transmitted Variants..etc.


## Start
For your first analysis, you will need to determine where your samples are located. The Yale Ruddle compute cluster or WashU compute1. 

