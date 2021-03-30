import hail as hl
import os

hl.init()

#Import combined.ht
combined = hl.read_table('/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/combined.gnomad.r2.1.1.sites.5.raw.mt')

combined.filter((combined.locus.position == 140951552) | 
				(combined.locus.position == 140961878) | 
				(combined.locus.position == 140966765) |
				(combined.locus.position == 140896419) |
				(combined.locus.position == 140903709) |
				(combined.locus.position == 140906029) | 
				(combined.locus.position == 140953143) |
				(combined.locus.position == 140953315) |
				(combined.locus.position == 140954663) |
				(combined.locus.position == 140955845) |
				(combined.locus.position == 140956322) |
				(combined.locus.position == 140957159) |
				(combined.locus.position == 140958653) |
				(combined.locus.position == 140958654) |
				(combined.locus.position == 140958748) |
				(combined.locus.position == 140960420) |
				(combined.locus.position == 140966667) |
				(combined.locus.position == 140967812) |
				(combined.locus.position == 140998408))

df = combined.to_pandas()

df.to_csv("/gpfs/ycga/project/kahle/sp2349/weilai_gnomad/tables/missing_vars_check.txt",sep="/t")
