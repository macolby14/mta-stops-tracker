"""
Module for modeling subway station data
"""

import geopy.distance  # type: ignore
from pydantic import BaseModel
import json

from .location import Location


class Station(BaseModel):
    """Model for a MTA subway station"""

    name: str
    lines: str
    northLabel: str
    southLabel: str
    location: Location
    gtfsId: str

    def to_json(self) -> str:
        return json.dumps(self.dict())


def load_stations_from_csv(filename: str) -> list[Station]:
    """Load station data from CSV"""
    stations: list[Station] = []
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("Station ID"):  # skip header
                continue

            (
                _,
                _,
                gtfsId,
                _,
                _,
                name,
                _,
                lines,
                _,
                lat,
                lon,
                northLabel,
                southLabel,
                *_,
            ) = line.split(  # noqa: E501
                ","
            )
            stationLocation = Location(lat=float(lat), lon=float(lon))
            station = Station(
                name=name,
                lines=lines,
                northLabel=northLabel,
                southLabel=southLabel,
                location=stationLocation,
                gtfsId=gtfsId,
            )
            stations.append(station)
    return stations


class StationLoader:
    """'Class for loading station data from CSV"""

    @staticmethod
    def _get_distance_between_locations(
        location1: Location, location2: Location
    ) -> float:
        """Get distance between two locations"""
        return geopy.distance.distance(
            (location1.lat, location1.lon), (location2.lat, location2.lon)
        ).miles

    @staticmethod
    def _get_stations_by_closest_to_location(
        stations: list[Station], location: Location
    ) -> list[Station]:
        """Get stations sorted by closest to a given location"""
        return sorted(
            stations,
            key=lambda s: StationLoader._get_distance_between_locations(
                s.location, location
            ),
        )

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.stations = load_stations_from_csv(filename)

    def get_n_closest_stations(self, location: Location, n=10) -> list[Station]:
        """Get stations sorted by closest to a given location"""
        return StationLoader._get_stations_by_closest_to_location(
            self.stations, location
        )[0:n]
