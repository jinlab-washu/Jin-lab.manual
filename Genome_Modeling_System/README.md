# WashU GMS

**[GMS Official Wiki](https://github.com/genome/genome/wiki)**

## GMS on compute0 / compute1

1. Simply type `gsub` to use GMS docker on compute0 / computer1

> The `gsub` wrapper command is designed to handle the details of loading an appropriate environment
>
> `gsub -h` ("help" option will present various parameters)

2. In GMS enviroment, using `genome -h` to check various parameters.

### Concept

![GMS](https://github.com/jinlab-washu/Jin-lab.manual/blob/master/Genome_Modeling_System/gms_diagram.png?raw=true)

### Basic Steps:

* [Creating and Setting analysis-project (AnP)](create_analysis_project_GMS.md)

* Import Data

  * [Import instrument data from Lims system (Internal data)](import_instrument_data_from_lims_system.md)
  
  * [Importing External Data](import_external_data_manually.md)
  
* Release AnP - `genome analysis-project release $AnP`
  
* Browsing Status - https://spectacle.gsc.wustl.edu/
  


_[Useful Commands](gms_commands.md)_

_[Helpful links](gms_info.md)_
