from typing import Dict, Any
import arrange_data
import datetime as dt


class WeatherService:

    @classmethod
    def get_weather(cls) -> Dict[str, Any]:
        return getAndParseData()


def getAndParseData():
    forecast = arrange_data.arrange_data()

    today = dt.datetime.now()
    tomorrow = dt.datetime(today.year, today.month, today.day + 1)
    days = []
    for tempDay in forecast:
        for tempHour in tempDay:
            if tomorrow.day == tempHour[0].day:
                days.append(tempHour)
    rainChances = get_rain_chances(days)
    temperature = getTemp(days)
    sky = getSky(days)
    if rainChances > 61:
        willRain = True
    else:
        willRain = False
    returnObj = {'temperature': temperature, 'rain': willRain}
    return returnObj

def getSky(days):
    sky = 0
    for day in days:
        if day[3][0] == "Despejado":
            sky += 1
        else:
            sky += 3
    if sky >= 4:
        return "Nublado"
    else:
        return "Despejado"

def getTemp(days):
    temperature = 0
    for day in days:
        temperature += int(day[1][1])
    temperature = temperature / len(days)
    return round(float(temperature),2)

def get_rain_chances(days):
    humidity = float(get_humidity(days))
    sky_desc = get_sky(days)

    sky_const = 0
    humidity_const = 0
    bias = 25

    sky = sky_desc.split(",")
    if sky[0] == "Despejado":
        sky_const = 0
        bias = 0
    elif sky[1] == " con pocas nubes":
        sky_const = 0.5
    elif sky[1] == " con nubes aisladas":
        sky_const = 0.8
    elif sky[1] == " totalmente nublado":
        sky_const = 1.1
    
    if humidity > 50:
        humidity_const = 0.6
    elif humidity > 70:
        humidity_const = 0.8
    else:
        humidity_const = 1
    
    return float(round(sky_const*humidity_const*humidity + bias, 2))

def get_humidity(days):
    humidity = 0
    for day in days:
        humidity += int(day[2])
    humidity = humidity / len(days)
    return str(humidity)

def get_sky(days):
    sky = [0, 0, 0]
    shorty = [0, 0]
    final = ""
    
    for day in days:
        skies = day[3][1]
        if skies == "pocas nubes":
            sky[0] += 1
        elif skies == "ninguna nube":
            sky[0] += 1
        elif skies == "nubes aisladas":
            sky[1] += 1
        elif skies == "muchas nubes":
            sky[2] += 1
        elif skies == "nubes dispersas":
            sky[1] += 1
        short = day[3][0]
        if short == "Despejado":
            shorty[0] += 1
        elif short == "Nublado":
            shorty[1] += 1
    
    if shorty.index(max(shorty)) == 0:
        final += "Despejado, "
    else:
        final += "Nublado, "
    if sky.index(max(sky)) == 0:
        final += "con pocas nubes"
    elif sky.index(max(sky)) == 1:
        final += "con nubes aisladas"
    else:
        final += " totalmente nublado"
    return final