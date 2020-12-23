# Variant Visualization with Plot Reads

> Plot Reads was created in Jim Knight's lab at Yale. We have incorporated this program into a docker image to run on the WashU compute clusters.

Requirements:
* Aligned BAM/CRAM
* Chromosome and position for variant visualization

Notes:
    The plot_reads docker image comes with several bioinformatic tools from the htslib library. 
    samtools, bgzip, and tabix can be accessed from the docker image.   

## Interactive Protocol

1. Gather list of all chromosomes and positions you want to visualize. Create a text document with each position on a new line.

    Example pos.txt:  
    chr1:5000  
    chr4:80000  
    chr4:457832
    
2. Create a `samples.txt` file with each sample on a new line.
    
    Example samples.txt:  
    Sample1  
    Sample2  
    Sample3
    
3. Submit an interactive job to run the plot_reads docker image:

    Compute0:
    
    `bsub -Is -q research-hpc -R "select[mem>8000] rusage[mem=8000]" -a 'docker(sam16711/plot_reads:v1)' /bin/bash`

    Compute1:
    
    `bsub -Is -G compute-jin810 -q general-interactive -M 8GB -R "select[mem>8GB] rusage[mem=8GB]" -a 'docker(sam16711/plot_reads:v1)' /bin/bash`
    
    Ruddle:
    `tmux new -s plotReads`
    
    Once in your new window run: `srun --pty -t 4:00:00 --mem=8G -p interactive bash` (Time limits can be modified based on needs)
    Wait for the node to start. Then run the follwing line:
    
    ``cat samples.txt | while read sample; do cat pos.txt | while read chr pos; do plotReads $chr:$pos $sample;done; done`
    
4. Create image plots at every position in pos.txt for every sample in samples.txt (Good for checking false positives based on sequence context).
    
    `cat samples.txt | while read sample; do cat pos.txt | while read chr pos; do plotReads $chr:$pos $sample;done; done`
    
    This will output all image plots in the current working directory.
    
    Example image plot below:
    ![image1](./NA12878_chr13_18174454.png)
    
5. Create text plots at every position in pos.txt for every sample in samples.txt (Good for checking bad alignments).
    
    `cat samples.txt | while read sample; do cat pos.txt | while read chr pos; do plotReads -t $chr:$pos >> ./$(basename $sample)_"$chr"_"$pos".txt $sample;done; done`
    
    This will output all text plots in the current working directory
    
    Example text plot below:
    ![image2](./NA12878_chr13_18174454_partial.png)
    
6. Validate Variants by eliminating false positives  
    False positive Checks:  
       * Bad alignments: 60 is max alignment score. Many alignments of 40 or less can indicate a redundant region  (See left side of text plots)  
       * Variants in homopolymers and repeat regions. (If the variant is in this region, it is most likely a false positive).  
       * Variants only ocurring in single orientation (forward or reverse). Denoted by carrot symbols in both image and text plots. `">": forward`,  `"<" reverse`
