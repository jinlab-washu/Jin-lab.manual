import os
import hail as hl
import gnomad
import pandas as pd

hl.init()

out_f = "gnomad_case_control_weilai_tables.out"
group_sel = "non_topmed"
with open(out_f, "w") as f:

	#Import gnomad v2.1 (GRCh37) exomes hail table annotated with Bravo and dbNSFP
	gnomad_e = hl.read_matrix_table('/gpfs/ycga/scratch60/kahle/sp2349/weilai_gnomad/gnomad.exomes.r2.1.1.sites.5.decomposed.normalized_anno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.mt')
	gnomad_e = gnomad_e.rows()
	gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(bravo = hl.if_else(hl.is_missing(gnomad_e.info.bravo[0]) == True,0.0,hl.float64(gnomad_e.info.bravo[0]))))
	gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(CADD_phred = hl.float64(gnomad_e.info.CADD_phred[0])))
	gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(MetaSVM_pred = gnomad_e.info.MetaSVM_pred[0]))
	gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_AC = hl.int64(gnomad_e.info.non_topmed_AC[0])))
	gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_AN = gnomad_e.info.non_topmed_AN))
	gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_nhomalt = hl.int64(gnomad_e.info.non_topmed_nhomalt[0])))

	#Import gnomad genomes (GRCh37) hail table annotated with Bravo and dbNSFP
	gnomad_g = hl.read_matrix_table('/gpfs/ycga/scratch60/kahle/sp2349/weilai_gnomad/gnomad.genomes.r2.1.1.sites.5.decomposed.normalized.hg19_multianno.hg19_multianno.mt')
	gnomad_g = gnomad_g.rows()
	gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(bravo = hl.if_else(hl.is_missing(gnomad_g.info.bravo[0]) == True,0.0,hl.float64(gnomad_g.info.bravo[0]))))
	gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(CADD_phred = hl.float64(gnomad_g.info.CADD_phred[0])))
	gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(MetaSVM_pred = gnomad_g.info.MetaSVM_pred[0]))
	gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_AC = hl.int64(gnomad_g.info.non_topmed_AC[0])))
	gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_AN = gnomad_g.info.non_topmed_AN))
	gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_nhomalt = hl.int64(gnomad_g.info.non_topmed_nhomalt[0])))

	print("Exomes count: {}".format(gnomad_e.count()),file=f)
	print("Genomes count: {}".format(gnomad_g.count()),file=f)

	#Filter on Bravo coordinates
	#filtered_e = gnomad_e.filter((gnomad_e.info.bravo <= 0.0005) | (gnomad_e.info.bravo.is_defined() == False))
	#filtered_g = gnomad_g.filter((gnomad_g.info.bravo <= 0.0005) | (gnomad_g.info.bravo.is_defined() == False))

	#Filter on Bravo coordinates
	filtered_e = gnomad_e.filter(gnomad_e.info.bravo <= 0.0005)
	filtered_g = gnomad_g.filter(gnomad_g.info.bravo <= 0.0005)

 	#Filter on DIAPH1 coordinates
	filtered_e = filtered_e.filter((filtered_e.locus >= hl.locus('5',140894583)) & (filtered_e.locus <= hl.locus('5',140998622)))
	filtered_g = filtered_g.filter((filtered_g.locus >= hl.locus('5',140894583)) & (filtered_g.locus <= hl.locus('5',140998622)))

	print("Exomes count filtered on gene: {}".format(filtered_e.count()),file=f)
	print("Genomes count filtered on gene: {}".format(filtered_g.count()),file=f)
    
	#Filter on CADD1.6 score >= 20 or MetaSVM == D
	filtered_e = filtered_e.filter((filtered_e.info.CADD_phred >=20) | (filtered_e.info.MetaSVM_pred == "D"))
	filtered_g = filtered_g.filter((filtered_g.info.CADD_phred >=20) | (filtered_g.info.MetaSVM_pred == "D"))
	
	print("Exomes count filtered on CADD >=20 or MetaSVM 'D': {}".format(filtered_e.count()),file=f)
	print("Genomes count filtered on CADD >=20 or MetaSVM 'D': {}".format(filtered_g.count()),file=f)
	
	#Gather non_topmed indicies. Collect() results in a list containing a dictionary. Too see all groups use freq_index_dict.collect()[0].
	#See Macarthur lab website for more information on the gnomad groups.
	#group_e = filtered_e.freq_index_dict.collect()[0][group_sel]
	#group_g = filtered_g.freq_index_dict.collect()[0][group_sel]

	#print("Exome non_topmed index: {}".format(group_e),file=f)
	#print("Genome non_topmed index: {}".format(group_g),file=f)

	#Calculate Cases and Controls. Cases = AC - (2*homozygote_count). Controls = max(AN - cases)
	filtered_e = filtered_e.annotate(nontopmed_cases=filtered_e.info.non_topmed_AC-(filtered_e.info.non_topmed_nhomalt *2))
	filtered_e = filtered_e.annotate(nontopmed_AN=filtered_e.info.non_topmed_AN)
	filtered_e = filtered_e.annotate(nontopmed_hom=filtered_e.info.non_topmed_nhomalt)
	
	filtered_g = filtered_g.annotate(nontopmed_cases=filtered_g.info.non_topmed_AC-(filtered_g.info.non_topmed_nhomalt *2))
	filtered_g = filtered_g.annotate(nontopmed_AN=filtered_g.info.non_topmed_AN)
	filtered_g = filtered_g.annotate(nontopmed_hom=filtered_g.info.non_topmed_nhomalt)

	e_max_AN = filtered_e.aggregate(hl.agg.max(filtered_e.nontopmed_AN))
	e_cases = filtered_e.aggregate(hl.agg.sum(filtered_e.nontopmed_cases))
	e_homs = filtered_e.aggregate(hl.agg.max(filtered_e.nontopmed_hom))
	e_controls = e_max_AN-e_cases-(e_homs*2)

	g_max_AN = filtered_g.aggregate(hl.agg.max(filtered_g.nontopmed_AN))
	g_cases = filtered_g.aggregate(hl.agg.sum(filtered_g.nontopmed_cases))
	g_homs = filtered_g.aggregate(hl.agg.max(filtered_g.nontopmed_hom))
	g_controls = g_max_AN-g_cases-(g_homs*2)
	
	print("Exomes max AN: {}".format(e_max_AN),file=f)
	print("Exomes cases: {}".format(e_cases),file=f)
	print("Exome Homs: {}".format(e_homs),file=f)
	print("Exome Controls: {}".format(e_controls),file=f)

	print("Genomes max AN: {}".format(g_max_AN),file=f)
	print("Genomes cases: {}".format(g_cases),file=f)
	print("Genomes Homs: {}".format(g_homs),file=f)
	print("Genome controls: {}".format(g_controls),file=f)	
	
	print("Running Fisher Exact Test")
	tot_cases = int(e_cases + g_cases)
	tot_controls = int(e_controls+g_controls)
	print("Combined controls: {}".format(tot_controls),file=f)
	print("Combined cases: {}".format(tot_cases),file=f)

result = hl.fisher_exact_test(3,45,tot_cases,tot_controls)
print("Exporting Fisher Exact Test Results...")
result.export('/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/diaph1_cc_weilai_tables.tsv')
print("Done!")	
