# Using VerifyBamID to Check Sample Contamination

We used VerifyBamID tool to check sample contamination. 

Basically most of people use "VerifyBamID" (Jun et al. 2012) as main tool, but in 2020, the same group published [the paper](https://doi.org/10.1101/gr.246934.118) whichshown that "verifyBamID can underestimate DNA contamination rates if the assumed population allele frequencies are inaccurate (Jun et al. 2012)." So, they provided a novel method to detect and estimate DNA contamination called "VerifyBamID2" (Zhang et al. 2020). 

[![verifyBamID vs verifyBamID2](https://genome.cshlp.org/content/30/2/185/F1.large.jpg)](https://genome.cshlp.org/content/30/2/185.full)

Althought, it's quite new for many of pipelines, but the way to run it is almost the same.

## Two versions of VerifyBamID

### 1. VerifyBamID

> Website: https://genome.sph.umich.edu/wiki/VerifyBamID
>
> Docker Image: `spashleyfu/ubuntu20_snakemake:verifyBamID`
> 
> Version: verifyBamID 1.1.3
> 
> Standards freemix cutoff: 1% or 5% (We use 1% mostly)

How to run it?

```
$ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(spashleyfu/ubuntu20_snakemake:verifyBamID)' /bin/bash

(base) fup@compute1-exec-131:~$ verifyBamID
verifyBamID 1.1.3 -- verify identity and purity of sequence data
(c) 2010-2014 Hyun Min Kang, Goo Jun, and Goncalo Abecasis


Available Options
                             Input Files : --vcf [], --bam [], --bai [],
                                           --subset [], --smID []
                    VCF analysis options : --genoError [1.0e-03],
                                           --minAF [0.01],
                                           --minCallRate [0.50]
   Individuals to compare with chip data : --site, --self, --best
          Chip-free optimization options : --free-none, --free-mix [ON],
                                           --free-refBias, --free-full
          With-chip optimization options : --chip-none, --chip-mix [ON],
                                           --chip-refBias, --chip-full
                    BAM analysis options : --ignoreRG, --ignoreOverlapPair,
                                           --noEOF, --precise, --minMapQ [10],
                                           --maxDepth [20], --minQ [13],
                                           --maxQ [40], --grid [0.05]
                 Modeling Reference Bias : --refRef [1.00], --refHet [0.50],
                                           --refAlt [0.00]
                          Output options : --out [], --verbose
                               PhoneHome : --noPhoneHome,
                                           --phoneHomeThinning [50]


FATAL ERROR - 
--vcf [vcf file] required

////////////////////////////////////
// Example for runing the sample:
// * The VCF are 1000 Genome VCF.
// * {input.bam}: Replace this whold thing as your BAM file full path.
// * {params.prefix}: The prefix for your output file name.
$ input_vcf="/storage1/fs1/jin810/Active/known_sites/1000G_phase1.snps.high_confidence.hg38.vcf"
$ verifyBamID --verbose --vcf $input_vcf --bam {input.bam} --best --ignoreRG --out {params.prefix}
////////////////////////////////////
```

### 2. VerifyBamID2

It's a newer method, ODI: [10.1101/gr.246934.118](https://doi.org/10.1101/gr.246934.118)

> Github Repo: https://github.com/Griffan/VerifyBamID 
> 
> Docker Image: `spashleyfu/ubuntu20_snakemake:verifyBamID2`
> 
> Standards freemix cutoff: 1% or 5% (We use 1% mostly)

How to run it?

```
$ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(spashleyfu/ubuntu20_snakemake:verifyBamID2)' /bin/bash

$ verifybamid2
VerifyBamID2: A robust tool for DNA contamination estimation from sequence reads using ancestry-agnostic method.

 Version:2.0.1
 Copyright (c) 2009-2020 by Hyun Min Kang and Fan Zhang
 This project is licensed under the terms of the MIT license.

The following parameters are available.  Ones with "[]" are in effect:

Available Options
                    Input/Output Files : --BamFile [Empty],
                                         --PileupFile [Empty],
                                         --Reference [Empty],
                                         --SVDPrefix [/opt/conda/share/verifybamid2-2.0.1-3/resource/1000g.100k.b38.vcf.gz.dat],
                                         --Output [result]
               Model Selection Options : --WithinAncestry,
                                         --DisableSanityCheck, --NumPC [2],
                                         --FixPC [Empty],
                                         --FixAlpha [-1.0e+00],
                                         --KnownAF [Empty], --NumThread [4],
                                         --Seed [12345], --Epsilon [1.0e-08],
                                         --OutputPileup, --Verbose
   Construction of SVD Auxiliary Files : --RefVCF [Empty]
                        Pileup Options : --min-BQ [13], --min-MQ [2],
                                         --adjust-MQ [40], --max-depth [8000],
                                         --no-orphans, --incl-flags [1040],
                                         --excl-flags [1796]
                    Deprecated Options : --UDPath [Empty], --MeanPath [Empty],
                                         --BedPath [Empty]



FATAL ERROR - 
--Reference is required

Exiting due to ERROR:
	Exception was thrown

////////////////////////////////////
// Example For BAM/CRAMs aligned to GRCh38:
// https://github.com/Griffan/VerifyBamID#for-bamcrams-aligned-to-grch38
// * This tool already contain the 1000 Genome datasets
$ VERIFY_BAM_ID_HOME="/opt/conda/pkgs/verifybamid2-2.0.1-h1854008_3/share/verifybamid2-2.0.1-3"
$ verifybamid2 \
--SVDPrefix $VERIFY_BAM_ID_HOME/resource/1000g.phase3.100k.b38.vcf.gz.dat \
--Reference /storage1/fs1/bga/Active/gmsroot/gc2560/core/model_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/all_sequences.fa \
--BamFile {input.bam_or_cram} \
--Output {output.file_prefix} \
--PileupFile 1000g.phase3.100k.b38.vcf.gz
////////////////////////////////////
```

**An Real Example:**

```
(base) fup@compute1-exec-132:~$ verifybamid2 \
--SVDPrefix $VERIFY_BAM_ID_HOME/resource/1000g.phase3.100k.b38.vcf.gz.dat \
--Reference /storage1/fs1/bga/Active/gmsroot/gc2560/core/model_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/all_sequences.fa \
--BamFile /storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/snakemake_results/crams/TWHJ-PNRR-10001-10001_germline.bam.cram \
--Output test_verifybam2 
VerifyBamID2: A robust tool for DNA contamination estimation from sequence reads using ancestry-agnostic method.

 Version:2.0.1
 Copyright (c) 2009-2020 by Hyun Min Kang and Fan Zhang
 This project is licensed under the terms of the MIT license.

The following parameters are available.  Ones with "[]" are in effect:

Available Options
                    Input/Output Files : --BamFile [/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/snakemake_results/crams/TWHJ-PNRR-10001-10001_germline.bam.cram],
                                         --PileupFile [Empty],
                                         --Reference [/storage1/fs1/bga/Active/gmsroot/gc2560/core/model_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/all_sequences.fa],
                                         --SVDPrefix [/opt/conda/pkgs/verifybamid2-2.0.1-h1854008_3/share/verifybamid2-2.0.1-3/resource/1000g.phase3.100k.b38.vcf.gz.dat],
                                         --Output [test_verifybam2]
               Model Selection Options : --WithinAncestry,
                                         --DisableSanityCheck, --NumPC [2],
                                         --FixPC [Empty],
                                         --FixAlpha [-1.0e+00],
                                         --KnownAF [Empty], --NumThread [4],
                                         --Seed [12345], --Epsilon [1.0e-08],
                                         --OutputPileup, --Verbose
   Construction of SVD Auxiliary Files : --RefVCF [Empty]
                        Pileup Options : --min-BQ [13], --min-MQ [2],
                                         --adjust-MQ [40], --max-depth [8000],
                                         --no-orphans, --incl-flags [1040],
                                         --excl-flags [1796]
                    Deprecated Options : --UDPath [Empty], --MeanPath [Empty],
                                         --BedPath [Empty]


Initialize from FullLLKFunc(int dim, ContaminationEstimator* contPtr)
[SimplePileup] 1 sample(s) in 1 input file(s)
NOTICE - Process chr1:920661-920661...
...
NOTICE - Process chr21:26604181-26604181...
[SimplePileup] Total Number Bases: 2511922
[SimplePileup] Total Number Markers: 99971
NOTICE - Number of marker in Reference Matrix:100000
NOTICE - Number of marker shared with input file:99971
NOTICE - Mean Depth:25.126507
NOTICE - SD Depth:5.701570
NOTICE - 99603 SNP markers remained after sanity check.
NOTICE - Passing Marker Sanity Check...
Estimation from OptimizeHeter:
Contaminating Sample PC1:-0.0121447	PC2:0.0261306	
Intended Sample PC1:-0.00957517	PC2:0.0253423	
FREEMIX(Alpha):0.0017266
NOTICE - Success!

// Two Output file:
[fup@compute1-client-3 Active]$ ls /storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/test_verifybam2*
/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/test_verifybam2.Ancestry
/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/test_verifybam2.selfSM

[fup@compute1-client-3 Active]$ cat /storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/test_verifybam2.Ancestry
PC	ContaminatingSample	IntendedSample
1	-0.0121447	-0.00957517
2	0.0261306	0.0253423

[fup@compute1-client-3 Active]$ cat /storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/test_verifybam2.selfSM
#SEQ_ID	RG	CHIP_ID	#SNPS	#READS	AVG_DP	FREEMIX	FREELK1	FREELK0	FREE_RH	FREE_RA	CHIPMIX	CHIPLK1	CHIPLK0	CHIP_RH	CHIP_RA	DPREF	RDPHET	RDPALT
TWHJ-PNRR-10001-10001	NA	NA	100000	2511922	25.1265	0.0017266	-665701	-667158	NA	NA	NA	NA	NA	NA	NA	NA	NA	NA
```
