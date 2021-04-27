# Benchmark WGS Parabricks Germline pipeline using GIAB NA12878

### Requirements:

* WashU compute1 GPU server
* Docker images for [`Hap.py`](https://github.com/Illumina/hap.py) (benchmarking tools)
    * [Dockerhub - sam16711/hap.py](https://hub.docker.com/r/sam16711/hap.py)
* Benchmarking samples (NIST NA12878)
    *  NA12878 300X WGS:
        *  Sample download from [sequence.index.NA12878_Illumina300X_wgs_09252015](https://github.com/genome-in-a-bottle/giab_data_indexes/blob/master/NA12878/sequence.index.NA12878_Illumina300X_wgs_09252015)
        *  Processing: `cat` all R1/R2 into merged_r1.fq / merged_r2.fq
        *  File saved at compute1: `/storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs/samples/NA12878_wgs`
    *  NA12878 Downsampled WGS:
        *  Sample processing: Using `seqtk` downsample 300X NA12878 to 10%. [DownSampling_using_seqtk.md](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/other_protocols/DownSampling_using_seqtk.md)
        *  File saved at compute1: `/storage1/fs1/jin810/Active/fup/NA12878_FQs/NA12878_WGS_downsampling/samples/NA12878_wgs_10persent_downsample_seqtk/`
* [High Confidence VCF calls and regions (.bed) files - FTP](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/NA12878_HG001/latest/GRCh38/)
* [GRch38 Difficult Regions - FTP](ftp://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/genome-stratifications/v2.0/GRCh38/union/GRCh38_alldifficultregions.bed.gz)
* Docker images for `bedtools`
    * [Docker Hub - spashleyfu/bedtools](https://hub.docker.com/repository/docker/spashleyfu/bedtools)

### Outline:

1. Call variants for gold standard benchmarking samples (As Query VCF) [link](#1-call-variants-for-gold-standard-benchmarking-samples-as-query-vcf)
    
    1a. Call variants using Parabricks Germline pipeline with NA12878 300X WGS sample [link](#1a-call-variants-using-parabricks-germline-pipeline-with-na12878-300x-wgs-sample)
    
    1b. Call variants using Parabricks Germline pipeline with NA12878 Downsampled WGS sample [link](#1b-call-variants-using-parabricks-germline-pipeline-with-na12878-downsampled-wgs-sample)

2. Create Regions of Interesting (BED file) [link](#2-create-regions-of-interesting-bed-file)
    
    2a. High confidence regions Subtract Difficult Regions - Regions of interest [link](#2a-high-confidence-regions-subtract-difficult-regions---regions-of-interest)
    
    2b. Evaluate the coverage of each BED files [link](#2b-evaluate-the-coverage-of-each-bed-files)

3. Run `hap.py` on compute1 [link](#3-run-happy-on-compute1)

### Steps:

#### 1. Call variants for gold standard benchmarking samples (As Query VCF)

**[GERMLINE PIPELINE](https://docs.nvidia.com/clara/parabricks/v3.5/text/germline_pipeline.html)**
![GERMLINE PIPELINE](https://docs.nvidia.com/clara/parabricks/v3.5/_images/germline.png)

#### 1a. Call variants using Parabricks Germline pipeline with NA12878 300X WGS sample

Script at compute1: `/storage1/fs1/jin810/Active/fup/pbrun_germline_v3.5.0.1_pfuTest_v5_NA12878_300X.sh`

```
[fup@compute1-client-4 fup]$ ./pbrun_germline_v3.5.0.1_pfuTest_v5_NA12878_300X.sh
Samples: /storage1/fs1/jin810/Active/fup/NA12878_FQs/NA12878_WGS_300X/samples/NA12878_wgs_300x
Sample: /storage1/fs1/jin810/Active/fup/NA12878_FQs/NA12878_WGS_300X/samples/NA12878_wgs_300x
InputStr will be: --in-fq /storage1/fs1/jin810/Active/fup/NA12878_FQs/NA12878_WGS_300X/samples/NA12878_wgs_300x/merged_R1.fastq.gz /storage1/fs1/jin810/Active/fup/NA12878_FQs/NA12878_WGS_300X/samples/NA12878_wgs_300x/merged_R2.fastq.gz
Temp Directory: /storage1/fs1/jin810/Active/fup/pb_testOut/pbrunGermline_v3.5.0.1_v5/temp
Out Directory: /storage1/fs1/jin810/Active/fup/pb_testOut/pbrunGermline_v3.5.0.1_v5
Job <720507> is submitted to queue <general>.

...SUCCESSED!


// OUT files:
[fup@compute1-client-3 fup]$ ls -lh /storage1/fs1/jin810/Active/fup/pb_testOut/pbrunGermline_v3.5.0.1_v5
total 675G
-rw-------. 1 fup domain users 5.9K Apr 10 08:44 dup_metrics.txt
-rw-------. 1 fup domain users 116K Apr 10 12:58 err.txt
-rw-------. 1 fup domain users 674G Apr 10 09:56 germline_output.bam
-rw-------. 1 fup domain users  12M Apr 10 09:56 germline_output.bam.bai
-rw-------. 1 fup domain users  92K Apr 10 09:57 germline_output_chrs.txt
-rw-------. 1 fup domain users 1.3M Apr 10 09:56 germline_report.txt
-rw-------. 1 fup domain users  13K Apr 10 12:58 out.txt
-rw-------. 1 fup domain users 1.1G Apr 19 14:53 pbrunGermlineSampleOutVariants.vcf
drwx------. 2 fup domain users 8.0K Apr 10 12:58 temp

```

#### 1b. Call variants using Parabricks Germline pipeline with NA12878 Downsampled WGS sample

Script at compute1: `/storage1/fs1/jin810/Active/fup/pbrun_germline_v3.5.0.1_pfuTest_v3_NA12878_downsampling.sh`

```
[fup@compute1-client-3 fup]$ ./pbrun_germline_v3.5.0.1_pfuTest_v3_NA12878_downsampling.sh
Samples: /storage1/fs1/jin810/Active/fup/NA12878_FQs/NA12878_WGS_downsampling/samples/NA12878_wgs_10persent_downsample_seqtk
Sample: /storage1/fs1/jin810/Active/fup/NA12878_FQs/NA12878_WGS_downsampling/samples/NA12878_wgs_10persent_downsample_seqtk
InputStr will be: --in-fq /storage1/fs1/jin810/Active/fup/NA12878_FQs/NA12878_WGS_downsampling//samples/NA12878_wgs_10persent_downsample_seqtk/NA12878_wgs_downsample_10percent_R1.fastq.gz /storage1/fs1/jin810/Active/fup/NA12878_FQs/NA12878_WGS_downsampling//samples/NA12878_wgs_10persent_downsample_seqtk/NA12878_wgs_downsample_10percent_R2.fastq.gz
Temp Directory: /storage1/fs1/jin810/Active/fup/pb_testOut/pbrunGermline_v3.5.0.1_v3_run2/temp
Out Directory: /storage1/fs1/jin810/Active/fup/pb_testOut/pbrunGermline_v3.5.0.1_v3_run2
Job <720318> is submitted to queue <general>.

...SUCCESSED!


// OUT files:
[fup@compute1-client-3 fup]$ ls -lh /storage1/fs1/jin810/Active/fup/pb_testOut/pbrunGermline_v3.5.0.1_v3_run2/
total 74G
-rw-------. 1 fup domain users 2.8K Apr  9 18:19 dup_metrics.txt
-rw-------. 1 fup domain users  23K Apr  9 18:55 err.txt
-rw-------. 1 fup domain users  73G Apr  9 18:28 germline_output.bam
-rw-------. 1 fup domain users 9.0M Apr  9 18:28 germline_output.bam.bai
-rw-------. 1 fup domain users  90K Apr  9 18:28 germline_output_chrs.txt
-rw-------. 1 fup domain users 1.2M Apr  9 18:28 germline_report.txt
-rw-------. 1 fup domain users  13K Apr  9 18:55 out.txt
-rw-------. 1 fup domain users 979M Apr  9 18:55 pbrunGermlineSampleOutVariants.vcf
drwx------. 2 fup domain users 8.0K Apr  9 18:55 temp

```


#### 2. Create Regions of Interesting (BED file)

Docker images: `bsub -Is -G compute-jin810 -q general-interactive -a 'docker(spashleyfu/bedtools)' -R "select[mem>16000] rusage[mem=15000]" /bin/bash`

#### 2a. High confidence regions Subtract Difficult Regions - Regions of interest

Commands - [bedtools subtract](https://bedtools.readthedocs.io/en/latest/content/tools/subtract.html)

![bedtools subtract](https://camo.githubusercontent.com/f74626f2f0609ebd7d5abcff8a47d3c2f4a6ee5f96ddf7a333ab9b2e81043bed/68747470733a2f2f626564746f6f6c732e72656164746865646f63732e696f2f656e2f6c61746573742f5f696d616765732f73756274726163742d676c7970682e706e67)

**`bedtools subtract [OPTIONS] -a <BED/GFF/VCF> -b <BED/GFF/VCF>`**

```
[fup@compute1-client-3 ~]$ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(spashleyfu/bedtools)' -R "select[mem>16000] rusage[mem=15000]" /bin/bash
bash-5.1$ 
bash-5.1$ /opt/bedtools2/bin/bedtools subtract \
-a HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_nosomaticdel_noCENorHET7.bed \
-b GRCh38_alldifficultregions.bed.gz \
> HG001_GRCh38_GIAB_highconf_Subtract_alldifficultregions_JinLab_WGS.bed

```

#### 2b. Evaluate the coverage of each BED files

Commands - [bedtools genomecov](https://bedtools.readthedocs.io/en/latest/content/tools/genomecov.html)

**`bedtools genomecov -i A.bed -g my.genome`**

```
// HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_nosomaticdel_noCENorHET7.bed
ash-5.1$ /opt/bedtools2/bin/bedtools genomecov -i HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_nosomaticdel_noCENorHET7.bed -g /opt/bedtools2/genomes/human.hg38.genome > genomecov_HG001_highConf.txt

bash-5.1$ tail genomecov_HG001_highConf.txt
...
chrUn_KI270392v1	0	971	971	1
chrUn_KI270394v1	0	970	970	1
genome	0	770250573	3209302674	0.240006
genome	1	2439052101	3209302674	0.759994


// GRCh38_alldifficultregions.bed
bash-5.1$ /opt/bedtools2/bin/bedtools genomecov -i GRCh38_alldifficultregions.bed.gz -g /opt/bedtools2/genomes/human.hg38.genome > genomecov_alldifficult.txt

bash-5.1$ tail genomecov_alldifficult.txt
...
chrUn_KI270392v1	0	971	971	1
chrUn_KI270394v1	0	970	970	1
genome	0	2580613283	3209302674	0.804104
genome	1	628689391	3209302674	0.195896


// HG001_GRCh38_GIAB_highconf_Subtract_alldifficultregions_JinLab_WGS.bed:
bash-5.1$ /opt/bedtools2/bin/bedtools genomecov -i HG001_GRCh38_GIAB_highconf_Subtract_alldifficultregions_JinLab_WGS.bed -g /opt/bedtools2/genomes/human.hg38.genome > genomecov_highConf_Subtract_DifficultRegions.txt

bash-5.1$ tail genomecov_highConf_Subtract_DifficultRegions.txt
...
chrUn_KI270392v1	0	971	971	1
chrUn_KI270394v1	0	970	970	1
genome	0	1107277863	3209302674	0.345021
genome	1	2102024811	3209302674	0.654979

```

| BED file | number of bases on genome | size of entire genome | fraction of bases on entire genome |
| -------- | ------------------------- | --------------------- | ---------------------------------- |
| HG001_GRCh38_GIAB_highconf_\*.bed | 2439052101 | 3209302674 | 0.759994 |
| GRCh38_alldifficultregions.bed | 628689391 | 3209302674 | 0.195896 |
| HG001_GRCh38_GIAB_highconf_Subtract_alldifficultregions_JinLab_WGS.bed | 2102024811 | 3209302674 | 0.654979 |


#### 3. Run `hap.py` on compute1

![hap.py](https://camo.githubusercontent.com/44897ee0b0bb921e12898602ccd348b26d40f9a58ecf995baaf7803068679ac9/68747470733a2f2f7777772e6e6362692e6e6c6d2e6e69682e676f762f706d632f61727469636c65732f504d43363639393632372f62696e2f6e69686d732d313533333738332d66303030312e6a7067)

**[Hap.py User's Manual](https://github.com/Illumina/hap.py/blob/master/doc/happy.md)**

Docker images: `bsub -Is -R "select[mem>15000] rusage[mem=15000]" -q general-interactive -a 'docker(sam16711/hap.py@sha256:f82481e5411aab643e99c66f47f1024d14a1c84bde60f61fa820502b34353b77)' /bin/bash`

**NA12878 300X sample:**

```
[fup@compute1-client-3 ~]$ bsub -Is -R "select[mem>15000] rusage[mem=15000]" -q general-interactive -a 'docker(sam16711/hap.py@sha256:f82481e5411aab643e99c66f47f1024d14a1c84bde60f61fa820502b34353b77)' /bin/bash
...

fup@compute1-exec-214:/storage1/fs1/jin810/Active/fup/benchmark_test/test2_newCallSet$ /opt/hap.py/bin/hap.py /storage1/fs1/jin810/Active/references/HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_PGandRTGphasetransfer.vcf.gz /storage1/fs1/jin810/Active/fup/pb_testOut/pbrunGermline_v3.5.0.1_v5/pbrunGermlineSampleOutVariants.vcf -f /storage1/fs1/jin810/Active/fup/benchmark_test/bedfile_test/HG001_GRCh38_GIAB_highconf_Subtract_alldifficultregions_JinLab_WGS.bed -o /storage1/fs1/jin810/Active/fup/benchmark_test/test2_newCallSet/NA12878_parabricks_JinLabCallSet -r /storage1/fs1/jin810/Active/fup/benchmark_test/compute0_REF_hg38/all_sequences.fa --engine vcfeval --engine-vcfeval-template /storage1/fs1/jin810/Active/references/hg38.sdf --engine-vcfeval-path /opt/hap.py/libexec/rtg-tools-install/rtg --threads 10
2021-04-21 22:17:41,146 WARNING  No reference file found at default locations. You can set the environment variable 'HGREF' or 'HG19' to point to a suitable Fasta file.
Hap.py v0.3.12-2-g9d128a9
[W] overlapping records at chr1:37070742 for sample 0
...
Benchmarking Summary:
Type Filter  TRUTH.TOTAL  TRUTH.TP  TRUTH.FN  QUERY.TOTAL  QUERY.FP  QUERY.UNK  FP.gt  FP.al  METRIC.Recall  METRIC.Precision  METRIC.Frac_NA  METRIC.F1_Score  TRUTH.TOTAL.TiTv_ratio  QUERY.TOTAL.TiTv_ratio  TRUTH.TOTAL.het_hom_ratio  QUERY.TOTAL.het_hom_ratio
INDEL    ALL       149114    149063        51      1025271       788     875250     11    127       0.999658          0.994747        0.853677         0.997197                     NaN                     NaN                   1.426534                   2.110712
INDEL   PASS       149114    149063        51      1025271       788     875250     11    127       0.999658          0.994747        0.853677         0.997197                     NaN                     NaN                   1.426534                   2.110712
 SNP    ALL      2572014   2571894       120      4245301      7422    1665958     25    801       0.999953          0.997123        0.392424         0.998536                2.211801                1.876534                   1.546028                   1.754752
 SNP   PASS      2572014   2571894       120      4245301      7422    1665958     25    801       0.999953          0.997123        0.392424         0.998536                2.211801                1.876534                   1.546028                   1.754752

```
**NA12878 Downsampled:**

```
[fup@compute1-client-3 ~]$ bsub -Is -R "select[mem>15000] rusage[mem=15000]" -q general-interactive -a 'docker(sam16711/hap.py@sha256:f82481e5411aab643e99c66f47f1024d14a1c84bde60f61fa820502b34353b77)' /bin/bash
...

fup@compute1-exec-214:/storage1/fs1/jin810/Active/fup/benchmark_test/test2_newCallSet$ /opt/hap.py/bin/hap.py /storage1/fs1/jin810/Active/references/HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_PGandRTGphasetransfer.vcf.gz /storage1/fs1/jin810/Active/fup/pb_testOut/pbrunGermline_v3.5.0.1_v3_run2/pbrunGermlineSampleOutVariants.vcf -f /storage1/fs1/jin810/Active/fup/benchmark_test/bedfile_test/HG001_GRCh38_GIAB_highconf_Subtract_alldifficultregions_JinLab_WGS.bed -o /storage1/fs1/jin810/Active/fup/benchmark_test/test2_newCallSet/NA12878_DownSample_parabricks_JinLabCallSet -r /storage1/fs1/jin810/Active/fup/benchmark_test/compute0_REF_hg38/all_sequences.fa --engine vcfeval --engine-vcfeval-template /storage1/fs1/jin810/Active/references/hg38.sdf --engine-vcfeval-path /opt/hap.py/libexec/rtg-tools-install/rtg --threads 10
2021-04-22 15:13:49,210 WARNING  No reference file found at default locations. You can set the environment variable 'HGREF' or 'HG19' to point to a suitable Fasta file.
Hap.py v0.3.12-2-g9d128a9
[W] overlapping records at chr1:37070742 for sample 0
[W] Variants that overlap on the reference allele: 93
[I] Total VCF records:         3619471
[I] Non-reference VCF records: 3619471
...

Benchmarking Summary:
Type Filter  TRUTH.TOTAL  TRUTH.TP  TRUTH.FN  QUERY.TOTAL  QUERY.FP  QUERY.UNK  FP.gt  FP.al  METRIC.Recall  METRIC.Precision  METRIC.Frac_NA  METRIC.F1_Score  TRUTH.TOTAL.TiTv_ratio  QUERY.TOTAL.TiTv_ratio  TRUTH.TOTAL.het_hom_ratio  QUERY.TOTAL.het_hom_ratio
INDEL    ALL       149114    148977       137       914333       552     764634     19    125       0.999081          0.996313        0.836275         0.997695                     NaN                     NaN                   1.426534                   1.802543
INDEL   PASS       149114    148977       137       914333       552     764634     19    125       0.999081          0.996313        0.836275         0.997695                     NaN                     NaN                   1.426534                   1.802543
  SNP    ALL      2572014   2570541      1473      4019658      4417    1444674    216    490       0.999427          0.998285        0.359402         0.998856                2.211801                 1.95898                   1.546028                   1.662447
  SNP   PASS      2572014   2570541      1473      4019658      4417    1444674    216    490       0.999427          0.998285        0.359402         0.998856                2.211801                 1.95898                   1.546028                   1.662447


```



