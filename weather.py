#Importing DateTime, Requests and TextToSpeech
import requests
from say import texttospeech
from datetime import datetime

#Converting Kelvin to Celcius
def kelvin_to_celsius(kelvin):
    celsius = kelvin -273.15
    return celsius

#Creating Weather Forcast Function
def weather_forcast():
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    key = "ec2d27af588ad0b5f601193384191452"
    city = "Windsor, UK"
    currentTime = datetime.now().time().strftime('%H:%M')

    url = base_url + "appid=" + key + "&q=" + city
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celcuis = kelvin_to_celsius(temp_kelvin)
    description = response['weather'][0]['description']
    
    texttospeech(f"The current time is {currentTime} in {city}: General Weather is {description}: The current temperature is {temp_celcuis:.2f}°C")
    print(f"The current time is {currentTime} in {city}: General Weather is {description}: The current temperature is {temp_celcuis:.2f}°C")
