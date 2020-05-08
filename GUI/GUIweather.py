#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import time
from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    var = StringVar()
    location = StringVar()
    windspeed = StringVar()
    temperature = StringVar()
    pressure = StringVar()
    humidity = StringVar()
    sealevel = StringVar()
    sunrise = StringVar()
    sunset = StringVar()
    geocoord = StringVar()
    root.title("Weather Forecast")

    def weatherreport():
        api_key = 'API_KEY'   #use your own API KEY
        serviceurl = 'https://api.openweathermap.org/data/2.5/weather?'
        choice = True

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        address = var.get()
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
                location.set(f'{"Weather at "}{js["name"]}{", "}{js["sys"]["country"]}{" : "}{js["weather"][0]["description"]}')
                windspeed.set(f'{"Wind Speed:"}{js["wind"]["speed"]}{"m/s"}')
                temperature.set(f'{"Temp: "}{js["main"]["temp"]-273.150}{"˚C"}')
                pressure.set(f'{"Pressure:"}{js["main"]["pressure"]}{"hpa"}')
                humidity.set(f'{"Humidity: "}{js["main"]["humidity"]}{"%"}')
                sealevel.set(f'{"Sea level: "}{js["main"]["sea_level"]}{"m"}')
                riseTime = time.strftime("%D %H:%M", time.localtime(int(js['sys']['sunrise']))).split()
                setTime = time.strftime("%D %H:%M", time.localtime(int(js['sys']['sunset']))).split()
                sunrise.set(f'{"Sunrise: "}{riseTime[1]}')
                sunset.set(f'{"Sunset: "}{setTime[1]}')
                geocoord.set(f'{"Geo coords: ["}{js["coord"]["lat"]}{" , "}{js["coord"]["lon"]}{"]"}')
            except:
                print("Sorry! some error occured")

    icon = PhotoImage(file ='weatherIcon.png').subsample(9, 9)
    frame1 = Frame(root, height =130, width = 200, relief = SUNKEN)
    frame1.grid(row = 0,column = 0)
    label1 = Label(frame1, image = icon).pack()
    frame2 = Frame(root, height = 130, width = 440, relief = SUNKEN, padx = 90)
    frame2.grid(row = 0,column = 1)
    label2 = Label(frame2, text = 'Enter the location: ').grid(row = 0,column = 0)
    entry = Entry(frame2, textvariable = var)
    entry.grid(row = 0,column = 1)
    button1 = Button(frame2, text = 'Submit', padx = 5,command = weatherreport).grid(row = 0,column = 3)
    frame3 = Frame(root, height = 510, width = 380, relief = SUNKEN)
    frame3.grid(row = 1,column = 1)
    label3 = Label(frame3, textvariable = location,foreground = 'blue', font = ("",15,'bold'),pady = 15).grid(row = 1,column = 1)
    label4 = Label(frame3, textvariable = windspeed).grid(row = 2,column = 1)
    label5 = Label(frame3, textvariable = temperature,pady=2).grid(row = 3,column = 1)
    label6 = Label(frame3, textvariable = pressure,pady = 2).grid(row = 4,column = 1)
    label7 = Label(frame3, textvariable = humidity,pady = 2).grid(row = 5,column = 1)
    label8 = Label(frame3, textvariable = sealevel,pady = 2).grid(row = 6,column = 1)
    label9 = Label(frame3, textvariable = sunrise,pady = 2).grid(row = 7,column = 1)
    label10 = Label(frame3, textvariable = sunset,pady = 2).grid(row = 8,column = 1)
    label11 = Label(frame3, textvariable = geocoord,pady = 2).grid(row = 9,column = 1)

    root.geometry('640x380+400+290')
    root.resizable(False , False)
    root.mainloop()


if __name__=='__main__':main()
