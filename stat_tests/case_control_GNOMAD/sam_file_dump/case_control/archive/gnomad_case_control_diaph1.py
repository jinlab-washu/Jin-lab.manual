import os
import hail as hl
import gnomad
import pandas as pd

hl.init()

out_f = "gnomad_case_control.out"
group_sel = "non_topmed"
with open(out_f, "w") as f:

	#Import gnomad v2.1 (GRCh37) exomes hail table annotated with Bravo and dbNSFP
	gnomad_e = hl.read_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/gnomad.exomes.r2.1.1.sites.bravo8-dbNSFP4.1a-fixed.annotated.ht')

	#Import gnomad genomes (GRCh37) hail table annotated with Bravo and dbNSFP
	gnomad_g = hl.read_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/gnomad.genomes.r2.1.1.sites.bravo8-dbNSFP4.1a-fixed.annotated.ht')

	print("Exomes count: {}".format(gnomad_e.count()),file=f)
	print("Genomes count: {}".format(gnomad_g.count()),file=f)
   
	#Filter on Bravo coordinates
	filtered_e = gnomad_e.filter(gnomad_e.bravo_freeze8 <= 0.0005)
	filtered_g = gnomad_g.filter(gnomad_g.bravo_freeze8 <= 0.0005)

	#Filter on DIAPH1 coordinates
	filtered_e = filtered_e.filter((filtered_e.locus >= hl.locus('5',140894583)) & (filtered_e.locus <= hl.locus('5',140998622)))
	filtered_g = filtered_g.filter((filtered_g.locus >= hl.locus('5',140894583)) & (filtered_g.locus <= hl.locus('5',140998622)))
	
	print("Exomes count filtered on gene: {}".format(filtered_e.count()),file=f)
	print("Genomes count filtered on gene: {}".format(filtered_g.count()),file=f)
    
	#Filter on CADD1.6 score >= 20 or MetaSVM == D
	filtered_e = filtered_e.filter((filtered_e.CADD_phred_hg19 >=20) | (filtered_e.MetaSVM_pred == "D"))
	filtered_g = filtered_g.filter((filtered_g.CADD_phred_hg19 >=20) | (filtered_g.MetaSVM_pred == "D"))
	
	print("Exomes count filtered on CADD >=20 or MetaSVM 'D': {}".format(filtered_e.count()),file=f)
	print("Genomes count filtered on CADD >=20 or MetaSVM 'D': {}".format(filtered_g.count()),file=f)
	
	#Gather non_topmed indicies. Collect() results in a list containing a dictionary. Too see all groups use freq_index_dict.collect()[0].
	#See Macarthur lab website for more information on the gnomad groups.
	group_e = filtered_e.freq_index_dict.collect()[0][group_sel]
	group_g = filtered_g.freq_index_dict.collect()[0][group_sel]

	print("Exome non_topmed index: {}".format(group_e),file=f)
	print("Genome non_topmed index: {}".format(group_g),file=f)

	#Calculate Cases and Controls. Cases = AC - (2*homozygote_count). Controls = max(AN - cases)
	filtered_e = filtered_e.annotate(nontopmed_cases=filtered_e.freq[group_e].AC-(filtered_e.freq[group_e].homozygote_count *2))
	filtered_e = filtered_e.annotate(nontopmed_AN=filtered_e.freq[group_e].AN - filtered_e.freq[group_e].AC)

	filtered_g = filtered_g.annotate(nontopmed_cases=filtered_g.freq[group_g].AC-(filtered_g.freq[group_g].homozygote_count *2))
	filtered_g = filtered_g.annotate(nontopmed_AN=filtered_g.freq[group_g].AN - filtered_g.freq[group_g].AC) 

	e_max_AN = filtered_e.aggregate(hl.agg.max(filtered_e.nontopmed_AN))
	e_cases = filtered_e.aggregate(hl.agg.sum(filtered_e.nontopmed_cases))
	
	g_max_AN = filtered_g.aggregate(hl.agg.max(filtered_g.nontopmed_AN))
	g_cases = filtered_g.aggregate(hl.agg.sum(filtered_g.nontopmed_cases))

	print("Exomes max AN: {}".format(e_max_AN),file=f)
	print("Exomes cases: {}".format(e_cases),file=f)

	print("Genomes max AN: {}".format(g_max_AN),file=f)
	print("Genomes cases: {}".format(g_cases),file=f)
	
	tot_cases = int(e_cases + g_cases)
	tot_controls = int((g_max_AN+e_max_AN) /2)
	print("Combined AN: {}".format(tot_controls),file=f)
	print("Combined cases: {}".format(tot_cases),file=f)
	
	print("Running Fisher Exact Test")
	print("Exome Cases: {}".format(e_cases),file=f)
	print("Exome Controls: {}".format(e_max_AN),file=f)
	print("Genome cases: {}".format(g_cases),file=f)
	print("Genome controls: {}".format(g_max_AN),file=f)

result = hl.fisher_exact_test(3,45,tot_cases,tot_controls)
print("Exporting Fisher Exact Test Results...")
result.export('/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/diaph1_cc.tsv')
print("Done!")	
