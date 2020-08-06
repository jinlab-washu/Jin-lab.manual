### Creating a Custom Processing Profile

The default profiles on the GMS have some hardcoded values, meaning they cannot be changed by your configuration file. If you want to make a custom pipeline not already in the GMS, you will need to create a custom processing profile. A custom processing profile specifies the analysis pipeline main workflow file, cwl files for that workflow, and parameters that you will be using.

We already have created a custom processing profile for joint-call genotyping of Whole-exome-sequencing data. See the Genome Modeling System Chapter of the Jin-lab manual.

#### If you need to create a new processing profile, see the steps below.

A fork of the analysis-workflows repository from the GMS/genome repository exisits on compute0 here: `/gscmnt/gc2698/jin810/analysis-workflows`

It is a good idea to create a new branch if you will be modifying cwl files within exisiting workflows. You can test these files out in the new branch before merging them back to our "GATK4" branch.

If you are adding new files, you can go ahead and add them to the GATK4 branch.

To ensure you are on the GATK4 branch, use the command `git checkout GATK4` while under `/gscmnt/gc2698/jin810/analysis-workflows`

If you need to clone the repository into a different location, use the command below: 

```
git clone https://github.com/jinlab-washu/analysis-workflows/tree/GATK4 for the jinlab specific branch

git clone https://github.com/genome/analysis-workflows for the master genome branch updated by the WashU MGIBio group
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
