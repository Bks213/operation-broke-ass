import requests
import pprint


auth_token = "5024855327:AAFC7oFEkgZfmr_oOsJ9JwJhvFGmgvVUhJk" #token API que botfather va vous procurrer
group_id = "1165631289"#assurez-vous de mettre le id qui appartient a votre groupe
 
""" telegram_update_api = "https://api.telegram.org/bot{auth}/getUpdates".format(auth=auth_token)
r = requests.get(telegram_update_api)
r = r.json()
pprint.pprint(r['result'])"""


crypto="BTC-PERP"

def send_message_on_telegram():
    message = ("La paires "+crypto+" a été acheter") 
    telegram_api = "https://api.telegram.org/bot{auth}/sendMessage?chat_id={group}&text={msg}".format(auth=auth_token, group=group_id, msg=message)
    telegram_response = requests.get(telegram_api)
    pprint.pprint(telegram_response)

    if telegram_response.status_code == 200:
        print("OK, 200")
    else:
        print ("ERROR, 400")

send_message_on_telegram()




