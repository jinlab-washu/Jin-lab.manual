# Protocol to Benchmark WES Variant calls using giab NA12878-HG001


Requirements
  - Docker
  - WashU compute0 lsf hpc
  - Called variants for gold standard benchmarking samples (here we use NIST NA12878)
  - High confidence vcf calls for benchmarking sample
  - High confidence regions (.bed) for benchmarking sample
  - Regions of interest (.bed) file. This can be the capture set for the gold standard sample excluding difficult to regions
  


## 1. Subset Joint-call VCF (if necessary)

**If you have a joint-called multi-sample vcf, you will need to subset the variant calls for only the nist/giab benchmark sample.*

### Method 1: GATK Select Variants

  1a. Load the docker image 

    bsub -Is -q research-hpc -a 'docker(broadinstitute/gatk:4.1.7.0)' -R "select[mem>16000] rusage[mem=15000]" /bin/bash

  Run the Select Variants Command

    Generic Example:
    
    /gatk/gatk SelectVariants -V $INPUT_VCF -R $REFERENCE_FILE --sample-name $SAMPLE_NAME/S --remove-unused-alternates --preserve-alleles -O OUTPUT_VCF
    
    WashU compute0 example:

      /gatk/gatk SelectVariants -V IDT_WES_hg38.vcf.gz -R /gscmnt/gc2560/core/model_data/ref_build_aligner_index_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/aligner-index-blade18-1-1.gsc.wustl.edu-tmooney-331-75fff591a14f4f7c910247fc39c4ea7f/bwamem/0_7_15/all_sequences.fa --sample-name NA12878-HG001 --remove-unused-alternates --preserve-alleles -O NA12878_no-alt_no-trim_w_ref.vcf.gz
      
   (Optional) Validate new VCF subset with Validate Variants
    
    Generic Example:
    
    /gatk/gatk ValidateVariants -V $INPUT_VCF -R $REFERENCE_FILE --dbsnp $DBSNP_FILE
    
    WashU compute0 example:
    
    /gatk/gatk ValidateVariants -V NA12878_no-alt_no-trim_w_ref.vcf.gz -R /gscmnt/gc2560/core/model_data/ref_build_aligner_index_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/aligner-index-blade18-1-1.gsc.wustl.edu-tmooney-331-75fff591a14f4f7c910247fc39c4ea7f/bwamem/0_7_15/all_sequences.fa --dbsnp /gscmnt/gc2560/core/build_merged_alignments/detect-variants--linus2112.gsc.wustl.edu-jwalker-19443-e48c595a620a432c93e8dd29e4af64f2/snvs.hq.vcf.gz


  1b. Load docker image
  
  ```bsub -Is -R "select[mem>15000] rusage[mem=15000]" -q research-hpc -a 'docker(sam16711/hap.py@sha256:f82481e5411aab643e99c66f47f1024d14a1c84bde60f61fa820502b34353b77)' /bin/bash```
  
You can 
Find samples within a vcf file

/opt/hap.py/bin/bcftools query -l ./na12878_WES_hg38_bcf.vcf.gz

## 2. Run hap.py

