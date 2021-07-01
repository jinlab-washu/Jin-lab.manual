# Connecting to Storage from MacOS

WUSTL RIS Doc: https://docs.ris.wustl.edu/doc/storage/macos/index.html

## Pre-requirement:

1. MacOS 10.10 and newer
2. Administrative privileges
3. Terminal

## Step-by-Step:

1. Open Terminal
2. Disable the writing of .DS_Store files

```
$ defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
```

3. Create or update the /etc/nsmb.conf file (Using sudo, administrative privileges)

```
$ sudo tee /etc/nsmb.conf <<EOF
[default]
smb_neg=smb2_only
dir_cache_off=yes
notify_off=yes
soft=yes
streams=yes
file_ids_off=yes
EOF
```

4. Synchronize the SMB config

```
$ /usr/libexec/smb-sync-preferences
```

5. Click in the background area of the desktop. This will put you in Finder. In the Finder menu at the top left of the screen, click “Go”:

![Go](https://docs.ris.wustl.edu/_images/mac-go-menu.png)

6. From the drop-down menu, click on “Connect to Server”. (Shortcut tip: press Command + K)

![Connect to Server](https://docs.ris.wustl.edu/_images/osx_finder_window.png)

Use the “Connect to Server” option on the menu drop-down.

7. Once the network folder interface pops up use `smb://storage1.ris.wustl.edu/jin810` as the server address:

![network interface]()

8. You will be prompted for your WUSTL Key credentials (you will enter your WUSTL Key ID and password)

9. Once you have completed these steps you will be presented with a finder window showing the Research Drive and all the folders you have access to:

![successed folder]()

After, mount Storage1 to your Mac desktop, you can use `rsync` to transfer files to Compute1.

ie, `$ rsync theFileYouWantToTransfer.txt /Volumes/jin810/thePathYouWantToSaveTheData`

![storage1 path list in Ternminal]()
