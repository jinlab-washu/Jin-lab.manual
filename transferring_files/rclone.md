# Transferring files from Google Drive / BOX Using RClone

Notes:
    
- There are two protocols below for the clusters we use in lab. One is for the yale cluster and one is for the WashU cluster. The major difference between the two is the WashU protocol uses a docker image and the yale protocol does not.
    
- You will need to have access to both the WashU and Yale vpn
    
    - See here for downloading Cisco anyconnect for VPN service: https://vpn.net.wustl.edu/+CSCOE+/logon.html#form_title_text

## Outline:

1. [WashU Rclone - BOX](#wustl-compute1)
2. [Yale Rclone - BOX](#yale-ruddle-protocol)
3. [Yale Rclone - Google Drive]()

# WUSTL Compute1:

RIS Doc: https://docs.ris.wustl.edu/doc/storage/rclone.html

* Prerequisites:
    1. A WUSTL Box account
    2. A user account for RIS storage1 and compute1 services

1. Building an Endpoint: [RIS Doc](https://docs.ris.wustl.edu/doc/storage/rclone.html?highlight=box#id4)

    1. Install Rclone:

         * For macOS: `$ brew install rclone`
         * For Windows: download the relevant archive file from https://rclone.org/downloads/ for your environment. Then, extract the rclone.exe binary from the archive.
         * For Linux/BSD: `curl https://rclone.org/install.sh | sudo bash`

    2. Configuration:
    
        [Follow the instruction...](https://docs.ris.wustl.edu/doc/storage/rclone.html#ii-configuration)
        
        An example: using Ubuntu
        
        ```
        // Download and Install:
        $ curl https://rclone.org/install.sh | sudo bash
        ...

        rclone v1.56.0 has successfully installed.
        Now run "rclone config" for setup. Check https://rclone.org/docs/ for more details.
        
        // Config:
        $ rclone config
        2021/07/21 10:50:54 NOTICE: Config file "/home/pyfu/.config/rclone/rclone.conf" not found - using defaults
        No remotes found - make a new one
        n) New remote
        s) Set configuration password
        q) Quit config
        n/s/q> n
        name> Box
        Type of storage to configure.
        Enter a string value. Press Enter for the default ("").
        Choose a number from below, or type in your own value
         1 / 1Fichier
           \ "fichier"
         2 / Alias for an existing remote
           \ "alias"
         3 / Amazon Drive
           \ "amazon cloud drive"
         4 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, SeaweedFS, and Tencent COS
           \ "s3"
         5 / Backblaze B2
           \ "b2"
         6 / Box
           \ "box"
         ...
        Storage> box
        OAuth Client Id
        Leave blank normally.
        Enter a string value. Press Enter for the default ("").
        client_id> 
        OAuth Client Secret
        Leave blank normally.
        Enter a string value. Press Enter for the default ("").
        client_secret> 
        Box App config.json location
        Leave blank normally.

        Leading `~` will be expanded in the file name as will environment variables such as `${RCLONE_CONFIG_DIR}`.

        Enter a string value. Press Enter for the default ("").
        box_config_file> 
        Box App Primary Access Token
        Leave blank normally.
        Enter a string value. Press Enter for the default ("").
        access_token> 

        Enter a string value. Press Enter for the default ("user").
        Choose a number from below, or type in your own value
         1 / Rclone should act on behalf of a user
           \ "user"
         2 / Rclone should act on behalf of a service account
           \ "enterprise"
        box_sub_type> user
        Edit advanced config?
        y) Yes
        n) No (default)
        y/n> 
        Use auto config?
         * Say Y if not sure
         * Say N if you are working on a remote or headless machine

        y) Yes (default)
        n) No
        y/n> 
        2021/07/21 10:54:00 NOTICE: If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth?state=sGYM0aTyMIcNSkxVvYEpeg
        2021/07/21 10:54:00 NOTICE: Log in and authorize rclone for access
        2021/07/21 10:54:00 NOTICE: Waiting for code...
        2021/07/21 10:54:03 NOTICE: Got code
        --------------------
        [Box]
        type = box
        token = {"access_token":"#########","token_type":"bearer","refresh_token":"#######","expiry":"2021-07-21T12:02:47.318375568-05:00"}
        --------------------
        y) Yes this is OK (default)
        e) Edit this remote
        d) Delete this remote
        y/e/d> y
        Current remotes:

        Name                 Type
        ====                 ====
        Box                  box

        e) Edit existing remote
        n) New remote
        d) Delete remote
        r) Rename remote
        c) Copy remote
        s) Set configuration password
        q) Quit config
        e/n/d/r/c/s/q> q
        
        ```
    3. Copying the credential file to the home directory on compute1: Using Globus or other ways.
    
        COPY the config file you just generated, normally the file should be `$HOME/.config/rclone/rclone.conf` (locally), 
        to Compute1 $HOME folder, and named it `.rclone.conf`.
        
        For exmple:
        ```
        local$ scp $HOME/.config/rclone/rclone.conf WUSTLKEY@compute1-client-1.ris.wustl.edu:~/.rclone.conf
        ```
    
    4. Test:

        * Login to compute1
        * Check config file exist at `~/.rclone.conf`: `$ ls -la ~/.rclone.conf`
        * Request Rclone Docker: `$ LSF_DOCKER_ENTRYPOINT=/bin/sh bsub -Is -G group-name -q general-interactive -a 'docker(rclone/rclone)' /bin/sh`
        * Listing the BOX directories using Rclone: `$ rclone lsd Box:/`

2. Use Case: 

    COPY CAKUT data from WUSTL BOX to compute1.

    1. Login to compute1
    2. Verify the rclone configuration file is in the home directory.
    
        ```
        [fup@compute1-client-3 ~]$ ls -la $HOME/.rclone.conf
        ```
    
    3. Request Rclone Docker Env: 
    
        ```
        [fup@compute1-client-3 ~]$ LSF_DOCKER_ENTRYPOINT=/bin/sh bsub -Is -G compute-jin810 -q general-interactive -a 'docker(rclone/rclone)' /bin/sh
        ```
    4. Listing the directories:
    
        ```
        ~ $ rclone lsd Box:/
                  -1 2020-05-21 20:52:37        -1 Box Notes Images
                  -1 2021-06-01 20:13:59        -1 Exome sequencing for analysis
                  -1 2021-06-17 21:29:51        -1 Jin Lab Files
                  -1 2020-05-21 17:09:26        -1 LabScript
                  -1 2021-07-20 22:20:43        -1 MGI exome sequencing 072021
        ```
    
    5. COPY the file/folder from BOX to compute1 Storage:

        Using rclone copy command: 
        For example, COPY CAKUT data from WUSTL BOX to compute1:
        
        ```
        ~ $ cd /cache2/fs1/jin810/Active/CAKUT_2021Jun/MGI_kidney_CAKUT_exome_sequencing_072021
        /cache2/fs1/jin810/Active/CAKUT_2021Jun/MGI_kidney_CAKUT_exome_sequencing_072021 $ rclone copy Box:/"MGI exome sequencing 072021" .
        ```
# Yale Ruddle Protocol (BOX)

1. SSH into Yale Ruddle server.
2. Load the Rclone module

    ```
    $ module load Rclone
    ```

3. Create a new rclone config for BOX

    ```
    $ rclone config
    2021/07/21 17:33:49 NOTICE: Config file "/home/pf374/.config/rclone/rclone.conf" not found - using defaults
    No remotes found - make a new one
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    name> WUSTLBOX         
    Type of storage to configure.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value
     1 / 1Fichier
       \ "fichier"
     2 / Alias for an existing remote
       \ "alias"
     3 / Amazon Drive
       \ "amazon cloud drive"
     4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, etc)
       \ "s3"
     5 / Backblaze B2
       \ "b2"
     6 / Box
       \ "box"
    ...
    Storage> box
    ** See help for box backend at: https://rclone.org/box/ **

    Box App Client Id.
    Leave blank normally.
    Enter a string value. Press Enter for the default ("").
    client_id> 
    Box App Client Secret
    Leave blank normally.
    Enter a string value. Press Enter for the default ("").
    client_secret> 
    Box App config.json location
    Leave blank normally.
    Enter a string value. Press Enter for the default ("").
    box_config_file> 

    Enter a string value. Press Enter for the default ("user").
    Choose a number from below, or type in your own value
     1 / Rclone should act on behalf of a user
       \ "user"
     2 / Rclone should act on behalf of a service account
       \ "enterprise"
    box_sub_type> user
    Edit advanced config? (y/n)
    y) Yes
    n) No (default)
    y/n> 
    Remote config
    Use auto config?
     * Say Y if not sure
     * Say N if you are working on a remote or headless machine
    y) Yes (default)
    n) No
    y/n> n
    For this to work, you will need rclone available on a machine that has a web browser available.
    Execute the following on your machine (same rclone version recommended) :
        rclone authorize "box"
    Then paste the result below:
    result> {"access_token":"##############","token_type":"bearer","refresh_token":"###############","expiry":"2021-07-21T17:39:21.870127571-05:00"}
    --------------------
    [WUSTLBOX]
    type = box
    box_sub_type = user
    token = {"access_token":"##############","token_type":"bearer","refresh_token":"###############","expiry":"2021-07-21T17:39:21.870127571-05:00"}
    --------------------
    y) Yes this is OK (default)
    e) Edit this remote
    d) Delete this remote
    y/e/d> 
    Current remotes:

    Name                 Type
    ====                 ====
    WUSTLBOX             box

    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q
    ```

4. Find the config file:

    ```
    $ rclone config file
    Configuration file is stored at:
    /home/pf374/.config/rclone/rclone.conf
    ```

5. Listing the directories:

    ```
    $ rclone lsd WUSTLBOX:/
              -1 2020-05-21 16:52:37        -1 Box Notes Images
              -1 2021-06-01 16:13:59        -1 Exome sequencing for analysis
              -1 2021-06-17 17:29:51        -1 Jin Lab Files
              -1 2020-05-21 13:09:26        -1 LabScript
              -1 2021-07-20 18:20:43        -1 MGI exome sequencing 072021
              ...

    ```

6. COPY files/Folder to Scratch60:

    ```
    $ rclone copy WUSTLBOX:/"MGI exome sequencing 072021" scratch60/MGI_CAKUT_2021Jul_rawdata/
    ```


# Yale Ruddle Protocol (Google Drive)

1. ssh into the yale ruddle hpc
    
    **If you have not set up ssh for the ruddle hpc yet, see here: https://docs.ycrc.yale.edu/clusters-at-yale/access/**
    
    
2. Load the Rclone module

    Command: ```module load Rclone```
  
3. Create a new rclone config for your google drive account

    Command: ```rclone config```
    
    *See here for more details: https://rclone.org/drive/*
  
4. Select n for new remote and name the new drive.

    ![select_remote.png](./select_remote.png)

5. (Optional) Create a client id and secret according to the following page: https://rclone.org/drive/#making-your-own-client-id 

    Creating a client id and secret improves performance, but is not necessary.
    
6. Enter client id and secret (if applicable)

7. Enter value for access type from selection that appears.

    E.g. 1-Full access

8. Leave blank for "root_folder_id" and "service_account_file" (unless you know what you are doing)
      
       service_account_file> 
       Edit advanced config? (y/n)
       y) Yes
       n) No (default)
    
9. Select ```n``` for edit advanced config (unless you know what you are doing)
    
    

10. Select ```n``` for remote config as we are working on a headless machine

    - A link will appear in order to authorize access for rclone to your google drive account. Click the link and authorize access.
    
11. Select ```n``` for ```Configure this as a team drive```

12. Check overview of drive information and select ```y``` if it looks okay.

------

Now you should be able to use rclone commands to transfer files to hpc clusters or local locations via the command line

```rclone copy rclone_remote:file dest:destpath``` 

If the files are under your "shared with me" folder, use the ```--drive-shared-with-me``` flag

```rclone copy rclone_remote:file dest:destpath --drive-shared-with-me```
