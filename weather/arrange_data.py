import datetime as dt
import phrases
import webScrapping_weather

def get_forecast():
    forecast = webScrapping_weather.get_data()
    if forecast == "No Internet":
        return forecast
    all_forecast = []
    for weather, day in forecast:
        f = phrases.print_data(day, phrases.parse_data_to_numbers(weather))
        all_forecast.append(f)
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
    
    return all_forecast

def get_weather_today(data, today):
    return_list = []
    for prediction in data:
        if prediction[0].day == today.day:
            return_list.append(prediction)
    return return_list

def get_weaher_per_day(data):
    return_list = []
    return_list.append([data[0]])
    for prediction in data:
        if return_list[0][0] == prediction:
            continue
        if return_list[len(return_list) - 1][0][0].day == prediction[0].day:
            return_list[len(return_list) - 1].append(prediction)
        else:
            return_list.append([prediction])
    return return_list
        

def arrange_data():
    forecast = get_forecast()
    if forecast == "No Internet":
        return forecast

    weather_per_day = get_weaher_per_day(forecast)

    return weather_per_day