# Transferring Data With Globus CLI

### Overview

Using Globus CLI docker Image to transfer data using command line.

### RIS Doc

1. [Transferring Data With Globus CLI](https://docs.ris.wustl.edu/doc/storage/globus-cli.html#globus-cli)

2. [Globus CLI Dockerimage](https://docs.ris.wustl.edu/doc/compute/recipes/tools/globus-cli-dockerimage.html?highlight=globus%20docker)

### Steps:

#### 1. Using docker image to access Globus CLI tool:

```
$ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(spashleyfu/globus_cli_wustl:latest)' /bin/bash

```

#### 2. Using `globus login` Login into your account:

Click the URL, it will redirect you to log-in with your WUSTL KEY.

```
fup@compute1-exec-128:~$ globus login --no-local-server
Please authenticate with Globus here:
------------------------------------
https://auth.globus.org/v2/oauth2/authorize?client_id=e41013cf-2e16-4ed3-81cb-0f18bff8c92e&redirect_uri=https%3A%2F%2Fauth.globus.org%2Fv2%2Fweb%2Fauth-code&scope=openid+profile+email+urn%3Aglobus%3Aauth%3Ascope%3Aauth.globus.org%3Aview_identity_set+urn%3Aglobus%3Aauth%3Ascope%3Atransfer.api.globus.org%3Aall&state=_default&response_type=code&access_type=offline&prompt=login
------------------------------------

Enter the resulting Authorization Code here: ********************

You have successfully logged in to the Globus CLI!

You can check your primary identity with
  globus whoami

For information on which of your identities are in session use
  globus session show

Logout of the Globus CLI with
  globus logout

```

#### 3. Search Endpoint:

```
fup@compute1-exec-128:~$ globus endpoint search "WashU"
ID                                   | Owner                                                        | Display Name                                    
------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------
01f0ac4c-9570-11ea-b3c4-0ae144191ee3 | wustl@globusid.org                                           | Wash U RIS storage1 dtn1                        
7e5cf228-8b33-11ea-bf85-0e6cccbb0103 | wustl@globusid.org                                           | Wash U RIS storage1 dtn2                        
...

```

#### 4. `ls` files:

Usage: `globus ls ENDPOINT_ID:/path/you/want/to/ls...`

```
fup@compute1-exec-128:~$ globus ls 01f0ac4c-9570-11ea-b3c4-0ae144191ee3:/storage1/fs1/jin810
Active/
Archive/
README.txt

```

#### 5. `transfer` files:

Once you have determined the endpoints that you wish to use to transfer data, you can utilize the transfer command. 
You can transfer between the WashU endpoints to move data that way.

Usage: `globus transfer ENDPOINT_ID:/source/path/ ENDPOINT_ID:/destination/path`

There are three ways you can transfer data:

```
* Transfer individual files:
    
Usage: `globus transfer ENDPOINT_ID:/source/file.txt ENDPOINT_ID:/destination/file.txt`

* Transfer a directory, using the recursive `-r` option:

Usage: `globus transfer -r ENDPOINT_ID:/source/dir ENDPOINT_ID:/destination/dir`

* Transfer files in bulk using the --batch option:

Usage: `globus transfer --batch ENDPOINT_ID:/source/dir ENDPOINT_ID:/destination/dir < list_of_transfer_file.txt`

You need a space separated text file with the location of the files in the source endpoint followed by the location in the destination endpoint. Each file must have it’s own line.

    Sample1.txt Group1/Sample1.txt

    Sample2.txt Group1/Sample2.txt

    Sample3.txt Group1/Sample3.txt

    Sample4.txt Group2/Sample4.txt

    Sample5.txt Group2/Sample5.txt

```

[More detail on RIS doc](https://docs.ris.wustl.edu/doc/storage/globus-cli.html#globus-transfer-command)







