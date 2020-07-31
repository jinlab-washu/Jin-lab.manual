## Add rms source to bashrc
In the lab, we will occasional use the yale ruddle hpc to do genomics analysis. We use a program called `rms` to start analysis scripts with the `.rms` extension.

In order to use rms, you will have to source it in the `.bashrc` file found in your home directory.

Move to your home directory with command `cd ~`. You should be here ```[USR_NAME@ruddle1 ~]```.

Once you are in your home directory, open your .bash rc file with a text editor (here we use vim): `vim .bashrc`

Add the following lines;

```
#RMS path
export PATH=/home/bioinfo/software/knightlab/bin_Mar2016.ruddle:$PATH
```

Restart your ssh session. You should now be able to use the ```rms``` command to run `.rms` scripts.
