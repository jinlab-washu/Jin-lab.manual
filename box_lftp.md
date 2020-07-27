# Transferring Files from Wustl Box to Compute0

Notes:

- Protocol based on wustl confluence protocol
- This protocol uses an interactive docker image with lftp installed: minidocks/lftp:latest@sha256:5923b4f2383c1cc2fe9a1134433431fd1c8a1e7a20c9640313df8411ee09fe15
    - https://hub.docker.com/r/minidocks/lftp

- The command ```lcd``` is used to change the current working directory after loading the lftp program
