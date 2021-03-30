import os
import hail as hl


hl.init()

format_gnomad_mt(chrom)
	#Import Exomes GNOMAD TABLE and modify for easier manipulation
	gnomad_e = hl.read_table('/gpfs/ycga/scratch60/kahle/sp2349/combined_weilai_mts/combined.filtered.gnomad.r2.1.1.sites.{}.mt')

	#If NA annotations for bravo, make value == 0
	gnomad_e = gnomad_e.annotate(bravo_freeze8 = hl.if_else(hl.is_missing(gnomad_e.bravo_freeze8) == True,0.0,gnomad_e.bravo_freeze8))

	#Check for missing MetaSVM, CADD, or Bravo frequencies. If exome missing use genome freqs and vice versa.
	#Joining of the tables causes NA values for positions missing in either dataset. Genomes have some positions missing in Exomes..etc
	combined = combined.annotate(MetaSVM_pred=hl.if_else(hl.is_missing(combined.info.MetaSVM_pred) == True, combined.info_1.MetaSVM_pred, combined.info.MetaSVM_pred))
	combined = combined.annotate(CADD16snv_PHRED=hl.if_else(hl.is_missing(combined.info.CADD16snv_PHRED) == True, hl.if_else(hl.is_missing(combined.info_1.CADD16snv_PHRED) == True, hl.null('float64'), hl.float64(combined.info_1.CADD16snv_PHRED)), hl.float64(combined.info.CADD16snv_PHRED)))
	combined = combined.annotate(CADD_phred=hl.if_else(hl.is_missing(combined.info.CADD13_PHRED) == True, hl.if_else(hl.is_missing(combined.info_1.CADD13_PHRED) == True, hl.null('float64'), hl.float64(combined.info_1.CADD13_PHRED)), hl.float64(combined.info.CADD13_PHRED)))
	combined = combined.annotate(MPC=hl.if_else(hl.is_missing(combined.info.MPC) == True, hl.if_else(hl.is_missing(combined.info_1.MPC_score) == True, hl.null('float64'), hl.float64(combined.info_1.MPC)),hl.float64(combined.info.MPC)))
	combined = combined.annotate(bravo=hl.if_else(hl.is_missing(combined.info.bravo) == True, combined.info_1.bravo, combined.info.bravo))

	Exonic_refGene
	#Add Genes and Function (Splicing/non-synonymous)
	#If exomes annotations is missing (NA), use Genome annotations.
	combined = combined.annotate(Exonic_refGene=hl.if_else(hl.is_missing(combined.info["ExonicFunc.refGene"][0]) == True, hl.if_else(hl.is_missing(combined.info_1["ExonicFunc.refGene"][0]) == True, hl.null('str'),combined.info_1["ExonicFunc.refGene"][0]), combined.info["ExonicFunc.refGene"][0]))
	combined = combined.annotate(Func_refGene=hl.if_else(hl.is_missing(combined.info["Func.refGene"][0]) == True, hl.if_else(hl.is_missing(combined.info_1["Func.refGene"][0]) == True, hl.null('str'),combined.info_1["Func.refGene"][0]), combined.info["Func.refGene"][0]))	
	
	#Make NA values 0 (float) if position missing in exomes
	combined = combined.annotate(info=combined.info.annotate(non_topmed_AC=hl.if_else(hl.is_missing(combined.non_topmed_AC) == True,0,combined.non_topmed_AC)))
	combined = combined.annotate(info=combined.info.annotate(non_topmed_AN=hl.if_else(hl.is_missing(combined.non_topmed_AN) == True,0,combined.non_topmed_AN)))
	combined = combined.annotate(info=combined.info.annotate(non_topmed_nhomalt=hl.if_else(hl.is_missing(non_topmed_nhomalt) == True,0,combined.non_topmed_nhomalt)))

	#Make NA values 0 (float) if position missing in exomes
	combined = combined.annotate(info_1=combined.info_1.annotate(non_topmed_AC=hl.if_else(hl.is_missing(combined.info_1.non_topmed_AC) == True,0,combined.info_1.non_topmed_AC)))
    combined = combined.annotate(info_1=combined.info_1.annotate(non_topmed_AN=hl.if_else(hl.is_missing(combined.info_1.non_topmed_AN) == True,0,combined.info_1.non_topmed_AN)))
    combined = combined.annotate(info_1=combined.info_1.annotate(non_topmed_nhomalt=hl.if_else(hl.is_missing(combined.info_1.non_topmed_nhomalt) == True,0,combined.info_1.non_topmed_nhomalt)))
	
	#Add nontopmed_AC,nontopmed_AN, non_topmed_nhomalt counts together from exome and genome (1)  datasets
	combined = combined.annotate(combined_nontopmed_AC=combined.info.nontopmed_AC + combined.info_1.nontopmed_AC)
	combined = combined.annotate(combined_nontopmed_AN=combined.info.nontopmed_AN + combined.info_1.nontopmed_AN)
	combined= combined.annotate(combined_nontopmed_nhomalt=combined.info.non_topmed_nhomalt + combined.info_1.non_topmed_nhomalt)

	final.write('/gpfs/ycga/scratch60/kahle/sp2349/datasets/gnomad/combined.filtered.formatted.gnomad.r2.1.1.sites.{}.mt'.format(chrom),overwrite=True)
