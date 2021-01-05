# Coverage Metrics with statsmerge_v2

> Requirements
> * statsmerge_v2 program
>   * Ruddle path: /gpfs/ycga/home/sp2349/programs/statsmerge.v2.py
>   * Compute0/1 path:
> * Python2.7
>   * Use `module load Python` on Ruddle
>   * Find a docker image with python2.7 on WashU Compute0/1
> * Per sample exomeMetrics.txt files produced by bamMetrics program (see [here](https://github.com/jinlab-washu/bamMetrics) for more details on bamMetrics)
>   * exomeMetrics files are produced by the `rms gatkExome` pipelines on Ruddle as well as the `fastq to merged gvcf` pipeline on Compute0/1


**Note:** The Joint-Calling step of the WashU Whole Exome Sequencing pipeline runs statsmerge_v2 for you and outputs the file in a cromwell workflow

**Description**:
The statsmerge_v2 program merges all per sample exomeMetrics files produced from the knightlab (Yale) bammetrics program into a single file 

## Protocol
1. Gather all sample directories and place into a file with each directory on a new line

    Example: `ls -d $PWD/*/ > statsfile.txt `  
    This will list the full path of all directories in the current working directory and direct the output into a new file called `statsfile.txt`
    
    Output:  
        
        [sp2349@ruddle2 test]$ ls -d $PWD/*/  
        /home/sp2349/scratch60/test/sample1/   /home/sp2349/scratch60/test/sample2/  /home/sp2349/scratch60/test/sample4/  /home/sp2349/scratch60/test/sample6/             /home/sp2349/scratch60/test/sample8/
        /home/sp2349/scratch60/test/sample10/  /home/sp2349/scratch60/test/sample3/  /home/sp2349/scratch60/test/sample5/  /home/sp2349/scratch60/test/sample7/             /home/sp2349/scratch60/test/sample9/
        
 2. Run statsmerge_v2 with the statsfile.txt created in step 1 (with python2.7)
    
    Ruddle:  
    
    (Optional) Copy statsmerge_v2 file to your local directory and run: `cp  /gpfs/ycga/home/sp2349/programs/statsmerge.v2.py path_to_destination`
    
    Load Python2.7: `module load Python`
    
    Run statsmerge_v2 and redirect output to new file: `python statsermge_v2 statsfile.txt > exomeMetricsSummary.txt`
    
 3. Check exomeMetricsSummary.txt produced in step 2 to ensure all samples have at least 90% of targets with 8X coverage
 
      Example Output:
 
        Sample1	Sample2	Sample3	Sample4	Sample5	Sample6	Sample7	Sample8	Sample9	Sample10
        Read Length:	101	101	101	101	101	101	101	101	101	101
        Num reads (M):	49.3	50.9	43.2	55	45.8	43.8	48.3	54.6	57	41.8
        Num bases (G):	5	5.1	4.4	5.6	4.6	4.4	4.9	5.5	5.8	4.2
        Mean coverage:  	55.1	55.6	50.5	48.4	41.2	55.4	56.1	63.2	48.9	48.8
        Median coverage:	54	53	49	46	39	52	54	61	46	46
        PCR duplicates: 	24.48%	22.50%	20.72%	34.52%	33.26%	21.31%	21.59%	23.19%	37.44%	24.12%
        Multiply mapped:	4.91%	4.92%	5.34%	4.85%	4.84%	5.32%	4.94%	5.23%	5.06%	4.41%
        Unmapped:       	0.07%	0.07%	0.10%	0.08%	0.11%	0.09%	0.05%	0.04%	0.09%	0.04%
        Reads on-target:	56.49%	56.02%	59.05%	45.32%	46.35%	63.24%	59.65%	58.52%	43.35%	60.58%
        Bases on-target:	42.15%	41.96%	44.12%	33.84%	34.62%	47.72%	44.49%	43.75%	32.38%	44.73%
        Mean error rate:	0.29%	0.31%	0.29%	0.28%	0.29%	0.26%	0.28%	0.28%	0.27%	0.27%
        1x target base coverage:	99.10%	99.10%	99.00%	99.20%	99.10%	98.90%	99.00%	99.00%	99.10%	98.90%
        2x target base coverage:	99.00%	99.00%	98.90%	99.00%	99.00%	98.80%	98.90%	98.90%	99.00%	98.80%
        4x target base coverage:	98.80%	98.90%	98.80%	98.90%	98.80%	98.60%	98.80%	98.80%	98.90%	98.60%
        8x target base coverage:	98.50%	98.60%	98.40%	98.50%	98.20%	98.10%	98.40%	98.50%	98.50%	98.10%
        10x target base coverage:	98.30%	98.30%	98.00%	98.10%	97.70%	97.80%	98.20%	98.30%	98.20%	97.70%
        15x target base coverage:	97.50%	97.40%	96.70%	96.50%	95.10%	96.30%	97.30%	97.60%	96.70%	95.80%
        20x target base coverage:	96.00%	95.60%	94.30%	93.30%	90.00%	93.70%	95.60%	96.30%	93.80%	92.30%
        30x target base coverage:	88.90%	87.70%	84.30%	80.70%	71.80%	84.30%	88.40%	90.90%	82.10%	79.90%
        40x target base coverage:	75.60%	74.10%	67.80%	62.20%	48.70%	69.90%	75.40%	81.00%	63.80%	62.60%
        50x target base coverage:	57.80%	57.00%	48.20%	42.70%	28.20%	53.60%	58.50%	67.30%	44.00%	44.50%
        100x target base coverage:	2.90%	3.90%	2.30%	2.30%	1.00%	6.30%	3.80%	8.80%	2.20%	2.50%
        Targets:	IDT	IDT	IDT	IDT	IDT	IDT	IDT	IDT	IDT	IDT
        
        
4. (Optional) Run check_exomeMetrics_8x.py to analyze exomeMetricsSummary.txt produced in Step 3. check_exomeMetrics_8x.py will output any sample that does not have at least 90% of targets with 8X coverage to a new falled called `8x_fail_qc_samples.txt`. If no samples are found that fit such criteria, no output file will be produced. 

    Usage: `python ../programs/check_exomeMetrics_8x.py exomeMetricsSummary.txt`
