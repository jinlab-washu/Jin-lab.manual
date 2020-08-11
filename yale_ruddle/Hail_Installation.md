# Hail Installation Guide

**On Yale Ruddle System**

Helpful links:

  [Installing Hail on Mac OS X or GNU/Linux with pip - Official Document](https://hail.is/docs/0.2/getting_started.html#installing-hail-on-mac-os-x-or-gnu-linux-with-pip)

  [Yale HPC Introduction](https://docs.google.com/presentation/d/1H9FgA8ER-VTJMyRDm0FRy_SH-xGDmBwcRVzY2Gk66fA/edit?usp=sharing)
  
Steps:

1. Login into Yale Ruddle with netid:

	`[netid@ruddle1 ~]$ `
  
2. Interactive Allocation:

	`[netid@ruddle1 ~]$ srun --pty -p interactive --mem=8g bash`
  
3. Create a conda environment named `hail`:

	`[netid@c13n01 ~]$ conda create -n hail python'>=3.6,<3.8'`
  
4. Activate `hail` environment:

	`[netid@c13n01 ~]$ conda activate hail`
  
5. Install Hail by pip:

	`(/.../netid/conda_envs/hail) [netid@c13n01 ~]$ pip install hail`
  
6. Import hail in python shell or other python environment:

	```
	(/.../netid/conda_envs/hail) [netid@c13n01 ~]$ python
	Python 3.7.7 (default, May  7 2020, 21:25:33)
	[GCC 7.3.0] :: Anaconda, Inc. on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import hail as hl
	>>> hl.init()
	...
	Running on Apache Spark version 2.4.1
	SparkUI available at http://c13n05.ruddle.hpc.yale.internal:4040
	Welcome to
	     __  __     <>__
	    / /_/ /__  __/ /
	   / __  / _ `/ / /
	  /_/ /_/\_,_/_/_/   version 0.2.41-b8144dba46e6
	LOGGING: writing to /.../netid/hail-20200522-1442-0.2.41-b8144dba46e6.log
	>>> quit()
	```
  
7. Check conda environment infomation:
	```
	(/.../netid/conda_envs/hail) [netid@c13n01 ~]$ conda info --envs
	# conda environments:
	# 
	hail 	*	/.../netid/conda_envs/hail
	base    	/.../apps/hpc/software/miniconda/4.7.10
	```
	
Note: If steps 5 or 6 fail try `pip3` and `python3` respectively.
