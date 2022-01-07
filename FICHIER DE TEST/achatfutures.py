from sys import int_info
import ftx
import pprint
import json
import requests
from requests.models import Response
import pprint
from ftx import FtxClient
import ccxt


client = ftx.FtxClient(api_key="TEiyW-MuA9al-cLgAw32nhEGrt9LgWY1K47-tHCh", api_secret="6PTcHT7s_gesH36U0nLbg4XgWhEMunxWQwfIM9ES")




def getcryptosize(cryptoname):
    cryptoname = requests.get('https://ftx.com/api/markets/'+cryptoname+'-PERP').json()
    price=(cryptoname["result"]['price'])
    quantitepre=(10/price)
    quantite=round(quantitepre,5)
    print(quantitepre)


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
    type='stop_limit'
    side = 'buy'
    qty = 0.00021
    price = 12345.0
    client.place_order(type,symbol, side, price, qty)
    

ccxt_bot = ccxt.ftx({
    'enableRateLimit': True,
    'apiKey': 'TEiyW-MuA9al-cLgAw32nhEGrt9LgWY1K47-tHCh',
    'secret': '6PTcHT7s_gesH36U0nLbg4XgWhEMunxWQwfIM9ES', 
})


coin='BTC-PERP'
amount=0.00019
stopPrice="40000"

ccxt_bot.create_order(coin, 'stop', stopPrice, 'buy', amount, {'leverage': 5})
