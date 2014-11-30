#Import packages
import getCompList
from getCompList import *
import datetime
import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
from pylab import *
import getMAvg
from getMAvg import *

for comp in compDict.keys():
	comp='Apple Inc'
	mpl.rc('figure',figsize=(13,13))
	tempStock = pd.io.data.get_data_yahoo(compDict[comp], 
				 start=datetime.datetime(2009, 1, 10), 
				 end=datetime.datetime(2014, 11, 29))
	close_px = tempStock['Adj Close'][::5]
	mavg = pd.rolling_mean(close_px, 10)
	exavg = pd.ewma(close_px, 10)
	#mavg[-10:]
	#exavg[-10:]
	close_px.plot(label=comp)
	mavg.plot(label='rolling_mean') 
	exavg.plot(label='exavg')
	#plt.figure()
	#plt.hold(False)
	plt.legend()
	#pylab.savefig('MvAvgPlots/'+comp+'.png')
	mpl.rc('figure', figsize=(8, 7))

	data = pd.read_csv('TrendsData/a.csv', index_col='Date', parse_dates=True)
	data.head()

	data.plot(label='actual search');
	search_trend = pd.rolling_mean(data['Search'], 5)
	search_trend.plot(label='publication_search_trend')
	plt.legend()

	close_px.plot(label=comp)
	#data['stock'] = close_px
	data['CSE591'] = 9*2
	data['CSE591'][data['Search'] < 90] = 8*2 # Long if search volume goes down relative to mavg.
	data['CSE591'][data['Search'] < 75] = 7*2 # Long if search volume goes down relative to mavg.
	data['CSE591'][data['Search'] < 60] = 4*2 # Long if search volume goes down relative to mavg.
	data['CSE591'][data['Search'] < 40] = 3*2 # Long if search volume goes down relative to mavg.
	data['CSE591'][data['Search'] < 25] = 2*2 # Long if search volume goes down relative to mavg.


	data['CSE591'][data['Search'] > search_trend+5] = data['CSE591'] + 4; # Short if search volume goes up relative to mavg.
	data['CSE591'][data['Search'] < search_trend-5] = data['CSE591'] + 4; # Long if search volume goes down relative to mavg.
	data.plot(label = 'CSE591 model')
	close_px.plot(label=comp)
	print data
	plt.show()
	#plt.show();
	tempStock.head()
	comp = comp.replace(' ','')

	open('StockData/'+comp+'.csv','w')

	tempStock.to_csv('StockData/'+comp+'.csv')
	print 'All Stock Data Files created.'
