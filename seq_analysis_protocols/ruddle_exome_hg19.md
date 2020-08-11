# Whole Exome Analysis with hg19

### Requirements:
- Yale Ruddle hpc
- rms path added to .bashrc

## Notes
- Common Error:  `rms /home/jk2269/pipelines/gatkExome.rms -19 /home/sp2349/scratch60/moyamoya_texas_scratch/rms_dir/* ERROR - FASTQ file name not in a parsable format: GVD_44_37789_R1.fastq.gz`
- Cannot have name with multiple periods(.)
- Name of samples cannot have periods to separate
## Protocol

1. Create Structure data structure required for rms GATKExome.rms


- Open interactive session on the cluster
