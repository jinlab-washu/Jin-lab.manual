# Using Annovar on Compute1

* Docker: `bioinfochrustrasbourg/annovar:latest` [link to docker hub](https://hub.docker.com/r/bioinfochrustrasbourg/annovar)
* Tools: `/home/TOOLS/tools/annovar/current/bin` (but we are not going to use this one)
* Folder on compute1: `/storage1/fs1/jin810/Active/annovar_20191024`
* Humandb path: `/storage1/fs1/jin810/Active/annovar_20191024/humandb`

### Example:

* Prepare humandb: 

1. CPOY `annovar_20191024.tar.gz` from Yale to WUSTL

2. Untar and leave the folder `/storage1/fs1/jin810/Active/annovar_20191024`


* Testing Docker on compute1:

```
[fup@compute1-client-3 ~]$ bsub -Is -G compute-jin810 -q general-interactive -a 'docker(bioinfochrustrasbourg/annovar:latest)' -n 16 -M 100GB -R 'rusage[mem=100GB] span[hosts=1]' /bin/bash
[fup@compute1-exec-97 ~]$ cd /storage1/fs1/jin810/Active/annovar_20191024
[fup@compute1-exec-97 annovar_20191024]$ ./annotate_variation.pl --downdb
Usage:
     annotate_variation.pl [arguments] <query-file|table-name> <database-location>

     Optional arguments:
            -h, --help                      print help message
            -m, --man                       print complete documentation
            -v, --verbose                   use verbose output
        
            Arguments to download databases or perform annotations
                --downdb                    download annotation database
                --geneanno                  annotate variants by gene-based annotation (infer functional consequence on genes)
                --regionanno                annotate variants by region-based annotation (find overlapped regions in database)
                --filter                    annotate variants by filter-based annotation (find identical variants in database)
...
     Version: $Date: 2018-04-16 00:43:31 -0400 (Mon, 16 Apr 2018) $

```

* Example:

Annotate VCF using `table_annovar.pl`. It will generated three output files: "$OUT".hg38_multianno.txt, "$OUT".hg38_multianno.vcf, and "$OUT".avinput.

```
[fup@compute1-exec-151 annovar_20191024]$ ./table_annovar.pl example/F309_vqsr.vcf humandb/ -buildver hg38 -out example/F309_vqsr -remove -protocol refGene,genomicSuperDups,clinvar_20190305,avsnp150,esp6500siv2_all,1000g2015aug_all,exac03,exac03nontcga,gnomad_exome,gnomad_genome,cadd16snv,cadd16indel,kaviar_20150923,dbnsfp41a,bravo_v8,mcap,revel,dbscsnv11 -operation g,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f -nastring . -vcfinput
NOTICE: the --polish argument is set ON automatically (use --nopolish to change this behavior)

NOTICE: Running with system command <convert2annovar.pl  -includeinfo -allsample -withfreq -format vcf4 example/F309_vqsr.vcf > example/F309_vqsr.avinput>
NOTICE: Finished reading 6803259 lines from VCF file
NOTICE: A total of 6799854 locus in VCF file passed QC threshold, representing 5583580 SNPs (3674310 transitions and 1909270 transversions) and 1437399 indels/substitutions
NOTICE: Finished writing allele frequencies based on 16750740 SNP genotypes (11022930 transitions and 5727810 transversions) and 4312197 indels/substitutions for 3 samples
WARNING: 52844 invalid alternative alleles found in input file

NOTICE: Running with system command <./table_annovar.pl example/F309_vqsr.avinput humandb/ -buildver hg38 -outfile example/F309_vqsr -remove -protocol refGene,genomicSuperDups,clinvar_20190305,avsnp150,esp6500siv2_all,1000g2015aug_all,exac03,exac03nontcga,gnomad_exome,gnomad_genome,cadd16snv,cadd16indel,kaviar_20150923,dbnsfp41a,bravo_v8,mcap,revel,dbscsnv11 -operation g,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f -nastring . -otherinfo>
NOTICE: the --polish argument is set ON automatically (use --nopolish to change this behavior)
-----------------------------------------------------------------
NOTICE: Processing operation=g protocol=refGene

NOTICE: Running with system command <annotate_variation.pl -geneanno -buildver hg38 -dbtype refGene -outfile example/F309_vqsr.refGene -exonsort -nofirstcodondel example/F309_vqsr.avinput humandb/>
NOTICE: Output files are written to example/F309_vqsr.refGene.variant_function, example/F309_vqsr.refGene.exonic_variant_function
NOTICE: Reading gene annotation from humandb/hg38_refGene.txt ... Done with 82500 transcripts (including 20366 without coding sequence annotation) for 28265 unique genes
NOTICE: Processing next batch with 5000000 unique variants in 5000000 input lines
NOTICE: Finished analyzing 1000000 query variants
NOTICE: Finished analyzing 2000000 query variants
NOTICE: Finished analyzing 3000000 query variants
NOTICE: Finished analyzing 4000000 query variants
NOTICE: Reading FASTA sequences from humandb/hg38_refGeneMrna.fa ... Done with 19667 sequences
WARNING: A total of 591 sequences will be ignored due to lack of correct ORF annotation
NOTICE: Processing next batch with 2073823 unique variants in 2073823 input lines
NOTICE: Finished analyzing 1000000 query variants
NOTICE: Finished analyzing 2000000 query variants
NOTICE: Reading FASTA sequences from humandb/hg38_refGeneMrna.fa ... Done with 10102 sequences
WARNING: A total of 591 sequences will be ignored due to lack of correct ORF annotation

NOTICE: Running with system command <coding_change.pl  example/F309_vqsr.refGene.exonic_variant_function.orig humandb//hg38_refGene.txt humandb//hg38_refGeneMrna.fa -alltranscript -out example/F309_vqsr.refGene.fa -newevf example/F309_vqsr.refGene.exonic_variant_function>
splice() offset past end of array at ./coding_change.pl line 281, <FASTA> line 160292.
Warning: 5 transcripts are flagged as having potential ORF issues (premature stopcodon or lack of stop codon)
-----------------------------------------------------------------
NOTICE: Processing operation=r protocol=genomicSuperDups
...


```
