from flask import Flask
import mta_processor
import json


app = Flask(__name__)


@app.get("/stops")
def stops():
    return json.dumps({"stops": mta_processor.get_upcoming_ace_stop_times()})
