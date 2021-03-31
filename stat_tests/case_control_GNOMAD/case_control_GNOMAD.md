
# HET, LoF Case Control Analysis with GNOMAD

## GOAL
To determine if LoF mutations occur in gene or genes of interest in sample vs controls. Non-topmed samples in GNOMAD are used as the controls.


## Protocol
### Pre-process GNOMAD VCFS (if not already done)
1. Convert vcfs to hail matrix tables. The matrix tables should be located here: `/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted`. If not you will need to convert them with the program [weilai_vcf_to_tables.py](./preprocess_GNOMAD/weilai_vcf_to_tables.py)
