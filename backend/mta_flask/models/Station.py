from pydantic import BaseModel
import json

from .Location import Location


class Station(BaseModel):
    """Model for a MTA subway station"""

    name: str
    lines: str
    northLabel: str
    southLabel: str
    location: Location
    gtfsId: str

    def to_json(self) -> str:
        return json.dumps(self.dict())
