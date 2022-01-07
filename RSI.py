import requests
from requests.models import Response
from tradingview_ta import TA_Handler, Interval, Exchange
import pprint
from getsymbolsfutures import *
from info import *
from proxy import *

def rsi():
    short = []
    long = []
    for i in listebinance: 
        try:
            BTC = TA_Handler(
                symbol=i+"USDTPERP",
                screener="CRYPTO",
                exchange="BINANCE",
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






