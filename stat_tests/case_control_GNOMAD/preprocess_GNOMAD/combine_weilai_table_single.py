import os
import hail as hl


hl.init()

chrom=10 # Change chromosome here

#Import Exomes GNOMAD TABLE and modify for easier manipulation
gnomad_e = hl.read_matrix_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted/gnomad.exomes.r2.1.1.sites.{}.decomposed.normalized_anno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.mt'.format(chrom))
gnomad_e = gnomad_e.rows()
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(bravo = hl.if_else(hl.is_missing(gnomad_e.info.bravo[0]) == True,0.0,hl.float64(gnomad_e.info.bravo[0]))))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(CADD16snv_PHRED = hl.float64(gnomad_e.info.CADD16snv_PHRED[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(CADD_phred = hl.float64(gnomad_e.info.CADD_phred[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(MetaSVM_pred = gnomad_e.info.MetaSVM_pred[0]))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_AC = hl.int64(gnomad_e.info.non_topmed_AC[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_AN = gnomad_e.info.non_topmed_AN))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(non_topmed_nhomalt = hl.int64(gnomad_e.info.non_topmed_nhomalt[0])))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(Exonic_refGene = gnomad_e.info["ExonicFunc.refGene"][0]))
gnomad_e = gnomad_e.annotate(info=gnomad_e.info.annotate(Func_refGene = gnomad_e.info["Func.refGene"][0]))
#Filter out variants that did not pass filters. "RF or AC0"
gnomad_e = gnomad_e.filter((gnomad_e.filters.contains('AC0')) | (gnomad_e.filters.contains('RF')),keep=False)

#Import Genomes GNOMAD TABLE and modify for easier manipulation
gnomad_g = hl.read_matrix_table('/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted/gnomad.genomes.r2.1.1.sites.{}.decomposed.normalized.hg19_multianno.hg19_multianno.mt'.format(chrom))
gnomad_g = gnomad_g.rows()
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(bravo = hl.if_else(hl.is_missing(gnomad_g.info.bravo[0]) == True,0.0,hl.float64(gnomad_g.info.bravo[0]))))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(CADD16snv_PHRED = hl.float64(gnomad_g.info.CADD16snv_PHRED[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(CADD_phred = hl.float64(gnomad_g.info.CADD_phred[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(MetaSVM_pred = gnomad_g.info.MetaSVM_pred[0]))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_AC = hl.int64(gnomad_g.info.non_topmed_AC[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_AN = gnomad_g.info.non_topmed_AN))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(non_topmed_nhomalt = hl.int64(gnomad_g.info.non_topmed_nhomalt[0])))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(Exonic_refGene = gnomad_g.info["ExonicFunc.refGene"][0]))
gnomad_g = gnomad_g.annotate(info=gnomad_g.info.annotate(Func_refGene = gnomad_g.info["Func.refGene"][0]))
#Filter out variants that did not pass filters. "RF or AC0"
gnomad_g = gnomad_g.filter((gnomad_g.filters.contains('AC0')) | (gnomad_g.filters.contains('RF')),keep=False)

combined = gnomad_e.join(gnomad_g,how='outer')

combined.write('/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/combined_filtered/combined.filtered.gnomad.r2.1.1.sites.{}.ht'.format(chrom),overwrite=True)
