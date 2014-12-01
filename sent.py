import nltk
from nltk import *
import trainWords
from trainWords import trainwords
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import getCompList
from getCompList import *
from nltk.corpus import stopwords

print 'before Classify'
#cl = NaiveBayesClassifier(trainwords)
print 'after Classify'

for cname in compDict.keys():
	
	name = compDict[cname]
	compfile = 'NewsData/'+name+'.txt'
	sentfile = 'SentData/'+name+'_sent.txt'
	fh=open(compfile,'r')
	fg=open(sentfile,'w')
	lines = fh.readlines()
	for line in lines:
		#fg.write(cl.classify(line)+'\n')
		filtered_words = [w for w in line if not w in stopwords.words('english')]


	#blob = TextBlob(line, 
	#		classifier=cl)

	#for sentence in blob.sentences:
	#    print(sentence)
	#    print(sentence.classify())
