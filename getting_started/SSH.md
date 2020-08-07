# SSH

## Overview
Secure Shell (SSH) is a cryptographic network protocol for operating network services securely over unsecured networks. You will be using it to access the compute clusters to do your work.

## Compute1
macOS/Linux/BSD:

```
ssh wustl-user@compute1-client-1.ris.wustl.edu
```

You will replace `wustl-user` with your username.

Windows:

You will need to use PuTTY or the Windows Subsystem for Linux (WSL). Check the [RIS IT Knowledge Base](https://confluence.ris.wustl.edu "RIS IT Knowledge Base") for recommendations and more information.

## Compute0 (Legacy)
macOS/Linux/BSD:

```
ssh wustl-user@virtual-workstation$NUMBER.gsc.wustl.edu

or the shorthand version

ssh wustl-user@vw$NUMBER.gsc.wustl.edu
```

You will replace `wustl-user` with your username and `$NUMBER` with the number of the workstation you would like to access (1, 2, 3, 4, or 5). They all have access to the same filesystem and software, so you are free to choose whichever you like. You can also have mutliple workshops open at the same time.

Windows:

You will need to use PuTTY or the Windows Subsystem for Linux (WSL). Check the [RIS IT Knowledge Base](https://confluence.ris.wustl.edu "RIS IT Knowledge Base") for recommendations and more information.

## Yale Ruddle
macOS/Linux/BSD:

You will need to create an ssh key-pair and upload your public key to your net id to be able to acess the cluster. See here for directions: https://docs.ycrc.yale.edu/clusters-at-yale/access/

```
ssh yale-net-id@ruddle.hpc.yale.edu
```

