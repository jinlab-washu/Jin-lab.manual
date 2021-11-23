# Using Hail on WashU Compute1 server


### Basic usage:

You can follow the document to run Hail with Jupyter Notebook - [Using Hail with Jupyter Lab on Compute1](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/hail/Using_Hail_with_JupyterLab_on_Compute1.md).

If you want to use Hail on the basic purpose or to annotate VCF, please use `spashleyfu/ubuntu18_vep104:hail_gsutil`.

If you want to use newer version of Hail, please use `spashleyfu/hail_0.2.78:notebook_6.4.6`.

For more detail, please see the section below. (You can find it in the table below)

### Docker collection

| Docker Images | Hail version | JAVA_HOME | Details |
| ------------- | ------------ | --------- | ------- |
| `spashleyfu/ubuntu20_pyspark:hail_gsuit` | version 0.2.61-3c86d3ba497a | `/opt/conda` | [go to detail section](#ubuntu20_pysparkhail_gsuit) |
| **`spashleyfu/ubuntu18_vep104:hail_gsutil`** | version 0.2.61-3c86d3ba497a | `/opt/conda` | VEP, [go to detail section](#spashleyfuubuntu18_vep104hail_gsutil) |
| `spashleyfu/hail_0.2.78:notebook_6.4.6` | **version 0.2.78-b17627756568** |  `/usr/lib/jvm/java-8-openjdk-amd64/jre` | [go to detail section](#spashleyfuhail_0278notebook_646) |


| Docker | Hail | Java | Python | Conda/Pip | PySpark |
| ------ | ---- | ---- | ------ | --------- | ------- |
| `spashleyfu/ubuntu20_pyspark:hail_gsuit` | version 0.2.61-3c86d3ba497a | openjdk version "1.8.0_282" | Python 3.7.10 | conda 4.10.3 | Apache Spark version 2.4.1 |
| `spashleyfu/ubuntu18_vep104:hail_gsutil` | version 0.2.61-3c86d3ba497a | openjdk version "1.8.0_282" | Python 3.7.10 | conda 4.10.3 | Apache Spark version 2.4.0 |
| `spashleyfu/hail_0.2.78:notebook_6.4.6` | version 0.2.78-b17627756568 | openjdk version "1.8.0_292" | Python 3.6.9 | pip 9.0.1 | Apache Spark version 3.1.2 |

---------------

## Detail:

### spashleyfu/hail_0.2.78:notebook_6.4.6

> JAVA_HOME: "/usr/lib/jvm/java-8-openjdk-amd64/jre"
> 

| Docker | Hail | Java | Python | Conda/Pip | PySpark |
| ------ | ---- | ---- | ------ | --------- | ------- | 
| `spashleyfu/hail_0.2.78:notebook_6.4.6` | version 0.2.78-b17627756568 | openjdk version "1.8.0_292" | Python 3.6.9 | pip 9.0.1 | Apache Spark version 3.1.2 |

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
#BSUB -a 'docker(spashleyfu/hail_0.2.78:notebook_6.4.6)'

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
/bin/sh the_hail_script_you_want_to_run.sh
```


**Docker Image detail:**

```
// JAVA
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ java -version
openjdk version "1.8.0_292"
OpenJDK Runtime Environment (build 1.8.0_292-8u292-b10-0ubuntu1~18.04-b10)
OpenJDK 64-Bit Server VM (build 25.292-b10, mixed mode)

fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ echo $JAVA_HOME #<-- which is the wrong one!!!
/opt/ibm/jre
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ which java
/usr/bin/java
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ ls -lh /usr/bin/java
lrwxrwxrwx. 1 root root 22 Nov 19 17:23 /usr/bin/java -> /etc/alternatives/java
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ ls -lh /etc/alternatives/java
lrwxrwxrwx. 1 root root 46 Nov 19 17:23 /etc/alternatives/java -> /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ ls -lh /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
-rwxr-xr-x. 1 root root 6.2K Apr 21  2021 /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java

// Python
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ python -V
bash: python: command not found
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ python3 -V
Python 3.6.9

// pip or conda
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ conda -V
bash: conda: command not found
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ pip -V
bash: pip: command not found
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ pip3 -V
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)

// Hail
fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre"

fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ ipython
Python 3.6.9 (default, Jan 26 2021, 15:33:00) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.16.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pyspark

In [2]: import hail

In [3]: hail.init()
2021-11-23 22:14:37 WARN  NativeCodeLoader:60 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
2021-11-23 22:14:37 WARN  Hail:43 - This Hail JAR was compiled for Spark 3.1.1, running with Spark 3.1.2.
  Compatibility is not guaranteed.
Running on Apache Spark version 3.1.2
SparkUI available at http://compute1-exec-135.ris.wustl.edu:4040
Welcome to
     __  __     <>__
    / /_/ /__  __/ /
   / __  / _ `/ / /
  /_/ /_/\_,_/_/_/   version 0.2.78-b17627756568
LOGGING: writing to /storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/hail-20211123-2214-0.2.78-b17627756568.log

```

-------------------------------

### spashleyfu/ubuntu18_vep104:hail_gsutil

> JAVA_HOME: "/opt/conda"
> 

| Docker | Hail | Java | Python | Conda/Pip | PySpark | VEP |
| ------ | ---- | ---- | ------ | --------- | ------- | --- |
| `spashleyfu/ubuntu18_vep104:hail_gsutil` | version 0.2.61-3c86d3ba497a | openjdk version "1.8.0_282" | Python 3.7.10 | conda 4.10.3 | Apache Spark version 2.4.0 | v104 |

#### Notice:

1. If you want to use this Docker to sent out the jobs to run Hail, please include two more lines below:

```
export JAVA_HOME=/opt/conda
```

**Docker Image detail:**

```
[fup@compute1-client-3 Neuropathy_WGS_2021May]$ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(spashleyfu/ubuntu18_vep104:hail_gsutil)' /bin/bash

// Java
(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ echo $JAVA_HOME
/opt/conda

(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ java -version
openjdk version "1.8.0_282"
OpenJDK Runtime Environment (Zulu 8.52.0.23-CA-linux64) (build 1.8.0_282-b08)
OpenJDK 64-Bit Server VM (Zulu 8.52.0.23-CA-linux64) (build 25.282-b08, mixed mode)

// Python
(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ python -V
Python 3.7.10
(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ python3 -V
Python 3.7.10

// Conda
(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ conda -V
conda 4.10.3

// Hail:
(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ ipython
Python 3.7.10 (default, Jun  4 2021, 14:48:32) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.26.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pyspark

In [2]: import hail as hl

In [3]: hl.init()
2021-11-23 21:58:22 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
2021-11-23 21:58:24 WARN  Hail:37 - This Hail JAR was compiled for Spark 2.4.5, running with Spark 2.4.0.
  Compatibility is not guaranteed.
Running on Apache Spark version 2.4.0
SparkUI available at http://compute1-exec-135.ris.wustl.edu:4040
Welcome to
     __  __     <>__
    / /_/ /__  __/ /
   / __  / _ `/ / /
  /_/ /_/\_,_/_/_/   version 0.2.61-3c86d3ba497a
LOGGING: writing to /storage1/fs1/jin810/Active/Neuropathy_WGS_2021May/hail-20211123-2158-0.2.61-3c86d3ba497a.log


// VEP:
(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ /opt/vep/src/ensembl-vep/vep
#----------------------------------#
# ENSEMBL VARIANT EFFECT PREDICTOR #
#----------------------------------#

Versions:
  ensembl              : 104.1af1dce
  ensembl-funcgen      : 104.59ae779
  ensembl-io           : 104.1d3bb6e
  ensembl-variation    : 104.6154f8b
  ensembl-vep          : 104.3
...

vep@696b8b0c09fd:~/src/ensembl-vep$ ./vep
#----------------------------------#
# ENSEMBL VARIANT EFFECT PREDICTOR #
#----------------------------------#

Versions:
  ensembl              : 104.1af1dce
  ensembl-funcgen      : 104.59ae779
  ensembl-io           : 104.1d3bb6e
  ensembl-variation    : 104.6154f8b
  ensembl-vep          : 104.3
...

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
