from sky_atlas.models.location import Coordinates, Location
from sky_atlas.services.weather_service import WeatherService

def main() -> None:
    # 1. Define our target location
    toms_river = Location(
        name="Toms River",
        region="NJ",
        country="United States",
        coordinates=Coordinates(latitude=39.9532, longitude=-74.1979)
    )
    
    # 2. Initialize our new service
    weather_api = WeatherService()
    
    print(f"Fetching live weather for {toms_river.name}, {toms_river.region}...")
    
    # 3. Fetch the data
    current = weather_api.get_current_weather(toms_river.coordinates)
    
    if current:
        print("==========================================")
        print(f" Condition:   {current.condition_text} {'☀️' if current.is_day else '🌙'}")
        print(f" Temperature: {current.temperature}°F (Feels like {current.feels_like}°F)")
        print(f" Wind Speed:  {current.wind_speed} mph")
        print(f" Humidity:    {current.humidity}%")
        print("==========================================")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()