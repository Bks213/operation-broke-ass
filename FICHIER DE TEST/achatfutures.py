from sys import int_info
import pprint
import json
import requests
from requests.models import Response
import pprint
import ccxt
from telegram import *
from info import *

ccxt_bot = ccxt.ftx({
    'enableRateLimit': True,
    'apiKey': 'TEiyW-MuA9al-cLgAw32nhEGrt9LgWY1K47-tHCh',
    'secret': '6PTcHT7s_gesH36U0nLbg4XgWhEMunxWQwfIM9ES', 
})


def balancecompte():
    infocompte=(ccxt_bot.fetch_balance())
    global balance
    balance=(float(infocompte['info']['result'][2]['free']))



def getcryptosize(cryptoname):
    balancecompte()
    requete = requests.get('https://ftx.com/api/markets/'+cryptoname+'-PERP').json()
    price=(requete['result']['price'])
    global montantautilisé
    montantautilisé=(pourcentage*balance)/100
    global quantite
    quantite=(montantautilisé/price)
    print(quantite)




cryptoaacheter='SOL'



def long():
    getcryptosize(cryptoaacheter)
    coin=cryptoaacheter+"-PERP"
    amount=quantite
    ccxt_bot.create_order(coin,'market','buy',amount,params={'leverage': 15})
    requete = requests.get('https://ftx.com/api/markets/'+cryptoaacheter+'-PERP').json()
    prix=(requete['result']['price'])
    stoploss=(prix-(prix*stoplosspourcentage/100))
    #ccxt_bot.create_order(coin,'stop','sell',amount,params={'triggerPrice':139})
    send_message_on_telegram_long(coin,str(montantautilisé))


long()

