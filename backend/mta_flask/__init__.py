from . import mta_processor
import json
from dotenv import load_dotenv
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if not load_dotenv():
        print("No .env file exists. Required to run program")
        exit(1)

    @app.get("/api/stops")
    def stops():
        try:
            nextTimes = mta_processor.get_upcoming_ace_stop_times()
        except:
            return json.dumps({"message": "internal error at GET /stops"}), 500

        return json.dumps(
            {
                "line": "c",
                "station": "clinton-washington",
                "nextTimes": mta_processor.get_upcoming_ace_stop_times(),
            }
        )

    return app
