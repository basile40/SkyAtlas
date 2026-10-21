from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float

@dataclass(frozen=True)
class Location:
    name: str
    region: str
    country: str
    coordinates: Coordinates