import urllib3
import json

from pprint import pprint

BASEURL = 'http://api.openweathermap.org/data/2.5/weather'
CONSUMER_KEY = '2bc3e79bb974a007818864813f53fd35'

def weather(cities):

    ''' Function to print weather data for various cities '''

    list_cities = []
    http = urllib3.PoolManager()
    units = 'metrics'

    for city in cities:
        r = http.request(
                'GET',
                BASEURL,
                fields={
                    'q':city,
                    'APPID': CONSUMER_KEY,
                    'units': units
                })

        list_cities.append(json.loads(r.data.decode('utf-8')))
    for city in list_cities:
        pprint(str(city['name']).ljust(20))
        print " - Temp: {0} Temp_min: {1} Temp_max: {2}".format(str(city['main']['temp']).ljust(10), str(city['main']['temp_min']).ljust(10), str(city['main']['temp_max']).ljust(10))

if __name__ == '__main__':
    weather(['Nairobi', 'Lagos', 'New York'])
