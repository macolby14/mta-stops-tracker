import os
from datetime import datetime

from .fetcher import FetchersGroup
from .models.StopTimeUpdate import StopTimeUpdate
from .models.StationSelection import StationSelected

from .proto import gtfs_realtime_pb2


def find_relevant_stops(
    feed: gtfs_realtime_pb2.FeedMessage,
    stations_selected: list[StationSelected],
) -> list[StopTimeUpdate]:
    """
    Produces a list of StopTimeUpdates that are relevant to the
    target_stops_ids and target_lines.
    """
    out: list[StopTimeUpdate] = []
    if not feed:
        return out
    for selection in stations_selected:
        for entity in feed.entity:
            if entity.trip_update.trip.route_id != selection.line:
                continue
            if not entity.trip_update:
                continue
            for stop_time_update in entity.trip_update.stop_time_update:
                if stop_time_update.stop_id == selection.stop_id:
                    out.append(
                        StopTimeUpdate(
                            stop_id=stop_time_update.stop_id,
                            arrival=stop_time_update.arrival.time,
                            route_id=entity.trip_update.trip.route_id,
                        )
                    )

    return out


def find_next_n_stop_times(stop_time_updates: list[StopTimeUpdate], n: int):
    """
    Produces a list of the next n stop times from the given list of StopTimeUpdates.
    """
    stop_time_updates.sort(key=lambda update: update.arrival)
    out = [datetime.fromtimestamp(update.arrival) for update in stop_time_updates[:n]]
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


async def get_upcoming_stop_times(lines: list[str]):
    MTA_API_KEY = os.getenv("MTA_API_KEY")
    if not MTA_API_KEY:
        raise Exception("MTA_API_KEY not set")

    fetcherGroup = FetchersGroup(lines, MTA_API_KEY)

    stations_selected = [StationSelected(stop_id="A44N", line="C")]

    mta_feed = await fetcherGroup.fetch_and_parse()

    # TODO - Make it so we can just declare the station name and direction.
    stops: list[StopTimeUpdate] = []
    for feed in mta_feed:
        stops.extend(
            find_relevant_stops(
                feed,
                stations_selected=stations_selected,
            )
        )

    upcoming_stop_times = find_next_n_stop_times(stops, 5)
    out = find_times_to_next_stop(upcoming_stop_times)
    return out
