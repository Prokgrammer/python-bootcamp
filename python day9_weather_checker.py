import requests
import csv

API_KEY = "6db1b5d4390549a8b49152712250508"  # ← Replace this with your key
BASE_URL = "http://api.weatherapi.com/v1/current.json"
LOG_FILE = "weather_log.csv"

city = input("Enter a city name: ")

with open(LOG_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Region", "Country", "Temp (°C)", "Feels Like (°C)", "Condition", "Humidity (%)", "Wind (kph)"])

while True:
    city = input("Enter a city name (or type 'exit' to quit): ")
    if city.lower() == "exit":
        print("👋 Exiting Weather Checker.")
        break

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]
        current = data["current"]

        location_name = location["name"]
        region = location["region"]
        country = location["country"]
        temp = current["temp_c"]
        feelslike = current["feelslike_c"]
        condition = current["condition"]["text"]
        humidity = current["humidity"]
        wind = current["wind_kph"]

        # Print result
        print(f"\n📍 {location_name}, {region}, {country}")
        print(f"🌡️ Temperature: {temp}°C (Feels like {feelslike}°C)")
        print(f"🌤️ Condition: {condition}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind} kph\n")

        # Save to CSV
        with open(LOG_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([location_name, region, country, temp, feelslike, condition, humidity, wind])
    else:
        print("❌ Failed to fetch data. Try another city.\n")