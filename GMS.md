## Create and Configure Analysis Workflow on External Data

### High Level Overview
1. Create an analysis project-[Project Setup on compute0 (MGI Legacy)](#project-setup-on-compute0-mgi-legacy)
   - add env file specifying disk info
2. Import data-[Importing External Data](#importing-external-data)
   - Create an individual, link them to a sample, link sample to library
   - Use instrument-data to import the library to the project
3. If needed, create a custom processing-profile and configuration-[Creating a Custom Processing Profile](#creating-a-custom-processing-profile)
4. Release the project-[Running a Project](#running-a-project)

### Project Setup on compute0 (MGI Legacy)

Start by invoking the 'modern' gms environment using `gsub` and creating an analysis project.

1. Create an analysis project:

    *Below we are using the --no-config parameter. We have our own lab specific configuration files we will add to the analyis project instead of choosing defaults provided in the gms system.

    #### Using Througly Tested pipeline
    
    1b. If you are using a pipeline that has been throughly tested or is known to run successfully,
    
     ```
     genome analysis-project create --name "Name of Analysis Project Here" --environment prod-builder --no-config
     ```

    #### Pipeline Testing

    1a. If you are testing a new pipeline, it is best to use the ad-hoc environment instead of the prod-builder. This enables more control over the builds (read-write permissions and start/stop builds) and the data that is produced by the experimental pipeline. See below.

     ```
     genome analysis-project create --name "Name of Analysis Project Here" --environment ad-hoc --no-config
     ```
     
2. Check for Environment file .yml file
    
    #### prod-builder environment (default)
    
    2a. If you are using the prod-builder environment, use the jin-lab environment file below:
    
    /gscmnt/gc2698/jin810/analysis-workflows/configuration_files/jinlab_environment_config_prod-builder.yaml

    The file contains the text below

    ```
    disk_group_models: "jin810_gms"
    disk_group_alignments: "jin810_gms"
    lsb_sub_additional: "docker(registry.gsc.wustl.edu/apipe-builder/genome_perl_environment:compute0-24)"
    cwl_runner: cromwell
    workflow_builder_backend: simple
    ```
    #### Ad-hoc environment (for pipeline testing)
    
    2b. If you set up your analysis project to use the ad-hoc environment, use the ad-hoc jin-lab environment file below: 
    
    /gscmnt/gc2698/jin810/analysis-workflows/configuration_files/jinlab_environment_config_user_specfic.yaml
   
    The file contains the text below
        
    ```
     disk_group_models: "jin810_gms"
     disk_group_alignments: "jin810_gms"
     disk_group_scratch: "jin810_gms"
     lsb_sub_additional: "docker(registry.gsc.wustl.edu/apipe-builder/genome_perl_environment:compute0-24)"
     cwl_runner: cromwell
     workflow_builder_backend: simple
     cromwell_server: "hsqldb:tmp"
    ```
    
  Universal Command for either environment chosen:

   ```genome analysis-project add-environment-file "ANALYSIS_PROJ_NAME OR ANALYSIS_PROJ_ID" /gscmnt/gc2698/jin810/configuration_files/$ENV_FILE```

   Where $ENV_FILE is the file based on the environment you chose in step 1 during the analysis-project creation

   *compute1-2 can be used instead of compute0-24 as well if you are using the modern gms image.*

   If using the legacy gms docker image, replace the line with starting with 'lsb_sub_additional' with the line below:

   ```lsb_sub_additional: "docker(registry.gsc.wustl.edu/genome/genome_perl_environment)" ```

3. Add the custom configuration file to the analysis-project. ***NOTE: THIS IS A NECESSARY STEP FOR EXTERNAL DATA***

   Configuration files for specific workflows can be found here: ```/gscmnt/gc2698/jin810/analysis-workflows/configuration_files```

   See the analysis-workflows repo for more specific config files. https://github.com/jinlab-washu/analysis-workflows/configuration_files

   The default GATK4 pipeline to be produce files for downstream joint-calling:

   ```/gscmnt/gc2698/jin810/analysis-workflows/configuration_files/human_germline_exome_bp_gatk4.yml```
   
   Command to add configuration file:
   
   ```
   genome analysis-project add-config-file ANALYSIS_PROJECT_ID /gscmnt/gc2698/jin810/analysis-workflows/configuration_files/human_germline_exome_bp_gatk4.yml
   ```
   
   *IF you are changing the configuration of an analysis project that has already run, use the command below to reprocess the fastq files*
   
    ```
    genome analysis-project add-config-file --reprocess-existing ANALYSIS_PROJECT_ID /gscmnt/gc2698/jin810/analysis-workflows/configuration_files/human_germline_exome_bp_gatk4.yml
    ```

   **This file enables the use of external data that is not in the same format as sequencing data produced internally at WashU. In addition, it changes the processing profile for the Whole-Exome-Sequencing alignment to our custom pipeline so that the emit_reference_confidence (ERC) variable is changed to "BP_RESOLUTION".**
   
   *IF YOU ARE NOT DOING WES-alignment, the "region_of_interest_set_name: xGen Lockdown Exome Panel v1 capture set" line will need to be changed to reflect the regions you will be comparing against and for what type of analysis (WGS or RNA-seq).*

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
genome individual create --taxon "human" --name=$NAME
```

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
***IF YOU HAVE MORE THAN 2 FASTQ.GZ Files, you will need to consolidate them into two final fastq.gz files. GMS looks for 2 fastq files, forward (R1) and Reverse (R2). If you ingest more, your pipeline will fail!!!***

```cat *R1* > Sample_HG001_all_R1.fastq.gz``` and ```cat *R2* > Sample_HG001_all_R2.fastq.gz```

Finally, you can import your data:

```
genome instrument-data import trusted-data --analysis-project=PROJECT_NAME --import-source-name=SOURCE_NAME --library=LIBRARY_NAME --source-directory=PATH --import-format=FORMAT --read-count=COUNT
```

Specific Example:

```
genome instrument-data import trusted-data --analysis-project=chiari_GATK4_exome_test import-source-name=https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data_indexes/NA12878/sequence.index.NA12878_Illumina_HiSeq_Exome_Garvan_fastq_09252015 --library=NA12878-HG001-extlibs --source-directory=/gscmnt/gc2698/jin810/fastq/benchmark/NA12878 —import-format=fastq —read-count=20203002
```

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

### Troubleshooting
If you cannot figure out why a pipeline is failing, shoot the MGIBIO analysis-workflows slack channel a message with the analysis project ID. They will be happy to help you out. 

