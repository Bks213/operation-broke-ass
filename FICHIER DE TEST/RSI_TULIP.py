from binance.client import Client
import pprint


client = Client('oA6Ym6v1Tj5lvco1sabFZ4rfH0qoxpZVI9NDhOPTr6M46KBq6PCM79MuAq6EW2aG', 'Bekkisb6')

test=client.futures_exchange_info()

listebinance=[]



for i in range(len(test['symbols'])):
    listebinance.append(test['symbols'][i]['baseAsset'])

pprint.pprint(listebinance)





