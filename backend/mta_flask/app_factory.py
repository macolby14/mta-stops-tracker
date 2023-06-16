from typing import Optional

from .stations import StationLoader


class AppFactory:
    """
    Class for generating objects with a singleton lifecycle
    """

    def __init__(self) -> None:
        self._station_loader: Optional[StationLoader] = None

    @property
    def station_loader(self) -> StationLoader:
        if self._station_loader is None:
            self._station_loader = StationLoader("./data/stations.csv")
        return self._station_loader
