# Pre-process GNOMAD v2.1.1 VCFs

> Date: 2021 Jun
> 
> Follower: Po-Ying
> 
> Server: Yale Ruddle server

This steps follow Sam Peter's document, try to replicate each steps. 

### Requirments:

1. gnomAD exome VCF: `/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/vcfs/weilai_vcfs/gnomad.exomes.r2.1.1.sites.5.decomposed.normalized_anno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.vcf.gz`
2. gnomAD genome VCF: `/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/vcfs/weilai_vcfs/gnomad.genomes.r2.1.1.sites.5.decomposed.normalized.hg19_multianno.hg19_multianno.vcf.gz`

### Details:

* Testing folder (scratch60): `/gpfs/ycga/scratch60/kahle/pf374/CaseControlAnalysis/preprocessGenomadVcfs`
* Testing output folder (scratch60): `/gpfs/ycga/scratch60/kahle/pf374/CaseControlAnalysis/preprocessGenomadVcfs/gnomad/MetricsTable`
* Final folder: `/gpfs/ycga/project/kahle/pf374/projects/CaseControl_PreprocessGnomadVCFs`

#### step1 - CONVERT Weilai gnomad2.1.1 vcfs to matrics tables

> `preprocessGenomadVcfs/CaseControl_Preprocess_01_gnomAD_vcf2ht.py`

```
### CONVERT Weilai gnomad2.1.1 vcfs to matrix tables
### Takes a file of vcf's path as input. In the code below, this is called 'weilai_vcfs_subset.txt'

import os
import hail as hl

hl.init()

out_path = "/gpfs/ycga/scratch60/kahle/pf374/CaseControlAnalysis/preprocessGenomadVcfs/gnomad/MetricsTable"
exomes_vcf = "/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/vcfs/weilai_vcfs/gnomad.exomes.r2.1.1.sites.5.decomposed.normalized_anno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.vcf.gz"
genomes_vcf = "/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/vcfs/weilai_vcfs/gnomad.genomes.r2.1.1.sites.5.decomposed.normalized.hg19_multianno.hg19_multianno.vcf.gz"

# clean out all the space around "input_vcf" string
vcf_exome = exomes_vcf.strip()
vcf_genomes = genomes_vcf.strip()
print("Input Exomes VCF name: {}".format(vcf_exome))
print("Input Genomes VCF name: {}".format(vcf_genomes))
# Read in vcf as Metrics Table:
exome_mt = hl.import_vcf(vcf_exome,force_bgz=True,reference_genome='GRCh37')
genome_mt = hl.import_vcf(vcf_genomes,force_bgz=True,reference_genome='GRCh37')
exome_out_name = os.path.join(out_path,os.path.basename(os.path.splitext(os.path.splitext(vcf_exome)[0])[0] + ".mt"))
genome_out_name = os.path.join(out_path,os.path.basename(os.path.splitext(os.path.splitext(vcf_genomes)[0])[0] + ".mt"))
print("Exome - Output Metrics Table name: {}".format(exome_out_name))
print("Genome - Output Metrics Table name: {}".format(genome_out_name))
exome_mt.write(exome_out_name,overwrite=True)
genome_mt.write(genome_out_name,overwrite=True)

```

#### step2 - Combind exome/genome hail table together:

> `preprocessGenomadVcfs/CaseControl_Preprocess_02_CombineExomeGenomeHT.py`

