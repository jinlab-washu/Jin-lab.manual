import os
import hail as hl
import gnomad

hl.init()
out_f = "diaph1_case_control_filtering.out"
with open(out_f, "w") as f:
	#Import matrix table already annotated with bravo and MetaSVM (In this case, using annovar)
	input_dir ="/gpfs/ycga/project/kahle/sp2349/moyamoya/hail_results"
	mt = hl.read_matrix_table(os.path.join(input_dir,'exome_calls_pass_step2_normalized_anno.hg19_multianno_subset_VEP_gnomad.mt'))

	#Make annotations easier for filtering. If no bravo frequency for variants, set bravo freq to 0
	mt = mt.annotate_rows(bravo=hl.cond(hl.is_defined(mt.info["bravo"][0]), hl.float64(mt.info["bravo"][0]), 0.0))
	mt = mt.annotate_rows(meta_svm_pred=mt.info.MetaSVM_pred[0])

	db_ht = hl.read_table('/gpfs/ycga/project/kahle/sp2349/datasets/dbNSFP/dbNSFp4.1a/dbNSFP4.1a_chr_all_GRCh37.ht')

	#Annotate mt with CADD16 scores. Original vcf was annotated with CADD13
	mt = mt.annotate_rows(cadd16=hl.cond(hl.is_defined(db_ht[mt.row_key]), db_ht[mt.row_key].CADD_phred_hg19, 0.0))

	#Subset probands for case_control

	# Step 1: Create a text file with the sample IDs you want to keep and import that text file as a hail table. 
	table = (hl.import_table('/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/final_probands_for_caseControl.txt', impute=True).key_by('Sample'))

	#The IDs_keep.txt file has the following format (including headers)
	# Sample        should_retain
	# 1-00005       yes
	# 1-00187       yes
	# 1-00252       yes
	# 1-00386       yes
	# 1-00668       yes
	# etc etc

	# Annotate columns of matrix table with Sample-IDs you want to keep
	mt = mt.annotate_cols(is_retain = table[mt.s])
	mt = mt.annotate_cols(should_retain = table[mt.s].should_retain)


	# Filter matrix table columns 
	mt = mt.filter_cols(mt.col.is_retain.should_retain == 'yes', keep=True)
	mt = mt.filter_cols(mt.should_retain == 'yes', keep=True)
	
	sample_count = mt.cols().count()
	print("Sample count: {}".format(sample_count),file=f)
	print("Total allele count: {}".format(sample_count*2),file=f)

	#Filter on Bravo frequency
	mt_filtered = mt.filter_rows(mt.bravo <= 0.0005)

	#Filter on DIAPH1 coordinates
	mt_filtered = mt_filtered.filter_rows((mt_filtered.locus >= hl.locus('5',140894583)) & (mt_filtered.locus <= hl.locus('5',140998622)))

	#Filter on CADD1.6 score >= 20 or MetaSVM == D
	mt_filtered = mt_filtered.filter_rows((mt_filtered.cadd16 >=20) | (mt_filtered.meta_svm_pred == "D"))

	print("Unique variants post bravo, CADD, and MetaSVM: {}".format(mt_filtered.rows().count()),file=f)

	#Filter for exonic and splice-site variants only
	mt_filtered = mt_filtered.filter_rows((mt_filtered.vep.most_severe_consequence == "stop_gained") | (mt_filtered.vep.most_severe_consequence == "splice_acceptor_variant") | (mt_filtered.vep.most_severe_consequence =="splice_donor_variant") | (mt_filtered.vep.most_severe_consequence == "frameshift_variant")| (mt_filtered.vep.most_severe_consequence =="stop_lost") | (mt_filtered.vep.most_severe_consequence =="start_lost") | (mt_filtered.vep.most_severe_consequence =='missense_variant')| (mt_filtered.vep.most_severe_consequence =='protein_altering_variant') )
	print("Variants: {} kept".format(mt_filtered.count()))

	mt_filtered.count()

	#Convert matrix table to table for easier dropping of homozygous reference samples
	mt_filtered = mt_filtered.key_cols_by()
	mt_filtered_table = mt_filtered.entries()

	#Filter samples with homozygous reference calls (WT)
	mt_filtered_table = mt_filtered_table.filter(mt_filtered_table.GT.is_hom_ref() == True, keep=False)
	mt_filtered_table.show()

	#Filter samples on GQ >= 20 and DP >= 8
	mt_filtered_table = mt_filtered_table.filter(mt_filtered_table.DP > 9)
	mt_filtered_table = mt_filtered_table.filter(mt_filtered_table.GQ > 19)
	
	#Write to matrix table
	mt_filtered_table.write('/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/moyamoya_diaph1_damaging_for_cc.ht',overwrite=True)
	
	print("Total Variants post filtering: {}".format(mt_filtered_table.count()),file=f)
	
	print("Total Cases (Alleles): {}".format(mt_filtered_table.aggregate(hl.agg.sum(mt_filtered_table.GT.n_alt_alleles()))),file=f)
	print("Total Homozygous Cases: {}".format(mt_filtered_table.aggregate(hl.agg.count_where(mt_filtered_table.GT.is_hom_var() == True))),file=f)
	print("Samples with variants: {}".format(mt_filtered_table.aggregate(hl.agg.counter(mt_filtered_table.s))),file=f)
	
#Write to text file
df = mt_filtered_table.to_pandas()
df.to_csv(os.path.join('/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/moyamoya_diaph1_damaging_for_cc.txt'),sep="\t")
