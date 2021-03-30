import os
import hail as hl
import gnomad
import pandas as pd

hl.init()

out_f = "/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/cc_output/combined_gnomad_case_control.out"
with open(out_f, "w") as f:
	#Import gnomad combined exome and genome table
	gnomad = hl.read_table('/gpfs/ycga/scratch60/kahle/sp2349/datasets/gnomad/combined.filtered.gnomad.r2.1.1.sites.bravo8-dbNSFP4.1a-fixed.chr5.ht')
	#Filter on Bravo coordinates
	#filtered = gnomad.filter((gnomad.info.bravo <= 0.0005) | (gnomad.info.bravo.is_defined() == False))
	#filtered_g = gnomad_g.filter((gnomad_g.info.bravo <= 0.0005) | (gnomad_g.info.bravo.is_defined() == False))

	#Filter on Bravo coordinates
	filtered = gnomad.filter(gnomad.bravo_freeze8 <= 0.0005)

 	#Filter on DIAPH1 coordinates
	filtered = filtered.filter((filtered.locus >= hl.locus('5',140894583)) & (filtered.locus <= hl.locus('5',140998622)))

	print("Exomes count filtered on gene: {}".format(filtered.count()),file=f)
    
	#Filter on CADD1.6 score >= 20 or MetaSVM == D
	filtered = filtered.filter(((filtered.most_severe_consequence == 'missense_variant') & (filtered.CADD_phred_hg19 >=20)) | 
							   ((filtered.most_severe_consequence == 'missense_variant') & (filtered.MetaSVM_pred == "D")) | 
							   ((filtered.most_severe_consequence == 'protein_altering_variant') & (filtered.CADD_phred_hg19 >=20)) |
							   ((filtered.most_severe_consequence == 'protein_altering_variant') & (filtered.MetaSVM_pred == "D")) |
							   (filtered.most_severe_consequence == 'frameshift_variant') |
							   (filtered.most_severe_consequence == 'stop_gained') |
							   (filtered.most_severe_consequence == 'stop_lost') |
							   (filtered.most_severe_consequence == 'splice_donor_variant'))
							   
	print("LoF variant rows kept: {}".format(filtered.count()),file=f)
	
	#Gather non_topmed indicies. Collect() results in a list containing a dictionary. Too see all groups use freq_index_dict.collect()[0].
	#See Macarthur lab website for more information on the gnomad groups.
	#group_e = filtered.freq_index_dict.collect()[0][group_sel]
	#group_g = filtered_g.freq_index_dict.collect()[0][group_sel]

	#print("Exome non_topmed index: {}".format(group_e),file=f)
	#print("Genome non_topmed index: {}".format(group_g),file=f)

	#Calculate Cases and Controls. Cases = AC - (2*homozygote_count). Controls = max(AN - cases)
	filtered = filtered.annotate(combined_nontopmed_cases=filtered.combined_nontopmed_AC-(filtered.combined_nontopmed_nhomalt *2))
	#filtered = filtered.annotate(nontopmed_AN=filtered.combined_nontopmed_AN)
	#filtered = filtered.annotate(nontopmed_hom=filtered.combined_nontopmed_nhomalt)
	
	max_AN = filtered.aggregate(hl.agg.max(filtered.combined_nontopmed_AN))
	cases = filtered.aggregate(hl.agg.sum(filtered.combined_nontopmed_cases))
	homs = filtered.aggregate(hl.agg.sum(filtered.combined_nontopmed_nhomalt))
	controls = max_AN-cases-(homs*2)

	print("Combined max AN: {}".format(max_AN),file=f)
	print("Combined cases: {}".format(cases),file=f)
	print("Combined Homs: {}".format(homs),file=f)
	print("Combined Controls: {}".format(controls),file=f)

	print("Running Fisher Exact Test")
	
	filtered.write("/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/cc_output/diaph1_gnomad-combined_sam.ht",overwrite=True)
	df = filtered.to_pandas()
	df.to_csv("/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/cc_output/diaph1_gnomad-combined_sam.csv")

result = hl.fisher_exact_test(3,45,cases,controls)
print("Exporting Fisher Exact Test Results...")
result.export('/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/cc_output/diaph1_gnomad-combined_sam_cc.tsv')
print("Done!")	