```
import os
import hail as hl

hl.init()

### VAR:
chrom = 5 # Change chromosome here
out_folder = "/gpfs/ycga/scratch60/kahle/pf374/CaseControlAnalysis/preprocessGenomadVcfs/gnomad/MetricsTable"
exome_mt = "{}/gnomad.exomes.r2.1.1.sites.{}.decomposed.normalized_anno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.mt".
format(out_folder,chrom)
genome_mt = "{}/gnomad.genomes.r2.1.1.sites.{}.decomposed.normalized.hg19_multianno.hg19_multianno.mt".format(out_folder, chrom)
combined_mt = "{}/combined.filtered.gnomad.r2.1.1.sites.{}.ht".format(out_folder, chrom)

#Import Exomes GNOMAD TABLE and modify for easier manipulation
#gnomad_e = hl.read_matrix_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted/gnomad.exomes.r2.1.1.sites.{}.decomposed.normalized_anno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.mt'.format(chrom))
gnomad_e = hl.read_matrix_table(exome_mt)
gnomad_e = gnomad_e.rows()
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(bravo = hl.if_else(hl.is_missing(gnomad_e.info.bravo[0]) == True,0.0,hl.float64(gnomad_e.info.bravo[0]))))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(CADD16snv_PHRED = hl.float64(gnomad_e.info.CADD16snv_PHRED[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(CADD_phred = hl.float64(gnomad_e.info.CADD_phred[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(MetaSVM_pred = gnomad_e.info.MetaSVM_pred[0]))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_AC = hl.int64(gnomad_e.info.non_topmed_AC[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_AN = gnomad_e.info.non_topmed_AN))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_nhomalt = hl.int64(gnomad_e.info.non_topmed_nhomalt[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(Exonic_refGene = gnomad_e.info["ExonicFunc.refGene"][0]))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(Func_refGene = gnomad_e.info["Func.refGene"][0]))
#Filter out variants that did not pass filters. "RF or AC0"
gnomad_e = gnomad_e.filter((gnomad_e.filters.contains('AC0')) | (gnomad_e.filters.contains('RF')),keep=False)

#Import Genomes GNOMAD TABLE and modify for easier manipulation
#gnomad_g = hl.read_matrix_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted/gnomad.genomes.r2.1.1.sites.{}.decomposed.normalized.hg19_multianno.hg19_multianno.mt'.format(chrom))
gnomad_g = hl.read_matrix_table(genome_mt)
gnomad_g = gnomad_g.rows()
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(bravo = hl.if_else(hl.is_missing(gnomad_g.info.bravo[0]) == True,0.0,hl.float64(gnomad_g.info.bravo[0]))))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(CADD16snv_PHRED = hl.float64(gnomad_g.info.CADD16snv_PHRED[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(CADD_phred = hl.float64(gnomad_g.info.CADD_phred[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(MetaSVM_pred = gnomad_g.info.MetaSVM_pred[0]))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_AC = hl.int64(gnomad_g.info.non_topmed_AC[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_AN = gnomad_g.info.non_topmed_AN))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_nhomalt = hl.int64(gnomad_g.info.non_topmed_nhomalt[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(Exonic_refGene = gnomad_g.info["ExonicFunc.refGene"][0]))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(Func_refGene = gnomad_g.info["Func.refGene"][0]))
#Filter out variants that did not pass filters. "RF or AC0"
gnomad_g = gnomad_g.filter((gnomad_g.filters.contains('AC0')) | (gnomad_g.filters.contains('RF')),keep=False)

#Combind TWO Metrics Table:
combined = gnomad_e.join(gnomad_g,how='outer')

#combined.write('/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/combined.filtered.gnomad.r2.1.1.sites.{}.ht'.format(chrom),overwrite=True)
combined.write(combined_mt,overwrite=True)

```

#### step3 - Format the combined hail table:

> `preprocessGenomadVcfs/CaseControl_Preprocess_03_FormatedCombinedHT.py`

