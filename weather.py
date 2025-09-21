import requests
import os

def get_weather(city):
    API_KEY = os.getenv("WEATHER_API")
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'error' in data:
            print(f"❌ {data['error']['message']}")
            return
        
        location = data['location']
        current = data['current']
        
        print(f"\n{'='*45}")
        print(f"  📍 {location['name']}, {location['country']}")
        print(f"{'='*45}")
        print(f"  🌡️  {current['temp_c']}°C (feels like {current['feelslike_c']}°C)")
        print(f"  ☁️  {current['condition']['text']}")
        print(f"  ☀️  UV Index: {current['uv']}")
        print(f"  💧 {current['humidity']}% humidity")
        print(f"  🌬️  {current['wind_kph']} km/h wind")
        print(f"{'='*45}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

city = input("\n🌍 Enter city: ").strip()
if city:
    get_weather(city)
else:
    print("Please enter a city name.")