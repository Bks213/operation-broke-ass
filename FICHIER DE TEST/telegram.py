import requests
import pprint
import emoji


auth_token = "5024855327:AAFC7oFEkgZfmr_oOsJ9JwJhvFGmgvVUhJk" #token API que botfather va vous procurrer
group_id = "1165631289"#assurez-vous de mettre le id qui appartient a votre groupe
 
""" telegram_update_api = "https://api.telegram.org/bot{auth}/getUpdates".format(auth=auth_token)
r = requests.get(telegram_update_api)
r = r.json()
pprint.pprint(r['result'])"""



def send_message_on_telegram_long(crypto,montantautilise):
    message = ("\U0001F4C8 \n+----LONG OUVERT-----\nLA PAIRE "+crypto+" À ÉTÉ ACHETÉ \n POUR UNE QUANTITÉ DE "+montantautilise+" USDT") 
    
    
    
    
    telegram_api = "https://api.telegram.org/bot{auth}/sendMessage?chat_id={group}&text={msg}".format(auth=auth_token, group=group_id, msg=message)
    telegram_response = requests.get(telegram_api)
    pprint.pprint(telegram_response)

    if telegram_response.status_code == 200:
        print("OK, 200")
    else:
        print ("ERROR, 400")


def send_message_on_telegram_short(crypto,usdt):
    message = ("La paires "+crypto+" a été acheter \n Pour une quantité de: "+usdt+" USDT") 
    telegram_api = "https://api.telegram.org/bot{auth}/sendMessage?chat_id={group}&text={msg}".format(auth=auth_token, group=group_id, msg=message)
    telegram_response = requests.get(telegram_api)
    pprint.pprint(telegram_response)

    if telegram_response.status_code == 200:
        print("OK, 200")
    else:
        print ("ERROR, 400")


send_message_on_telegram_long("BTC-PERP","15")



