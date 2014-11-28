import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))

data = pd.read_csv('aapl.csv', index_col='Date', parse_dates=True)
data.head()
