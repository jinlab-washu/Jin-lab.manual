import os
import hail as hl
import gnomad
import pandas as pd

hl.init()

def gnomad_het_case_control(exp_cases,exp_controls,chrm='0',start=0,end=0,out_dir=os.getcwd(),name=""):
	"""Performs case Control Test for specified coordinates using the Gnomad combined exome and genome dataset."""
	#Convert chromosome integer to string
	if type(chrm) == 'int':
		chrm = str(chrm)
	chrm = str(chrm)	
	
	#Check if name provided
	if name == "":
		name = "results_{}_{}-{}".format(chrm,start,end)
	
	#Create folder structure for ouput
	parent_dir = os.path.join(out_dir,"gnomad_case_control",name)
	if os.path.exists(os.path.join(parent_dir)) == False:
		os.makedirs(parent_dir)
	
	out_f = os.path.join(parent_dir,"results_{}_{}-{}.out".format(chrm,start,end))	
	with open(out_f, "w") as f:
		#Import gnomad combined exome and genome table
		gnomad_e = hl.read_table('/gpfs/ycga/scratch60/kahle/sp2349/combined_weilai_mts/combined.filtered.final.gnomad.r2.1.1.sites.{}.mt'.format(chrm))
		
		#Filter on Bravo coordinates
		#filtered_e = gnomad_e.filter((gnomad_e.info.bravo <= 0.0005) | (gnomad_e.info.bravo.is_defined() == False))
		#filtered_g = gnomad_g.filter((gnomad_g.info.bravo <= 0.0005) | (gnomad_g.info.bravo.is_defined() == False))

		#Filter on Bravo coordinates
		filtered_e = gnomad_e.filter(gnomad_e.bravo <= 0.0005)

		#Filter on DIAPH1 coordinates
		filtered_e = filtered_e.filter((filtered_e.locus >= hl.locus(chrm,start)) & (filtered_e.locus <= hl.locus(chrm,end)))

		print("Exomes count filtered on gene: {}".format(filtered_e.count()),file=f)
	   
		#Filter for variants with AC == 0
		filtered_e = filtered_e.filter(filtered_e.combined_nontopmed_AC	> 0)

		filtered_e 
		#Filter for LoF variants.If missense, CADD1.6 score >= 20 or MetaSVM == D
		filtered_e = filtered_e.filter(((filtered_e["Exonic_refGene"] == 'nonsynonymous_SNV') & (filtered_e.CADD16snv_PHRED >=20)) | 
									   ((filtered_e["Exonic_refGene"] == 'nonsynonymous_SNV') & (filtered_e.MetaSVM_pred == "D")) | 
									   (filtered_e["Func_refGene"] == 'splicing') |
									   (filtered_e["Exonic_refGene"] == 'frameshift_deletion') |
									   (filtered_e["Exonic_refGene"] == 'frameshift_insertion') |
									   (filtered_e["Exonic_refGene"] == 'stopgain') |
									   (filtered_e["Exonic_refGene"] == 'stoploss') |
									   (filtered_e["Func_refGene"] == 'exonic\\x3bsplicing'))
		
		print("Lof var rows kept: {}".format(filtered_e.count()),file=f)
		
		#Gather non_topmed indicies. Collect() results in a list containing a dictionary. Too see all groups use freq_index_dict.collect()[0].
		#See Macarthur lab website for more information on the gnomad groups.
		#group_e = filtered_e.freq_index_dict.collect()[0][group_sel]
		#group_g = filtered_g.freq_index_dict.collect()[0][group_sel]

		#print("Exome non_topmed index: {}".format(group_e),file=f)
		#print("Genome non_topmed index: {}".format(group_g),file=f)

		#Calculate Cases and Controls. Cases = AC - (2*homozygote_count). Controls = max(AN - cases)
		filtered_e = filtered_e.annotate(nontopmed_cases=filtered_e.combined_nontopmed_AC-(filtered_e.combined_nontopmed_nhomalt *2))
		filtered_e = filtered_e.annotate(nontopmed_AN=filtered_e.combined_nontopmed_AN)
		filtered_e = filtered_e.annotate(nontopmed_hom=filtered_e.combined_nontopmed_nhomalt)
		
		e_max_AN = filtered_e.aggregate(hl.agg.max(filtered_e.nontopmed_AN))
		e_cases = filtered_e.aggregate(hl.agg.sum(filtered_e.nontopmed_cases))
		e_homs = filtered_e.aggregate(hl.agg.sum(filtered_e.nontopmed_hom))
		e_controls = e_max_AN-e_cases-(e_homs*2)

		print("Combined max AN: {}".format(e_max_AN),file=f)
		print("Combined cases: {}".format(e_cases),file=f)
		print("Combined Homs: {}".format(e_homs),file=f)
		print("Combined Controls: {}".format(e_controls),file=f)

		print("Running Fisher Exact Test")
		
		filtered_e.write(os.path.join(parent_dir,"results_{}_{}-{}.ht".format(chrm,start,end)),overwrite=True)
		df = filtered_e.to_pandas()
		df.to_csv(os.path.join(parent_dir,"results_{}_{}-{}.csv".format(chrm,start,end)))

		result = hl.fisher_exact_test(exp_cases,exp_controls,e_cases,e_controls)
		print("Exporting Fisher Exact Test Results...")
		result.export(os.path.join(parent_dir,"results_{}_{}-{}.tsv".format(chrm,start,end)))
		print("Done!")

gnomad_het_case_control(3, 45, chrm=5, start=140894583, end=140998622, out_dir="/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/results",name="DIAPH1")
