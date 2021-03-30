import os
import hail as hl
import gnomad


hl.init()

#Import gnomad v2.1 (GRCh37) exomes hail table annotated with Bravo and dbNSFP
#Note: this removes any varaints that does not have an associated bravo frequency
gnomad_e = hl.read_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/gnomad.exomes.r2.1.1.sites.bravo8-dbNSFP4.1a.annotated.ht')

#Import gnomad genomes (GRCh37) hail table annotated with Bravo and dbNSFP
#Note: this removes any varaints that does not have an associated bravo frequency
gnomad_g = hl.read_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/gnomad.genomes.r2.1.1.sites.bravo8-dbNSFP4.1a.annotated.ht')

#Filter on Bravo Frequency
filtered_e = gnomad_e.filter(gnomad_e.bravo_freeze8 <= 0.0005)
filtered_g = gnomad_g.filter(gnomad_g.bravo_freeze8 <= 0.0005)

#Filter on DIAPH1 coordinates
filtered_e = filtered_e.filter((filtered_e.locus >= hl.locus('5',140894583)) & (filtered_e.locus <= hl.locus('5',140998622)))
filtered_g = filtered_g.filter((filtered_g.locus >= hl.locus('5',140894583)) & (filtered_g.locus <= hl.locus('5',140998622)))

#Filter on CADD1.6 score >= 20 or MetaSVM == D
filtered_e = filtered_e.filter((filtered_e.CADD_phred_hg19 >=20) | (filtered_e.MetaSVM_pred == "D"))
filtered_g = filtered_g.filter((filtered_g.CADD_phred_hg19 >=20) | (filtered_g.MetaSVM_pred == "D"))


#Filter on coding sequences
filtered_e = filtered_e.filter((filtered_e.vep.most_severe_consequence == "stop_gained") | (filtered_e.vep.most_severe_consequence == "splice_acceptor_variant") | (filtered_e.vep.most_severe_consequence =="splice_donor_variant") | (filtered_e.vep.most_severe_consequence == "frameshift_variant")| (filtered_e.vep.most_severe_consequence =="stop_lost") | (filtered_e.vep.most_severe_consequence =="start_lost") | (filtered_e.vep.most_severe_consequence =='missense_variant') )
filtered_g = filtered_g.filter((filtered_g.vep.most_severe_consequence == "stop_gained") | (filtered_g.vep.most_severe_consequence == "splice_acceptor_variant") | (filtered_g.vep.most_severe_consequence =="splice_donor_variant") | (filtered_g.vep.most_severe_consequence == "frameshift_variant")| (filtered_g.vep.most_severe_consequence =="stop_lost") | (filtered_g.vep.most_severe_consequence =="start_lost") | (filtered_g.vep.most_severe_consequence =='missense_variant') )

#Write out matrix tables
filtered_e.write('/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/filtered_e.ht',overwrite=True)

filtered_g.write('/gpfs/ycga/project/kahle/sp2349/moyamoya/case_control/filtered_g.ht',overwrite=True)



