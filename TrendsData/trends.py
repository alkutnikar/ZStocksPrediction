import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))

data = pd.read_csv('a.csv', index_col='Date', parse_dates=True)
data.head()

data.plot(label='actual search');
search_trend = pd.rolling_mean(data['Search'], 5)
search_trend.plot(label='search_trend')
plt.legend()
plt.show()

data['order'] = 9*2
data['order'][data['Search'] < 90] = 8*2 # Long if search volume goes down relative to mavg.
data['order'][data['Search'] < 75] = 7*2 # Long if search volume goes down relative to mavg.
data['order'][data['Search'] < 60] = 4*2 # Long if search volume goes down relative to mavg.
data['order'][data['Search'] < 40] = 3*2 # Long if search volume goes down relative to mavg.
data['order'][data['Search'] < 25] = 2*2 # Long if search volume goes down relative to mavg.


data['order'][data['Search'] > search_trend+5] = data['order'] + 4; # Short if search volume goes up relative to mavg.
data['order'][data['Search'] < search_trend-5] = data['order'] + 4; # Long if search volume goes down relative to mavg.
data.plot(label = 'order')
plt.show()

'''
data['ret_search'] = data['Search'].pct_change()
print data

data['ret_search'] = data['ret_search'].shift(-1)

data['ret_aapl'] = data.order * data.ret_search
print data

(1 + data.ret_aapl).cumprod().plot();
plt.ylabel('Portfolio value')
plt.show()
'''
