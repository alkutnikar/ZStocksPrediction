import getCompList
from getCompList import *
import re
fw = open('AllSocialSents','w')
for cname in compDict.keys():
	fr = open('SocialMediaData/'+compDict[cname]+'.txt','r')
	lines = fr.readlines()
	i=0
	for line in lines:
		if i==0:
			i=i+1
			continue
		line = re.sub(r'"',r'',line)
		sents = line.split(',')
		pos = int(sents[0])
		neg = int(sents[2])
		nuetral = int(sents[1])
		stName=compDict[cname]
		if pos>neg:
			if pos>nuetral:
				print stName+':+ '+str(pos-neg)
				continue
			else:
				try:
					fw.write(str(stName+':nuetral-pos '+str(float(nuetral)/float(pos))+'\n'))
				except ZeroDivisionError:
					fw.write(stName+':nuetral\n')
		else: 
			if neg>nuetral:
				print stName+':- '+str(neg-pos)
				continue
			else:
				try:
					fw.write(str(stName+':nuetral-neg '+str(float(nuetral)/float(neg))+'\n'))
				
				except ZeroDivisionError:
					fw.write(stName+':nuetral\n')
