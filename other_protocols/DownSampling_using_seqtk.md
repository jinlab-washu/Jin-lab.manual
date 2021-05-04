# Downsampling 300X NA12878 WGS using `seqtk`

### Requirements:

* Compute1 access

* DownSampling Tools: `seqtk`

    1. **[Github - lh3/seqtk](https://github.com/lh3/seqtk)**

    2. **[Docker Images - biocontainers/seqtk](https://hub.docker.com/r/biocontainers/seqtk)**

* Sample files:

    * NA12878 300X: `/storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs/samples/NA12878_wgs/`



### Steps:

#### 1. Load the `biocontainers/seqtk` Docker image on compute1:

```
[fup@compute1-client-4 ~]$ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(biocontainers/seqtk:v1.3-1-deb_cv1)' -R "select[mem>16000] rusage[mem=15000]" /bin/bash
...
Status: Downloaded newer image for biocontainers/seqtk:v1.3-1-deb_cv1
docker.io/biocontainers/seqtk:v1.3-1-deb_cv1


// Check out command:
fup@compute1-exec-195:~$ seqtk

Usage:   seqtk <command> <arguments>
Version: 1.3-r106

Command: seq       common transformation of FASTA/Q
         comp      get the nucleotide composition of FASTA/Q
         sample    subsample sequences
         subseq    extract subsequences from FASTA/Q
         fqchk     fastq QC (base/quality summary)
         mergepe   interleave two PE FASTA/Q files
         trimfq    trim FASTQ using the Phred algorithm

         hety      regional heterozygosity
         gc        identify high- or low-GC regions
         mutfa     point mutate FASTA at specified positions
         mergefa   merge two FASTA/Q files
         famask    apply a X-coded FASTA to a source FASTA
         dropse    drop unpaired from interleaved PE FASTA/Q
         rename    rename sequence names
         randbase  choose a random base from hets
         cutN      cut sequence at long N
         listhet   extract the position of each het

```

#### 2. Downsampling using `seqtk`:

Follow the example from seqtk's GitHub with your own files:

```
seqtk sample -s100 read1.fq 10000 > sub1.fq
seqtk sample -s100 read2.fq 10000 > sub2.fq
```

Sample data files can be found at:

NA12878_300X R1 path: `/storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs/samples/NA12878_wgs/merged_R1.fastq.gz`

NA12878_300X R2 path: `/storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs/samples/NA12878_wgs/merged_R2.fastq.gz`

Below are example results using random seed 200 (-s200) for both R1 and R2:

```
// NA12878 300X file size:
[fup@compute1-client-3 fup]$ ls -lh /storage1/fs1/jin810/Active/fastq/benchmark/NA12878/wgs/merged_R*.fastq.gz
-rw-------. 1 s.peters domain users 367G Jan 25 15:56 /storage1/fs1/jin810/Active/fastq/benchmark/NA12878/wgs/merged_R1.fastq.gz
-rw-------. 1 s.peters domain users 393G Jan 25 15:57 /storage1/fs1/jin810/Active/fastq/benchmark/NA12878/wgs/merged_R2.fastq.gz


// R1:
fup@compute1-exec-195:/storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs_downsample/samples/NA12878_wgs_downsampling$ seqtk sample -s 200 /storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs/samples/NA12878_wgs/merged_R1.fastq.gz 0.1 > NA12878_wgs_downsample_10percent_R1.fastq   

fup@compute1-exec-195:/storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs_downsample/samples/NA12878_wgs_downsampling$ ls -lh
total 103G
-rw-------. 1 fup domain users 103G Apr  8 02:57 NA12878_wgs_downsample_10percent_R1.fastq

// R2:
fup@compute1-exec-195:/storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs_downsample/samples/NA12878_wgs_downsampling$ seqtk sample -s 200 /storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs/samples/NA12878_wgs/merged_R2.fastq.gz 0.1 > NA12878_wgs_downsample_10percent_R2.fastq
fup@compute1-exec-195:/storage1/fs1/jin810/Active/pb_runs/benchmark_NA12878_wgs_downsample/samples/NA12878_wgs_downsampling$ ls -lh
total 205G
-rw-------. 1 fup domain users 103G Apr  8 02:57 NA12878_wgs_downsample_10percent_R1.fastq
-rw-------. 1 fup domain users 103G Apr  8 05:37 NA12878_wgs_downsample_10percent_R2.fastq

```



