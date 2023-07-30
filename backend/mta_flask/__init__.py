import json

from dotenv import load_dotenv
from flask import Flask

from . import mta_processor
from .app_factory import AppFactory
from .location import Location
from .models.StationSelection import StationSelected

import dataclasses


HOME_LOCATION = Location(lat=40.684026, lon=-73.967782)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if not load_dotenv():
        print("No .env file exists. Required to run program")
        exit(1)

    app_factory = AppFactory()

    @app.get("/api/health")
    def health() -> tuple[str, int]:
        return json.dumps({"message": "healthy"}), 200

    @app.get("/api/stops")
    async def stops() -> tuple[str, int]:
        stations_selected = [StationSelected(stop_id="A44N", line="C")]
        nextStops = await mta_processor.get_upcoming_stop_times(
            stations_selected=stations_selected
        )
        return json.dumps([dataclasses.asdict(stop) for stop in nextStops]), 200

    @app.get("/api/stations")
    def stations() -> tuple[str, int]:
        closest_stations = app_factory.station_loader.get_n_closest_stations(
            HOME_LOCATION
        )
        return json.dumps([station.dict() for station in closest_stations]), 200

    return app
