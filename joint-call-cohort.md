# Joint-Calling

***WORK IN PROGRESS***

Purpose: To Produce a mutlisample vcf for downstream analysis. Currently, there is no GMS pipeline for joint-calling a cohort.

Input: .g.vcfs for each chromosome produced by GATK HaploTypeCaller in BP_RESOLUTION mode.

Goals: Produce an alternative pipeline for joint-calling analysis in cwl. 


## Bash Script Alternative Protocol
### Merge gvcfs with Picard MergeVcfs
1. Enter the gms environment by typing in ```gsub```
2. Run the get_chrom_gvcfs.sh script in the under the bash_scripts folder with two inputs: $ANALYSIS_ID $OUTPUTDIR. ```/gscmnt/gc2698/jin810/bash_scripts/get_chrom_gvcf.sh $ANALYSIS_ID $OUTPUTDIR```

*The program creates directories for each sample in the format: OUTPUTDIR/ANALYSIS_ID/MODEL_ID/BUILD_ID/SAMPLE/outputfiles*
