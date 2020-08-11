# Import instrument data from Lims system

## Note:

You should login into **`gsub`** system!

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
 
 But most important, you get instrument data ID!


## Import Data by instrument data ID:

**`genome config analysis-project add-instrument-data $projectID $id`**

You only need **`$projectID`** and instrument data **`$id`**.

```
~$ genome analysis-project add-instrument-data --help

USAGE
 genome config analysis-project add-instrument-data ANALYSIS-PROJECT INSTRUMENT-DATA

SYNOPSIS
genome config analysis-project add-instrument-data <analysis-project> <instrument-data>
REQUIRED INPUTS
  INSTRUMENT-DATA
    instrument data to add to this analysis project 

REQUIRED PARAMS
  ANALYSIS-PROJECT
    the analysis project on which to operate--must be in one of the following statuses: Pending,
    Hold, In Progress 

DESCRIPTION
    This will associate instrument data with an analysis project.

```

For example:

```
~$ genome config analysis-project add-instrument-data 80cef865bf23467f87b6ace3a77799e4 2896651370
'instrument_data', and 'analysis_project' may require verification...
Resolving parameter 'instrument_data' from command argument '2896651370'... found 1
Resolving parameter 'analysis_project' from command argument '80cef865bf23467f87b6ace3a77799e4'... found 1
Asked to assign (1) of which (0) were already assigned. Proceeding to assign (1)
Analysis Project is in a "Pending" state. Assigned Instrument Data will not be processed until it has been released.

```

Before release project, check your import data:

```
~$ genome analysis-project view --fast 80cef865bf23467f87b6ace3a77799e4
'analysis_project' may require verification...
Resolving parameter 'analysis_project' from command argument '80cef865bf23467f87b6ace3a77799e4'... found 1
=== Analysis Project ===
ID: 80cef865bf23467f87b6ace3a77799e4                                        Name: hydrocephalus_GBD_32_38_53_55
Run as: prod-builder                                                        Created: 2020-08-07 20:53:39
Updated: 2020-08-07 20:53:39                                                Created by: fup
Status: Pending

    ** Analysis Project is PENDING **

=== Instrument Data ===
Genome::InstrumentData::Solexa
             new 106
           Total 106

=== Configuration Items ===
Custom configuration item
    ID: 2299a11ae76d450282f3d6879e4be433                                        Concrete: Yes
    Created by: fup                                                             Status: active
    Created: 2020-08-07 20:59:06                                                Updated: 2020-08-07 20:59:06
    Tags: 

Environment config: /gscmnt/gc2560/core/analysis_project/80cef865bf23467f87b6ace3a77799e4

```


