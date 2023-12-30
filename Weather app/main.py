import datetime as dt
import requests

location = input("Enter the city name: ")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "88c41e51b124172573d7573af96ba42a"

url = BASE_URL + "appid=" + API_KEY + "&q=" + location
response = requests.get(url).json()

if response['cod'] == '404':
    print("Invalid City: {}, Please Check Your City Name".format(location))
else:
    temp_cels = ((response['main']['temp']) - 273.15)
    temp_fahr = (temp_cels * 9/5) + 32
    weather_desc = response['weather'][0]['description']
    hdmt = response['main']['humidity']
    wind_spd = response['wind']['speed']
    date_time = dt.datetime.now().strftime("%d %b %y | %I:%M:%S %p")

    print("---------------------------------------------------------")
    print("Weather Stats for - {} || {}".format(location.upper(), date_time))
    print("---------------------------------------------------------")


    print("Current temperature in Celsius is: {:.2f} deg C".format(temp_cels))
    print("Current temperature in Fahrenheit is: {:.2f} deg F".format(temp_fahr))
    print("Current weather description:", weather_desc)
    print("Current Humidity:", hdmt, '%')
    print("Current wind speed:", wind_spd, 'kmph')