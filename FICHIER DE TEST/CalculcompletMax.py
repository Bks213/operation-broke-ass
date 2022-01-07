import threading
import multiprocessing
import time
import pprint
import requests
from requests.models import Response
import json
import re
import time

r = requests.get('https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=14')

r=r.json()

price_list = []
short_list = []
long_list = []

#rajouter nos 14 dernieres prix du coin
for i in range(14):
    price_list.append(r['Data']['Data'][i]['close'])
price_list.sort()

#rajouter les 7 prix les plus bas a une nouvelle liste
for i in range(7):
    short_list.append(price_list[i])
#rajouter les 7 derniers prix a une autre liste
for i in range(7):
    long_list.append(price_list[7+i])

avg_loss = (sum(short_list)/7)
avg_gain = (sum(long_list)/7)
coin = "asscoin"    #example
num_coin = 140   #exemple (nombre de coins qu'on va passer par le calcul)


#calculer le RSI sur une periode determinee
def get_rsi_1(avg_gain,avg_loss,coin):
    short_val = 76
    long_val = 24
    short = []
    long = []
    rsi_1 = 100 - (100 / (1 + ((avg_gain / 14) / (avg_loss / 14))))
#conditions si le coin va etre mis dans la liste long (overvalued) ou short (undervalued)
    if rsi_1 >= short_val:
        short.append(coin)
        print(coin, " is overvalued.")
    elif rsi_1 <= long_val:
        long.append(coin)
        print(coin, " is undervalued.")
    return(short,long,rsi_1)


#calculer RSI a chaque 60 secondes
def rsi_automated():
    threading.Timer(60.0, rsi_automated).start()
    print(get_rsi_1(avg_gain,avg_loss,coin))


#optimisation du calcul RSI automatise (rsi_automated) en utilisant le multi-processing
if __name__ == '__main__':
    tic = time.time()

    liste_taches = []
    var = { "avg_gain": avg_gain, "avg_loss": avg_loss, "coin": coin }

    for i in range(num_coin):
        tache = multiprocessing.Process(target=get_rsi_1, args=(var["avg_gain"], var["avg_loss"], var["coin"]))
        tache.start()
        liste_taches.append(tache)

    for t in liste_taches:
        t.join()

    toc = time.time()

    print("Fini en: {:.4f} secondes".format(toc-tic))

# #timeout de la tache automatisee du calcul de RSI
# def rsi_timeout(timeout, rsi_automated):
#     #verifier si la marge de l'execution d'un proces est valide
#     if type(timeout) not in [int, float] or timeout <= 0.0:
#         print("Invalid timeout.")
#     #verifier si la fonction get_rsi_1 peut etre appelee
#     elif not callable (rsi_automated):
#         print("{} function is not callable.".format(type(rsi_automated)))
#     #on fait marcher des taches simultanement (optimisation)
#     else:
#         tache = multiprocessing.Process(target=rsi_automated)
#         tache.start()
#         tache.join(timeout)
#         #on verifie si la fonction marche toujours apres que le temps maximal pour l'execution de la tache est expire
#         #condition: si oui, on tue le processus, sinon, we good
#         if tache.is_alive():
#             tache.terminate()
#             return False
#         else:
#             return True





