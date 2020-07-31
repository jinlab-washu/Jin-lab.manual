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
