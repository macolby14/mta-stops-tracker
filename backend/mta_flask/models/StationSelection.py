from dataclasses import dataclass


@dataclass
class StationSelected:
    """Represents a stop time update from the MTA feed."""

    stop_id: str
    line: str

    def __init__(
        self, id: str, direction: str, line: str, selected: bool | None
    ) -> None:
        direction_letter = direction[0].upper()
        self.stop_id = id + direction_letter
        self.line = line