**Notes:**
  - Best practices recommends using the vcfeval enging for hap.py. 
  See here for more information: https://github.com/ga4gh/benchmarking-tools or the best practices paper found here https://doi.org/10.1101/270157
  
  - The NA12878 gold standard sample used the nextera rapidcapture and expanded exome probe set. Therefore, we are using these regions to benchmark calls by our pipeline. To restrict analysis to these regions, we use the -R parameter followed by the associated .bed file for those target regions. The file is located here: /gscmnt/gc2698/jin810/references/nexterarapidcapture_expandedexome_targetedregions_hg38_liftover_sorted_merged.bed. 
  **USE THIS FILE FOR EXOME benchmarking NA12878 (-R PARAMETER)**
  
  - In order to restrict regions to distinct intervals with the -R parameter (e.g. exomes), you will need to have a sorted and merged bed file. For sorting see: [custom-interval-creation](custom-interval-creation.md#protocol) For merging use, ```bedtools merge -a $file.bed```.
  
2a. Load docker image

```bsub -Is -R "select[mem>15000] rusage[mem=15000]" -q research-hpc -a 'docker(sam16711/hap.py@sha256:f82481e5411aab643e99c66f47f1024d14a1c84bde60f61fa820502b34353b77)' /bin/bash```

2b. Run hap.py

*The truth vcf and bed file for NA12878 can be found here on compute0: /gscmnt/gc2698/jin810/known_sites*

*The giab NA1878 download repo can be found here ftp://ftp-trace.ncbi.nih.gov/ReferenceSamples/giab/data/NA12878/Garvan_NA12878_HG001_HiSeq_Exome*

    Generic Example:
    
    /opt/hap.py/bin/hap.py truth.vcf query.vcf -f confident.bed -o output_prefix -r reference.fa

    WashU compute0 Example (Interactive):
    
    /opt/hap.py/bin/hap.py /gscmnt/gc2698/jin810/known_sites/HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_PGandRTGphasetransfer.vcf.gz /gscmnt/gc2698/jin810/jointcalling/2284092a1c7f45b297475ade68d03118/cromwell-executions/JointGenotyping/9f724805-1082-4f60-b710-82d132e89e4e/call-FinalGatherVcf/execution/NA12878_no-alt_no-trim_w_ref.vcf.gz -f /gscmnt/gc2698/jin810/known_sites/HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_nosomaticdel_noCENorHET7.bed -o /gscmnt/gc2698/jin810/jointcalling/2284092a1c7f45b297475ade68d03118/cromwell-executions/JointGenotyping/9f724805-1082-4f60-b710-82d132e89e4e/call-FinalGatherVcf/execution/vcfeval/NA12878_nextera_no_diffcult_reg -r /gscmnt/gc2560/core/model_data/ref_build_aligner_index_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/aligner-index-blade18-1-1.gsc.wustl.edu-tmooney-331-75fff591a14f4f7c910247fc39c4ea7f/bwamem/0_7_15/all_sequences.fa -R /gscmnt/gc2698/jin810/references/nextera_without_difficult_regions_hg38.bed --engine vcfeval --engine-vcfeval-template /gscmnt/gc2698/jin810/references/hg38.sdf --engine-vcfeval-path /opt/hap.py/libexec/rtg-tools-install/rtg --threads 10
    
    WashU compute0 Example (Non-Interactive):
    
    bsub -oo /gscmnt/gc2698/jin810/jointcalling/2284092a1c7f45b297475ade68d03118/cromwell-executions/JointGenotyping/9f724805-1082-4f60-b710-82d132e89e4e/call-FinalGatherVcf/execution/vcfeval/hap_py_out.txt -eo /gscmnt/gc2698/jin810/jointcalling/2284092a1c7f45b297475ade68d03118/cromwell-executions/JointGenotyping/9f724805-1082-4f60-b710-82d132e89e4e/call-FinalGatherVcf/execution/vcfeval/hap_py_err.txt -R "select[mem>15000] rusage[mem=15000]" -q research-hpc -a 'docker(sam16711/hap.py@sha256:f82481e5411aab643e99c66f47f1024d14a1c84bde60f61fa820502b34353b77)' /opt/hap.py/bin/hap.py /gscmnt/gc2698/jin810/known_sites/HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_PGandRTGphasetransfer.vcf.gz /gscmnt/gc2698/jin810/jointcalling/2284092a1c7f45b297475ade68d03118/cromwell-executions/JointGenotyping/9f724805-1082-4f60-b710-82d132e89e4e/call-FinalGatherVcf/execution/NA12878_no-alt_no-trim_w_ref.vcf.gz -f /gscmnt/gc2698/jin810/known_sites/HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_nosomaticdel_noCENorHET7.bed -o /gscmnt/gc2698/jin810/jointcalling/2284092a1c7f45b297475ade68d03118/cromwell-executions/JointGenotyping/9f724805-1082-4f60-b710-82d132e89e4e/call-FinalGatherVcf/execution/vcfeval/NA12878_nextera_no_diffcult_reg -r /gscmnt/gc2560/core/model_data/ref_build_aligner_index_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/aligner-index-blade18-1-1.gsc.wustl.edu-tmooney-331-75fff591a14f4f7c910247fc39c4ea7f/bwamem/0_7_15/all_sequences.fa -R /gscmnt/gc2698/jin810/references/nextera_without_difficult_regions_hg38.bed --engine vcfeval --engine-vcfeval-template /gscmnt/gc2698/jin810/references/hg38.sdf --engine-vcfeval-path /opt/hap.py/libexec/rtg-tools-install/rtg --threads 10
    
*Note: If the non-interactive version fails. Run it interactively. That seems to fix it.

## 3. Calculate Coverage Statistics

```bsub -Is -R "select[mem>16000] rusage[mem=15000]" -q research-hpc -a 'docker(biocontainers/bedtools:v2.27.1dfsg-4-deb_cv1@sha256:c042e405f356bb44cc0d7a87b4528d793afb581f0961db1d6da6e0a7e1fd3467)' /bin/bash```

```bedtools coverage -header -b nexterarapidcapture_expandedexome_targetedregions_hg38_liftover_sorted_merged.bed -a HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_nosomaticdel_noCENorHET7.bed > benchmarking_stats/nextera_coverage_std-out_high_conf.txt```

#CODE below computes the coverage for each interval in a overlapped by b. Therefore, output is each interval of a with the amount of coverage by -b.

bedtools coverage -header -b nexterarapidcapture_expandedexome_targetedregions_hg38_liftover_sorted_merged.bed -a HG001_GRCh38_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-10X-SOLID_CHROM1-X_v.3.3.2_highconf_nosomaticdel_noCENorHET7.bed > benchmarking_stats/nextera_coverage_std-out_high_conf.txt

  Tab-delmimited output:
  
[CHROM] [START] [END] [DEPTH] [bp overlap of "-a" interval in "-b"] [Length of A Interval] [Fraction of -a interval covered in -b]

## 4. Determine false negative variants and quality from hap.py results

1. Load Docker Image

	```bsub -Is -R "select[mem>15000] rusage[mem=15000]" -q research-hpc -a 'docker(sam16711/hap.py@sha256:f82481e5411aab643e99c66f47f1024d14a1c84bde60f61fa820502b34353b77)' /bin/bash```
	
*NOTE: Use the ALL row for calculating Benchmarking results. Using the PASS filter seems to show inaccurate results, TP show up as FN even though genotypes match the high confidence (TRUTH) vcf file. Additionally, using the PASS filter decreases the FP and increases the FN results. If the --pass-only parameter is passed to hap.py, the output vcf will only contain the variants filtered by "PASS"*

*NOTE2: Due to differences in the merged gvcf from HaplotypeCaller, the benchmark vcf that is created by hap.py, and the final joint-called, subset vcf file, there are a lot of steps that extract coordinates instead of comparing the vcf's directly with bedtools or bcftools. This is to avoid errors. 

*FN = False Negative, FP = False Positive, TP = True Positive*

2. Extract Variant Coordinates (<CHROM><TAB><VARIANT_COORDINATE) from the hap.py output vcf. 
								 
    The hap.py output vcf will contain the coordinates for every TP, FP, and FN call. 
    
    ```/opt/hap.py/bin/bcftools view -H hap.py_output.vcf | grep FN | cut -f1-2 > hap.py_output_FN_coord.vcf.txt```

3. Gather FN variants from merged gvcf (haplotypecaller output) using the FN coordinates file created in step 1.
            
    ```/opt/hap.py/bin/bcftools view -h gold_standard_merged_gvcf.vcf.gz > gold_standard_merged_gvcf_FN.vcf && /opt/hap.py/bin/bcftools view -H -R hap.py_output_FN_coord.vcf.txt gold_standard_merged_gvcf.vcf.gz >> gold_standard_merged_gvcf_FN.vcf```

4. Compress the vcf to vcf.gz
        
    ```/opt/hap.py/bin/bgzip gold_standard_merged_gvcf_FN.vcf```
	
5. Determine the low quality FN variant calls that do not pass Read Depth and Genotype Quality filters
        
    ```/opt/hap.py/bin/bcftools filter -i "DP < 8 || GQ <= 20" gold_standard_merged_gvcf_FN.vcf -o gold_standard_merged_gvcf_filtered_FN.vcf.gz -O z```

6. Determine the FN variant calls that pass Read Depth and Genotype Quality filters 
        
    ```/opt/hap.py/bin/bcftools filter -e "DP < 8 || GQ <= 20" gold_standard_merged_gvcf_FN.vcf -o gold_standard_merged_gvcf_passed_FN.vcf.gz -O z```

7. Count the number of low_quality FN calls and high_quality FN call as compared to all FN calls.

    Total FN = ```/opt/hap.py/bin/bcftools view -H gold_standard_merged_gvcf_FN.vcf | wc -l```

    Total low quality FN = ```/opt/hap.py/bin/bcftools view -H gold_standard_merged_gvcf_filtered_FN.vcf.gz | wc -l```

    Total high quality FN = ```/opt/hap.py/bin/bcftools view -H gold_standard_merged_gvcf_passed_FN.vcf.gz | wc -l```

    **QC Check**
    Calculate any regions not called from HaplotypeCaller

    Missed FN calls = ```bedtools intersect -v -a gold_standard_merged_gvcf_FN.vcf -b gold_standard_merged_gvcf.vcf.gz```

8. Determine the number of passed FN calls that are in the final joint-genotyped vcf

    Extract Passed FN coordinates from gold_standard_merged_gvcf_passed_FN.vcf.gz created in step 7.
    
    ```/opt/hap.py/bin/bcftools view -H gold_standard_merged_gvcf_passed_FN.vcf.gz | cut -f1-2 > gold_standard_merged_gvcf_passed_FN.vcf.gz.txt```

9. Extract passed FN variants from the final joint-genotyped vcf

    ```/opt/hap.py/bin/bcftools view -h gold_standard_jg.vcf.gz > gold_standard_jg_passed_FN.vcf && /opt/hap.py/bin/bcftools view -H -R gold_standard_merged_gvcf_passed_FN.vcf.gz.txt gold_standard_jg.vcf.gz >> gold_standard_jg_passed_FN.vcf```
	
10. Compress vcf created in step 9

    ```/opt/hap.py/bin/bgzip gold_standard_jg_passed_FN.vcf```

11. Determine the number of FN variants in final joint-genotyped vcf

    ```/opt/hap.py/bin/bcftools view -H gold_standard_jg_passed_FN.vcf.gz | wc -l```

10. Determine number of variants that have low MQ values (low Mapping scores) from passed FN calls in joint-genotyped vcf

    ```/opt/hap.py/bin/bcftools filter -i "MQ < 40" gold_standard_jg_passed_FN.vcf.gz -o low_MQ_in_gold_standard_jg_passed_FN.vcf.gz -O z```

11. Determine number of variants that have high MQ values (high mapping scores) from passed FN calls in joint-genotyped vcf
  
    ```/opt/hap.py/bin/bcftools filter -e "MQ < 40" gold_standard_jg_passed_FN.vcf.gz -o high_MQ_in_gold_standard_jg_passed_FN.vcf.gz -O z```

12. Subtract low MQ variant calls from the passed FN calls in the merged gvcf created in step 7

    ```bedtools subtract -a gold_standard_merged_gvcf_passed_FN.vcf.gz -b low_MQ_in_gold_standard_jg_passed_FN.vcf.gz > all_high_qual_FN_final.vcf.gz```

13. Count number of variants final files to ensure they add up

    Total High Quality FN variant calls = ```/opt/hap.py/bin/bcftools view -H all_high_qual_FN_final.vcf.gz | wc -l```

    Total FN variant calls Filtered by Joint-Genotyping = ```/opt/hap.py/bin/bcftools view -H gold_standard_jg_passed_FN.vcf.gz | wc -l```

    Total FN variant calls that did not pass MQ cutoff (MQ < 40) = ```/opt/hap.py/bin/bcftools view -H low_MQ_in_gold_standard_jg_passed_FN.vcf.gz | wc -l```

    Total FN variants calls that passed MQ cutoff (MQ >= 40) = ```/opt/hap.py/bin/bcftools view -H high_MQ_in_gold_standard_jg_passed_FN.vcf.gz | wc -l```

### Troubleshooting

----

#### Error 1

2020-06-25 17:18:58,372 ERROR    One of the preprocess jobs failed

2020-06-25 17:18:58,373 ERROR    Traceback (most recent call last):

2020-06-25 17:18:58,373 ERROR      File "/opt/hap.py/bin/hap.py", line 529, in <module>
2020-06-25 17:18:58,374 ERROR        main()
  
2020-06-25 17:18:58,374 ERROR      File "/opt/hap.py/bin/hap.py", line 383, in main
2020-06-25 17:18:58,374 ERROR        convert_gvcf_to_vcf=args.convert_gvcf_query)

