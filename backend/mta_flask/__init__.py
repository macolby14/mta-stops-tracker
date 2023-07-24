import json

from dotenv import load_dotenv
from flask import Flask

from . import mta_processor
from .app_factory import AppFactory
from .location import Location

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
        nextTimes = await mta_processor.get_upcoming_stop_times(line="C")

        return (
            json.dumps(
                {
                    "line": "c",
                    "station": "clinton-washington",
                    "nextTimes": nextTimes,
                }
            ),
            200,
        )

    @app.get("/api/stations")
    def stations() -> tuple[str, int]:
        closest_stations = app_factory.station_loader.get_n_closest_stations(
            HOME_LOCATION
        )
        return json.dumps([station.dict() for station in closest_stations]), 200

    return app
