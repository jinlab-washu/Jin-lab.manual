# Transferring files from Google Drive Using RClone

Notes:
    
- There are two protocols below for the clusters we use in lab. One is for the yale cluster and one is for the WashU cluster. The major difference between the two is the WashU protocol uses a docker image and the yale protocol does not.
    
- You will need to have access to both the WashU and Yale vpn
    
    - See here for downloading Cisco anyconnect for VPN service: https://vpn.net.wustl.edu/+CSCOE+/logon.html#form_title_text


# Yale Ruddle Protocol

1. ssh into the yale ruddle hpc
    
    **If you have not set up ssh for the ruddle hpc yet, see here: https://docs.ycrc.yale.edu/clusters-at-yale/access/**
    
    
2. Load the Rclone module

    Command: ```module load rclone```
  
3. Create a new rclone config for your google drive account

    Command: ```rclone config```
    
    *See here for more details: https://rclone.org/drive/*
  
4. Select n for new remote and name the new drive.

    ![select_remote.png](./select_remote.png)