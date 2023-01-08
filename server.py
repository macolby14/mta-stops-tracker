from flask import Flask
import mta_processor


app = Flask(__name__)


@app.get("/stops")
def stops():
    return mta_processor.get_upcoming_ace_stop_times()
