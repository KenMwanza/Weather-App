import urllib3
import json

def weather(cities):

    list_cities = []
    http = urllib3.PoolManager()
    consumer_key = '2bc3e79bb974a007818864813f53fd35'
    units = 'metrics'

    baseurl = 'http://api.openweathermap.org/data/2.5/weather'
   
    for city in cities:
        r = http.request(
                'GET',
                baseurl,
                fields={
                    'q':city,
                    'APPID': consumer_key,
                    'units': units
                })

        list_cities.append(json.loads(r.data.decode('utf-8')))
    for city in range(len(list_cities)):
        pprint(list_cities[city]['main']) + " - " + list_cities[city]['name']

