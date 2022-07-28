import pandas as pd
import datetime

df = pd.read_csv('EURUSDmin.csv')
df.columns = [['date','open','high','low','close','volume']]
pd.read_csv( s, index_col=0, parse_dates=True, dayfirst=True)