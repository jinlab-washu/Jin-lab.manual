## Purpose

To create custom .bed and interval (.list) files used for specifying genomic coordinates for variant analysis

**Note: This protocol is based on merging 3 pre-made .bed files containing genomic coordinates into a final file labeled jin_lab_exome_targets.bed. If you are starting from scratch, we recommend looking up an example bed file on UCSC https://genome.ucsc.edu/ or another bioinformatics site for a bed file containing some or most of the regions you are interested in.**

File locations (jin-lab): /gscmnt/gc2698/jin810/references

Files (jin-lab): 

- hg38_idt_target_region.bed (IDT_xGen_exome_panel_v1_targets)

- 94b23d66f667472690a7ee165e2037b6_hg38.bed (WashU-GMS_IDT_custom_xGen_exome_panel_v1_targets)

- hg38_target_regions_Apr2020.all.bed (knight_lab_yale_Custom_IDT_xGen_exome_panel_v1_targets)

### Software Requirements

- bedtools (using bedtools v2.17.0)
  - Default in gms environment on compute0 (jin-lab)
- Docker image: broadinstitute/gatk:4.1.7.0@sha256:192fedf9b9d65809da4a2954030269e3f311d296e6b5e4c6c7deec12c7fe84b2 (jin-lab)
  or
- Broadinstitute gatk:4.1.7.0 installation

### Protocol

1. Locate example .bed file you would like to extract intervals from or merge. 

2. Sort each of your bed files to ensure they are in the correct order.
    
    ```sort -V -k1 -k2,2n hg38_target_regions_Apr2020.all.bed > hg38_target_regions_Apr2020.all_sorted.bed```
    
    This will sort in ascending order of chromosome and chromosome coordinates. 
    
    To sort in lexicographical order, omit the -V parameter. (E.g. 1,10,11,12,2,21,22)
    
    ```sort -k1,1 -k2,2n bed_file > bed_file_lexo_sorted```
    
    ***Note: For sorting, make sure not to output into the same file name. This will create an empty ouput file erasing your orignal file. Output into a new file and change the file to the original name if you want to keep the sorted file name the same before sorting.***
    
3. Determine what features are missing from all three files. Choose one of the three files as the target file for comparing the other two files against. Output missing features into a new file.

   ```bedtools instersect -v -a bed_file1 -b bed_file2```

    The -v tells bedtools to show only the features in '-a' that are not also found in file '-b'

    In the example below, our destination file is labeled ```gms_and_idt_hg38_missing_feats.bed```.

    You may encounter an error at this step: ```Differing number of BED fields encountered at line: 3.  Exiting...```. The number of fields mismatch between bed files, specifically for ```hg38_target_regions_Apr2020.all.bed```. I'm not sure why this file is causing problems as the bed file "94b23d66f667472690a7ee165e2037b6_hg38.bed" also has more than three fields. I'm guessing the formatting of ```hg38_target_regions_Apr2020.all.bed``` is wrong. 
    
    To correct this, cut the last column from the bed file:
    
    ```cut -f 1-3 > hg38_target_regions_Apr2020.all_cut_sorted.bed```

    ```name<tab>chr-start<tab>chr-end``` See here for more information: https://bedtools.readthedocs.io/en/latest/content/general-usage.html

    ```bedtools intersect -v -a 94b23d66f667472690a7ee165e2037b6_hg38.bed -b hg38_target_regions_Apr2020.all_cut_sorted.bed > gms_and_idt_hg38_missing_feats.bed```

    ```bedtools intersect -v -a hg38_idt_target_regions.bed -b hg38_target_regions_Apr2020.all_cut_sorted.bed >> gms_and_idt_hg38_missing_feats.bed```

4. Add padding around intervals (optional).
    
    If we look at the missing features using the UCSC genome browser, the intervals have no padding around our target exomes. If we want to look at variants in splice sites, we need to add bp (padding) around each interval. GATK recommneds 100bp padding around exomes. We can add this padding with bedtools slop and a "genome" file. The genome file must be sorted and contain the end coordinates of each chromosome so that the program does not exceed chromosomal end positions.

    ```bedtools slop -i gms_and_idt_hg38_missing_feats_cut_sorted.bed -g hg38_genome_all_regions_sorted_myg.bed -b 100 > gms_and_idt_hg38_missing_feats_cut_sorted_100bp_pad.bed```
    
    -b specifies the amount of padding to add around each site. 
    
    See here for an example of the "genome" file. [hg38_sorted.genome.bed](./bed_files/hg38_sorted.genome.bed)
    
5. Concatenate the missing features and the features from the file you compared against. In this case, the file we compared against is hg38_target_regions_Apr2020

    ``` cat gms_and_idt_hg38_missing_feats_cut_sorted_100bp_pad.bed > jin_lab_exome_targets.bed && cat hg38_target_regions_Apr2020.all_cut_sorted.bed >> jin_lab_exome_targets.bed```

6. Now, re-sort the file with the concatenated features. *It is always good to double check that the size of the new concatenated file matches the sum of the file used for the concatenation.

    ```sort -V -k1 -k2,2n jin_lab_exome_targets.bed >j in_lab_exome_targets_sorted.bed```
    
    We can use this file for HaploTypeCaller and BQSR to call bp for the padded exome targets we will provide from this file.
    
7. For joint-calling, we need to convert the .bed file into a interval file that contains a header. To do this, you need to use Picard Bed to Interval List. 

    On the washU compute0 cluster we can use the following docker image:
    ```broadinstitute/gatk:4.1.7.0@sha256:192fedf9b9d65809da4a2954030269e3f311d296e6b5e4c6c7deec12c7fe84b2```

    The following command can be used with bsub or interactively to create the interval file. See below for the command with an interactive docker shell using the image above. 
    
    ```/gatk/gatk BedToIntervalList -I $input_file.bed -O output_file.list -SD reference_dictionary```
    
    ```/gatk/gatk BedToIntervalList -I jin_lab_exome_targets.bed  -O jin_lab_exome_targets_2.list -SD /gscmnt/gc2560/core/model_data/ref_build_aligner_index_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/aligner-index-blade18-1-1.gsc.wustl.edu-tmooney-331-75fff591a14f4f7c910247fc39c4ea7f/bwamem/0_7_15/all_sequences.dict```

See here for more information: https://gatk.broadinstitute.org/hc/en-us/articles/360042913631-CreateSequenceDictionary-Picard-
