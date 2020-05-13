## Introduction
The Genome Institute at Washington University has developed a high-throughput, fault-tolerant analysis information management system called the Genome Modeling System (GMS), capable of executing complex, interdependent, and automated genome analysis pipelines at a massive scale. The GMS framework provides detailed tracking of samples and data coupled with reliable and repeatable analysis pipelines.  The GMS code, installation instructions and usage tutorials are available at http://github.com/genome/gms.

Helpful links:
(To access confluence pages, you must be connected to washU VPN)

 Overview of the GMS: https://confluence.ris.wustl.edu/pages/viewpage.action?pageId=3637349

 Setting up gms environment: https://confluence.ris.wustl.edu/display/BIO/GMS+-+Docker+Image+-+gsub

 Pipelines: https://confluence.ris.wustl.edu/display/BIO/GMS+-+CWL+Pipeline

 Importing Data: https://confluence.ris.wustl.edu/display/BIO/GMS+-+Imported+Instrument+Data

 A walk-through of setting up a somatic project (NOTE: skip the subject mapping steps for single-sample, germline):
 https://confluence.ris.wustl.edu/display/CI/CWL+Somatic+Pipeline+Walkthrough

 Github pipeline documentation is typically maintained on the github repo where we keep the code (CWL) for each pipeline,
 subworkflow and tool used: https://github.com/genome/analysis-workflows

 The wiki is the best place to start when looking for documentation on the CWL. Much of it is auto-generated, but there are 
 some pages for each pipeline that include process diagrams and high-level overviews:
 https://github.com/genome/analysis-workflows/wiki


## Set-up
You will need to modify your .bashrc file located in your home directory in order to invoke the 'gsub' command to access the GMS environment. 

See here for more information https://confluence.ris.wustl.edu/display/BIO/GMS+-+Docker+Image+-+gsub

1. Edit the .bashrc file located in your home directory. Your home directory is located at `/~`. 
Typing ```cd ~ ``` into the command line will take you directly to your home directory.
**Note: The .bashrc file is hidden so you wont be able to see it by typing ```ls```*

2. Edit the file using emacs/vim. ```emacs .bashrc``` 

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
Restart your ssh session and you should be good to go!

## Invoke GMS environment
To start the genome modeling system environment from which you can launch pipelines and run `genome` commands, enter `gsub` for the modern docker version or `gsub -l` for the legacy version. See below for more information.

For users of the Genome Modeling System (GMS), the first thing you must do after logging in to a virtual-workstation (TODO: add link) at MGI is launch a docker container using the appropriate image.

There are currently two environments to choose from:

Legacy - This environment will allow the execution of the Genome Modeling Tools, commands that rely on the old lucid environment, ex. feature-lists, reference sequences, etc. as well as legacy model types, ex. ReferenceAlignment, SingleSampleGenotype, SomaticVariation, SomaticValidation, RnaSeq, ClinSeq, etc.
Modern - This environment supports both Workflow Execution Services (WES) Toil and Cromwell. The only currently supported model type is CwlPipeline. However, there are germline, somatic, RNA-seq and more pipelines to choose from soon.

## Create and Run Analysis Workflow


