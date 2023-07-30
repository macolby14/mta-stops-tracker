from dataclasses import dataclass


@dataclass
class StationSelected:
    """Represents a stop time update from the MTA feed."""

    stop_id: str
    line: str
