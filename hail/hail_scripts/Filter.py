# define new filter functions 
# Nick Diab 

import hail as hl
import pprint 

def filter_major_consequence(de_novo_results):
        '''filter de novo calls based on their major consequence that are not in coding regions or splice sites'''
        
        de_novo_results_filtered = de_novo_results.filter(de_novo_results.major_consequence == "intron_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())

        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "3_prime_UTR_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "5_prime_UTR_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "splice_region_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "upstream_gene_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "downstream_gene_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "transcript_ablation", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "transcript_amplification", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "start_retained_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "stop_retained_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "intergenic_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "non_coding_transcript_exon_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "start_lost", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "regulatory_region_amplification", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "feature_elongation", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "regulatory_region_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        de_novo_results_filtered = de_novo_results_filtered.filter(de_novo_results_filtered.major_consequence == "TF_binding_site_variant", keep=False)
        pprint.pprint(de_novo_results_filtered.count())


        return de_novo_results_filtered

def filter_DP(de_novo_results):
        '''filter de novo results based on DP for parents and proband'''
        
        de_novo_results = de_novo_results.filter(de_novo_results.proband_entry.DP >= 10, keep=True)
        pprint.pprint(de_novo_results.count())
        
        de_novo_results = de_novo_results.filter(de_novo_results.father_entry.DP >= 10, keep=True)
        pprint.pprint(de_novo_results.count())
        
        de_novo_results = de_novo_results.filter(de_novo_results.mother_entry.DP >= 10, keep=True)
        pprint.pprint(de_novo_results.count())
        
        return de_novo_results 
   
   
     
# Filter matrix table before calling de novo events

# Filter out variants with a gnomad_af > 0.0004 
# mt = mt.filter_rows(mt.gnomad_af > 0.0004, keep=False) 

def filter_mt_gnomad_af(mt): 
        mt = mt.filter_rows(mt.gnomad_af > 0.0004, keep=False)
        pprint.pprint(mt.count())
        return mt


def filter_mt_major_consequence(mt):
        mt = mt.filter_rows(mt.major_consequence == "intron_variant", keep=False)
        pprint.pprint(mt.count())
        
        mt = mt.filter_rows(mt.major_consequence == "3_prime_UTR_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "5_prime_UTR_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "splice_region_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "upstream_gene_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "downstream_gene_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "transcript_ablation", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "transcript_amplification", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "start_retained_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "stop_retained_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "intergenic_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "non_coding_transcript_exon_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "start_lost", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "regulatory_region_amplification", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "feature_elongation", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "regulatory_region_variant", keep=False)
        #pprint.pprint(mt.count())


        mt = mt.filter_rows(mt.major_consequence == "TF_binding_site_variant", keep=False)
        pprint.pprint(mt.count())
        
        return mt 
