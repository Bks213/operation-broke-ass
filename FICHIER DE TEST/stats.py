
import pprint
import requests
from requests.models import Response
import json
import re
import time

tic = time.time()

r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=150&page=1&sparkline=false')

r=r.json()

liste=[]


for i in range(150):
    liste.append(r[i]['symbol'])







