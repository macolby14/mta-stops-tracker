from dataclasses import dataclass


@dataclass
class StopTimeUpdate:
    """Represents a stop time update from the MTA feed."""

    stop_id: str
    arrival_time: int
    route_id: str
