#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import hail as hl


# In[ ]:


#Did not work for increasing java heap size
#get_ipython().system('export PYSPARK_SUBMIT_ARGS="--driver-memory 16g --executor-memory 16g pyspark-shell"')


# In[ ]:


#get_ipython().system('echo "$PYSPARK_SUBMIT_ARGS"')


# In[2]:


hl.init()


# In[ ]:


#group_sel = "non_topmed"


# In[ ]:


#IMport Weilais converted vcf
#mt_exomes = hl.read_matrix_table('/gpfs/ycga/scratch60/kahle/sp2349/weilai_gnomad/gnomad.exomes.r2.1.1.sites.5.decomposed.normalized_anno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.mt')


# In[ ]:


gnomad_e = hl.read_matrix_table('/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/gnomad.exomes.r2.1.1.sites.5.decomposed.normalized_anno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.mt')
gnomad_e = gnomad_e.rows()
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(bravo = hl.if_else(hl.is_missing(gnomad_e.info.bravo[0]) == True,0.0,hl.float64(gnomad_e.info.bravo[0]))))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(CADD_phred = hl.float64(gnomad_e.info.CADD_phred[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(MetaSVM_pred = gnomad_e.info.MetaSVM_pred[0]))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_AC = hl.int64(gnomad_e.info.non_topmed_AC[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_AN = gnomad_e.info.non_topmed_AN))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_nhomalt = hl.int64(gnomad_e.info.non_topmed_nhomalt[0])))


# In[ ]:


#mt_exomes.count()


# In[ ]:


#Import Weilais converted vcf
#mt_genomes = hl.read_matrix_table('/gpfs/ycga/scratch60/kahle/sp2349/weilai_gnomad/gnomad.genomes.r2.1.1.sites.5.decomposed.normalized.hg19_multianno.hg19_multianno.mt')


# In[ ]:


gnomad_g = hl.read_matrix_table('/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/gnomad.genomes.r2.1.1.sites.5.decomposed.normalized.hg19_multianno.hg19_multianno.mt')
gnomad_g = gnomad_g.rows()
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(bravo = hl.if_else(hl.is_missing(gnomad_g.info.bravo[0]) == True,0.0,hl.float64(gnomad_g.info.bravo[0]))))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(CADD_phred = hl.float64(gnomad_g.info.CADD_phred[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(MetaSVM_pred = gnomad_g.info.MetaSVM_pred[0]))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_AC = hl.int64(gnomad_g.info.non_topmed_AC[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_AN = gnomad_g.info.non_topmed_AN))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_nhomalt = hl.int64(gnomad_g.info.non_topmed_nhomalt[0])))


# In[ ]:


#mt_genomes.count()


# In[3]:

gnomad_e_subset = gnomad_e.filter((gnomad_e.locus >= hl.locus('5',140894583)) & (gnomad_e.locus <= hl.locus('5',140998622)))

gnomad_e_subset.write('/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/gnomad_e.diaph1.coords.mt')

gnomad_g_subset = gnomad_g.filter((gnomad_g.locus >= hl.locus('5',140894583)) & (gnomad_g.locus <= hl.locus('5',140998622))) 

gnomad_g_subset.write('/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/gnomad_g.subset.diaph1.coords.mt')

combined = hl.read_table('/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/combined.gnomad.r2.1.1.sites.5.raw.mt')

combined_subset = combined.filter((combined.locus >= hl.locus('5',140894583)) & (combined.locus <= hl.locus('5',140998622)))

combined_subset.write('/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/combined.subset.diaph1.coords.mt')


# In[ ]:


#combined.count()


# In[ ]:


#combined.describe()


# In[ ]:


#combined.info_1.CADD16snv_PHRED.show()


# In[ ]:


#combined.info_1.CADD13_PHRED.show()


# In[4]:


converted = "None"


# In[5]:

