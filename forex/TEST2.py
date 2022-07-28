import MetaTrader5
import fxcmpy as fxcmpy
from numpy.distutils.command import install


import fxcmpy
import datetime as dt
import socketIO_client
token = "0671c9c9802ff587ca5c049333dc7fe550decc70"
con = fxcmpy.fxcmpy(access_token=token, log_level='error',log_file=None, proxy_port='https://tradingstation.fxcm.com/?fx_sh=dHNtYXAlMjAlM0UlMjBmeGNtdWs=&fx_lce&fx_sid=1615081881427ziBU8S0&cmp&btag&lc=en_US&_ga=2.189314539.1733783855.1615081884-1763458435.1604463971')
def on_tick(data, df):
    print('price change')

con.subscribe_market_data('EURUSD'(on_tick,))