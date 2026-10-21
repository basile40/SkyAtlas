from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class CurrentWeather:
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float
    condition_code: int
    condition_text: str
    timestamp: datetime
    is_day: bool