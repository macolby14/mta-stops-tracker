from .stations import StationLoader


class AppFactory:
    """
    Class for generating objects with a singleton lifecycle
    """

    def __init__(self):
        self._station_loader = None

    @property
    def station_loader(self):
        if self._station_loader is None:
            self._station_loader = StationLoader()
        return self._station_loader
