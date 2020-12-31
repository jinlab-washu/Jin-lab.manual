# Add rms path to .bashrc configuration file
> Adding the rms path to your .bashrc file allows for you to use rms from the command line without providing the full path. 

Run the following command. This will add a line to your .bashrc configuration file to enable the use of rms with the shortuct `rms`
```
echo export PATH=/gpfs/ycga/apps/bioinfo/software/knightlab/soft/plotReads_Apr2019:$PATH >> ~/.bashrc
```
