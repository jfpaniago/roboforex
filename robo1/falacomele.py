import duka.app.app as import_ticks_method
from duka.core.utils import TimeFrame
import datetime
import pandas as pd
import matplotlib.pyplot as plt

start_date = datetime.date(2020,3,2)
end_date = datetime.date(2021,1,1)
Assets = ['EUR/USD']

import_ticks_method(Assets,start_date, end_date, 1, TimeFrame.TICK,".", True)

looping_year = 2020

while looping_year < 2022:
    print("downloading data from year: " + str())
    import_ticks_method(Assets,start_date, end_date,1, TimeFrame.TICK,".",True)
