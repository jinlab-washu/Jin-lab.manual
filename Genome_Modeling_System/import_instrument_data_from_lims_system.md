# Import instrument data from Lims system

## Note:

You should login into **`gsbu`** system!

You can simply typing `gsub` to login in both **computer0** and **computer1**.

## Finding instrument data ID:

```
$ genome instrument-data list --help

USAGE
 genome instrument-data list [--style=?] [--csv-delimiter=?] [--noheaders]
    --subject-class-name=? [--show=?] [--order-by=?] [SUBTYPE] FILTER

REQUIRED INPUTS
  subject-class-name
    the type of object to list 

REQUIRED PARAMS
  FILTER
    Filter results based on the parameters.  See below for details. 

...
```

For example: 

```
$ genome instrument-data list solexa --filter sample_name~H_WQ-GBD-053,library.protocol!="TruSeqStranded Total RNA" --order-by library_name --show id,sample_name,library_name,target_region_set_name,disk_allocation.absolute_path
ID           SAMPLE_NAME                    LIBRARY_NAME                            TARGET_REGION_SET_NAME                     DISK_ALLOCATION.ABSOLUTE_PATH
--           -----------                    ------------                            ----------------------                     -----------------------------
2896651370   H_WQ-GBD-053.1-GBD-053.1       H_WQ-GBD-053.1-GBD-053.1-lg1-lib1       xGen Lockdown Exome Panel v1 capture set   /gscmnt/gc2698/jin810/instrument_data/2896651370
2896651571   H_WQ-GBD-053.1-GBD-053.1       H_WQ-GBD-053.1-GBD-053.1-lg1-lib1       xGen Lockdown Exome Panel v1 capture set   <NULL>
2896686635   H_WQ-GBD-053.1-GBD-053.1       H_WQ-GBD-053.1-GBD-053.1-lg1-lib1       xGen Lockdown Exome Panel v1 capture set   <NULL>
...
```
If DISK_ALLOCATION.ABSOLUTE_PATH is <NULL>, it means the file is in archive folder. But when you import it, system should automatically handle unarchiving the data for you.


## Import Data From Lims system:

**`/gsc/scripts/opt/genome/bin/genome-site-tgi import-data-from-lims --analysis-project=$projectID --instrument-data=$id`**

You only need $projectID and instrument data $id.

```
~$ /gsc/scripts/opt/genome/bin/genome-site-tgi import-data-from-lims --help

USAGE
 genome-site-tgi import-data-from-lims --analysis-project=? --instrument-data=?[,?]

REQUIRED INPUTS
  analysis-project
    The Analysis Project for which this instrument data is being imported 
  instrument-data
    The data to look up in the LIMS 
...
```

For example:

```
/gsc/scripts/opt/genome/bin/genome-site-tgi import-data-from-lims --analysis-project=80cef865bf23467f87b6ace3a77799e4 --instrument-data=2896688903
'instrument_data', and 'analysis_project' may require verification...
Resolving parameter 'instrument_data' from command argument '2896688903'... found 1
Resolving parameter 'analysis_project' from command argument '80cef865bf23467f87b6ace3a77799e4'... found 1
Created allocation b97e5163ff574245979598a26548a3f8 at /gscmnt/gc2698/jin810/instrument_data/2896688903
RUN: rsync -rlHt '--chmod=Dug=rx,Fug=r' '--chown=:info' /gscmnt/gc13037/archive/2017-03/csf_157193108/ /gscmnt/gc2698/jin810/instrument_data/2896688903
```


