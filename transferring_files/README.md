# Transfering data


## Comput1:

Transfering data inside compute group WILL cause problems. 
For example, `rsync` data from Active to Archive space (or reverse) inside compute1 may get ERRORS.

The best practice is using either [Globus](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/transferring_files/Globus.md) or 
[Your local compute with `rsync`](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/transferring_files/connect_Storage1_to_Mac.md) 
to transfer data, which using different compute system to do the transfering.

Also, When we get the raw data from sequencing center, we shoulde put our data to Active space, then `tar` the folder to one TAR file, then transfer it to Archive.


For example, if you already have some files in Archive space, please COPY file from Archive to Active using GLOBUS, then use `md5sum` generate md5 for each file. After you prepared md5 file, you cna tar the folder using `tar zcvf yourTarFileName.tar.gz theFolderName1 [theFolderNameN...]`. Finally when you got the tar file, you can use GLOBUS move the tar file to Archive.
