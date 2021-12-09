# Useful resources collection for WUSTL Compute1

## Reference files

| Desc | File Type | Path | Details |
| ---- | --------- | ---- | ------- |
| GRCh38 REF (Jin's Lab) | FASTA | `/storage1/fs1/bga/Active/gmsroot/gc2560/core/model_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/all_sequences.fa` | All WGS projects in Jin's Lab |
| GRCh38 REF (broad REF) | FASTA | `/storage1/fs1/jin810/Active/references/Homo_sapiens_assembly38.fasta` | For UDN's bam files and gnomAD v3 |
| Coding Region from Yale | BED | `/storage1/fs1/jin810/Active/references/Yale_knightlab/knightlab_genomes_hs38DH_bed_files/hg38_coding_padded15_Sep2020.bed` | for extracting coding regions from WGS |

* Information of Lab's REF (Copied from MGI Slack)

  ```
  This later version added the alternate HLA haplotypes back in: GRC-human-build38_GRCh38_full_analysis_set_plus_decoy_hla_fix_FP236240_8 (21f22873ebe0486c8e6f69c15435aa96)
  FASTA path: /gscmnt/gc2560/core/model_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/all_sequences.fa
  ```

* [Broad Institute - GATK Resources Bundle](https://gatk.broadinstitute.org/hc/en-us/articles/360035890811-Resource-bundle)

## The Docker Image collection for Compute1

It's the Docker Images I used for my projects. Feel free to add more information on it.

| Main tools | Docker Images | Required Resources | dockerhub | Image size | Detail/Note |
| ---------- | ------------- | ------------------ | --------- | ---------- | ----------- |
| **Parabricks** | `us.gcr.io/ris-appeng-shared-dev/parabricks:v3.5.0.1` | 2 GPU with 256GB MEM | - | 3.78 GB | v3.5.0.1, [RIS doc](https://docs.ris.wustl.edu/doc/compute/recipes/tools/parabricks-quickstart.html) |
| **GATK**4 | `broadinstitute/gatk:latest` | 16GB MEM | [broadinstitute/gatk](https://hub.docker.com/r/broadinstitute/gatk/) | 1.64 GB | GATK 4.x and Picard, September 16, 2021 latest version is v4.2.2.0 |
| **Hail** + **VEP** | `spashleyfu/hail_vep_gnomad` | 24 CPU with 96GB MEM | [spashleyfu/hail_vep_gnomad](https://hub.docker.com/repository/docker/spashleyfu/hail_vep_gnomad) | 5.34GB | Hail with VEP and JupyterLab, bgzip |
| **Hail** | `spashleyfu/hail_0.2.79:jupyterlab` | 24 CPU with 96GB MEM | [spashleyfu/hail_0.2.79](https://hub.docker.com/repository/docker/spashleyfu/hail_0.2.79) | 2.01GB | Hail 0.2.79, JupyterLab, bgzip |
| **PlotRead** | `spashleyfu/plotreads` | 16GB MEM | [spashleyfu/plotreads](https://hub.docker.com/repository/docker/spashleyfu/plotreads) | 1.02 GB | plotRead with Python 2.7 && conda 4.8.4 && samtools 1.11 |
| Knight's **bamMetrics** | `sam16711/bam_metrics:v1` | - | [sam16711/bam_metrics](https://hub.docker.com/r/sam16711/bam_metrics) | 113.43 MB | Python 2.7; Suit for run bamMetrics alone |
| Knight's **bamMetrics** | `spashleyfu/knight_bam_metrics:py38_pandas` | - | [sam16711/bam_metrics](https://hub.docker.com/r/sam16711/bam_metrics) | 113.43 MB | with Python 3.8 and Pandas; Suit for running [mergeBamMetrics.py](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/quality_control_analyses/create_bamMetrics.md#mergebammetricspy) |
| **PLINK** 1.9 | `spashleyfu/ubuntu20_snakemake:plink` | - | [spashleyfu/ubuntu20_snakemake](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_snakemake) | 991.89 MB | PLINK 1.9 with Sankemake |
| **PLINK** 2 | `spashleyfu/ubuntu20_snakemake:plink2` | - | [spashleyfu/ubuntu20_snakemake](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_snakemake) | 1014.88 MB | PLINK 2.0 with Sankemake |
| **samtools** | `biocontainers/samtools:v1.9-4-deb_cv1` | - | [biocontainers/samtools](https://hub.docker.com/r/biocontainers/samtools) | 244.41 MB | v1.9 |
| **bcftools** | `spashleyfu/bcftools_snakemake` | - | [spashleyfu/bcftools_snakemake](https://hub.docker.com/repository/docker/spashleyfu/bcftools_snakemake) | 928.23 MB | bcftools 1.12 with Sankemake |
| **verifyBamID** | `spashleyfu/bcftools_snakemake` | - | [spashleyfu/bcftools_snakemake](https://hub.docker.com/repository/docker/spashleyfu/bcftools_snakemake) | 1.19 GB | |
| **verifyBamID2** | `spashleyfu/ubuntu20_snakemake:verifyBamID2` | - | [spashleyfu/ubuntu20_snakemake](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_snakemake) | 1.01 GB | |
| **LEASER TRACE (PCA)** | `spashleyfu/laser_trace_v2.04` | - | [spashleyfu/laser_trace_v2.04](https://hub.docker.com/repository/docker/spashleyfu/laser_trace_v2.04) | 492.42 MB | [LASER server](https://laser.sph.umich.edu/index.html#!) |
| **Triodenovo** | `spashleyfu/ubuntu20_triodenovo:0.0.4` | - | [spashleyfu/ubuntu20_triodenovo](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_triodenovo) | 174.39 MB | Triodenovo v0.0.4 |
| **Triodenovo** | `spashleyfu/ubuntu20_triodenovo:0.0.6` | - | [spashleyfu/ubuntu20_triodenovo](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_triodenovo) | 172.88 MB | Triodenovo v0.0.6 |
| **GLnexus** CLI | `atgenomix/glnexus_cli` | 500GB+ MEM | [atgenomix/glnexus_cli](https://hub.docker.com/r/atgenomix/glnexus_cli) | 107.51 MB | |
| **DeepVariant** | `google/deepvariant:latest` | - | [google/deepvariant](https://hub.docker.com/r/google/deepvariant) | 3.28 GB | Sep 16, 2021 latest version is v1.2.0 |
| **Globus** CLI | `spashleyfu/globus_cli_wustl:latest` | - | [spashleyfu/globus_cli_wustl](https://hub.docker.com/repository/docker/spashleyfu/globus_cli_wustl) | 260.74 MB | For Transfering files |
| Parabricks + Snakemake | `spashleyfu/parabricksv35_snakemake:latest` | 2 GPU with 256GB MEM | - | 7.05 GB | Parabricks v3.5.0.1 + Snakemake v6.6.0, For snakemake use only, Detail see [RIS doc](https://docs.ris.wustl.edu/doc/compute/recipes/tools/parabricks-quickstart.html) |

