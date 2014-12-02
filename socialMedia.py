import requests
import getCompList 
from getCompList import *

for cname in compDict.keys():
	queryString = cname+' "'+compDict[cname]+'"'
	fg = open('SocialMediaData/'+compDict[cname]+'.txt','w')
	print queryString
	sentiment = requests.get("http://socialmention.com/search?q="+queryString+"&t=all&f=csv&metadata=sentiment")
	print sentiment.content
	fg.write(sentiment.content)
	#mention = requests.get("http://socialmention.com/search?q="+queryString+"&t=all&f=csv")
	#print mention

