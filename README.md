# 
## Table of Contents
**Getting Started in the Lab**
  * [Git Account Creation and Basics](./getting_started/Git.md "Git")
  * [Computation Environments](./getting_started/computation_environments.md)
  * [Log Into Compute Clusters (SSH)](./getting_started/SSH.md "Logging In (SSH)")
  * [Set up GMS Environment](./getting_started/gms_set_up.md)
  * [Set up Ruddle .bashrc File](./getting_started/set_up_ruddle_bashrc.md)
  * [Running your first whole exome sequencing](./getting_started/first_exome_run.md)

**Transferring Files**
  * [Globus](./transferring_files/Globus.md "Globus")
    * Large File Transfers from compute0 to compute1 or compute0/1 to external clusters
  * [SCP](./transferring_files/SCP.md "SCP")
    * Command line file transfers from local computer to compute0/1
  * [Box-lftp](./transferring_files/box_lftp.md)
    * Command line file transfers from wustl BOX to compute0/1
  * [rclone](./transferring_files/rclone.md)
    * Command line file transfers from google Drive to computing cluster

**Software**
  * [Docker](./tools/Docker.md "Docker")
    * Washu Compute clusters use Docker containers that come pre-installed with all the necessary packages for analysis instead of downloading individual programs to the cluster

**Quality Control Analyses**
  * [PCA Analysis using LASER](./quality_control_analyses/pca_analysis_w_trace.md)
  * [Kinship, Relatedness, and Sex-Check using Hail](https://github.com/jinlab-washu/Yale.CMG.workflows/blob/master/qc_analyses.md)
  * [Kinship, Relatedness, and Sex-Check using PLINK](./quality_control_analyses/plink_analysis.md)
  * [Coverage Metrics with statsmergev2](./quality_control_analyses/statsmerge_v2.md)

**Sequencing Analysis Protocols (Upstream Processing)**  
  * [Whole Exome Sequencing with alignment to hg38 - Compute0](./seq_analysis_protocols/whole_exome_compute0.md)
  * [Whole Exome Sequencing Processing - Ruddle](./seq_analysis_protocols/ruddle_exome.md)
  * [Joint-Call Genotyping - Ruddle](./seq_analysis_protocols/joint_call_genotyping_ruddle.md)

**Downstream Variant Analysis**
  * [Variant Visualization using Plot Reads](./downstream_variant_analysis/plot_reads.md)
  * [Annotate Variants using Hail](https://github.com/jinlab-washu/Yale.CMG.workflows/blob/master/hail_pipeline/generate_mt_generic.md)  
  * [Annotate Variants Using Annovar](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/downstream_variant_analysis/AnnotateVariantsUsingAnnovar.md)

**Statistical Tests**
  * [Case Control using GNOMAD](./stat_tests/case_control_GNOMAD)  

**Genome Modeling System**
  * [Create and Configure a New Analysis Project](./Genome_Modeling_System/create_analysis_project_GMS.md)
  * [Import of External Data - Automated]
  * [Import External Data - Manual](./Genome_Modeling_System/import_external_data_manually.md)
  * [Import Instrument Data from Lims system](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/Genome_Modeling_System/import_instrument_data_from_lims_system.md)
  * [Add Instrument Data to Analysis Project]
  * [Create Custom Processing Profile](./Genome_Modeling_System/custom_processing_profile.md)
  * [Helpful Commands](./Genome_Modeling_System/gms_commands.md)
  * [Helpful Information](./Genome_Modeling_System/gms_info.md)
  * [Deleting Analysis Projects and Associated Model Data](./Genome_Modeling_System/delete_model_data.md)

**Yale Ruddle HPC**
  * [Conda](./yale_ruddle/conda.md)
  * [Install Hail on Ruddle](./yale_ruddle/Hail_Installation.md)

**Hail**
  * [Examples](./hail/examples)
  * [Hail Workflows Repo](https://github.com/jinlab-washu/Yale.CMG.workflows)

**Other Protocols**
  * [Benchmarking](./other_protocols/benchmarking_WES.md)
  * [Benchmarking Parabricks WGS pipeline](./other_protocols/benchmarking_WGS_Parabricks_Germline_pipeline.md)
  * [Custom Intervals File Creation](./other_protocols/custom-interval-creation.md)
