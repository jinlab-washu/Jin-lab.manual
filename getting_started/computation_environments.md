# Computation Environments Used in the Jinlab
8/6/2020

For genomics analysis, you will be using three main high performance computing clusters. Compute0 and Compute1 at WashU and the Ruddle hpc at Yale University.

## WashU Compute0 and Compute1
The main difference between Compute0 and Compute1 is Compute0 is the "MGI" legacy server. It is being phased out in favor of moving to the newer Compute1 cluster.
Genomics and sequencing analysis has mainly been used on Compute0 with a system called the Genome Modeling System (GMS). 
They are working on moving the GMS to Compute1, however; it is very much in a testing phase. 
Several features of the GMS including our custom analysis pipelines do not work on Compute1. 
You will be using a mix of the two until the kinks have been fully worked out on Compute1.

### Important Features shared between Compute0 and Compute1:

- Docker is used to containerize program and tool versions. You will not be downloading and installing programs to the cluster in the traditional way. 
- Interactive or Non-Interactive jobs are submitted to the cluster with a docker image.
- GMS has its own storage system that imports your data on either cluster.

### Differences between Compute0 and Compute1
- Compute0 storage for jinlab is /gscmnt/gc2698/jin810
- Syntax for submitting jobs is slighlty different between each cluster

Note: Compute0 and Compute1 are slightly different and some commands will have to be slightly changed when using one or the other.

For Ruddle,
