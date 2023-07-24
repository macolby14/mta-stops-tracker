import os
from datetime import datetime

from .fetcher import FetcherFactory

# # takes a url and api key and returns the response content
# def read_gtfs_realtime(feed_url: str, api_key):
#     req_headers = {"x-api-key": api_key}
#     response = requests.get(feed_url, headers=req_headers)
#     if response.status_code != 200:
#         print(
#             f"HTTP Response not 200, url:{response.request.url},status_code:{response.status_code}, reason:{response.reason}"
#         )
#         return

#     return response.content


# takes a FeedMessage and gets returns a list of stop_time_updates that stop at target
def find_stop_on_ace(feed, target_stop_id):
    out = []
    if not feed:
        return out
    for entity in feed.entity:
        if not entity.trip_update:
            continue
        for stop_time_update in entity.trip_update.stop_time_update:
            if stop_time_update.stop_id == target_stop_id:
                out.append(stop_time_update)

    return out


# takes list of stop_time_updates and returns next n stops
def find_next_n_stop_times(stop_time_updates, n):
    stop_time_updates.sort(key=lambda update: update.arrival.time)
    out = [
        datetime.fromtimestamp(update.arrival.time) for update in stop_time_updates[:n]
    ]
    return out


def find_times_to_next_stop(upcoming_stop_times):
    times_to_next_stop = []

    for t in upcoming_stop_times:
        now = datetime.now()
        if t < now:
            continue
        delta = t - now
        times_to_next_stop.append(delta.seconds // 60)

    return times_to_next_stop


async def get_upcoming_stop_times(line: str):
    MTA_API_KEY = os.getenv("MTA_API_KEY")
    fetcher = FetcherFactory().create(line, MTA_API_KEY)

    mta_feed = await fetcher.fetch_and_parse()

    # TODO - Make it so we can just declare the station name and direction.
    ace_stops = find_stop_on_ace(mta_feed, "A44N")

    upcoming_ace_stop_times = find_next_n_stop_times(ace_stops, 5)
    out = find_times_to_next_stop(upcoming_ace_stop_times)
    return out
