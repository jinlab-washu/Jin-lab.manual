# How to use GMS on Computer 1

Because "WashU RIS uses Docker to manage the containers within compute1." ([RIS doc](https://docs.ris.wustl.edu/doc/compute/compute-quick-start.html#understanding-what-a-container-is))
We need to do some configuration for using Genome Modeling System (GMS).

## First time setting: (Only need to do it once)

[GMS on compute1 - official doc](https://github.com/genome/genome/wiki/GMS-on-compute1)

### 1. Editing `.bashrc` file:

Add this code to your file:

```bash
PATH=$PATH:/storage1/fs1/bga/Active/gmsroot/gc2560/core/env/v2/bin
if [[ -f /gscmnt/gc2560/core/env/v2/bashrc ]]; then
  source /gscmnt/gc2560/core/env/v2/bashrc
fi
```

> This command add `gsub` path (`/storage1/fs1/bga/Active/gmsroot/gc2560/core/env/v2/bin`) to $PATH
>
> You can `$ ls /storage1/fs1/bga/Active/gmsroot/gc2560/core/env/v2/bin`, you should see `gsub` program is the folder.
>


### 2. Activate the setting:

```~$ source .bashrc```

### 3. Test command:

```
[fup@compute1-client-4 ~]$ gsub
Job <386326> is submitted to queue <general-interactive>.
<<Waiting for dispatch ...>>
<<Starting on compute1-exec-153.ris.wustl.edu>>
compute1-10: Pulling from apipe-builder/genome_perl_environment
ca9ffbe3c33d: Pull complete 
...
c44ea9f15123: Pull complete 
Digest: sha256:1790a587e107aa5d33e8b6c5125adf8d8deca703fd637897f656010ec4856fc3
Status: Downloaded newer image for registry.gsc.wustl.edu/apipe-builder/genome_perl_environment:compute1-10
registry.gsc.wustl.edu/apipe-builder/genome_perl_environment:compute1-10
Loading LSF_DOCKER_VOLUMES from ~/.bashrc
Using compute-jin810 as LSF_COMPUTE_GROUP

fup@compute1-exec-177:~$ genome -h
Sub-commands for genome:
 analysis-project    ...  work with analysis projects                           
 config              ...  work with analysis project configurations             
 db                  ...  external database interfaces                          
 disk                ...  work with allocations, volumes, etc                   
 feature-list        ...  work with feature-lists                               
 individual          ...  work with individuals                                 
 instrument-data     ...  work with instrument data                             
 library             ...  work with libraries                                   
 model               ...  work with models                                      
 model-group         ...  work with model-groups                                
 population-group    ...  work with population groups                           
 process             ...  commands for working with processes                   
 processing-profile  ...  work with processing profiles.                        
 project             ...  work with projects                                    
 project-part        ...  work with project parts                               
 qc                  ...  work with QC configuration and results                
 report                   work with reports                                     
 sample              ...  work with samples                                     
 search                   search at the command line for various genome objects 
 software-result     ...  work with software results                            
 subject             ...  work with subjects                                    
 sys                 ...  work with OS integration                              
 task                ...  work with tasks                                       
 taxon               ...  work with taxons                                      
 test                ...  commands for testing various parts of the GMS         
 tools               ...  bioinformatics tools for genomics                     
 variant-reporting   ...  annotation related commands    

```

**NEXT**: [GMS commands](https://github.com/AmberFu/JinLabNote/blob/master/server_GMS_docs/GMS_command.md)

-------------------------------------

**My `.bashrc` file:**

```bash
# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# GMS:
PATH=$PATH:/storage1/fs1/bga/Active/gmsroot/gc2560/core/env/v2/bin
if [[ -f /gscmnt/gc2560/core/env/v2/bashrc ]]; then
  source /gscmnt/gc2560/core/env/v2/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# User specific aliases and functions
# Doc: https://confluence.ris.wustl.edu/display/RSUM/Access+Storage+Volumes
echo "Loading LSF_DOCKER_VOLUMES from ~/.bashrc"

export BGA="/storage1/fs1/bga/Active"

#Use the scratch file system for temp space
export SCRATCH1="/scratch1/fs1/jin810"

#Use your Active storage for input and output data
#export JIN="/storage1/fs1/jin810/Active" # same as STORAGE1
export STORAGE1="/storage1/fs1/jin810/Active"

export LSF_DOCKER_VOLUMES="$SCRATCH1:$SCRATCH1 $STORAGE1:$STORAGE1 $HOME:$HOME $BGA:$BGA"

export LSF_COMPUTE_GROUP="compute-jin810"
echo "Using compute-jin810 as LSF_COMPUTE_GROUP"

```


**What is in `/gscmnt/gc2560/core/env/v2/bashrc`?**

```
fup@compute1-exec-153:~$ cat /gscmnt/gc2560/core/env/v2/bashrc
#load all this only if in a GMS container
if [[ $LSB_DOCKER_IMAGE =~ "genome_perl_environment" ]];then 
    export PERL5LIB=/gsc/scripts/opt/genome/current/user/lib/perl:$PERL5LIB
    export PATH=/gsc/scripts/opt/genome/current/user/bin:$PATH
 fi

# #only source this in the legacy container
if [[ $LSB_DOCKER_IMAGE =~ "registry.gsc.wustl.edu/genome/genome_perl_environment" ]];then 
    export PATH=/gsc/bin/:/gsc/scripts/bin:$PATH
fi

```
