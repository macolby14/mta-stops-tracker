import json

from dotenv import load_dotenv
from flask import Flask, request

from . import mta_processor
from .app_factory import app_factory
from .models.location import Location
from .models.station_selection import StationSelected

import dataclasses


HOME_LOCATION = Location(lat=40.7626049, lon=-73.96191)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if not load_dotenv():
        print("No .env file exists. Required to run program")
        exit(1)

    @app.get("/api/health")
    def health() -> tuple[str, int]:
        return json.dumps({"message": "healthy"}), 200

    @app.post("/api/stops")
    async def stops() -> tuple[str, int]:
        """
        Returns the next stop times for the specified stations.
        """
        request_json = request.get_json()
        if request_json is None:
            raise Exception("No JSON in request")
        stations = request_json["stations"]
        stations_selected = [StationSelected(**station) for station in stations]
        nextStops = await mta_processor.get_upcoming_stop_times(
            stations_selected=stations_selected
        )
        return json.dumps([dataclasses.asdict(stop) for stop in nextStops]), 200

    @app.get("/api/stations")
    def stations() -> tuple[str, int]:
        """
        Returns the closest stations to the home location.
        """
        closest_stations = app_factory.station_loader.get_n_closest_stations(
            HOME_LOCATION
        )
        return json.dumps([station.dict() for station in closest_stations]), 200

    return app
