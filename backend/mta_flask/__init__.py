from . import mta_processor
from .stations import StationLoader, Location
import json
from dotenv import load_dotenv
from flask import Flask

HOME_LOCATION = Location(lat=40.684026, lon=-73.967782)


def load_station_data() -> None:
    # yapf: disable
    stations = StationLoader(filename='mta_flask/data/stations.csv').get_n_closest_stations(HOME_LOCATION)  # noqa: E501
    # yapf: enable
    print(stations)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if not load_dotenv():
        print("No .env file exists. Required to run program")
        exit(1)

    load_station_data()

    @app.get("/api/stops")
    def stops():
        try:
            nextTimes = mta_processor.get_upcoming_ace_stop_times()
        except Exception:
            return json.dumps({"message": "internal error at GET /stops"}), 500

        return json.dumps({
            "line": "c",
            "station": "clinton-washington",
            "nextTimes": nextTimes,
        })

    return app
