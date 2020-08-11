Move to your home directory and open the .bashrc file with a text editor
```
$ cd ~
$ vim .bashrc (or whichever editor you like)
```
Add the following to the .bashrc file in your home directory


```
# Source rms path
export PATH="/home/jk2269/rms:$PATH"
```

You should now be able to use the rms command to run .rms scripts
