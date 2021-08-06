# Using Hail on WashU cluster Compute1


### How to run Hail with Jupyter Lab:

Jupyter Lab is a newer version of Jupyter Notebook. The default port is 8888.


1. Request a docker with PORT 8888:

> Docker Image: `spashleyfu/ubuntu20_pyspark:hail_gsuit`

```
$ export JPORT=8888; LSF_DOCKER_PORTS="$JPORT:$JPORT" bsub -Is -G compute-jin810 -q general-interactive -n 32 -M 128GB -R 'select[port8888=1] rusage[mem=128GB]' -a 'docker(spashleyfu/ubuntu20_pyspark:hail_gsuit)' /bin/bash
```

2. Running Jupyter Lab in your project folder:

> CMD: `jupyter lab --no-browser --ip "*"`

```
(base) fup@compute1-exec-123:~$ cd /storage1/fs1/jin810/Active/YOUR_PROJECT_FOLFER

(base) fup@compute1-exec-123:/storage1/fs1/jin810/Active/Neuropathy_WGS_2021May$ jupyter lab --no-browser --ip "*"
[I 2021-08-05 19:56:33.938 ServerApp] jupyterlab | extension was successfully linked.
[I 2021-08-05 19:56:34.136 ServerApp] nbclassic | extension was successfully linked.
[W 2021-08-05 19:56:34.152 ServerApp] WARNING: The Jupyter server is listening on all IP addresses and not using encryption. This is not recommended.
[I 2021-08-05 19:56:34.156 ServerApp] nbclassic | extension was successfully loaded.
[I 2021-08-05 19:56:34.157 LabApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
[I 2021-08-05 19:56:34.157 LabApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 2021-08-05 19:56:34.161 ServerApp] jupyterlab | extension was successfully loaded.
[I 2021-08-05 19:56:34.162 ServerApp] Serving notebooks from local directory: /storage1/fs1/jin810/Active/Neuropathy_WGS_2021May
[I 2021-08-05 19:56:34.162 ServerApp] Jupyter Server 1.10.2 is running at:
[I 2021-08-05 19:56:34.162 ServerApp] http://compute1-exec-123.ris.wustl.edu:8888/lab?token=XXXXXXXXXXXX
[I 2021-08-05 19:56:34.162 ServerApp]  or http://127.0.0.1:8888/lab?token=XXXXXXXXXXXX
[I 2021-08-05 19:56:34.162 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2021-08-05 19:56:34.169 ServerApp] 
    
    To access the server, open this file in a browser:
        file:///home/fup/.local/share/jupyter/runtime/jpserver-20-open.html
    Or copy and paste one of these URLs:
        http://compute1-exec-123.ris.wustl.edu:8888/lab?token=XXXXXXXXXXXX
     or http://127.0.0.1:8888/lab?token=XXXXXXXXXXXX

```

3. Open a browser and paste the link:

> URL: http://compute1-exec-123.ris.wustl.edu:8888/lab?token=XXXXXXXXXXXX

