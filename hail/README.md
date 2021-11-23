# Using Hail on WashU Compute1 server


### Basic usage:

You can follow the document to run Hail with Jupyter Notebook - [Using Hail with Jupyter Lab on Compute1](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/hail/Using_Hail_with_JupyterLab_on_Compute1.md).

### Docker collection

| Docker Images | Hail version | JAVA_HOME | Details |
| ------------- | ------------ | --------- | ------- |
| `spashleyfu/ubuntu20_pyspark:hail_gsuit` |  | `/opt/conda` | [go to detail section](#ubuntu20_pysparkhail_gsuit) |
| `spashleyfu/ubuntu18_vep104:hail_gsutil` |  | `/opt/conda` |  |
| `spashleyfu/hail_0.2.78:notebook_6.4.6` |  |  |  |



### 

```



```

### spashleyfu/ubuntu18_vep104:hail_gsutil

| Docker | Hail | Java | Python | Conda/Pip | PySpark | VEP |
| ------ | ---- | ---- | ------ | --------- | ------- | --- |
| `spashleyfu/ubuntu18_vep104:hail_gsutil` | version 0.2.61-3c86d3ba497a | openjdk version "1.8.0_282" | Python 3.7.10 | conda 4.10.3 | Apache Spark version 2.4.0 | v104 |

```
[fup@compute1-client-3 Neuropathy_WGS_2021May]$ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(spashleyfu/ubuntu18_vep104:hail_gsutil)' /bin/bash

(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ echo $JAVA_HOME
/opt/conda

(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ python -V
Python 3.7.10
(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ python3 -V
Python 3.7.10

(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ conda -V
conda 4.10.3

(base) fup@compute1-exec-135:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ java -version
openjdk version "1.8.0_282"
OpenJDK Runtime Environment (Zulu 8.52.0.23-CA-linux64) (build 1.8.0_282-b08)
OpenJDK 64-Bit Server VM (Zulu 8.52.0.23-CA-linux64) (build 25.282-b08, mixed mode)

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


```

### ubuntu20_pyspark:hail_gsuit

| Docker | Hail | Java | Python | Conda/Pip | PySpark |
| ------ | ---- | ---- | ------ | --------- | ------- | 
| `spashleyfu/ubuntu20_pyspark:hail_gsuit` | version 0.2.61-3c86d3ba497a | openjdk version "1.8.0_282" | Python 3.7.10 | conda 4.10.3 | Apache Spark version 2.4.1 |

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
