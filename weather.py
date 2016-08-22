import urllib3
import json

from pprint import pprint

BASEURL = 'http://api.openweathermap.org/data/2.5/weather'
CONSUMER_KEY = '2bc3e79bb974a007818864813f53fd35'

def weather(cities):

    ''' Function to print weather data for various cities '''

    list_cities = []
    http = urllib3.PoolManager()
    units = 'metric'

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
    print '{:>0}  {:>20}  {:>30}'.format('City', 'Temp', 'Description')
    print '='*60

    for city in list_cities:
        pprint(str(city['name']).ljust(20) + "{0}{1}".format(str(city['main']['temp']).ljust(25), str(city['weather'][0]['description'])))

if __name__ == '__main__':
    weather(['Nairobi', 'Lagos', 'New York'])
