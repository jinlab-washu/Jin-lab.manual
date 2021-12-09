# Using Hail on WashU Compute1 server


### Basic usage:

You can follow the document to run Hail with Jupyter Notebook - [Using Hail with Jupyter Lab on Compute1](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/hail/Using_Hail_with_JupyterLab_on_Compute1.md).

If you want to use Hail on the basic purpose or to annotate VCF, please use `spashleyfu/hail_vep_gnomad`.

If you want to use newer version of Hail, please use `spashleyfu/hail_0.2.79:jupyterlab`.

For more detail, please see the section below. (You can find it in the table below)

### Docker collection

| Docker Images | Hail version | JAVA_HOME | Details |
| ------------- | ------------ | --------- | ------- |
| `spashleyfu/hail_vep_gnomad` | version 0.2.79-f141af259254 | `/usr/lib/jvm/java-8-openjdk-amd64/jre` | Image size: 5.34GB, with VEP104, [Details on Docker Hub](https://hub.docker.com/repository/docker/spashleyfu/hail_vep_gnomad) |
| `spashleyfu/hail_0.2.79:jupyterlab` | version 0.2.79-f141af259254 |  `/usr/lib/jvm/java-8-openjdk-amd64/jre` | Image size: 2.01GB, [Details on Docker Hub](https://hub.docker.com/repository/docker/spashleyfu/hail_0.2.79) |
| `spashleyfu/ubuntu20_pyspark:hail_gsuit` | version 0.2.61-3c86d3ba497a | `/opt/conda` | [go to detail section](#ubuntu20_pysparkhail_gsuit) |


| Docker | Hail | Java | Python | Conda/Pip | PySpark | VEP |
| ------ | ---- | ---- | ------ | --------- | ------- | --- |
| `spashleyfu/ubuntu20_pyspark:hail_gsuit` | version 0.2.61-3c86d3ba497a | openjdk version "1.8.0_282" | Python 3.7.10 | conda 4.10.3 | Apache Spark version 2.4.1 | - |
| `spashleyfu/hail_0.2.79:jupyterlab` | version 0.2.79-f141af259254 | openjdk version "1.8.0_282" | Python 3.8.10 | pip 20.0.2 | Apache Spark version 3.1.2 | - |
| `spashleyfu/hail_vep_gnomad` | version 0.2.79-f141af259254 | openjdk version "1.8.0_292" | Python 3.7.7 | conda 4.11.0, and pip 21.3.1 | Apache Spark version 3.1.2 | 104 |

---------------

## Detail:

### spashleyfu/hail_0.2.79:jupyterlab

> JAVA_HOME: "/usr/lib/jvm/java-8-openjdk-amd64/jre"
> 

| Docker | Hail | Java | Python | Conda/Pip | PySpark |
| ------ | ---- | ---- | ------ | --------- | ------- | 
| `spashleyfu/hail_0.2.79:jupyterlab` | version 0.2.79-f141af259254 | openjdk version "1.8.0_282" | Python 3.8.10 | pip 20.0.2 | Apache Spark version 3.1.2 |

1. If you want to use this Docker to sent out the jobs to run Hail, please include two more lines below:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
```

So, As an example, your bsub file will look like this:

```bash
#!/bin/bash

#BSUB -n 4
#BSUB -q general
#BSUB -G compute-jin810
#BSUB -J PROJECT_NAME
#BSUB -M 24GB
#BSUB -N
#BSUB -u WUSTL_KEY@wustl.edu
#BSUB -o out.txt
#BSUB -e err.txt
#BSUB -R 'rusage[mem=24GB] span[hosts=1]'
#BSUB -a 'docker(spashleyfu/hail_0.2.79:jupyterlab)'

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
/bin/sh the_hail_script_you_want_to_run.sh
```


**Docker Image detail:**

```
root@ d2f92a992e16:/# java -version
openjdk version "1.8.0_292"
OpenJDK Runtime Environment (build 1.8.0_292-8u292-b10-0ubuntu1~20.04-b10)
OpenJDK 64-Bit Server VM (build 25.292-b10, mixed mode)

root@ d2f92a992e16:/# python3 -V
Python 3.8.10

root@8505c8b10279:/# node -v
v16.13.1

root@8505c8b10279:/# npm -v
8.1.2

root@8505c8b10279:/# voila -V
0.3.0

root@8505c8b10279:/# jupyter --version
Selected Jupyter core packages...
IPython          : 7.30.1
ipykernel        : 6.6.0
ipywidgets       : 7.6.5
jupyter_client   : 7.1.0
jupyter_core     : 4.9.1
jupyter_server   : 1.13.1
jupyterlab       : 3.2.4
nbclient         : 0.5.9
nbconvert        : 6.3.0
nbformat         : 5.1.3
notebook         : 6.4.6
qtconsole        : not installed
traitlets        : 5.1.1

root@ d2f92a992e16:/# perl -version
This is perl 5, version 30, subversion 0 (v5.30.0) built for x86_64-linux-gnu-thread-multi
...

root@d2f92a992e16:/# pip -V
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)

root@d2f92a992e16:/# bzip2 -V
bzip2, a block-sorting file compressor.  Version 1.0.8, 13-Jul-2019.

root@d2f92a992e16:/# ipython
Python 3.8.10 (default, Sep 28 2021, 16:10:42) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.30.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pyspark, gnomad

In [2]: import hail as hl

In [3]: hl.init()
2021-12-09 19:21:34 WARN  NativeCodeLoader:60 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Running on Apache Spark version 3.1.2
SparkUI available at http://d2f92a992e16:4040
Welcome to
     __  __     <>__
    / /_/ /__  __/ /
   / __  / _ `/ / /
  /_/ /_/\_,_/_/_/   version 0.2.79-f141af259254

In [4]: gnomad.__file__ = '/usr/local/lib/python3.8/dist-packages/gnomad'

In [5]: from gnomad.resources.import_resources import get_module_importable_resources
           import gnomad.resources.grch37 as grch37

In [6]: get_module_importable_resources(grch37)
Out[6]: 
{'clinvar.20181028': ('clinvar.20181028',
  GnomadPublicTableResource(path=gs://gnomad-public-requester-pays/resources/grch37/clinvar/clinvar_20181028.vep.ht,import_args={'path': 'gs://gnomad-public-requester-pays/resources/grch37/clinvar/clinvar_20181028.vcf.bgz', 'force_bgz': True, 'skip_invalid_loci': True, 'min_partitions': 100, 'reference_genome': 'GRCh37'})),
...}
```

-------------------------------

### spashleyfu/hail_vep_gnomad

> JAVA_HOME: "/usr/lib/jvm/java-8-openjdk-amd64/jre"
> 

| Docker | Hail | Java | Python | Conda/Pip | PySpark | VEP |
| ------ | ---- | ---- | ------ | --------- | ------- | --- |
| `spashleyfu/hail_vep_gnomad` | version 0.2.79-f141af259254 | openjdk version "1.8.0_292" | Python 3.7.7 | conda 4.11.0, and pip 21.3.1 | Apache Spark version 3.1.2 | 104 |
| `spashleyfu/hail_vep_gnomad:0.2.79_104_0.6.0` | version 0.2.79-f141af259254 | openjdk version "1.8.0_292" | Python 3.7.7 | conda 4.11.0, and pip 21.3.1 | Apache Spark version 3.1.2 | 104 |

#### Notice:

1. If you want to use this Docker to sent out the jobs to run Hail, please include two more lines below:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
```

**Docker Image detail:**

```
(base) root@d6a5e54177fc:/# java -version
openjdk version "1.8.0_292"
OpenJDK Runtime Environment (build 1.8.0_292-8u292-b10-0ubuntu1~20.04-b10)
OpenJDK 64-Bit Server VM (build 25.292-b10, mixed mode)

(base) root@d6a5e54177fc:/# python -V
Python 3.7.7

(base) root@d6a5e54177fc:/# pip -V
pip 21.3.1 from /opt/conda/lib/python3.7/site-packages/pip (python 3.7)

(base) root@d6a5e54177fc:/# conda -V
conda 4.11.0

(base) root@d6a5e54177fc:/# vep
Possible precedence issue with control flow operator at /opt/conda/lib/site_perl/5.26.2/Bio/DB/IndexedBase.pm line 805.
#----------------------------------#
# ENSEMBL VARIANT EFFECT PREDICTOR #
#----------------------------------#

Versions:
  ensembl              : 104.1af1dce
  ensembl-funcgen      : 104.59ae779
  ensembl-io           : 104.1d3bb6e
  ensembl-variation    : 104.6154f8b
  ensembl-vep          : 104.3

(base) root@d6a5e54177fc:/# perl -version
This is perl 5, version 26, subversion 2 (v5.26.2) built for x86_64-linux-thread-multi

(base) root@d6a5e54177fc:/# jupyter --version
Selected Jupyter core packages...
IPython          : 7.30.1
ipykernel        : 6.6.0
ipywidgets       : 7.6.5
jupyter_client   : 7.1.0
jupyter_core     : 4.9.1
jupyter_server   : 1.13.0
jupyterlab       : 3.2.4
nbclient         : 0.5.9
nbconvert        : 6.3.0
nbformat         : 5.1.3
notebook         : 6.4.6
qtconsole        : not installed
traitlets        : 5.1.1

(base) root@d6a5e54177fc:/# bzip2 --help
bzip2, a block-sorting file compressor.  Version 1.0.8, 13-Jul-2019.

(base) root@d6a5e54177fc:/# ipython
Python 3.7.7 (default, May  7 2020, 21:25:33) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.30.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import gnomad

In [2]: import pyspark

In [3]: import hail

In [4]: hail.init()
2021-12-09 20:11:45 WARN  NativeCodeLoader:60 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Running on Apache Spark version 3.1.2
SparkUI available at http://d6a5e54177fc:4040
Welcome to
     __  __     <>__
    / /_/ /__  __/ /
   / __  / _ `/ / /
  /_/ /_/\_,_/_/_/   version 0.2.79-f141af259254
LOGGING: writing to /hail-20211209-2011-0.2.79-f141af259254.log

In [5]: from gnomad.resources.import_resources import get_module_importable_resources

In [6]: import gnomad.resources.grch37 as grch37

In [7]: get_module_importable_resources(grch37)
Out[7]: 
{'clinvar.20181028': ('clinvar.20181028',
  GnomadPublicTableResource(path=gs://gnomad-public-requester-pays/resources/grch37/clinvar/clinvar_20181028.vep.ht,import_args={'path': 'gs://gnomad-public-requester-pays/resources/grch37/clinvar/clinvar_20181028.vcf.bgz', 'force_bgz': True, 'skip_invalid_loci': True, 'min_partitions': 100, 'reference_genome': 'GRCh37'})),
...}
```

---------------------------------

### ubuntu20_pyspark:hail_gsuit

| Docker | Hail | Java | Python | Conda/Pip | PySpark |
| ------ | ---- | ---- | ------ | --------- | ------- | 
| `spashleyfu/ubuntu20_pyspark:hail_gsuit` | version 0.2.61-3c86d3ba497a | openjdk version "1.8.0_282" | Python 3.7.10 | conda 4.10.3 | Apache Spark version 2.4.1 |

#### Notice:

1. If you want to use this Docker to sent out the jobs to run Hail, please include two more lines below:

```bash
export JAVA_HOME=/opt/conda
```

So, As an example, your bsub file will look like this:

```bash
#!/bin/bash

#BSUB -n 4
#BSUB -q general
#BSUB -G compute-jin810
#BSUB -J PROJECT_NAME
#BSUB -M 24GB
#BSUB -N
#BSUB -u WUSTL_KEY@wustl.edu
#BSUB -o out.txt
#BSUB -e err.txt
#BSUB -R 'rusage[mem=24GB] span[hosts=1]'
#BSUB -a 'docker(spashleyfu/ubuntu20_pyspark:hail_gsuit)'

export JAVA_HOME=/opt/conda
/bin/sh the_hail_script_you_want_to_run.sh
```

**Docker Image detail:**

```
[fup@compute1-client-3 ~]$ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(spashleyfu/ubuntu20_pyspark:hail_gsuit)' /bin/bash

(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ echo $JAVA_HOME
/opt/conda

(base) fup@compute1-exec-135:~$ /opt/conda/bin/java -version
openjdk version "1.8.0_282"
OpenJDK Runtime Environment (Zulu 8.52.0.23-CA-linux64) (build 1.8.0_282-b08)
OpenJDK 64-Bit Server VM (Zulu 8.52.0.23-CA-linux64) (build 25.282-b08, mixed mode)

(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ python -V
Python 3.7.10

(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ conda -V
conda 4.10.3

(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ ipython
Python 3.7.10 (default, Jun  4 2021, 14:48:32) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.26.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pyspark

In [2]: import hail as hl

In [3]: hl.init()
2021-11-23 21:41:55 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
2021-11-23 21:41:55 WARN  Hail:37 - This Hail JAR was compiled for Spark 2.4.5, running with Spark 2.4.1.
  Compatibility is not guaranteed.
Running on Apache Spark version 2.4.1
SparkUI available at http://compute1-exec-135.ris.wustl.edu:4040
Welcome to
     __  __     <>__
    / /_/ /__  __/ /
   / __  / _ `/ / /
  /_/ /_/\_,_/_/_/   version 0.2.61-3c86d3ba497a
LOGGING: writing to /storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/hail-20211123-2141-0.2.61-3c86d3ba497a.log

```
