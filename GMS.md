## Introduction
The Genome Institute at Washington University has developed a high-throughput, fault-tolerant analysis information management system called the Genome Modeling System (GMS), capable of executing complex, interdependent, and automated genome analysis pipelines at a massive scale. The GMS framework provides detailed tracking of samples and data coupled with reliable and repeatable analysis pipelines.  The GMS code, installation instructions and usage tutorials are available at http://github.com/genome/gms.

Helpful Confluence links:
(must be connected to washU VPN to view these)

Overview of the GMS: https://confluence.ris.wustl.edu/pages/viewpage.action?pageId=3637349

Setting up gms environment: https://confluence.ris.wustl.edu/display/BIO/GMS+-+Docker+Image+-+gsub

## Set-up
You will need to modify your .bashrc file located in your home directory in order to invoke the 'gsub' command to access GMS. 
See here for more information https://confluence.ris.wustl.edu/display/BIO/GMS+-+Docker+Image+-+gsub

1. Edit your .bashrc file in your home directory. If you are not there now, type cd ~ into the command line. This will direct you to your home directory.
2. 
For users of the Genome Modeling System (GMS), the first thing you must do after logging in to a virtual-workstation (TODO: add link) at MGI is launch a docker container using the appropriate image.

There are currently two environments to choose from:

Legacy - This environment will allow the execution of the Genome Modeling Tools, commands that rely on the old lucid environment, ex. feature-lists, reference sequences, etc. as well as legacy model types, ex. ReferenceAlignment, SingleSampleGenotype, SomaticVariation, SomaticValidation, RnaSeq, ClinSeq, etc.
Modern - This environment supports both Workflow Execution Services (WES) Toil and Cromwell. The only currently supported model type is CwlPipeline. However, there are germline, somatic, RNA-seq and more pipelines to choose from soon.
