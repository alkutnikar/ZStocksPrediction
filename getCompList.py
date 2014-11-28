import feedparser as fp
import os
from subprocess import call
import subprocess
import pandas as pd

comp=[]
sentDict={}
compFile = open('CompanyList.txt');
NameFile = open('CompaniesNames.txt');
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
