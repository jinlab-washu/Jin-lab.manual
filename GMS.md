[Introduction](#introduction)

[Set-up](#set-up)

[Invoke GMS environment](#invoke-gms-environment)

[Create and Configure Analysis Workflow on External Data](#create-and-run-analysis-workflow-on-external-data)

[Importing External Data](#importing-external-data)

[Creating a Custom Processing Profile](#creating-a-custom-processing-profile)

[Running a Project](#running-a-project)

[Misc](#misc)

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

## Create and Configure Analysis Workflow on External Data

### High Level Overview
1. Create an analysis project
   - add env file specifying disk info
2. Import data
   - Create an individual, link them to a sample, link sample to library
   - Use instrument-data to import the library to the project
3. If needed, create a custom processing-profile and configuration
4. Release the project


### Project Setup

Start by invoking the 'modern' gms environment using `gsub` and creating an analysis project.

1. Create an anlalysis project:
```
genome analysis-project create --name "Name of Analysis Project Here" --environment prod-builder
```
2. Next add an .yml environment file to your analysis project. Make sure to replace DOCKERVERSIONHERE with the correct notation.

File format:

```
disk_group_models: "jin810_gms"
disk_group_alignments: "jin810_gms"
lsb_sub_additional: "docker(registry.gsc.wustl.edu/apipe-builder/genome_perl_environment:DOCKERVERSIONHERE)"
cwl_runner: cromwell
workflow_builder_backend: simple
```
Command:

```genome analysis-project add-environment-file "ANALYSIS_PROJ_NAME OR ANALYSIS_PROJ_ID" /gscmnt/gc2698/jin810/configuration_files/jinlab_environment_config.yaml```

**If using the modern gms docker image (most likely using this one), repalce DOCKERVERSIONHERE with compute0-24 or compute1-2.
If using the legacy gms docker image, replace the line with starting with 'lsb_sub_additional' with the line below:

`lsb_sub_additional: "docker(registry.gsc.wustl.edu/genome/genome_perl_environment)" `

3. Add the custom configuration file to the analysis-project. ***NOTE: THIS IS A NECESSARY STEP FOR EXTERNAL DATA***

Configuration files for specific workflows can be found here: ```/gscmnt/gc2698/jin810/configuration_files```

See the GATK4-cwl-wdl repository for more specific config files. https://github.com/jinlab-washu/GATK4-cwl-wdl

The default GATK4 pipeline to be produce files for downstream joint-calling:

```/gscmnt/gc2698/jin810/configuration_files/human_germline_exome_bp_gatk4.yml```

```genome analysis-project add-config-file --reprocess-existing ANALYSIS_PROJECT_ID /gscmnt/gc2698/jin810/configuration_files/human_germline_exome_bp.yml```

**This file enables the use of external data that is not in the same format as sequencing data produced internally at WashU. In addition, it changes the processing profile for the Whole-Exome-Sequencing alignment to our custom pipeline so that the emit_reference_confidence (ERC) variable is changed to "BP_RESOLUTION". ***IF YOU ARE NOT DOING WES-alignment,
the "region_of_interest_set_name: 'xGen Lockdown Exome Panel v1 capture set" line will need to be changed to reflect the regions you will be comparing against and for what type of analysis (WGS or RNA-seq). 

4. Disable the original configuration file (Optional).

Unless you are analyzing the data with mutliple configuration files (and thus different models), it is best to disable the configuration file you will no longer be using. See command below:
```
genome analysis-project disable-config-file --profile-item CONFIG_ID
```
Both configuration files will now show with the command:

```genome analysis-project view --fast PROJECT_ID```

The config files will be lableled based on their status.


### Importing External Data

First, you will need to create an individual:

```
genome individual create --taxon "human" 
```

To update an individual, e.g. changing their name:

```
genome individual update name --value=NAME --individual=ID
```

Where `NAME` is the name you would like to use and `ID` is the ID of the individual created previously.

Next, you will need to create samples:

```
genome sample create --description=DESC --name=NAME --source=INDIVIDUAL_ID
```

You can verify that the sample was linked correctly with:

```
genome sample list --filter individual.id=INDIVIDUAL_ID

or

genome sample list --filter individual.name=INDIVIDUAL_NAME
```

Next, you will will need to create libraries for each sample:

```
genome library create --sample=SAMPLE_NAME --name=LIBRARY_NAME
```

Finally, you can import your data:

```
genome instrument-data import trusted-data --analysis-project=PROJECT_NAME --import-source-name=SOURCE_NAME --library=LIBRARY_NAME --source-directory=PATH --import-format=FORMAT --read-count=COUNT
```

Specific Example:

``` genome instrument-data import trusted-data --analysis-project=chiari_GATK4_exome_test import-source-name=https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data_indexes/NA12878/sequence.index.NA12878_Illumina_HiSeq_Exome_Garvan_fastq_09252015 --library=NA12878-HG001-extlibs --source-directory=/gscmnt/gc2698/jin810/fastq/benchmark/NA12878 —import-format=fastq —read-count=20203002```

The read-count can be determined by running 

```
zcat reads.fastq.gz | wc -l
```

for each read, dividing the outputs by 4, and then summing.

The source-directory should only contain your read files. The import will copy all data in the source directory, even if there are unrelated files in the directory.

### Creating a Custom Processing Profile

Depending on your intended workflow, you may need to create a custom processing profile. The provided profile hardcodes some values, meaning they cannot be changed by your configuration file. 

First, you will need to clone MGI's analysis-workflows repository if it does not already exist:

```
git clone https://github.com/genome/analysis-workflows
```

Next, you will need to create a new processing profile:

```
genome processing-profile create cwl-pipeline --cwl-directory /gscmnt/gc2698/jin810/analysis-workflows/definitions --main-workflow-file pipelines/germline_exome.cwl --primary-docker-image "docker(registry.gsc.wustl.edu/apipe-builder/genome_perl_environment:20)" --name "Germline Exome with BP Resolution" --short-pipeline-name exomeBP
```

The `cwl-directory` is the path to the cloned analysis-workflows repository and `main-workflow-file` is the path within that directory to the workflow you want to run. You should not need to change `primary-docker-image`. Finally, select a `name` and `short-pipeline-name` for your new profile.

You can now make changes to the profile as needed. For example, if you need to select `BP_RESOLUTION` for generated GVCF files you will need to modify `process_inputs.pl`. If this file does not already exist you can copy it from another profile and make your modifications:

```
cat /gscmnt/gc2560/core/processing-profile/cwl-pipeline/a231384ea6724035b4c90fa50d890e7b/process_inputs.pl > process_inputs.pl
```

### Running a Project

When you are ready to run your project:

```
genome analysis-project release PROJECT_NAME
```

To view the status of your project:

```
genome analysis-project view --fast PROJECT_NAME
```
Or you can view the status of your project with a graphical interface by typing your analysis project ID into the search bar found here:

spectacle.gsc.wustl.edu/

If the build is successful, the results can be found within the model_data folder in the lab directory shown below:

```/gscmnt/gc2698/jin810/model_data/MODEL_ID/BUILD_ID/results```

For example:
```/gscmnt/gc2698/jin810/model_data/10a7507ab8ca46e09567439ddfcacac3/build4b6e86de7cd243599e6e500489d5b584/results```

### Output

It is important to QC the sequencing results to ensure there is enough coverage of your targets for quality analysis.

There will be HsMetrics files created for 2 different gene databases (ClinVAR and ACMG) with statistics per base (".base"),  per target (".target"), and a summary (".summary"). Right now, it is a good idea to check the ".target" HsMetrics files for both databases to ensure at least 90% of all targets have at least 10X coverage. This is a column in the file. 



There will be many files produced from the pipeline. 

Errors and standard output will be produced in the logs folder under your build id:
```/gscmnt/gc2698/jin810/model_data/MODEL_ID/BUILD_ID/logs```

### Intrepreting Results
Helpful links for intrepreting results:

VCF file: https://gatk.broadinstitute.org/hc/en-us/articles/360035531692-VCF-Variant-Call-Format

Picard Metrics: https://broadinstitute.github.io/picard/picard-metric-definitions.html

### Misc

#### Disable configurations you don't need:
```
genome analysis-project disable-config-file --profile-item CONFIG_ID
```
**Disabling vs Inactivating Config Files

The difference between disable and inactive: disabled means "remove all analysis generated by this, I don't need it" vs. inactive means "I still need the resulting data from previous models, but don't make any new models" -jw

Re-process instrument data with new configuration file:

```genome analysis-project add-config-file --reprocess PROJ_ID NEW_CONFIG_YAML_FILE```

#### Queue new builds for models

**This can happen when trying a new pipeline and the builds fail. See command below:

 ```genome model build queue --reason 'added process_inputs.pl' MODELID```

#### Show configuration file location

```genome analysis-project show-config <ANALYSIS_PROJ_NAME/ID>```

#### Show genome models for an analysis project

```genome model list --show=id --filter "analysis_project.id=$analysis_ID"```

#### Find instrument data ids with library names

```genome instrument-data list --filter  "library.name ~ <Part of library names, e.g. KCM>"```

~ : "like" operator

### Troubleshooting
If you cannot figure out why a pipeline is failing, shoot the MGIBIO analysis-workflows slack channel a message with the analysis project ID. They will be happy to help you out. 

