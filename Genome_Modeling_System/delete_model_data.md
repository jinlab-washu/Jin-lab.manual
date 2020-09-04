# Deleting Analysis Projects and Associated Model Data
**Note: You must have created the Analysis Project in the ad-hoc environment. If you chose prod-builder, you will need to contact the MGIBIO team so that they can delete the necessary builds for you**

1. Deprecate the analysis projects you are going to remove

`genome analysis-project deprecate "a420e0496a14459594740b816b6f9479,2284092a1c7f45b297475ade68d03118,f9b8974844994e8d97d78eb4e6d57ff5,1467991003b84123bae0fdb0e05614be,a3abf14359a4409884a1b534c6861239,54ecfc334d4c413aa25a471001fa5bdb,c43406645c874221a7607ebd2a7c0497,def52bd5013a4d59bc168f274fc1566a,f5c27eefbf1143afbc3a2e31e3b167c8,99832e22f9ef48538515d8894ca30bbb"`

This signals the GMS to do an automated removal of the analysis project. This does not occur instantly.

2. (Optional) Check if builds were ran by multiple users.

    *If you know that builds were ran by different users, you can check the user who ran each build*
    
    ```
    $ genome model build list -f model.analysis_project.id=f9b8974844994e8d97d78eb4e6d57ff5 --show run_by --nohead | sort | uniq -c
      8 s.peters
    ```
    
      *A project could be set to run_as prod-builder, but if you use genome model build start (as opposed to queue) they will still run under your username*
      
2. List the builds to be deleted

    Use the command below to run the delete in a "test" mode. It will print all of the builds that will be deleted to the console.

        **For a single analysis project**
        ```
        genome model build list -f model.analysis_project.id=$ANALYSIS_PROJECT_ID --show id --nohead | xargs | tr ' ' '/' | xargs -I BUILD_IDS echo genome disk allocation purge --reason "deprecation of Analysis Project $ANALYSIS_PROJECT_ID" owner_id:BUILD_IDS
        ```

        **For multiple analysis projects:**

        ```
        for ANALYSIS_PROJECT_ID in $ID_1 $ID_2 $ID_3 $ID_4 $ID_5 $ID_6 $ID_7; do  genome model build list -f model.analysis_project.id="$ANALYSIS_PROJECT_ID" --show id --nohead | xargs | tr ' ' '/' | xargs -I BUILD_IDS echo genome disk allocation purge --reason "deprecation of Analysis Project $ANALYSIS_PROJECT_ID" owner_id:BUILD_IDS; done
        ```
3. Delete the builds

    If you everything looks okay, remove the echo located here (denoted with *): `BUILD_IDS *echo* genome disk allocation purge`.


    Next, run the command again (now without the `echo` shown above) 

        **For a single analysis project**
        ```
        genome model build list -f model.analysis_project.id=$ANALYSIS_PROJECT_ID --show id --nohead | xargs | tr ' ' '/' | xargs -I BUILD_IDS genome disk allocation purge --reason "deprecation of Analysis Project $ANALYSIS_PROJECT_ID" owner_id:BUILD_IDS
        ```

        **For multiple analysis projects:**

        ```
        for ANALYSIS_PROJECT_ID in $ID_1 $ID_2 $ID_3 $ID_4 $ID_5 $ID_6 $ID_7; do  genome model build list -f model.analysis_project.id="$ANALYSIS_PROJECT_ID" --show id --nohead | xargs | tr ' ' '/' | xargs -I BUILD_IDS genome disk allocation purge --reason "deprecation of Analysis Project $ANALYSIS_PROJECT_ID" owner_id:BUILD_IDS; done
        ```

    
