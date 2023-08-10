from dataclasses import dataclass


@dataclass
class StopTimeUpdate:
    """Represents a stop time update from the MTA feed."""

    stop_id: str
    arrival_time: int
    route_id: str


@dataclass
class StopInfo:
    """Represents a stop time update from the MTA feed."""

    direction: str
    station_id: str
    station_name: str
    line: str
    time: int  # time_to_next_stop
