import getCompList
from getCompList import *

for cname in compDict.keys():
	fr = open('SocialMediaData/'+compDict[cname]+'.txt','r')
	lines = fr.readlines()
	for line in lines:
		print line