2020-06-25 17:18:58,374 ERROR      File "/opt/hap.py/bin/pre.py", line 206, in preprocess
2020-06-25 17:18:58,375 ERROR        haploid_x=gender == "male")

2020-06-25 17:18:58,375 ERROR      File "/opt/hap.py/lib/python27/Haplo/partialcredit.py", line 214, in partialCredit
2020-06-25 17:18:58,375 ERROR        raise Exception("One of the preprocess jobs failed")

2020-06-25 17:18:58,375 ERROR    Exception: One of the preprocess jobs failed

**Potential ALT allele error. Alt alleles occuring in some positions that do not correspond with any sample genotypes. 
Check VCF format with GATK ValidateVariants. 
If you see the error: ```fails strict validation of type ALL: one or more of the ALT allele(s) for the record at position chr$:$ are not observed at all in the sample genotypes```, use GATK SelectVariants with --remove-unused-alternates paramter**

----
#### Warning 1:

2020-06-25 17:18:56,417 WARNING  [W] too many AD fields at chr7:154795793 max_ad = 2 retrieved: 3

2020-06-25 17:18:56,418 WARNING  [W] too many AD fields at chr7:154795796 max_ad = 2 retrieved: 3

2020-06-25 17:18:56,430 WARNING  [W] too many AD fields at chr9:135090387 max_ad = 2 retrieved: 3

