## Introduction
We will be using WashU's Genome Modeling System (GMS) to run whole pipelines and parts of pipelines for sequencing analysis. This system has a steep learning curve. It is good to be familiar with this system as it is used as an integral part in our Whole Exome Sequencing analysis pipeline.

For an overview of the GMS, see here: https://confluence.ris.wustl.edu/pages/viewpage.action?pageId=3637349

**Note: Any link that has confluence in the name, can only be accessed if you are connected to the WashU VPN**

## Set-up
Right now, there are two clusters at Washu that are used for sequencing analysis. The legacy cluster, compute0 , and the new cluster, compute1. Everything on compute0 is slowly being moved to compute1 so that compute0 can be discontinued in a few years.

1. Log into compute0 using ssh.

    Compute 0 has 4 "workstations" you can log into. Below we will use virtual-workstation 1 or "vw1".
  
    ```ssh $wustl_ID@vw1.gsc.wustl.edu``` where ```$wustl_ID``` is your personal wustl ID. 
  
    **NOTE: The password for compute0 uses an MGI account password instead of the normal one you created at the time of setting up your ID. If you don't have an MGI account, you will need to have one created.** 

2. Modify your .bashrc file in order to access the GMS environment.
  
    Edit the .bashrc file located in your home directory. Your home directory is located at `/~`. 
  
    Typing ```cd ~ ``` into the command line will take you directly to your home directory.
  
    **Note: The .bashrc file is hidden. To see it in your home directory, you can use the command: ```ls -a```*

3. Edit the file using emacs/vim. ```emacs .bashrc``` 

    **Nano is not installed  on the default command line in compute0*

    Once you are in the file, delete the information listed below:
    ```
    # source global definitions
     if [ -f /etc/bashrc ]; then             # redhat
         . /etc/bashrc
     elif [ -f /etc/bash.bashrc ]; then # debian
         . /etc/bash.bashrc
     fi

     # source the gapp bashrc
     if [ -f /gapp/noarch/share/login/gapp.bashrc ]; then
         . /gapp/noarch/share/login/gapp.bashrc
     fi

    # source the gapp profile
     if [ -f /gapp/noarch/share/login/gapp.profile ]; then
         . /gapp/noarch/share/login/gapp.profile
     fi
     ```
    Once deleted, add the following to the top lines of the file:

    ```
    PATH=$PATH:/gscmnt/gc2560/core/env/v1/bin
    source /gscmnt/gc2560/core/env/v1/bashrc
    ```
4. Reload your `.bashrc` file using: `source ~/.bashrc`

5. Test your access to the GMS environemnt
  
    On compute0, use the command: ```gsub```
    
    On compute1, use the command: `gsub -G compute-jin810` 
    
If you are having trouble, see here for more infromation: https://confluence.ris.wustl.edu/display/BIO/GMS+-+Docker+Image+-+gsub

## See here for more information
To start the genome modeling system environment from which you can launch pipelines and run `genome` commands, enter `gsub` for the modern docker version or `gsub -l` for the legacy version. See below for more information. On compute1 you will need to use `gsub -G compute-jin810` in order to have access to our lab space.

For users of the Genome Modeling System (GMS), the first thing you must do after logging in to a virtual-workstation (TODO: add link) at MGI is launch a docker container using the appropriate image.

There are currently two environments to choose from:

Legacy - This environment will allow the execution of the Genome Modeling Tools, commands that rely on the old lucid environment, ex. feature-lists, reference sequences, etc. as well as legacy model types, ex. ReferenceAlignment, SingleSampleGenotype, SomaticVariation, SomaticValidation, RnaSeq, ClinSeq, etc.

Modern - This environment supports both Workflow Execution Services (WES) Toil and Cromwell. The only currently supported model type is CwlPipeline. However, there are germline, somatic, RNA-seq and more pipelines to choose from soon.
