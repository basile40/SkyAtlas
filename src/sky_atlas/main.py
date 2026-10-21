import sys
from sky_atlas.models.location import Coordinates, Location

def main() -> None:
    # Test sample location: Toms River, NJ
    toms_river = Location(
        name="Toms River",
        region="NJ",
        country="United States",
        coordinates=Coordinates(latitude=39.9532, longitude=-74.1979)
    )
    print("==========================================")
    print(f" SkyAtlas initialized successfully!")
    print(f" Default Target: {toms_river.name}, {toms_river.region}")
    print(f" Coordinates:    {toms_river.coordinates.latitude}, {toms_river.coordinates.longitude}")
    print("==========================================")

if __name__ == "__main__":
    main()