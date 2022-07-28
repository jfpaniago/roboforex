import fxcmpy
import pandas as pd
import json
import requests
import socketio
print(fxcmpy.__version__)
print(socketio.__version__)
TOKEN = '7bb98a981628726a9534889b662befb20479e64b'
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='debug', server='demo', log_file='mylog2.txt')
data = con.get_candles('EUR/USD',period='m1', number=10)

