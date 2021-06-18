KELVIN = 273.15

def parse_data_to_numbers(forecast):
    current_temp = forecast["main"]["temp"] - KELVIN
    feels_like = forecast["main"]["feels_like"] - KELVIN
    humidity = forecast["main"]["humidity"]
    main_weather = forecast["weather"][0]["main"]
    description = forecast["weather"][0]["description"]

    return current_temp, feels_like, humidity, main_weather, description

def get_sky(data):
    if data == "Clouds":
        return "Nublado"
    elif data == "Clear":
        return "Despejado"
    elif data == "Rain":
        return "Lluvias"
    else:
        print(data)
        return "OJO CON ESTE QUE ES NUEVO"

def get_sky_description(data):
    if data == "few clouds":
        return "pocas nubes"
    elif data == "clear sky":
        return "ninguna nube"
    elif data == "scattered clouds":
        return "nubes aisladas"
    elif data == "overcast clouds":
        return "muchas nubes"
    elif data == "broken clouds":
        return "nubes dispersas"
    elif data == "light rain":
        return "lluvias aisladas"
    elif data == "moderate rain":
        return "lluvias moderadas"
    elif data == "heavy intensity rain":
        return "lluvias intensas"
    else:
        print(data)
        print("----------------")

def get_temps(data):
    temp = str(int(data[0]))
    feels_like = str(int(data[1]))
    return (temp, feels_like)

def print_data(day, data):
    temps = get_temps(data)
    sky = get_sky(data[3])
    humidity = str(data[2])
    sky_description = get_sky_description(data[4])
    weather = (sky, sky_description)
    return day, temps, humidity, weather