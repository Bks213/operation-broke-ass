import requests
from requests.models import Response
from tradingview_ta import TA_Handler, Interval, Exchange
import pprint
from getsymbolsfutures import *


BTC = TA_Handler(
    symbol="BTCUSDTPERP",
    screener="CRYPTO",
    exchange="BINANCE",
    interval=Interval.INTERVAL_1_MINUTE,
    proxies={'http': 'https://178.128.178.169:3128'}
)


r=(BTC.get_indicators())

pprint.pprint(r['RSI'])


