from sys import int_info
import ftx
import pprint
import json
import requests
from requests.models import Response
from tradingview_ta import TA_Handler, Interval, Exchange
import pprint
from info import *
from proxy import *

client = ftx.FtxClient(api_key="TEiyW-MuA9al-cLgAw32nhEGrt9LgWY1K47-tHCh", api_secret="6PTcHT7s_gesH36U0nLbg4XgWhEMunxWQwfIM9ES")
futures2 = requests.get('https://ftx.com/api/funding_rates').json()
listeftx=[]
for i in range(len(futures2['result'])):
    listeftx.append(futures2['result'][i]['future'])
listesansperp=[]
for i in range(len(listeftx)):
    listesansperp.append(listeftx[i][:-5])
print(listesansperp)

def rsi():
    short = []
    long = []
    for i in listesansperp: 
        try:
            BTC = TA_Handler(
                symbol=i+"PERP",
                screener="CRYPTO",
                exchange="FTX",
                interval=intervales,
                proxies=proxy)
            c=(BTC.get_indicators()) 
            r=(c["RSI"])
            if r >= rsiplushaut:
                short.append(i)
            elif r <= rsiplusbas:
                long.append(i)
            print(i)
            print(r)
        except:
            print("error",i)
        pass

    print("RSI PLUS HAUT QUE "+str(rsiplushaut)+": "+str(short))
    print("RSI PLUS BAS QUE "+str(rsiplusbas)+": "+str(long))

rsi()