2020-06-25 17:18:56,833 WARNING  [W] too many AD fields at chr9:110375287 max_ad = 2 retrieved: 3

2020-06-25 17:18:56,833 WARNING  [W] too many AD fields at chr9:111544347 max_ad = 4 retrieved: 5

2020-06-25 17:18:56,890 WARNING  [W] too many AD fields at chr8:135862647 max_ad = 2 retrieved: 3

2020-06-25 17:18:58,033 WARNING  [W] too many AD fields at chr9:124854513 max_ad = 2 retrieved: 3

2020-06-25 17:18:58,034 WARNING  [W] too many AD fields at chr9:125335387 max_ad = 2 retrieved: 3

*Not sure what causes this. Seems to be Allelic depths being off. Seems okay to move forward with warning as AD is not used for benchmarking. 
See here for more info: https://github.com/Illumina/hap.py/issues/86

----
**Error encountered 7-8-20**

2020-07-08 16:12:49,966 ERROR    Error running rtg tools. Return code was 1, output:  / /opt/hap.py/lib/python27/Haplo/../../../libexec/rtg-tools-install/rtg: line 217: /gsc/bin/awk: No such file or directory
Exception in thread "main" java.lang.UnsupportedClassVersionError: com/rtg/util/ChooseMemory : Unsupported major.minor version 52.0
	at java.lang.ClassLoader.defineClass1(Native Method)
	at java.lang.ClassLoader.defineClassCond(ClassLoader.java:632)
	at java.lang.ClassLoader.defineClass(ClassLoader.java:616)
	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:141)
	at java.net.URLClassLoader.defineClass(URLClassLoader.java:283)
	at java.net.URLClassLoader.access$000(URLClassLoader.java:58)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:197)
	at java.security.AccessController.doPrivileged(Native Method)
	at java.net.URLClassLoader.findClass(URLClassLoader.java:190)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:307)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:301)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:248)
