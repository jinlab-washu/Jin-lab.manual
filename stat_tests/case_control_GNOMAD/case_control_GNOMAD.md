
# HET, Damaging Case Control Analysis with GNOMAD v2.1.1
> Notes: Missing chromosome 18 for GNOMAD genomes!!! Only have the exomes file.
> Damaging = LoF or CADD > 20 or MetaSVM Damaging ("D")
## GOAL
To determine if LoF mutations occur in gene or genes of interest in sample vs controls. Non-topmed samples in GNOMAD are used as the controls.

## File locations
* vcfs: '/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/vcfs/weilai_vcfs' - Original vcfs before conversion  
* vcfs converted to matrix tables: `/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted`  
* combined_filtered hail tables: `/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/combined_filtered`  
* formatted_final hail tables: `/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/formatted_final` - These are the tables used for the case control  

## Protocol
### Pre-process GNOMAD VCFS (if not already done)
**Currently (03/30/21), only two final_filtered hail tables exist for the GNOMAD case control test. chr5 and chr10. If you need a different chromosome, you MUST  follow the preprocess steps below to create a combined genome/exome hail table in the correct format!!!**
1. Convert vcfs to hail matrix tables. The matrix tables should be located here: `/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted`. If not you will need to convert them with the program [weilai_vcf_to_tables.py](./preprocess_GNOMAD/weilai_vcf_to_tables.py)
2. Combine exome and genome matrix tables. 
** For a single chromosome, use [combine_weilai_table_single.py](./preprocess_GNOMAD/combine_weilai_table_single.py)
** For multiple chromosomes, use [combine_weilai_gnomad_tables.py](./preprocess_GNOMAD/combine_weilai_gnomad_tables.py)
3. Format combined exome and genome hail table created from step 2 using [format_weilai_combined_mt.py](./preprocess_GNOMAD/format_weilai_combined_mt.py)

## Run Gene Specific Filtering Program
**IMPORTANT** Make sure no samples are related in the case control analysis
1. Filter your cohort vcf for damaging, het variants. Use [case_control_gene_specific_filtering.py](./case_control_programs/case_control_gene_specific_filtering.py)
2. Check your output. If more than 1 damaging variant on same gene, only count as 1 allele.
3. Grab allele counts. Ex: for 24 probands = 48 alleles. If 3 het variants found for 3 samples, cases = 3. controls = 48 - 3 = 45.

## Run GNOMAD case control program
1. Use [gnomad_combined_case_control.py](./case_control_programs/gnomad_combined_case_control.py)
*YOU must enter the experimental cases and controls from the previous filtering steps and the coordinates for the specific gene you are looking at (chrm, start, end). Name is optional. If you input "name", an output folder will be created for the specific word you put here".
