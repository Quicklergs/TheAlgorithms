import requests

APPID = ""  # <-- Put your OpenWeatherMap appid here!
URL_BASE = "https://api.openweathermap.org/data/2.5/"


def current_weather(q: str = "Chicago", appid: str = APPID) -> dict:
    """https://openweathermap.org/api"""
    return requests.get(URL_BASE + "weather", params=locals()).json()


def weather_forecast(q: str = "Kolkata, India", appid: str = APPID) -> dict:
    """https://openweathermap.org/forecast5"""
    return requests.get(URL_BASE + "forecast", params=locals()).json()


def weather_onecall(lat: float = 55.68, lon: float = 12.57, appid: str = APPID) -> dict:
    """https://openweathermap.org/api/one-call-api"""
    return requests.get(URL_BASE + "onecall", params=locals()).json()


if __name__ == "__main__":
    from pprint import pprint

    while True:
        location = input("Enter a location:").strip()
        if location:
            pprint(current_weather(location))
            
            #for extracting exact data from json 
            json_data = current_weather(location)
            condition = json_data['weather'][0]['main']
            description=json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']



            print("\n Condition:",condition)
            print("\n description:",description)
            print("\n temp:",temp)
            print("\n pressure:",pressure)
            print("\n humidity:",humidity)
            print("\n wind:",wind)
            
        else:
            break
