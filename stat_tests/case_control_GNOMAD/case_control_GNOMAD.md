
# HET, LoF Case Control Analysis with GNOMAD v2.1.1
> Notes: Missing chromosome 18 for GNOMAD genomes!!! Only have the exomes file.
## GOAL
To determine if LoF mutations occur in gene or genes of interest in sample vs controls. Non-topmed samples in GNOMAD are used as the controls.

## File locations
vcfs: 
vcfs converted to matrix tables: `/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted`

## Protocol
### Pre-process GNOMAD VCFS (if not already done)
**Currently (03/30/21), only two final_filtered hail tables exist for the GNOMAD case control test. chr5 and chr10. If you need a different chromosome, you MUST  follow the preprocess steps below to create a combined genome/exome hail table in the correct format!!!**
1. Convert vcfs to hail matrix tables. The matrix tables should be located here: `/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted`. If not you will need to convert them with the program [weilai_vcf_to_tables.py](./preprocess_GNOMAD/weilai_vcf_to_tables.py)
2. Combine exome and genome matrix tables. 
** For a single chromosome, use [combine_weilai_table_single.py](./preprocess_GNOMAD/combine_weilai_table_single.py)
** For multiple chromosomes, use [combine_weilai_gnomad_tables.py](./preprocess_GNOMAD/combine_weilai_gnomad_tables.py)
3. Format combined exome and genome hail table created from step 2 using [format_weilai_combined_mt.py](/preprocess_GNOMAD/format_weilai_combined_mt.py)
4. 
