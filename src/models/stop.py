from internal_types import TypedDict, Optional, Dict
from coordinates import Coordinates

class Stop(TypedDict, total=False):
    id: Optional[str]
    coordinates: Coordinates
    address: str


class StopWithContact(Stop, TypedDict, total=False):
    name: str
    phone: str
    POD: Optional[Dict]