"""
#Make NA values 0 if position missing in exomes
converted = combined.annotate(info=combined.info.annotate(non_topmed_AC=hl.if_else(hl.is_missing(combined.info.non_topmed_AC) == True,0,combined.info.non_topmed_AC)))
converted = converted.annotate(info=converted.info.annotate(non_topmed_AN=hl.if_else(hl.is_missing(converted.info.non_topmed_AN) == True,0,converted.info.non_topmed_AN)))
converted = converted.annotate(info=converted.info.annotate(non_topmed_nhomalt=hl.if_else(hl.is_missing(converted.info.non_topmed_nhomalt) == True,0,converted.info.non_topmed_nhomalt)))


# In[6]:


#Make NA values 0 if position missing genomes
converted = converted.annotate(info_1=converted.info_1.annotate(non_topmed_AC=hl.if_else(hl.is_missing(converted.info_1.non_topmed_AC) == True,0,converted.info_1.non_topmed_AC)))
converted = converted.annotate(info_1=converted.info_1.annotate(non_topmed_AN=hl.if_else(hl.is_missing(converted.info_1.non_topmed_AN) == True,0,converted.info_1.non_topmed_AN)))
converted = converted.annotate(info_1=converted.info_1.annotate(non_topmed_nhomalt=hl.if_else(hl.is_missing(converted.info_1.non_topmed_nhomalt) == True,0,converted.info_1.non_topmed_nhomalt)))


# In[ ]:


#converted.info.non_topmed_nhomalt.show()


# In[ ]:


#combined.info.non_topmed_nhomalt.show()


# In[ ]:


#converted.info_1.non_topmed_nhomalt.show()


# In[ ]:


#combined.info_1.non_topmed_nhomalt.show()


# In[7]:


#Add nontopmed_AC,nontopmed_AN, nad non_topmed_nhomalt counts together from exome (info) and genome datasets (info_1)

converted = converted.annotate(combined_nontopmed_AC=converted.info.non_topmed_AC + converted.info_1.non_topmed_AC)
converted = converted.annotate(combined_nontopmed_AN=converted.info.non_topmed_AN + converted.info_1.non_topmed_AN)
converted = converted.annotate(combined_nontopmed_nhomalt=converted.info.non_topmed_nhomalt + converted.info_1.non_topmed_nhomalt)


# In[8]:

#Check for missing MetaSVM, CADD, or Bravo frequencies. If exome missing use genome freqs and vice versa.
#Joining of the tables causes NA values for positions missing in either dataset. Genomes have some positions missing in Exomes..etc
converted = converted.annotate(MetaSVM_pred=hl.if_else(hl.is_missing(converted.info.MetaSVM_pred) == True, converted.info_1.MetaSVM_pred, converted.info.MetaSVM_pred))
converted = converted.annotate(CADD_phred=hl.if_else(hl.is_missing(converted.info.CADD_phred) == True, hl.if_else(hl.is_missing(converted.info_1.CADD_phred) == True, hl.null('float64'), converted.info_1.CADD_phred), converted.info.CADD_phred))
converted = converted.annotate(CADD16snv_PHRED=hl.if_else(converted.info.CADD16snv_PHRED[0] == 'NA', hl.if_else(converted.info_1.CADD16snv_PHRED[0] == 'NA', hl.null(hl.tfloat), hl.float64(converted.info_1.CADD16snv_PHRED[0])), hl.float64(converted.info.CADD16snv_PHRED[0])))
converted = converted.annotate(CADD16indel_PHRED=hl.if_else(converted.info.CADD16indel_PHRED[0] == 'NA', hl.if_else(converted.info_1.CADD16indel_PHRED[0] == 'NA', hl.null('float64'), hl.float64(converted.info_1.CADD16indel_PHRED[0])), hl.float64(converted.info.CADD16indel_PHRED[0])))

converted = converted.annotate(MPC=hl.if_else(converted.info.MPC[0] == 'NA', hl.if_else(converted.info_1.MPC[0] == 'NA', hl.null('float64'), hl.float64(converted.info_1.MPC[0])),hl.float64(converted.info.MPC[0])))

converted = converted.annotate(bravo=hl.if_else(hl.is_missing(converted.info.bravo) == True, converted.info_1.bravo, converted.info.bravo))


# In[9]:


converted = converted.drop(converted.info)
converted = converted.drop(converted.info_1)


# In[10]:

converted.write("/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/combined.gnomad.r2.1.1.sites.5.mt")
#converted.show()


# In[11]:


test = combined.select(ex_AC=combined.info.non_topmed_AC, g_AC=combined.info_1.non_topmed_AC, ex_AN= combined.info.non_topmed_AN, g_AN=combined.info_1.non_topmed_AN, ex_nhomalt=combined.info.non_topmed_nhomalt, g_nhomalt=combined.info_1.non_topmed_nhomalt, ex_meta=combined.info.MetaSVM_pred, g_meta=combined.info_1.MetaSVM_pred, ex_CADD16=combined.info.CADD16snv_PHRED, g_CADD16=combined.info_1.CADD16snv_PHRED)


# In[12]:

test.write("/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/comparison.mt")
#test.tail(5000).show(100)


# In[ ]:


#test.filter(test.locus >= hl.locus('5',140894583)).show()


# In[ ]:


#test.filter((test.locus >= hl.locus('5',140894583)) & (test.locus <= hl.locus('5',140894583))).show()


# In[ ]:


#converted.filter((converted.locus >= hl.locus('5',140894583)) & (converted.locus <= hl.locus('5',140894583))).show()


# In[ ]:


#gnomad_g[gnomad_e.locus,gnomad_e.alleles].info.non_topmed_AC.show()


# In[ ]:


#Exomes Count
#print("Exomes Count: {}".format(mt_exomes.count()))


# In[ ]:


#Genomes Count
#print("Genomes Count: {}".format(mt_genomes.count()))


# In[ ]:
"""



