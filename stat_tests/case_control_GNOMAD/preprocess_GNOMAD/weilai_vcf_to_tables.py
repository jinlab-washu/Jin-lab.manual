### CONVERT Weilai gnomad2.1.1 vcfs to matrix tables
### Takes a file of vcf's path as input. In the code below, this is called 'weilai_vcfs_subset.txt'

import os
import hail as hl

hl.init()

out_path= '/gpfs/ycga/project/kahle/sp2349/datasets/gnomad/tables/weilai_converted'
with open("weilai_vcfs_subset.txt", "r") as f:

	for vcf in f:
		vcf = vcf.strip()
		print(vcf)
		mt = hl.import_vcf(vcf,force_bgz=True,reference_genome='GRCh37')
		out_name = os.path.join(out_path,os.path.basename(os.path.splitext(os.path.splitext(vcf)[0])[0] + ".mt"))
		print("out name: {}".format(out_name))
		mt.write(out_name,overwrite=True)
