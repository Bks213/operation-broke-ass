import requests
from requests.models import Response
import pprint

r = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&filterUpTime=100&country=US&protocols=https')
rdic=r.json()

for i in rdic['data']:
    try:
        if r.status_code == 200:
            print(r.status_code)
            ip = (i['ip'])
            port = (i['port'])
            proxy = ({'http': 'https://' + str(ip) + ':' + str(port)})
            print(proxy)
    except:
        pass