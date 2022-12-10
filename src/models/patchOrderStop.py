from internal_types import TypedDict, Optional
from coordinates import Coordinates

class PatchOrderStop(TypedDict, total=False):
    coordinates: Optional[Coordinates]
    address: str
    name: Optional[str]
    phone: Optional[str]
    remarks: Optional[str]
