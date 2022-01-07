from sys import int_info
import ftx
import pprint
import json
import requests
from requests.models import Response
import pprint
from ftx import FtxClient








def short():
    api_key = 'TEiyW-MuA9al-cLgAw32nhEGrt9LgWY1K47-tHCh'
    api_secret = '6PTcHT7s_gesH36U0nLbg4XgWhEMunxWQwfIM9ES'
    client = FtxClient(api_key=api_key, api_secret=api_secret)
    symbol = 'BTC-PERP'
    side = 'sell'
    qty = 0.00021
    price = 12345.0
    client.place_order(symbol, side, price, qty)

def long():
    api_key = 'TEiyW-MuA9al-cLgAw32nhEGrt9LgWY1K47-tHCh'
    api_secret = '6PTcHT7s_gesH36U0nLbg4XgWhEMunxWQwfIM9ES'
    client = FtxClient(api_key=api_key, api_secret=api_secret)
    symbol = 'BTC-PERP'
    side = 'buy'
    qty = 0.00021
    price = 12345.0
    client.place_order(symbol, side, price, qty)