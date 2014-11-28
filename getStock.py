#Import packages
import getCompList
from getCompList import *
import datetime
import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('figure',figsize=(8,7))

for comp in compDict.keys():
    tempStock = pd.io.data.get_data_yahoo(compDict[comp], 
                                 start=datetime.datetime(2009, 1, 1), 
                                 end=datetime.datetime(2014, 12, 2))
    tempStock.head()
    comp = comp.replace(' ','')
    
    open('StockData/'+comp+'.csv','w')

    tempStock.to_csv('StockData/'+comp+'.csv')
print 'All Stock Data Files created.'
