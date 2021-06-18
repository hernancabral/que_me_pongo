import requests
import datetime as dt

KELVIN = 273.15

def get_obj(day, data):
    for forecast in data["list"]:
        if forecast["dt_txt"] == str(day):
            return forecast
    return None

def get_data():
    try:
        url = "http://api.openweathermap.org/data/2.5/forecast?q=Buenos Aires&appid=8e5b09317f9f795dc7a425b969cae64c"
        res = requests.get(url)
        data = res.json()
    except:
        return "No Internet"

    today = dt.datetime.now()

    if today.hour < 15:
        day = dt.datetime(today.year, today.month, today.day, 15)
    elif today.hour < 21:
        day = dt.datetime(today.year, today.month, today.day, 21)
    else:
        day = dt.datetime(today.year, today.month, today.day, 23)
    weather_list = []

    weather = True
    second_none_flag = False

    while weather:
        weather = get_obj(day, data)
        if weather:
            weather_list.append((weather, day))
        if not second_none_flag:
            second_none_flag = True
            weather = True
        if day.hour + 3 <= 21:
            day = dt.datetime(day.year, day.month, day.day, day.hour + 6)
        else:
            try:
                day = dt.datetime(day.year, day.month, day.day + 1, 9)
            except:
                try:
                    day = dt.datetime(day.year, day.month + 1, 1, 9)
                except:
                    day = dt.datetime(day.year + 1, 1, 1, 9)
    
    return weather_list