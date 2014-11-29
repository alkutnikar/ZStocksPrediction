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
    mpl.rc('figure',figsize=(13,13))
    tempStock = pd.io.data.get_data_yahoo(compDict[comp], 
                                 start=datetime.datetime(2009, 1, 1), 
                                 end=datetime.datetime(2014, 12, 2))
    close_px = tempStock['Adj Close']
    mavg = pd.rolling_mean(close_px, 10)
    exavg = pd.ewma(close_px, 10)
    #mavg[-10:]
    #exavg[-10:]
    close_px.plot(label=comp)
    mavg.plot(label='mavg') 
    exavg.plot(label='exavg')
    #plt.figure()
    #plt.hold(False)
    plt.legend()
    #pylab.savefig('MvAvgPlots/'+comp+'.png')
    #plt.show();
    tempStock.head()
    comp = comp.replace(' ','')
    
    open('StockData/'+comp+'.csv','w')

    tempStock.to_csv('StockData/'+comp+'.csv')
print 'All Stock Data Files created.'
