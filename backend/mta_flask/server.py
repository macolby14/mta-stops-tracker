from flask import Flask, send_from_directory
from . import mta_processor
import json
import os
from dotenv import load_dotenv


app = Flask(__name__, static_folder="mta-fe/build")

# ensure .env gets loaded for config
print(os.path.join(os.path.dirname(__file__), ".env"))
if not os.path.join(os.path.dirname(__file__), ".env"):
    print("No .env file exists. Required to run program")
    exit(1)
load_dotenv()

# serve staticn react app
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


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
