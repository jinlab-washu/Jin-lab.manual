# In-depth Protocol for Joint-Calling WES with WashU compute0

Cromwell scripts Based on lek lab scripts found here: https://github.com/leklab/cromwell_wdl/tree/master/gatk4_multisample


*Protocol was written for use with WashU Genome Modeling System and optimized for WashU compute0 hpc*


### Prerequisites:
- lsf cluster capable of running docker and cromwell
- Merged gvcf for each sample produced with WashU genome modeling system
  - Scripts can be modified to use gvcf without analysis project
- bash launch script for compute0
- Genome Modeling System Analysis Project ID

### Links to Scripts:

## Protocol

1. Invoke the gms enviroment on compute0 if you have not already done so using ```gsub```

2. Check your builds to ensure there is only 1 build per sample that contains results

    - If you only have 1 build per sample, you will use the get_input_and_run_jointcall_exome_hg38.sh script to launch the Joint-Calling. This script automates the input gathering and launching of the main cromwell file. Use the script followed by the analysis project id given by the GMS system. 
    
        2a. Launch Joint-Call Genotyping with the following command.
        
        - ```/gscmnt/gc2698/jin810/bash_scripts/get_input_and_run_jointcall_exome_hg38.sh $ANALYS_PROJ_ID```
    
    - If you have more than 1 build per sample, you will need to gather the input first before launching joint-calling. 
    
        2b. Gather input with the following script: 
    
        - ```get_jointcall_input.sh $ANALYSIS_PROJ_ID```
        
        2c. Manually delete any builds that you would not like joint-called and ensure that each sample name is specific. 
        
        *If the same sample name is used more than once, you may get weird results. (THIS has not been tested)
        
        2d. Launch Joint-Call Genotyping with the following bash script:
        
         - ```run_jc_GATK4.1.7.0.sh $ANALYSIS_PROJ_ID```
  

## Input Files

#### Automated Input

  *Automated processing places the 3 files below in the working directory which is located at the "OUTPUT DIRECTORY" location listed above*
  
  - cromwell.conf (Cromwell configuration file)
    
  - gvcfs_hg38.list (sample list)
  
  - cromwell.options (Currently not in use)
  
  #### Hard-coded files
  
  *Files with paths that are hardcoded and NOT placed in the working directory listed below*
  
  - INPUT DIRECTORY: ```/gscmnt/gc2698/jin810/analysis-workflows/cromwell_wdl```
  
  - jointgt_GATK4_exome_hg38_inputs.json (Cromwell Inputs)
  
  - lek_joint_genotyping_jinlab_mod.wdl (Maint Cromwell file)


## Outputs

- OUTPUT DIRECTORY: ```/gscmnt/gc2698/jin810/jointcalling/$AnP```

- CROMWELL RESULTS FOR EACH CALL: ```/gscmnt/gc2698/jin810/jointcalling/$AnP/cromwell-executions/call-*```
  - where ```$AnP``` is the analysis project number given by the GMS system
  - where ```call-*``` is the specific call ran in the workflow
  
- bsub_exec.out (bsub job command line log)

- bsub_exec.err (bsub job command line error)


