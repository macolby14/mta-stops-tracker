from flask import Flask, send_from_directory
import mta_processor
import json
import os


app = Flask(__name__, static_folder="mta-fe/build")


# serve staticn react app
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


@app.get("/stops")
def stops():
    return json.dumps({"stops": mta_processor.get_upcoming_ace_stop_times()})