Could not find the main class: com.rtg.util.ChooseMemory.  Program will exit.
Could not automatically choose percentage based memory allocation, check configuration. Using Java default.
Exception in thread "main" java.lang.UnsupportedClassVersionError: com/rtg/RtgTools : Unsupported major.minor version 52.0
	at java.lang.ClassLoader.defineClass1(Native Method)
	at java.lang.ClassLoader.defineClassCond(ClassLoader.java:632)
	at java.lang.ClassLoader.defineClass(ClassLoader.java:616)
	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:141)
	at java.net.URLClassLoader.defineClass(URLClassLoader.java:283)
	at java.net.URLClassLoader.access$000(URLClassLoader.java:58)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:197)
	at java.security.AccessController.doPrivileged(Native Method)
	at java.net.URLClassLoader.findClass(URLClassLoader.java:190)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:307)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:301)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:248)
Could not find the main class: com.rtg.RtgTools. Program will exit.
 

2020-07-08 16:12:49,967 ERROR    Traceback (most recent call last):
2020-07-08 16:12:49,967 ERROR      File "/opt/hap.py/bin/hap.py", line 529, in <module>
2020-07-08 16:12:49,967 ERROR        main()
2020-07-08 16:12:49,968 ERROR      File "/opt/hap.py/bin/hap.py", line 473, in main
2020-07-08 16:12:49,968 ERROR        tempfiles += Haplo.vcfeval.runVCFEval(args.vcf1, args.vcf2, output_name, args)
2020-07-08 16:12:49,968 ERROR      File "/opt/hap.py/lib/python27/Haplo/vcfeval.py", line 98, in runVCFEval
2020-07-08 16:12:49,968 ERROR        raise Exception("Error running rtg tools. Return code was %i, output: %s / %s \n" % (rc, o, e))
2020-07-08 16:12:49,969 ERROR    Exception: Error running rtg tools. Return code was 1, output:  / /opt/hap.py/lib/python27/Haplo/../../../libexec/rtg-tools-install/rtg: line 217: /gsc/bin/awk: No such file or directoryException in thread "main" java.lang.UnsupportedClassVersionError: com/rtg/util/ChooseMemory : Unsupported major.minor version 52.0	at java.lang.ClassLoader.defineClass1(Native Method)	at java.lang.ClassLoader.defineClassCond(ClassLoader.java:632)	at java.lang.ClassLoader.defineClass(ClassLoader.java:616)	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:141)	at java.net.URLClassLoader.defineClass(URLClassLoader.java:283)	at java.net.URLClassLoader.access$000(URLClassLoader.java:58)	at java.net.URLClassLoader$1.run(URLClassLoader.java:197)	at java.security.AccessController.doPrivileged(Native Method)	at java.net.URLClassLoader.findClass(URLClassLoader.java:190)	at java.lang.ClassLoader.loadClass(ClassLoader.java:307)	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:301)	at java.lang.ClassLoader.loadClass(ClassLoader.java:248)Could not find the main class: com.rtg.util.ChooseMemory.  Program will exit.Could not automatically choose percentage based memory allocation, check configuration. Using Java default.Exception in thread "main" java.lang.UnsupportedClassVersionError: com/rtg/RtgTools : Unsupported major.minor version 52.0	at java.lang.ClassLoader.defineClass1(Native Method)	at java.lang.ClassLoader.defineClassCond(ClassLoader.java:632)	at java.lang.ClassLoader.defineClass(ClassLoader.java:616)	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:141)	at java.net.URLClassLoader.defineClass(URLClassLoader.java:283)	at java.net.URLClassLoader.access$000(URLClassLoader.java:58)	at java.net.URLClassLoader$1.run(URLClassLoader.java:197)	at java.security.AccessController.doPrivileged(Native Method)	at java.net.URLClassLoader.findClass(URLClassLoader.java:190)	at java.lang.ClassLoader.loadClass(ClassLoader.java:307)	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:301)	at java.lang.ClassLoader.loadClass(ClassLoader.java:248)Could not find the main class: com.rtg.RtgTools. Program will exit. 
  
