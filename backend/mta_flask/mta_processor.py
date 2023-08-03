import os
from datetime import datetime

from .fetcher import FetchersGroup
from .models.StopTimeUpdate import StopTimeUpdate, StopInfo
from .models.StationSelection import StationSelected
from .app_factory import app_factory

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
                            arrival_time=stop_time_update.arrival.time,
                            route_id=entity.trip_update.trip.route_id,
                        )
                    )

    return out


def find_next_n_stop_times(
    stop_time_updates: list[StopTimeUpdate], n: int
) -> list[StopTimeUpdate]:
    """
    Produces a list of the next n stop times from the given
    list of StopTimeUpdates.
    """
    stop_time_updates.sort(key=lambda update: update.arrival_time)
    return stop_time_updates[:n]


def format_stop_info(upcoming_stops: list[StopTimeUpdate]) -> list[StopInfo]:
    formatted_stops: list[StopInfo] = []

    for stop in upcoming_stops:
        t = datetime.fromtimestamp(stop.arrival_time)
        now = datetime.now()
        if t < now:
            continue
        delta = t - now
        time_to_next_stop = delta.seconds // 60

        stop_gtfs_id = stop.stop_id[:-1]
        line_name = stop.route_id
        direction = stop.stop_id[-1]
        direction_name = None
        if direction == "N":
            direction_name = app_factory.station_loader.get_station_by_gtfsId(
                stop_gtfs_id
            ).northLabel
        elif direction == "S":
            direction_name = app_factory.station_loader.get_station_by_gtfsId(
                stop_gtfs_id
            ).southLabel
        else:
            raise Exception("Invalid direction")

        formatted_stops.append(
            StopInfo(
                station=stop_gtfs_id,
                line=line_name,
                direction=direction_name,
                time=time_to_next_stop,
            )
        )

    return formatted_stops


async def get_upcoming_stop_times(
    stations_selected: list[StationSelected],
) -> list[StopInfo]:
    MTA_API_KEY = os.getenv("MTA_API_KEY")
    if not MTA_API_KEY:
        raise Exception("MTA_API_KEY not set")

    lines = set([station.line for station in stations_selected])

    fetcherGroup = FetchersGroup(lines, MTA_API_KEY)

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

    upcoming_stop_times = find_next_n_stop_times(stops, 10)
    return format_stop_info(upcoming_stop_times)
