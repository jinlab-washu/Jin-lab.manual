import os
import hail as hl


hl.init()

group_sel = "non_topmed"
#Import Exomes GNOMAD TABLE and modify for easier manipulation
gnomad_e = hl.read_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/gnomad.exomes.r2.1.1.bravo8-dbNSFP4.1a-fixed.chr5.ht')

#Filter out variants that did not pass filters. "RF or AC0"
gnomad_e = gnomad_e.filter((gnomad_e.filters.contains('AC0')) | (gnomad_e.filters.contains('RF')),keep=False)

#If NA annotations for bravo, make value == 0
gnomad_e = gnomad_e.annotate(bravo_freeze8 = hl.if_else(hl.is_missing(gnomad_e.bravo_freeze8) == True,0.0,gnomad_e.bravo_freeze8))

#Extract non_topmed group in gnomad table. (nontopmedAC, nontopmedAN, nontopmed_nhomalt)
group_e = gnomad_e.freq_index_dict.collect()[0][group_sel]
gnomad_e = gnomad_e.annotate(nontopmed_cases=gnomad_e.freq[group_e].AC-(gnomad_e.freq[group_e].homozygote_count *2))
gnomad_e = gnomad_e.annotate(nontopmed_AN=gnomad_e.freq[group_e].AN)
gnomad_e = gnomad_e.annotate(nontopmed_hom=gnomad_e.freq[group_e].homozygote_count)
gnomad_e = gnomad_e.annotate(nontopmed_AC=gnomad_e.freq[group_e].AC)
#Import Genomes GNOMAD TABLE and modify for easier manipulation
gnomad_g = hl.read_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/gnomad.genomes.r2.1.1.bravo8-dbNSFP4.1a-fixed.chr5.ht')

#Filter out variants that did not pass filters. "RF or AC0"
gnomad_g = gnomad_g.filter((gnomad_g.filters.contains('AC0')) | (gnomad_g.filters.contains('RF')),keep=False)

#If NA annotations for bravo, make value == 0
gnomad_g = gnomad_g.annotate(bravo_freeze8 = hl.if_else(hl.is_missing(gnomad_g.bravo_freeze8) == True,0.0,gnomad_g.bravo_freeze8))

#Extract non_topmed group in gnomad table. (nontopmedAC, nontopmedAN, nontopmed_nhomalt)
group_g = gnomad_g.freq_index_dict.collect()[0][group_sel]
gnomad_g = gnomad_g.annotate(nontopmed_cases=gnomad_g.freq[group_g].AC-(gnomad_g.freq[group_g].homozygote_count *2))
gnomad_g = gnomad_g.annotate(nontopmed_AN=gnomad_g.freq[group_g].AN)
gnomad_g = gnomad_g.annotate(nontopmed_hom=gnomad_g.freq[group_g].homozygote_count)
gnomad_g = gnomad_g.annotate(nontopmed_AC=gnomad_g.freq[group_g].AC)
combined = gnomad_e.join(gnomad_g,how='outer')

#Clean up MPC annotations
#combined = combined.annotate(MPC_score=combined.MPC_score.replace(".",""))
#combined = combined.annotate(MPC_score=combined.MPC_score.replace(";",""))
#combined = combined.annotate(MPC_score_1=combined.MPC_score_1.replace(";",""))
#combined = combined.annotate(MPC_score_1=combined.MPC_score_1.replace(".",""))
#Check for missing MetaSVM, CADD, or Bravo frequencies. If exome missing use genome freqs and vice versa.
#Joining of the tables causes NA values for positions missing in either dataset. Genomes have some positions missing in Exomes..etc
combined = combined.annotate(MetaSVM_pred=hl.if_else(hl.is_missing(combined.MetaSVM_pred) == True, combined.MetaSVM_pred_1, combined.MetaSVM_pred))
combined = combined.annotate(CADD_phred_hg19=hl.if_else(hl.is_missing(combined.CADD_phred_hg19) == True, hl.if_else(hl.is_missing(combined.CADD_phred_hg19_1) == True, hl.null('float64'), combined.CADD_phred_hg19_1), combined.CADD_phred_hg19))
combined = combined.annotate(CADD_phred=hl.if_else(hl.is_missing(combined.CADD_phred) == True, hl.if_else(hl.is_missing(combined.CADD_phred_1) == True, hl.null('float64'), combined.CADD_phred_1), combined.CADD_phred))
combined = combined.annotate(MPC=hl.if_else(hl.is_missing(combined.MPC_score) == True, hl.if_else(hl.is_missing(combined.MPC_score_1) == True, hl.null('str'), combined.MPC_score_1),combined.MPC_score))
combined = combined.annotate(bravo_freeze8=hl.if_else(hl.is_missing(combined.bravo_freeze8) == True, combined.bravo_freeze8_1, combined.bravo_freeze8))

