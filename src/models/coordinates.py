from .internal_types import TypedDict

class Coordinates(TypedDict, total=True):
    lat: str
    lng: str

