import feedparser as fp
import os
from subprocess import call
import subprocess
import pandas as pd

comp=[]
sentDict={}
compFile = open('../CompanyList.txt');
NameFile = open('../CompaniesNames.txt');
line = compFile.readlines()
comp = line[0].split(' ')
i=0
newsDict={}

compNames = NameFile.readlines()

compDict={}
name_arr = compNames[0].split(']')
for cname in name_arr:
    if cname=='\n':
        continue
    name = cname.split('(')
    tempName = name[0]
    if len(name) > 1:
        tempAbbr = name[1]
    tempName = tempName[:-1].replace('\n','')
    tempAbbr = tempAbbr[:-1]
    compDict[str(tempName)] = str(tempAbbr)
print compDict


#Import packages
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
    
    open(comp+'.csv','w')

    tempStock.to_csv('data/'+comp+'.csv')