#Add Genes and Function (Splicing/non-synonymous)
#If exomes annotations is missing (NA), use Genome annotations.
combined = combined.annotate(most_severe_consequence=hl.if_else(hl.is_missing(combined.vep.most_severe_consequence) == True, hl.if_else(hl.is_missing(combined.vep_1.most_severe_consequence) == True, hl.null('str'),combined.vep_1.most_severe_consequence), combined.vep.most_severe_consequence))
combined = combined.annotate(allele_type=hl.if_else(hl.is_missing(combined.allele_type) == True, hl.if_else(hl.is_missing(combined.allele_type_1) == True, hl.null('str'), combined.allele_type_1), combined.allele_type))

#Make NA values 0 (float) if position missing in exomes
combined = combined.annotate(nontopmed_AC=hl.if_else(hl.is_missing(combined.nontopmed_AC) == True,0,combined.nontopmed_AC))
combined = combined.annotate(nontopmed_AN=hl.if_else(hl.is_missing(combined.nontopmed_AN) == True,0,combined.nontopmed_AN))
combined = combined.annotate(nontopmed_hom=hl.if_else(hl.is_missing(combined.nontopmed_hom) == True,0,combined.nontopmed_hom))

#Make NA values 0 (float) if position missing in exomes
combined = combined.annotate(nontopmed_AC_1=hl.if_else(hl.is_missing(combined.nontopmed_AC_1) == True,0,combined.nontopmed_AC_1))
combined = combined.annotate(nontopmed_AN_1=hl.if_else(hl.is_missing(combined.nontopmed_AN_1) == True,0,combined.nontopmed_AN_1))
combined = combined.annotate(nontopmed_hom_1=hl.if_else(hl.is_missing(combined.nontopmed_hom_1) == True,0,combined.nontopmed_hom_1))

#Add nontopmed_AC,nontopmed_AN, non_topmed_nhomalt counts together from exome and genome (1)  datasets
combined = combined.annotate(combined_nontopmed_AC=combined.nontopmed_AC + combined.nontopmed_AC_1)
combined = combined.annotate(combined_nontopmed_AN=combined.nontopmed_AN + combined.nontopmed_AN_1)
combined= combined.annotate(combined_nontopmed_nhomalt=combined.nontopmed_hom + combined.nontopmed_hom_1)

final = combined.select(combined.combined_nontopmed_AC,
							combined.combined_nontopmed_AN,
							combined.combined_nontopmed_nhomalt,
							combined.nontopmed_AN,
							combined.nontopmed_AC,
							combined.nontopmed_hom,
							combined.nontopmed_cases,
							combined.nontopmed_AN_1,
							combined.nontopmed_AC_1,
							combined.nontopmed_hom_1,
							combined.nontopmed_cases_1,
							combined.most_severe_consequence,
							combined.allele_type,
							combined.MetaSVM_pred,
							combined.CADD_phred_hg19,
							combined.CADD_phred,
							combined.MPC,
							combined.bravo_freeze8,
							combined.filters,
							combined.filters_1,
							combined.genename,
							combined.genename_1,
							combined.qual,
							combined.qual_1,
							exome_assembly = combined.vep.assembly_name,
							genome_assembly = combined.vep_1.assembly_name)
final = final.transmute(exome_nontopmed_AN = final.nontopmed_AN,
						exome_nontopmed_AC = final.nontopmed_AC,
						exome_nontopmed_hom = final.nontopmed_hom,
						exome_nontopmed_cases = final.nontopmed_cases,
						genome_nontopmed_AN = final.nontopmed_AN_1,
						genome_nontopmed_AC = final.nontopmed_AC_1,
						genome_nontopmed_hom = final.nontopmed_hom_1,
						genome_nontopmed_cases = final.nontopmed_cases_1,
						exome_filters = final.filters,
						genome_filters = final.filters_1,
						exome_qual = final.qual,
						genome_qual = final.qual_1)
final.write('/gpfs/ycga/scratch60/kahle/sp2349/datasets/gnomad/combined.filtered.gnomad.r2.1.1.sites.bravo8-dbNSFP4.1a-fixed.chr5.ht',overwrite=True)
