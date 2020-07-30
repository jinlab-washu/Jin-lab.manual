## Introduction
We will be using WashU's Genome Modeling System (GMS) to run whole pipelines and parts of pipelines for sequencing analysis. This system has a steep learning curve, but the protocol below demonstrates how to create, configure, and run a new analysis project on external Whole Exome Sequencing data. It is good to be familiar with this system as it is used as an integral part in our Whole Exome Sequencing analysis pipeline.

For an overview of the GMS, see here: https://confluence.ris.wustl.edu/pages/viewpage.action?pageId=3637349

**Note: Any link that has confluence in the name, can only be accessed if you are connected to the WashU VPN**

## Set-up
Right now, there are two clusters at Washu that are used for sequencing analysis. The legacy cluster, compute0 , and the new cluster, compute1. Everything on compute0 is slowly being moved to compute1 so that compute0 can be discontinued in a few years. *AS OF NOW, MOST OF OUR ANALYSIS ONLY WORKS ON COMPUTE0* 

**1. Log into compute0 using ssh.**

  Compute 0 has 4 "workstations" you can log into. Below we will use virtual-workstation 1 or "vw1".
  
   ```ssh $wustl_ID@vw1.gsc.wustl.edu``` where ```$wustl_ID``` is your personal wustl ID. 
  
  **NOTE: The password for compute0 uses an MGI account password instead of the normal one you created at the time of setting up your ID. If you don't have an MGI account, you will need to have one created.** 

**2. Modify your .bashrc file in order to access the GMS environment.**
  
  Edit the .bashrc file located in your home directory. Your home directory is located at `/~`. 
  
  Typing ```cd ~ ``` into the command line will take you directly to your home directory.
  
  **Note: The .bashrc file is hidden. To see it in your home directory, you can use the command: ```ls -a```*

2. Edit the file using emacs/vim. ```emacs .bashrc``` 

**Nano is not installed  on the default command line in compute0*

Once you are in the file, delete the information listed below:
```
# source global definitions
 if [ -f /etc/bashrc ]; then             # redhat
     . /etc/bashrc
 elif [ -f /etc/bash.bashrc ]; then # debian
     . /etc/bash.bashrc
 fi
 
 # source the gapp bashrc
 if [ -f /gapp/noarch/share/login/gapp.bashrc ]; then
     . /gapp/noarch/share/login/gapp.bashrc
 fi

# source the gapp profile
 if [ -f /gapp/noarch/share/login/gapp.profile ]; then
     . /gapp/noarch/share/login/gapp.profile
 fi
 ```
Once deleted, add the following to the top lines of the file:

```
PATH=$PATH:/gscmnt/gc2560/core/env/v1/bin
source /gscmnt/gc2560/core/env/v1/bashrc
```
Restart your ssh session and you should be good to go!

If you are having trouble, see here for more infromation: https://confluence.ris.wustl.edu/display/BIO/GMS+-+Docker+Image+-+gsub
