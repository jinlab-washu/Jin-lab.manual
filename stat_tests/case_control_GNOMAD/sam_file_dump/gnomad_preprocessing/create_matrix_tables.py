import os
import hail as hl

hl.init()
vcfs = ['gnomad.exomes.r2.1.1.sites.5.decomposed.normalized_anno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.hg19_multianno.vcf.gz','gnomad.genomes.r2.1.1.sites.5.decomposed.normalized.hg19_multianno.hg19_multianno.vcf.gz']


for i in vcfs:
	mt = hl.import_vcf(i,force_bgz=True,reference_genome='GRCh37')
	out_name = os.path.splitext(os.path.splitext(i)[0])[0] + ".mt"
	print("out name: {}".format(out_name))
	mt.write(out_name)
