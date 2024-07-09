from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Caracas"):

    requests_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(requests_url).json()

    return weather_data

if __name__ == "__main__":

    print(f"--- Get Current Weather Conditions ---")

    city = input("\nPlease enter a city name: ")

    if not bool(city.strip()):
        city = "Caracas"

    weather_data = get_current_weather(city)

    print()
    pprint(weather_data)
    