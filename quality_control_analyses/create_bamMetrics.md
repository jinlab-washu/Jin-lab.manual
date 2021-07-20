# Generate bamMetrics

> Tool: 
> Jim Knight's bamMetrics
> 
> Docker:
> Sam Peter's Knight bam_metrics image (sam16711/bam_metrics:v1)
> 
> [Docker hub](https://hub.docker.com/r/sam16711/bam_metrics/tags?page=1&ordering=last_updated), 
> [Github Doc](https://github.com/jinlab-washu/bamMetrics)
> 
> Script: 
> [01 - Peter Jin's statsmerge.v2.py program (Python v2.7)](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/quality_control_analyses/statsmerge_v2.md)
> 
> [02 - mergebammetrics.py](#mergebammetricspy)

### How to use it on WUSTL Compute1?

#### 1. Request bamMetrics docker:

  ```
  $ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(sam16711/bam_metrics:v1)' -n 6 -R "select[mem>16000] rusage[mem=15000]" /bin/bash
  ```

#### 2. Generate bamMetrics for each sample:

  * How to execute program:

  ```
  $ /opt/bamMetrics 
  Usage:  bamMetrics [-g] [-1] [-b bedFile] [-r refFile] [-o outputFile] [-c coverageOutputFile] [-d depthOutputFile] [--countdups] [--long] [-q #] bamFile
  
  ```
  
  * WGS example:

  Basic Usage: `/opt/bamMetrics -g -t {CPUs} -r $REF -o {output_file_name.txt} {bam/cram_file_path}`

  ```
  $ /opt/bamMetrics -g -t 6 -r /storage1/fs1/bga/Active/gmsroot/gc2560/core/model_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/all_sequences.fa -o testBamMetrics.txt snakemake_results/pb_germline/TWHJ-PNRR-10248-10248/TWHJ-PNRR-10248-10248_germline.bam
   -> 1000000 reads, at chr1:2786231
   -> 2000000 reads, at chr1:5566079
   ...
  
  ```

#### 3. Merge all bamMetrics results :

You have TWO ways to do it:

##### `statsmerge.v2_washu.py`
  
    * program: `/storage1/fs1/jin810/Active/programs/statsmerge.v2_washu.py`
    * Docker: `sam16711/bam_metrics:v1`
    * Detail Please See Doc: [statsmerge_v2](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/quality_control_analyses/statsmerge_v2.md) 
  
##### `mergeBamMetrics.py`

    * program: `/storage1/fs1/jin810/Active/programs/mergeBamMetrics.py`
    * Docker: `spashleyfu/knight_bam_metrics:py38_pandas`
    * Usage: `$ python3 mergeBamMetrics.py sample_list_file`

  Example:
  
  ```
  // Request a interactive job:
  $ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(spashleyfu/knight_bam_metrics:py38_pandas)' -n 2 -R "select[mem>16000] rusage[mem=15000]" /bin/bash
  
  // Generate sample.list
  $ ls -d $PWD/data/TWHJ-PNRR-10* > sample.list
  
  // Run the program:
  $ python3 mergeBamMetrics.py sample.list 
                            TWHJ-PNRR-10001-10001 TWHJ-PNRR-10004-10004 TWHJ-PNRR-10006  ... TWHJ-PNRR-10598 TWHJ-PNRR-10600 TWHJ-PNRR-10976
  index                                                                                    ...                                                
  Read Length:                                  151                   151             151  ...             151             151             151
  Num reads (M):                              706.9                 639.7           734.1  ...           784.9           633.5           631.8
  Num bases (G):                              106.7                  96.6           110.9  ...           118.5            95.7            95.4
  Mean coverage:                               28.0                  26.7            31.0  ...            33.0            27.2            27.1
  Median coverage:                               28                    27              31  ...              33              27              27
  PCR duplicates:                            13.13%                 9.99%          12.51%  ...           9.69%           9.73%          11.78%
  Multiply mapped:                            4.01%                 4.44%           4.55%  ...           4.11%           4.44%           4.30%
  Unmapped:                                   5.68%                 4.24%           0.57%  ...           2.27%           2.56%           0.43%
  Reads on-target:                           74.30%                78.12%          79.14%  ...          78.94%          80.01%          80.21%
  Genome Target Reads:                       73.40%                77.10%          78.15%  ...          77.97%          79.05%          79.29%
  Genome ChrX Reads:                          2.05%                 2.17%           2.20%  ...           4.26%           2.23%           2.22%
  Genome ChrY Reads:                          0.18%                 0.28%           0.29%  ...           0.03%           0.26%           0.29%
  Genome MT/Decoy Reads:                      0.46%                 0.55%           0.54%  ...           0.52%           0.55%           0.55%
  Mean error rate:                            0.58%                 0.58%           0.71%  ...           0.67%           0.61%           0.59%
  1x target base coverage:                    98.7%                 98.7%           98.8%  ...           98.9%           98.7%           98.7%
  2x target base coverage:                    98.4%                 98.4%           98.5%  ...           98.6%           98.4%           98.4%
  4x target base coverage:                    98.0%                 98.0%           98.1%  ...           98.2%           98.0%           98.0%
  8x target base coverage:                    97.5%                 97.5%           97.6%  ...           97.7%           97.5%           97.5%
  10x target base coverage:                   97.3%                 97.3%           97.4%  ...           97.5%           97.3%           97.3%
  15x target base coverage:                   96.1%                 95.7%           96.7%  ...           97.0%           95.9%           96.0%
  20x target base coverage:                   89.9%                 87.2%           93.7%  ...           95.3%           88.5%           88.7%
  30x target base coverage:                   41.4%                 32.8%           58.8%  ...           69.3%           35.8%           35.4%
  40x target base coverage:                    5.2%                  3.0%           12.3%  ...           19.2%            3.6%            3.4%
  50x target base coverage:                    0.5%                  0.4%            1.1%  ...            1.9%            0.4%            0.4%
  100x target base coverage:                   0.1%                  0.1%            0.1%  ...            0.1%            0.1%            0.1%
  1x target cov, incl MQ 0:                   99.9%                 99.8%           99.9%  ...           99.9%           99.8%           99.8%
  2x target cov, incl MQ 0:                   99.8%                 99.8%           99.8%  ...           99.8%           99.8%           99.8%
  4x target cov, incl MQ 0:                   99.7%                 99.6%           99.7%  ...           99.7%           99.6%           99.6%
  8x target cov, incl MQ 0:                   99.4%                 99.4%           99.5%  ...           99.5%           99.4%           99.4%
  10x target cov, incl MQ 0:                  99.2%                 99.2%           99.3%  ...           99.4%           99.2%           99.2%
  15x target cov, incl MQ 0:                  98.1%                 97.7%           98.7%  ...           99.0%           97.8%           98.0%
  20x target cov, incl MQ 0:                  91.9%                 89.2%           95.7%  ...           97.3%           90.4%           90.6%
  30x target cov, incl MQ 0:                  43.1%                 34.3%           60.6%  ...           71.2%           37.3%           36.9%
  40x target cov, incl MQ 0:                   6.1%                  3.8%           13.5%  ...           20.5%            4.4%            4.2%
  50x target cov, incl MQ 0:                   1.0%                  0.8%            1.8%  ...            2.7%            0.8%            0.8%
  100x target cov, incl MQ 0:                  0.2%                  0.2%            0.3%  ...            0.3%            0.2%            0.2%

  [36 rows x 29 columns]
  
  ```
