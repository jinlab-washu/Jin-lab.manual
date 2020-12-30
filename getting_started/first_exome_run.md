# Guide for Starting your First Whole Exome Sequence Analysis

Tasks
- [ ] Gather fastq and/or bam files
- [ ] Transfer data (if necessary)
- [ ] Create folder structure (Either import into GMS or create structure according to compute cluster and pipeline)
  - Typically this will be `$sample/$fastq_files`
  
  
Outline
1. Preprocess samples: Align and generate gvcfs per sample
2. Joint-call genotype: Genotype all gvcfs and produce a single multi-sample vcf
3. Check 8X Coverage with ExomeMetrics output 
4. Annotate multisample vcf
5. Run downstream analyses: Call De-novo Mutations, Filter for Rare Transmitted Variants..etc.

