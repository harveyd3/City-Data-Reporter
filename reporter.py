import requests
import json
import csv

city = input("Enter a city: ")
city = city.strip()

while not city:
    city = input("Enter a city: ")
    city = city.strip()

api_url = "https://api.openweathermap.org/data/2.5/weather"
api_key = ""

api_request = {
        "q": city,
        "appid": api_key
}

response = requests.get(api_url, params=api_request)
weather_data = response.json()

if response.status_code == 200:
    city_name = weather_data["name"]
    country_code = weather_data["sys"]["country"]
    temperature = weather_data["main"]["temp"]
    temperature_c = temperature - 273.15
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]
    report = f"The weather for {city_name},{country_code}, is {temperature_c} degrees Celsius, a humidity of {humidity}, and {description}"
    print(report)
    with open("city_data.csv", "a", newline = "", encoding = "utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["City", "Country", "Temperature", "Humidity", "Description"])
        writer.writerow([city_name, country_code, temperature_c, humidity, description])
else:
    print("City not found.")




