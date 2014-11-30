from subprocess import call
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import pandas.io.data
from pandas import Series, DataFrame
from textblob import TextBlob
 
comp=[]
sentDict={}
comp = line[0].split(' ')
i=0
newsDict={}
fh = None;


import feedparser as fp
import os
from subprocess import call
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import pandas.io.data
from pandas import Series, DataFrame
from textblob import TextBlob

comp=[]
sentDict={}
compFile = open('../CompanyList.txt');
NameFile = open('../CompaniesNames.txt');
line = compFile.readlines()
comp = line[0].split(' ')
i=0
newsDict={}
fh = None;



compNames = NameFile.readlines()

compList = []
name_arr = compNames[0].split(']')
for cname in name_arr:
    name = cname.split('(')
    tempname = name[0]
    compList.append(tempname[:-1].replace('\n',''))
print compList



def getSentiments():
	i=0
	global entryList
	for name,cname in zip(comp[:-1],compList[:-1]):
		print cname
		i=i+1
		if i > 5:
		    break
		if name!=None:
			rss_aapl = get_rss_yahoo(name)
			entryList=[]
			compfile = name+'.txt'
			sentFile = name+'_sent.txt'
			fh = open(compfile,'w')
			fg = open(sentFile,'w')
			write_rss(rss_aapl)
			rss_aapl = get_rss_google(name)
			write_rss(rss_aapl)
			cn = cname.split(' ')
			#proc = subprocess.Popen(['curl','--data-binary','@AAPL.txt',"http://www.sentiment140.com/api/bulkClassify?query=Apple"], stdout=subprocess.PIPE, shell=True)
			cmdString = 'curl --data-binary @'+name+'.txt "http://www.sentiment140.com/api/bulkClassify?query=Apple"'
			#cmdString = 'curl --data-binary @AAPL.txt "http://www.sentiment140.com/api/bulkClassify?query=Apple"'
			output = subprocess.check_output(cmdString,shell=True)
			print cn[0]
			lines = output.split('\n')
			sum = 0
			for line in lines:
			    sent=line.split(',')
			    sentiment = sent[0].replace('"','')
			    if sentiment=='0':
				sum=sum-1
			    elif sentiment=='4':
				sum=sum+1
			sentDict[name] = sum
			newsDict[name]=entryList
			fh.close()
			fg.close()
			print sentDict
	print 'done'



def get_rss_yahoo(name):
    url = r"http://feeds.finance.yahoo.com/rss/2.0/headline?s={0}&region=US&lang=en-US".format(name)
    return fp.parse(url)

def get_rss_google(name):
    url = r"https://www.google.com/finance/company_news?q=NASDAQ:{0}&ei=MrxZVNjKI8u68gaRxoG4Bg&output=rss".format(name)
    return fp.parse(url)


def write_rss(rss_aapl):
    global fh;
    for entry in rss_aapl.entries:
                        title = entry.title
                        entryList.append(entry.title)
                        import unicodedata
                        title = unicodedata.normalize('NFKD', title).encode('ascii','ignore')
                        fh.write(title+'\n')

def display_mvavg_plot():
	mpl.rc('figure', figsize=(8, 7))

	aapl = pd.io.data.get_data_yahoo('AAPL', 
					 start=datetime.datetime(2014, 9, 1), 
					 end=datetime.datetime(2014, 11, 1))
	aapl.head(6)

	ts = aapl['Close'][-10:]
	ts

	close_px = aapl['Adj Close']

	mavg = pd.rolling_mean(close_px, 40)
	mavg[-10:]


	close_px.plot(label='AAPL')
	mavg.plot(label='mavg')
	plt.legend()
	plt.show()


def textblob_sentiment():
	text = '''
	Apple Store looks for a boost with new leader Angela Ahrendts.
	What 1 Expert Is Watching At Tesla.
	How the iPad mini became Apples middle child.
	My dream investor. 
	Timexs $36 Watch Answer to Apple Watch.
	Facebook, Skyworks Among IBD 50's Top 5 Tech Earnings.
	Apple told its sapphire supplier Put on your big boy pants.
	World losing battle against global warming.
	Apple Accused of Bait and Switch.
	GoPro mum on new cameras; SNL suggests a colonoscopy cam.
	Apple Loop: Eleven iPhone Tips, Apple Watch SDK, Xperia Defeats iPhone.
	Taiwan Semiconductor In Buy Range From Breakout.
	ATM Czar Euronet Adds U.S. To A Global Growth Engine.
	Final Glance: Computer companies.
	Final Glance: Computer companies.
	What Apple has in common with F-35 maker Lockheed Martin.
	GT Advanced says fell victim to 'bait-and-switch' by Apple.
	GT Advanced says fell victim to 'bait-and-switch' by Apple.
	The top 15 smartphones you can buy right now.
	Documents show acrimony over failed Apple deal.
	Apple Inc.'s Latest Supplier Negotiating Tactics With GT Advanced Revealed.
	Is Apple, Inc. Stock Still Cheap at All-Time Highs?
	Should Apple, Inc. Investors Fear a 2016 iPhone Sales Meltdown?
	Profit
	'''

	blob = TextBlob(text)
	blob.tags           # [(u'The', u'DT'), (u'titular', u'JJ'),
			    #  (u'threat', u'NN'), (u'of', u'IN'), ...]

	blob.noun_phrases   # WordList(['titular threat', 'blob',
			    #            'ultimate movie monster',
			    #            'amoeba-like mass', ...])

	for sentence in blob.sentences:
	    print(sentence.sentiment.polarity)
	# 0.060
	# -0.341

	blob.translate(to="es")  # 'La amenaza titular de The Blob...'


getSentiments()
