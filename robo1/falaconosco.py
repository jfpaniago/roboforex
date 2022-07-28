import pandas as pd
import datetime




df = pd.read_csv('EURUSDmin.csv')
df.columns = [['date','open','high','low','close','volume']]

print(df)