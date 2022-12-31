import gtfs_realtime_pb2
import google.protobuf
import requests
from dotenv import load_dotenv
import os

print("Starting")

def read_gtfs_realtime(feed_url, api_key):

    req_headers = {"x-api-key": api_key}
    response = requests.get(feed_url, headers=req_headers)

    if response.status_code != 200:
        print(f"HTTP Response not 200, url:{response.request.url},status_code:{response.status_code}, reason:{response.reason}")
        return

    return response.content


# main
load_dotenv()
MTA_API_KEY=os.getenv("MTA_API_KEY")
A_C_E_URI=os.getenv("A_C_E_URI")

proto_res = read_gtfs_realtime("https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace", MTA_API_KEY)
if not proto_res:
    print("No response from api. Exiting")
    exit(1)

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(proto_res)
print(feed)