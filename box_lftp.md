# Transferring Files from Wustl Box to Compute0

Notes:

- Protocol based on wustl confluence protocol: https://confluence.ris.wustl.edu/pages/viewpage.action?pageId=52635520
- This protocol uses an interactive docker image with lftp installed: minidocks/lftp:latest@sha256:5923b4f2383c1cc2fe9a1134433431fd1c8a1e7a20c9640313df8411ee09fe15
    - https://hub.docker.com/r/minidocks/lftp

- The command ```lcd``` is used to change the current working directory after loading the lftp program


1. Load the docker image with an interactive session:

    ```bsub -Is -q research-hpc -a 'docker(minidocks/lftp:latest@sha256:5923b4f2383c1cc2fe9a1134433431fd1c8a1e7a20c9640313df8411ee09fe15)' -R "select[mem>5000] rusage[mem=5000]" /bin/bash```

2. Load the lftp program using wustl email and password:

    ```lftp -u $wustl.email,$password -p 990 ftps://ftp.box.com```
    
3. Change the current working directory to the target directory you wish to download the data to:

    ```lcd $target_directory```
    
    *lcd changes the current working directory to the one specified following the command*
    
4. Tansfer files from box using get for a specific file or mirror to transfer all files in the lftp directory to the target directory
