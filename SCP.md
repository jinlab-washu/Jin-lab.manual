# SCP

## Overview

Secure copy protocol (SCP) is a method of securely transferring files between hosts, based on the SSH protocol. 

## Uploading to a remote host

If you have a file on your local machine that you need on one of the clusters you can use [Globus](./Globus.md "Globus") or you can use SCP.

On a unix machine (macOS, Linux, etc):

```
scp file.txt username@to_host:/remote/directory/
```

You can also copy entire directories:

```
scp -r /local/directory/ username@to_host:/remote/directory/
```

## Downloading from a remote host

You can also copy files from the cluster to your local machine by changing the order of arguments. For example, when uploading a directory we provided our local directory and then the remote directory. This order is reversed when downloading:

```
scp -r username@from_host:/remote/directory/  /local/directory/
```