Fix1: Use path to sdf file for reference fasta for ----engine-vcfeval-template $SDF_REF instead of producing on-the-fly during the run.
	Created sdf using: ```/opt/hap.py/libexec/rtg-tools-install/rtg format -o /gscmnt/gc2698/jin810/references/hg38.sdf /gscmnt/gc2560/core/model_data/ref_build_aligner_index_data/2887491634/build21f22873ebe0486c8e6f69c15435aa96/aligner-index-blade18-1-1.gsc.wustl.edu-tmooney-331-75fff591a14f4f7c910247fc39c4ea7f/bwamem/0_7_15/all_sequences.fa```
	
	Path: /gscmnt/gc2698/jin810/references/hg38.sdf

Fix2: Use --engine-vcfeval-path to correct the path of rgt to the one found in the docker image:

	--engine-vcfeval-path /opt/hap.py/libexec/rtg-tools-install/rtg

----

Validate Variants via gatk ValidateVariants

docker: "broadinstitute/gatk:4.1.7.0"

IDT_WES_hg38.vcf.gz  was subsetted for NA12878-HG001 using gatk SelectVariants ---> NA12878_WES_hg38.vcf.gz 

```/gatk/gakt ValidateVariants NA12878_WES_hg38.vcf.gz ```

Fails: NA12878_WES_hg38.vcf.gz fails strict validation of type ALL: one or more of the ALT allele(s) for the record at position chr1:12807 are not observed at all in the sample genotypes

/gatk/gakt ValidateVariants IDT_WES_hg38.vcf.gz

Passed
