import json as js
import feedparser as fp
rss_aapl = fp.parse('http://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US')
type(rss_aapl)

rss_aapl.feed.title
# OUT: u'Yahoo! Finance: AAPL News'
rss_aapl.feed.link
# OUT: u'http://finance.yahoo.com/q/h?s=aapl'
for entry in rss_aapl.entries:
    print entry.title
    
