import pandas as pd
import datetime

from datetime import date

df = pd.read_csv('estrategia.csv')
df.columns
print(df)
df.date= pd.to_datetime(df.date,format='%d.%m.%Y %H:%M%:%S.%f')