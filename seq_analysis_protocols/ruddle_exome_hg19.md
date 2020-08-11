# Whole Exome Analysis with hg19

### Requirements:
- Yale Ruddle hpc
- rms path added to .bashrc

## Notes
- Common Error:  `rms /home/jk2269/pipelines/gatkExome.rms -19 /home/sp2349/scratch60/moyamoya_texas_scratch/rms_dir/* ERROR - FASTQ file name not in a parsable format: GVD_44_37789_R1.fastq.gz`
- Cannot have name with multiple periods(.)
- Name of samples cannot have periods to separate
## Protocol

1. Create data structure required for rms GATKExome.rms


- Open interactive session on the cluster
`srun --pty -t 2:00:00 --mem=8G -p interactive bash`

- Open a new tmux seesion
`tmux new -s $myproject` where `$myproject` is the name you give it
