"""Test nearest-station selection for configured locations."""

import pandas as pd

from src.nws_api import select_nearest_station


def main() -> None:
    """Print nearest observation station for each configured location."""
    locations = pd.read_csv("locations.csv")

    for _, row in locations.iterrows():
        station = select_nearest_station(
            row["latitude"],
            row["longitude"],
        )

        print()
        print(f"Requested location: {row['name']}")
        print(f"Nearest station: {station['station_id']}")
        print(f"Station name: {station['name']}")
        print(f"Distance: {station['distance_km']:.2f} km")


if __name__ == "__main__":
    main()
