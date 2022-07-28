import MetaTrader5 as mt5
import time

mt5.initialize()

ativo = 'EURUSD'

while(True):

    mt5.symbol_select(ativo)
    print(mt5.symbol_info_tick(ativo).last)
    print(mt5.)

