# The Docker Image collection for Compute1

It's the Docker Images I used for my projects. Feel free to add more information on it.

| Docker Images | Required Resources | Main tools | dockerhub | Image size | Detail/Note |
| ------------- | ------------------ | ---------- | --------- | ---------- | ----------- |
| `us.gcr.io/ris-appeng-shared-dev/parabricks:v3.5.0.1` | [RIS doc](https://docs.ris.wustl.edu/doc/compute/recipes/tools/parabricks-quickstart.html) | Parabricks v3.5 | - | 3.78 GB | Official Image |
| `broadinstitute/gatk:latest` | 16GB MEM | GATK 4.x and Picard | [broadinstitute/gatk](https://hub.docker.com/r/broadinstitute/gatk/) | 1.64 GB | Sep 16, 2021 latest version is v4.2.2.0 
| `spashleyfu/plotreads` | 16GB MEM | plotRead with Python 2.7 && conda 4.8.4 && samtools 1.11 | [spashleyfu/plotreads](https://hub.docker.com/repository/docker/spashleyfu/plotreads) | 1.02 GB | |
| `sam16711/bam_metrics:v1` | - | Knight's bamMetrics with Python 2.7 | [sam16711/bam_metrics](https://hub.docker.com/r/sam16711/bam_metrics) | 113.43 MB | Suit for run bamMetrics alone |
| `spashleyfu/knight_bam_metrics:py38_pandas` | - | Knight's bamMetrics with Python 3.8 and Pandas | [spashleyfu/knight_bam_metrics](https://hub.docker.com/repository/docker/spashleyfu/knight_bam_metrics) | 229.49 MB | Suit for running [mergeBamMetrics.py](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/quality_control_analyses/create_bamMetrics.md#mergebammetricspy) |
| `spashleyfu/ubuntu20_snakemake:plink` | - | PLINK 1.9 with Sankemake | [spashleyfu/ubuntu20_snakemake](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_snakemake) | 991.89 MB | |
| `docker pull spashleyfu/ubuntu20_snakemake:plink2` | - | PLINK 2.0 with Sankemake | [spashleyfu/ubuntu20_snakemake](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_snakemake) | 1014.88 MB | |
| `spashleyfu/parabricksv35_snakemake:latest` | [RIS doc](https://docs.ris.wustl.edu/doc/compute/recipes/tools/parabricks-quickstart.html) | Parabricks v3.5 + Snakemake | [spashleyfu/parabricksv35_snakemake](https://hub.docker.com/repository/docker/spashleyfu/parabricksv35_snakemake) | 7.05 GB | For snakemake use only |
| `spashleyfu/ubuntu20_snakemake:samtools` | - | samtools with Sankemake | [spashleyfu/ubuntu20_snakemake](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_snakemake) | 989.26 MB | |
| `biocontainers/samtools:v1.9-4-deb_cv1` | - | samtools v1.9 | [biocontainers/samtools](https://hub.docker.com/r/biocontainers/samtools) | 244.41 MB | |
| `spashleyfu/bcftools_snakemake` | - | bcftools 1.12 with Sankemake | [spashleyfu/bcftools_snakemake](https://hub.docker.com/repository/docker/spashleyfu/bcftools_snakemake) | 928.23 MB | |
| `spashleyfu/ubuntu20_snakemake:verifyBamID` | - | verifyBamID | [spashleyfu/ubuntu20_snakemake](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_snakemake) | 1.19 GB | |
| `spashleyfu/ubuntu20_snakemake:verifyBamID2` | - | verifyBamID2 | [spashleyfu/ubuntu20_snakemake](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_snakemake) | 1.01 GB | |
| `spashleyfu/ubuntu20_triodenovo:0.0.4` | - | Triodenovo v0.0.4 | [spashleyfu/ubuntu20_triodenovo](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_triodenovo) | 174.39 MB | |
| `spashleyfu/ubuntu20_triodenovo:0.0.6` | - | Triodenovo v0.0.6 | [spashleyfu/ubuntu20_triodenovo](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_triodenovo) | 172.88 MB | |
| `atgenomix/glnexus_cli` | - | GLnexus CLI | [atgenomix/glnexus_cli](https://hub.docker.com/r/atgenomix/glnexus_cli) | 107.51 MB | |
| `spashleyfu/ubuntu18_vep104:hail_gsutil` | 32 CPU with 128GB MEM | Hail with VEP and JupyterLab, bgzip | [spashleyfu/ubuntu18_vep104](https://hub.docker.com/repository/docker/spashleyfu/ubuntu18_vep104) | 1.93 GB | |
| `spashleyfu/ubuntu20_snakemake:bamMetrics` | - | Snakemake v6.6.0 with Knight's bamMetrics | [spashleyfu/ubuntu20_snakemake](https://hub.docker.com/repository/docker/spashleyfu/ubuntu20_snakemake) | 1.18 GB | |
| `spashleyfu/globus_cli_wustl:latest` | - | Globus CLI | https://hub.docker.com/repository/docker/spashleyfu/globus_cli_wustl | 260.74 MB | For Transfering files |
| `google/deepvariant:latest` | ? | DeepVariant v1.2.0 | [google/deepvariant](https://hub.docker.com/r/google/deepvariant) | 3.28 GB | Sep 16, 2021 latest version is v1.2.0 |
