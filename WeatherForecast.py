import urllib.request, urllib.parse, urllib.error
import json
import ssl
import time

api_key = '541afa84d57****************2'   #use your own API KEY
serviceurl = 'https://api.openweathermap.org/data/2.5/weather?'
choice = True

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while(choice):
    address = input('Enter location: ')
    parms = dict()
    parms['q'] = address
    if api_key is not False: parms['appid'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving the report...',)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js :
        print('==== Failure To Retrieve ====')
        print(data)
    else:
        try:
            print("============= Welcome to the weather forecasting =============")
            print('Weather report in: ', js['name'], ',', js['sys']['country'], 'is' , js['weather'][0]['description'])
            print('\t Wind Speed:', js['wind']['speed'], 'm/s')
            print('\t Temp:', (js['main']['temp']-273.150),"˚C")
            print('\t Pressure:', js['main']['pressure'], 'hpa')
            print('\t Humidity:', js['main']['humidity'], '%')
            print('\t Sea level:', js['main']['sea_level'], 'm')
            riseTime = time.strftime("%D %H:%M", time.localtime(int(js['sys']['sunrise']))).split()
            setTime = time.strftime("%D %H:%M", time.localtime(int(js['sys']['sunset']))).split()
            print('\t Sunrise:', riseTime[1])
            print('\t Sunrise:', setTime[1])
            print('\t Geo coords: [', js['coord']['lat'], ',', js['coord']['lon'], ']')
        except:
            print("=============================================================")
    choice = input("Do you want to search for weather again[Y/N]:")
    if choice == 'Y':
        choice = True
    else:
        choice = False
        print("Thank You! Visit Again :) ")
