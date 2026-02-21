import requests


def get_coordinates(city):
    response = requests.get(
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
    data = response.json()

    if 'results' not in data or not data['results']:
        print(f"City {city} not found")
        return None, None

    lat = data['results'][0]['latitude']
    lon = data['results'][0]['longitude']

    return lat, lon


def get_weather(lat, lon):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,windspeed_10m")
    data = response.json()

    temperature = data['current']['temperature_2m']
    windspeed = data['current']['windspeed_10m']

    return temperature, windspeed


city = input("Enter a city name: ")
while city == "":
    city = input("You must enter a city name: ")


lat, lon = get_coordinates(city)
if lat is None:
    exit()

temperature, windspeed = get_weather(lat, lon)
print(f"Temperature: {temperature}°C")
print(f"Wind speed: {windspeed} km/h")
