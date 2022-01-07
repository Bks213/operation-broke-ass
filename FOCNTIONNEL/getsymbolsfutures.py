from binance.client import Client
import pprint
from info import *


client = Client(ApiKey, SecretKey)

test=client.futures_exchange_info()

listebinance=[]



for i in range(len(test['symbols'])):
    listebinance.append(test['symbols'][i]['baseAsset'])

print(listebinance)


