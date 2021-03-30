import fisher
from fisher import pvalue
import sys
#import scipy.stats as stats
# python /home/wd256/scripts/fisher_file.py <input>
# 5 columns: gene, group1 outcome1, group1 outcome2, group2 outcome1, group2 outcome2

out = open(sys.argv[1][:-4]+"_fisher.txt", 'w')
out.write('\t'.join(['cate','case_mut','case_nor','control_mut','control_nor','pvalue_2_sided','oddsratio_2_sided','pvaluel_less','oddsratiol_less','pvalue_greater','oddsratio_greater'])+'\n')

with open(sys.argv[1],'r') as file:
	for line in file:
		data = line.strip().split('\t')
		if data[0] != 'gene':
			cate = data[0]
			num1 = int(data[1]) # group1, outcome1
			num2 = int(data[2]) # group1, outcome2
			num3 = int(data[3]) # group2, outcome1
			num4 = int(data[4]) # group2, outcome2
			
			p=pvalue(int(num1), int(num2), int(num3), int(num4))
			pvaluet = p.two_tail # total
			pvaluel = p.left_tail
			pvalueg = p.right_tail
			
			if num3 == 0:
				oddsratio = 'inf'
				oddsratiol = 'inf'
				oddsratiog = 'inf'
			else:
				oddsratio = float(num1)/float(num2)/(float(num3)/float(num4))
				oddsratiol = float(num1)/float(num2)/(float(num3)/float(num4))
				oddsratiog = float(num1)/float(num2)/(float(num3)/float(num4))
			
			out.write('\t'.join(map(str,[cate,num1,num2,num3,num4,pvaluet,oddsratio,pvaluel,oddsratiol,pvalueg,oddsratiog]))+'\n')

out.close()