import requests
from datetime import datetime
from sky_atlas.models.location import Coordinates
from sky_atlas.models.weather import CurrentWeather

class WeatherService:
    """Handles API communication with Open-Meteo for forecast data."""
    
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    
    # Standard WMO Weather Codes translated to human-readable text
    WMO_CODES = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog", 51: "Light drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow", 95: "Thunderstorm"
    }

    def get_current_weather(self, coords: Coordinates) -> CurrentWeather | None:
        """Fetches the current weather conditions for the given coordinates."""
        params = {
            "latitude": coords.latitude,
            "longitude": coords.longitude,
            "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "is_day", "weather_code", "wind_speed_10m"],
            "temperature_unit": "fahrenheit", # Setting to Fahrenheit for US locations
            "wind_speed_unit": "mph",
            "timezone": "auto"
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            curr = data.get("current", {})
            if not curr:
                return None

            code = curr.get("weather_code", 0)
            
            return CurrentWeather(
                temperature=curr.get("temperature_2m", 0.0),
                feels_like=curr.get("apparent_temperature", 0.0),
                humidity=curr.get("relative_humidity_2m", 0),
                wind_speed=curr.get("wind_speed_10m", 0.0),
                condition_code=code,
                condition_text=self.WMO_CODES.get(code, "Unknown"),
                timestamp=datetime.fromisoformat(curr.get("time")),
                is_day=bool(curr.get("is_day", 1))
            )
            
        except requests.RequestException as e:
            print(f"Failed to fetch weather data: {e}")
            return None