```
import os
import hail as hl

### CPOY from: /gpfs/ycga/project/kahle/sp2349/weilai_gnomad/code/format_weilai_combined_mt.py
### EDIT by Po-Ying (2021/06/23)

hl.init()

# VARs:
chrom = 5
out_dir = "/gpfs/ycga/scratch60/kahle/pf374/CaseControlAnalysis/preprocessGenomadVcfs/gnomad/MetricsTable"

#Import Combind gnomAD exome/genome Hail Table (hail.table.Table):
combined = hl.read_table('{}/combined.filtered.gnomad.r2.1.1.sites.{}.ht'.format(out_dir,chrom))

#Check for missing MetaSVM, CADD, or Bravo frequencies. If exome missing use genome freqs and vice versa.
#Exome using info; Genome using info_1.
#Joining of the tables causes NA values for positions missing in either dataset. 
#Genomes have some positions missing in Exomes..etc
# MetaSVM_pred:
combined = combined.annotate(MetaSVM_pred=hl.if_else(combined.info.MetaSVM_pred == 'NA', hl.if_else(combined.info_1.MetaSVM_pred == 'NA',hl.null('str'),combined.info_1.MetaSVM_pred),combined.info.MetaSVM_pred))

# CADD16snv_PHRED:
combined = combined.annotate(CADD16snv_PHRED=hl.if_else(hl.is_missing(combined.info.CADD16snv_PHRED) == True, hl.if_else(hl.is_missing(combined.info_1.CADD16snv_PHRED) == True, hl.null('float64'), hl.float64(combined.info_1.CADD16snv_PHRED)), hl.float64(combined.info.CADD16snv_PHRED)))
# CADD_phred: (CADD13)
combined = combined.annotate(CADD_phred=hl.if_else(hl.is_missing(combined.info.CADD_phred) == True, hl.if_else(hl.is_missing(combined.info_1.CADD_phred) == True, hl.null('float64'), hl.float64(combined.info_1.CADD_phred)), hl.float64(combined.info.CADD_phred)))
# MPC:
combined = combined.annotate(MPC=hl.if_else(combined.info.MPC[0] == 'NA', hl.if_else(combined.info_1.MPC[0] == 'NA', hl.null('float64'), hl.float64(combined.info_1.MPC[0])),hl.float64(combined.info.MPC[0])))
# BRAVO:
combined = combined.annotate(bravo=hl.if_else(hl.is_missing(combined.info.bravo) == True, hl.if_else(hl.is_missing(combined.info_1.bravo) == True,hl.null('float64'), hl.float64(combined.info_1.bravo)),hl.float64(combined.info.bravo)))

#Add Genes and Function (Splicing/non-synonymous)
#If exomes annotations is missing (NA), use Genome annotations.
# Exonic_refGene:
combined = combined.annotate(Exonic_refGene=hl.if_else(hl.is_missing(combined.info["ExonicFunc.refGene"][0]) == True, hl.if_else(hl.is_missing(combined
.info_1["ExonicFunc.refGene"][0]) == True, hl.null('str'),combined.info_1["ExonicFunc.refGene"][0]), combined.info["ExonicFunc.refGene"][0]))
# Func_refGene
combined = combined.annotate(Func_refGene=hl.if_else(hl.is_missing(combined.info["Func.refGene"][0]) == True, hl.if_else(hl.is_missing(combined.info_1[
"Func.refGene"][0]) == True, hl.null('str'),combined.info_1["Func.refGene"][0]), combined.info["Func.refGene"][0]))

#Process - NON_TOPMED_AC/AN/NHOMALT:
#Make NA values 0 (float) if position missing in exomes
combined = combined.annotate(info=combined.info.annotate(non_topmed_AC=hl.if_else(hl.is_missing(combined.info.non_topmed_AC) == True,0,combined.info.non_topmed_AC)))
combined = combined.annotate(info=combined.info.annotate(non_topmed_AN=hl.if_else(hl.is_missing(combined.info.non_topmed_AN) == True,0,combined.info.non_topmed_AN)))
combined = combined.annotate(info=combined.info.annotate(non_topmed_nhomalt=hl.if_else(hl.is_missing(combined.info.non_topmed_nhomalt) == True,0,combined.info.non_topmed_nhomalt)))
#Make NA values 0 (float) if position missing in genome
combined = combined.annotate(info_1=combined.info_1.annotate(non_topmed_AC=hl.if_else(hl.is_missing(combined.info_1.non_topmed_AC) == True,0,combined.info_1.non_topmed_AC)))
combined = combined.annotate(info_1=combined.info_1.annotate(non_topmed_AN=hl.if_else(hl.is_missing(combined.info_1.non_topmed_AN) == True,0,combined.info_1.non_topmed_AN)))
combined = combined.annotate(info_1=combined.info_1.annotate(non_topmed_nhomalt=hl.if_else(hl.is_missing(combined.info_1.non_topmed_nhomalt) == True,0,combined.info_1.non_topmed_nhomalt)))
#Add nontopmed_AC,nontopmed_AN, non_topmed_nhomalt counts together from exome and genome (1)  datasets (WHY?)
combined = combined.annotate(combined_nontopmed_AC=combined.info.non_topmed_AC + combined.info_1.non_topmed_AC)
combined = combined.annotate(combined_nontopmed_AN=combined.info.non_topmed_AN + combined.info_1.non_topmed_AN)
combined = combined.annotate(combined_nontopmed_nhomalt=combined.info.non_topmed_nhomalt + combined.info_1.non_topmed_nhomalt)

# Add rsid and quality filters from both genomes ane exomes
combined = combined.annotate(exome_rsid=hl.if_else(hl.is_missing(combined.rsid)==True,hl.null('str'),combined.rsid))
combined = combined.annotate(exome_qual=hl.if_else(hl.is_missing(combined.qual)==True,hl.null('float64'),combined.qual))
combined = combined.annotate(exome_filters = combined.filters) #set<str>
combined = combined.annotate(genome_rsid=hl.if_else(hl.is_missing(combined.rsid_1)==True,hl.null('str'),combined.rsid_1))
combined = combined.annotate(genome_qual=hl.if_else(hl.is_missing(combined.qual_1)==True,hl.null('float64'),combined.qual_1))
combined = combined.annotate(genome_filters = combined.filters_1) #set<str>

# Drop info and info_1 fields as no longer necessary
fields_to_drop = ['info','info_1','rsid','rsid_1','qual','qual_1','filters','filters_1']
combined = combined.drop(*fields_to_drop)

# Write to specified directory
combined.write('{}/combined.filtered.formatted.gnomad.r2.1.1.sites.{}.ht'.format(out_dir,chrom),overwrite=True)

```
