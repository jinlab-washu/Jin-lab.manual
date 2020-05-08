# Docker

## Overview
Docker is a tool for delivering collections of software in a package called a container. It is useful for deploying applications requiring a complex web of dependencies. The compute clusters use it to avoid having to install potentially conflicting versions of software for different users' needs.

## Using a Container
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

Many other parameters can be adjusted as well; the complete documentation can be viewed in `bsub`'s manual page:

```
man bsub
```

## Recommended Images
[https://hub.docker.com/u/mgibio](https://hub.docker.com/u/mgibio)
