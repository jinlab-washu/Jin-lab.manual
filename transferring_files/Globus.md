# Globus

## Overview

Globus is a service for accessing and transferring research data. 

## Transferring Data

### Storage1 to Storage0

![File Manager](./media/globus/globus1.png "File Manager")

Transferring data is simple if you are using the Globus web application. First, you will need to select the source and  destination locations. If you are prompted for credentials you should use your WUSTL key and password. On Storage0 you will likely receive a "Permission Denied" message. This is because you do not have access to the root directory. All you need to do is input the path of a directory for which you do have access.


![Transfer from Storage1 to Storage0](./media/globus/globus2.png "Transfer from Storage1 to Storage0")

Finally, to transfer a file you just need to select the directory or file you would like to transfer and click on the "Transfer or Sync to..." button. 


### Downloading to your machine

Globus also allows you to download files to your personal machine. To do this you will need to install the Globus Connect Personal application and create an endpoint for your machine. 

Globus Connect Personal (GCP) [Installation Guide](https://www.globus.org/globus-connect-personal): (Choose OS version to see details)

![Globus Connect Personal downloading page](/media/globus/globus4.PNG "Globus Connect Personal downloading page")

1. In the Globus web application select "ENDPOINTS" in the left menu.

![ENDPOINTS](/media/globus/globus6.PNG "ENDPOINTS")

2. Click the "Create a personal endpoint" button and follow the steps. [link](https://app.globus.org/file-manager/gcp)

![Download Application](/media/globus/globus5.PNG "Download Application")

3. Specify which directories Globus should have access to on your machine.

![Globus Preferences](./media/globus/globus3.png "Globus Preferences")

Files can be transferred in the exact same way as moving to Storage0. The only difference is you will select your machine in the dropdown menu.
