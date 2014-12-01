import nltk
from nltk import *
import trainWords
from trainWords import negwords
from trainWords import poswords
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import getCompList
from getCompList import *
from nltk.corpus import stopwords
import re

#cl = NaiveBayesClassifier(trainwords)

fg=open('AllSents','w')
for cname in compDict.keys():
	
	name = compDict[cname]
	compfile = 'NewsData/'+name+'.txt'
	sentfile = 'SentData/'+name+'_sent.txt'
	fh=open(compfile,'r')
	lines = fh.readlines()
	sum=0
	for line in lines:
		#fg.write(cl.classify(line)+'\n')
		line = re.sub('\n','', line.rstrip())
		line = re.sub('\.','', line.rstrip())
		line = re.sub(',','', line.rstrip())
		line = re.sub(':','', line.rstrip())
		line = re.sub('\'','', line.rstrip())
		words = line.split(' ')
		for word in words:
			word = word.upper()
			print word
			if word in negwords:
				sum = sum - 1;
			if word in poswords:
				sum = sum + 1;
	fg.write(name+','+str(sum)+';')
	#blob = TextBlob(line, 
	#		classifier=cl)

	#for sentence in blob.sentences:
	#    print(sentence)
	#    print(sentence.classify())
