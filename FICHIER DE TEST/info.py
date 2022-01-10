from tradingview_ta import TA_Handler, Interval, Exchange
from proxy import *
import ccxt

#------------------------------------INSTALLATION----------------------------------#



"""IL FAUDRA INSTALLER LES LIBRAIRIES SUIVANTES DANS LE CMD

pip install python-binance
pip install tradingview_ta
pip install binance-futures-connector


"""

#------------------------------------BINANCE----------------------------------#

ApiKey=""#METTRE VOTRE CLÉ API ENTRE LES 2 PARENTHÈSES
SecretKey=""    #METTRE VOTRE CLÉ SECRÈTE ENTRE LES 2 PARENTHÈSES


#-----------------------------------PARAMÈTRES DU RSI-----------------------------------#

rsiplushaut=(76)#METTRE LA VALEUR SUPÉRIEUR DU RSI
rsiplusbas=(24)#METTRE LA VALEUR INFÉRIEUR DU RSI


#-----------------------------------PARAMÈTRES INTERVAL-----------------------------------#

#CE BASER SUR LE TABLEAU SI DESSOUS POUR CHOISIR L'INTERVAL EN SUIVANT LE MODÈLE SUIVANT

intervales=Interval.INTERVAL_1_MINUTE

"""
    INTERVAL_1_MINUTE 
    INTERVAL_5_MINUTES
    INTERVAL_15_MINUTES
    INTERVAL_30_MINUTES
    INTERVAL_1_HOUR
    INTERVAL_2_HOURS
    INTERVAL_4_HOURS
    INTERVAL_1_DAY
    INTERVAL_1_WEEK
    INTERVAL_1_MONTH
    """


#-----------------------------------PARAMÈTRES DU COMPTE-----------------------------------#
ccxt_bot = ccxt.ftx({
    'enableRateLimit': True,
    'apiKey': 'TEiyW-MuA9al-cLgAw32nhEGrt9LgWY1K47-tHCh',
    'secret': '6PTcHT7s_gesH36U0nLbg4XgWhEMunxWQwfIM9ES', 
})


pourcentage=50 #pourcentage du portefeuille utilisé à chaque trade

stoplosspourcentage=10
