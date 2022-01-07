from requests import Request, Session
import json
import pprint



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'


parameters = {
    'slug':"bitcoin",
    'convert':'USD'
}


headers = {
  'Accepts':'application/json',
  'X-CMC_PRO_API_KEY':'a890905b-52e8-4283-a02c-574185becfd4'
}



session = Session()

session.headers.update(headers)

response = session.get(url, params=parameters)

liste=[]

liste[(json.loads(response.text)['data']['1']['quote']['USD']['market_cap'])]

print(test)

