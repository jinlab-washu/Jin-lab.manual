# 
## Table of Contents
**Getting Started in the Lab**
  * [Git Account Creation and Basics](./getting_started/Git.md "Git")
  * [Computation Environments](./getting_started/computation_environments.md)
  * [Log Into Compute Clusters (SSH)](./getting_started/SSH.md "Logging In (SSH)")
  * [Set up GMS Environment](./getting_started/gms_set_up.md)
  * [Set up Ruddle .bashrc File](./getting_started/set_up_ruddle_bashrc.md)

**Transferring Files**
* [Globus](./transferring_files/Globus.md "Globus")
  * Large File Transfers from compute0 to compute1 or compute0/1 to external clusters
* [SCP](./transferring_files/SCP.md "SCP")
  * Command line file transfers from local computer to compute0/1
* [Box-lftp](./transferring_files/box_lftp.md)
  * Command line file transfers from wustl BOX to compute0/1
* [rclone](./transferring_files/rclone.md)
  * Command line file transfers from google Drive to computing cluster

**Tools**
  * [Docker](./tools/Docker.md "Docker")
    * Washu Compute clusters use Docker containers that pre-installed with all the necessary packages for analysis instead of downloading individual programs to the cluster
    
**Sequencing Analysis Protocols***  
  * [PCA Analysis using LASER](./seq_analysis_protocols/pca_analysis_w_trace.md)
  * [Whole Exome Sequencing with alignment to hg38] (C0)
  * [Whole Exome Sequencing Processing (R)](./seq_analysis_protocols/ruddle_exome.md)
    
**HPC specific protocols denoted with a C0 for WashU-Compute0, C1 for WashU-Comptue1, or R for Ruddle*
    
**Genome Modeling System**
  * [Create and Configure a New Analysis Project](./Genome_Modeling_System/create_analysis_project_GMS.md)
  * [Import of External Data - Automated]
  * [Import External Data - Manual](./Genome_Modeling_System/import_external_data_manually.md)
  * [Import Instrument Data from Lims system](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/Genome_Modeling_System/import_instrument_data_from_lims_system.md)
  * [Add Instrument Data to Analysis Project]
  * [Create Custom Processing Profile](./Genome_Modeling_System/custom_processing_profile.md)
  * [Helpful Commands](./Genome_Modeling_System/gms_commands.md)
  * [Helpful Information](./Genome_Modeling_System/gms_info.md)

**Yale Ruddle HPC**
  * [Set Up .bashrc for RMS Script Execution (Start Here)]
  * [Convert BAM/CRAM to FASTQ]
  * [Install Hail on Ruddle](./yale_ruddle/Hail_Installation.md)

**Hail**
  * [Examples](./hail/examples)
