# Docker

## Overview
Docker is a tool for delivering collections of software in a package called a container. It is useful for deploying applications requiring a complex web of dependencies. The compute clusters use it to avoid having to install potentially conflicting versions of software for different users' needs.

## Using an Interactive Container
For a short, quick workflows you can use the docker-interactive queue:

```
bsub -Is -q docker-interactive -a 'docker(mgibio/dna-alignment)' /bin/bash
```

This will download a Docker image for DNA alignment, run the image, and provide you with an interactive bash shell. The docker-interactive queue is only intended for light work and has limited resources.

For longer running and more resource intensive jobs you can use the research-hpc queue:

```
bsub -Is -q research-hpc -a 'docker(mgibio/dna-alignment)' /bin/bash
```

While doing your work it is possible (and likely) that the default resource allocation will not be enough. For example, indexing a human genome will require at least 64gb of memory, which is far more than the default. To get additional memory, in this case 75gb, you can do:

```
bsub -Is -q research-hpc -M 75000000 -R 'select[mem>75000] span[hosts=1] rusage[mem=75000]' -a 'docker(mgibio/dna-alignment)' /bin/bash
```
## Using a Non-interactive Container
Creating a bash script that uses a docker container is an easy way to use non-interactive containers for multiple samples.

In order to use a non-interactive container with the cluster (lsf) scheduler, bsub, you need to export a few variables within your script.

```
export LSF_DOCKER_VOLUMES="local_dir:dir_dest_in_image"
export LSF_DOCKER_NETWORK=host
export LSF_DOCKER_IPC=host
```
Replace 'local_dir' with the directory you would like to mount in the image followed by the destination of that directory within the docker containter.

For example, ```"/my_data/:/my_data/"``` will mount the local directory /my_data/ and any subsequent folders in that directory under the mounted directory /my_data/ in the docker image. You can mount mulitple local locations within the image. If you would like to mount multiple locations, there needs to be a space between the different mounts:```"/my_data/:/my_data/ my_scratch/:my_scratch/"``` all in cased in a single pair of double quotes.

Example script:
```
DIR=my_data/
export LSF_DOCKER_VOLUMES="local_dir:dir_dest_in_image"
export LSF_DOCKER_NETWORK=host
export LSF_DOCKER_IPC=host

bsub -o "$DIR"output.txt -e "$DIR"error.txt -R "rusage[mem=30000]" -q research-hpc -a 'docker(mgibio/dna-alignment)' [command here]
```
Above, an output file and error file are created in the specified DIR variable. A job is submitted to the research-hpc queue (intenive compute queue) with 30GB of memory ("rusage[mem=30000]") in which a command will be run with the docker image specified (-a application flag).


See here for more information: https://confluence.ris.wustl.edu/display/ITKB/WUIT+-+RIS+-+Compute+104. This page is for compute1, but the process is the same for compute0.


For more information on scripting and general hpc usage, check out the RIS training workshops in the confluence page below:
**You will need to be connected to the VNP to access.**
Location of the 4 training workshops: https://confluence.ris.wustl.edu/display/ITKB/Workshops+and+Training


Many other parameters can be adjusted as well; the complete documentation can be viewed in `bsub`'s manual page:

```
man bsub
```

## Recommended Images
[https://hub.docker.com/u/mgibio](https://hub.docker.com/u/mgibio)
