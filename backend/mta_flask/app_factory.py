import os
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
            current_directory = os.path.dirname(os.path.realpath(__file__))
            stations_abs_path = os.path.join(current_directory, "data/stations.csv")
            self._station_loader = StationLoader(stations_abs_path)
        return self._station_loader


# global singleton
app_factory = AppFactory()
