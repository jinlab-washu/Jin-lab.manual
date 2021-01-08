# Variant Visualization with Plot Reads

> Plot Reads was created in Jim Knight's lab at Yale. We have incorporated this program into a docker image to run on the WashU compute clusters.

Requirements:
* Aligned BAM/CRAM
* Chromosome and position for variant visualization

Notes:
    The plot_reads docker image comes with several bioinformatic tools from the htslib library. 
    samtools, bgzip, and tabix can be accessed from the docker image.   

## Interactive Protocol

**READ: There are many ways to use this program and you might have to adjust the protocol below for your own specific needs. The protocol below is used when you have a list positions you would like to visualize for all samples.**  


1. Create necessary files that will contain positions and samples you want to visualize.

    1a. You have a list of positions you would like to visualize for several samples
    
      Create a new file called `pos.txt` with each position on a new line in the format, `chr:position`. **Do not include a header!**. See below.  
        
        GRCh38/hg38 Positions Example         GRCh37/hg19 Positions Example  
        chr1:5000                             1:5000
        chr4:80000                            4:80000
        chr4:457832                           4:457832
    
      Create a `samples.txt` file with each sample's `.bam or .cram` file on a new line. See below for example.
    
        Example samples.txt:  
        path/Sample1.cram  
        path/Sample2.cram  
        path/Sample3.cram  
    
    1b. You have a list of unique positions for each sample. 
    
      Create a new file  called `pos_visualizations.txt`. This file will have two columns separated by a tab (tab delimited). Position`<tab>`path_to_Sample_bam_or_cram. **Do not include a header!**
      
        Example GRCh38/hg38               Example GRCh37/hg19
        chr1:5000   path/Sample1.cram     1:5000    path/Sample1.cram
        chr4:80000  path/Sample2.cram     4:80000   path/Sample2.cram 
        chr4:457832 path/Sample3.cram     4:457832  path/Sample3.cram
        
    Example for finding sample paths on Ruddle:
    
    If your samples are on ruddle, they will most likely be organized with each sample having its own folder. See below:
    
            [sp2349@ruddle1 project1]$ ls -d */
            KAVM10-1/  KAVM10-2/  KAVM10-3/
            
    One way to find all of the crams is to to use the command below. This will output the paths of all the crams for a project into a file called `paths`
            
            Command: ls path_to_project_folder/*/*.cram
            
            Example: ls /gpfs/ycga/home/sp2349/project1/*/*.cram > paths
            
            Output: [sp2349@ruddle1 project1]$ cat paths 
                    /gpfs/ycga/home/sp2349/project1/KAVM10-1/KAVM10-1.cram
                    /gpfs/ycga/home/sp2349/project1/KAVM10-2/KAVM10-2.cram
                    /gpfs/ycga/home/sp2349/project1/KAVM10-3/KAVM10-3.cram
      
    
    
2. Submit an interactive job on a compute node to run plot_reads:

    Compute0:
    
    `bsub -Is -q research-hpc -R "select[mem>8000] rusage[mem=8000]" -a 'docker(sam16711/plot_reads:v1)' /bin/bash`

    Compute1:
    
    `bsub -Is -G compute-jin810 -q general-interactive -M 8GB -R "select[mem>8GB] rusage[mem=8GB]" -a 'docker(sam16711/plot_reads:v1)' /bin/bash`
    
    Ruddle:
    `tmux new -s plotReads` : opens a new tmux window to run plotReads in the background
    
    Once in your new window run: `srun --pty --mem=8G -p interactive bash`
    
    Wait for the node to start. Then run the follwing line:
    
        cat samples.txt | while read sample; do cat pos.txt | while read chr pos; do plotReads $chr:$pos $sample;done; done
    
4. Create image plots at every position in pos.txt for every sample in samples.txt (Good for checking false positives based on sequence context).  
        
        Example command when you have a list of positions you would like to visualize for several samples
        
        cat samples.txt | while read sample; do cat pos.txt | while read chr pos; do plotReads $chr:$pos $sample;done; done`
    
    This will output all image plots in the current working directory.
    
    Example image plot below:
    ![image1](./NA12878_chr13_18174454.png)
    
5. Create text plots at every position in pos.txt for every sample in samples.txt (Good for checking bad alignments).
    
        Example command when you have a list of positions you would like to visualize for several samples
        
        cat samples.txt | while read sample; do cat pos.txt | while read chr pos; do plotReads -t $chr:$pos >> ./$(basename $sample)_"$chr"_"$pos".txt $sample;done; done
    
    This will output all text plots in the current working directory
    
    Example text plot below:
    ![image2](./NA12878_chr13_18174454_partial.png)
    
6. Validate Variants by eliminating false positives  
    False positive Checks:  
       * Bad alignments: 60 is max alignment score. Many alignments of 40 or less can indicate a redundant region  (See left side of text plots)  
       * Variants in homopolymers and repeat regions. (If the variant is in this region, it is most likely a false positive).  
       * Variants only ocurring in single orientation (forward or reverse). Denoted by carrot symbols in both image and text plots. `">": forward`,  `"<" reverse`
